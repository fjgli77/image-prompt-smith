#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""image_prep.py — 反推前的图片预处理（裁切 / 转码 / 去边 / 缩放 / 网格切分）

为什么要有这个脚本：
    `image-to-prompt.md` 的第一步是「先修图」——裁到主体、去水印/边框。
    但只写这句话没用：手边没有工具时，执行者只能现写脚本，或者跳过这步直接反推，
    结果水印被写进正向词、边框被当成构图元素复刻一遍。

用法:
    # 看尺寸与格式
    python image_prep.py --info in.webp

    # 转 PNG（webp/heic 等模型不吃的格式先转）
    python image_prep.py --in in.webp --out out.png

    # 裁掉留白边（按四角颜色自动判定容差）
    python image_prep.py --in in.png --out trimmed.png --trim --tolerance 12

    # 手动裁一块（x,y,宽,高）
    python image_prep.py --in in.jpg --out crop.png --crop 120,80,900,1200

    # 切成 3 列（三视图/三格设定稿），并按列导出
    python image_prep.py --in sheet.png --grid 3x1 --outdir cut

    # 长边缩到 1536（大多数视觉模型的高清阈值附近）
    python image_prep.py --in big.png --out small.png --max-side 1536

依赖：Pillow（`pip install pillow`）。其余全用标准库。
"""

from __future__ import annotations

import argparse
import os
import sys

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    print("需要 Pillow：pip install pillow", file=sys.stderr)
    raise SystemExit(2)

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
    except Exception:
        pass


def _open(path: str) -> Image.Image:
    try:
        im = Image.open(path)
        im.load()
        return im
    except Exception as e:
        print(f"打不开这张图：{path}\n  {type(e).__name__}: {e}", file=sys.stderr)
        print("确认它是 png/jpg/webp/gif/bmp/tiff 之一；heic 需先转码。", file=sys.stderr)
        raise SystemExit(2)


def _fmt(size: tuple[int, int]) -> str:
    return f"{size[0]}×{size[1]}"


def cmd_info(args) -> int:
    im = _open(args.inp)
    w, h = im.size
    print(f"文件：{args.inp}")
    print(f"格式：{im.format}  模式：{im.mode}  尺寸：{_fmt(im.size)}  比例：{w / h:.3f}（{w}:{h}）")
    if im.info.get("icc_profile"):
        print("ICC：有（转码时建议保留，否则颜色会偏）")
    return 0


def _corner_colors(im: Image.Image, box: int = 8) -> list[tuple[int, int, int]]:
    rgb = im.convert("RGB")
    w, h = rgb.size
    pts = [(0, 0), (w - box, 0), (0, h - box), (w - box, h - box)]
    return [rgb.getpixel(p) for p in pts]


def _close(a, b, tol: int) -> bool:
    return all(abs(x - y) <= tol for x, y in zip(a, b))


def trim_border(im: Image.Image, tol: int = 10) -> Image.Image:
    """裁掉与四角同色的外框（对付纯色底 / 白边 / 黑边）。"""
    rgb = im.convert("RGB")
    w, h = rgb.size
    corners = _corner_colors(rgb)
    px = rgb.load()

    left, right, top, bottom = 0, w - 1, 0, h - 1
    while left < right and all(_close(px[left, y], corners[0], tol) for y in range(0, h, max(1, h // 40))):
        left += 1
    while right > left and all(_close(px[right, y], corners[1], tol) for y in range(0, h, max(1, h // 40))):
        right -= 1
    while top < bottom and all(_close(px[x, top], corners[0], tol) for x in range(0, w, max(1, w // 40))):
        top += 1
    while bottom > top and all(_close(px[x, bottom], corners[2], tol) for x in range(0, w, max(1, w // 40))):
        bottom -= 1

    if (left, top, right, bottom) == (0, 0, w - 1, h - 1):
        print("未检测到可裁的纯色边框（或边框与主体同色）。")
        return im
    box = (left, top, right + 1, bottom + 1)
    print(f"裁边：{_fmt(im.size)} → {_fmt((box[2] - box[0], box[3] - box[1]))}")
    return im.crop(box)


def cmd_convert(args) -> int:
    im = _open(args.inp)

    if args.trim:
        im = trim_border(im, args.tolerance)
    if args.crop:
        try:
            x, y, cw, ch = (int(v) for v in args.crop.split(","))
        except ValueError:
            print("--crop 格式应为 x,y,宽,高（四个整数）", file=sys.stderr)
            return 2
        if x + cw > im.size[0] or y + ch > im.size[1]:
            print(f"裁切框超出图像范围：图 {_fmt(im.size)}，框 {cw}×{ch} @({x},{y})", file=sys.stderr)
            return 2
        im = im.crop((x, y, x + cw, y + ch))
        print(f"裁切后：{_fmt(im.size)}")

    if args.max_side:
        w, h = im.size
        long_side = max(w, h)
        if long_side > args.max_side:
            k = args.max_side / long_side
            im = im.resize((max(1, round(w * k)), max(1, round(h * k))), Image.LANCZOS)
            print(f"缩放后：{_fmt(im.size)}（长边 {args.max_side}）")

    ext = os.path.splitext(args.out)[1].lower()
    if ext in (".jpg", ".jpeg"):
        im.convert("RGB").save(args.out, quality=args.quality)
    else:
        im.save(args.out)
    print(f"已保存：{args.out}（{_fmt(im.size)}）")
    return 0


def cmd_grid(args) -> int:
    """按行列切分（三视图 / 三格设定稿 / 九宫格表情）。"""
    try:
        cols, rows = (int(v) for v in args.grid.lower().split("x"))
    except ValueError:
        print("--grid 格式应为 列x行，例如 3x1", file=sys.stderr)
        return 2
    im = _open(args.inp)
    w, h = im.size
    cw, ch = w // cols, h // rows
    os.makedirs(args.outdir, exist_ok=True)
    base = os.path.splitext(os.path.basename(args.inp))[0]
    n = 0
    for r in range(rows):
        for c in range(cols):
            box = (c * cw, r * ch, (c + 1) * cw, (r + 1) * ch)
            out = os.path.join(args.outdir, f"{base}_r{r + 1}c{c + 1}.png")
            im.crop(box).save(out)
            n += 1
    print(f"已切 {cols}×{rows} 共 {n} 块 → {args.outdir}/（每块 {_fmt((cw, ch))}）")
    print("提示：切完逐块看一遍——手/脚被切断的块不要拿去反推，会被写成「肢体缺失」。")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="反推前图片预处理：转码 / 裁切 / 去边 / 缩放 / 网格切分",
        epilog="典型顺序：--info 看尺寸 → --trim 去边 → --max-side 1536 → --grid 切格",
    )
    p.add_argument("--in", dest="inp", required=True, help="输入图片")
    p.add_argument("--out", help="输出图片（转码/裁切/缩放时必填）")
    p.add_argument("--info", action="store_true", help="只看信息，不改文件")
    p.add_argument("--trim", action="store_true", help="裁掉纯色外框（白边/黑边）")
    p.add_argument("--tolerance", type=int, default=10, help="裁边颜色容差，默认 10")
    p.add_argument("--crop", help="手动裁切 x,y,宽,高")
    p.add_argument("--max-side", type=int, default=0, help="长边上限（0 = 不改）")
    p.add_argument("--quality", type=int, default=95, help="JPEG 质量，默认 95")
    p.add_argument("--grid", help="按 列x行 切分，例如 3x1、2x2、3x3")
    p.add_argument("--outdir", default="cut", help="--grid 的输出目录，默认 cut/")
    args = p.parse_args(argv)

    if not os.path.exists(args.inp):
        print(f"找不到文件：{args.inp}", file=sys.stderr)
        return 2
    if args.info:
        return cmd_info(args)
    if args.grid:
        return cmd_grid(args)
    if not args.out:
        print("需要 --out（或用 --info / --grid）", file=sys.stderr)
        return 2
    return cmd_convert(args)


if __name__ == "__main__":
    raise SystemExit(main())

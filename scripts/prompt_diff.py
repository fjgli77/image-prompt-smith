#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""prompt_diff.py — 两版提示词的「锚点漂移」核对

为什么需要它：
    `text-only-consistency.md` 要求"锚点段逐字复制"，但人做不到每轮都肉眼比对。
    多轮改下来最常见的事故不是脸变了，是**服装 / 配色 / 数量 / 方位悄悄漂了**——
    上一轮"分片鳞甲 + 薄纱广袖"，这一轮变成"裹身长袍"，看图才发现。

它做什么：
    从两段提示词里各抽出六组锚点，逐组比对，输出「一致 / 变化 / 丢失 / 新增」。
    变化项默认判 P1：**锚点变了，就是换了一个人/一套衣服**。

用法:
    python prompt_diff.py --old v1.txt --new v2.txt
    python prompt_diff.py --old v1.txt --new v2.txt --json
    python prompt_diff.py --old v1.txt --new v2.txt --strict     # 有漂移则退出码 1
    python prompt_diff.py --self-test

六组锚点：数量实体 / 配色 / 服装部件 / 材质 / 方位元素 / 比例（头身比·发色·瞳色）
说明：启发式抽取，命中后请人工复核；它查"有没有变"，不判"变得对不对"。
"""

from __future__ import annotations

import argparse
import json
import re
import sys

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
    except Exception:
        pass


# ---------------------------------------------------------------- 抽取规则

# ① 数量实体：九条冰龙 / 双环 / 三枚冰晶
COUNT_RE = re.compile(
    r"([0-9一二两三四五六七八九十百]+)\s*(条|只|枚|名|位|柄|座|层|重|道|颗|头|个)\s*"
    r"([^。；;，,、]{0,6}?(?:龙|凤|剑|兽|环|轮|晶|羽|铃|珠|法相|分身|灵兽))")
# 英文数量：exactly nine ice dragons / three rings
COUNT_EN_RE = re.compile(
    r"(?:exactly\s+)?(two|three|four|five|six|seven|eight|nine|ten|\d+)\s+"
    r"([a-z\- ]{0,14}?(?:dragons?|rings?|swords?|shards?|orbs?|wings?|beasts?))", re.I)

# ② 配色声明
COLOR_DECL_RE = re.compile(r"(?:主色|辅色|点缀色?|配色)[^。；;，,\n]{0,40}")
COLOR_NAME_RE = re.compile(
    r"(冰蓝|银白|玄黑|墨黑|月白|朱红|暗赤|鎏金|青玉|石青|天青|铁灰|暗铜|藏青|奶白|浅杏|雾蓝|"
    r"暗紫|血赤|幽紫|荧光绿|琥珀|绯红|冷白|暖金|苔绿|暖米|锈红|酒红|墨绿|浅金|纯白|深靛|"
    r"赤红|暗红|火红|深蓝|浅蓝|墨蓝|天蓝|象牙|砂金)")

# ③ 服装部件
CLOTH_PARTS = ["肩甲", "胸甲", "护臂", "护腕", "腰封", "腰带", "腰链", "披风", "披帛", "大氅",
               "纱袖", "广袖", "长袍", "法袍", "战衣", "短衣", "裙摆", "长裙", "短裙", "开衩",
               "腿环", "战靴", "长靴", "衣摆", "面纱", "兜帽", "高领", "立领", "臂钏", "发冠"]
# ④ 材质
MATERIALS = ["冰晶", "玉石", "青玉", "玄铁", "鎏金", "薄纱", "半透", "灵绸", "丝绸", "鳞片", "甲片",
             "锁子甲", "皮革", "绒毛", "羽毛", "骨", "鎏银", "亮片", "织锦", "绣"]
# ⑤ 方位元素
ORIENT_RE = re.compile(
    r"(头顶|正上方|头上|身后|背后|脚下|肩侧|腰侧|身前|手中)[^。；;，,\n]{0,10}"
    r"(光环|光轮|法轮|轮盘|法相|法阵|灵兽|龙|枪|剑|杖|羽|披帛|光柱)")
# ⑥ 比例 / 发色 / 瞳色
RATIO_RE = re.compile(r"([0-9]+(?:\.[0-9]+)?)\s*(?:头身|[-\s]?head)")
HAIR_RE = re.compile(r"([一-龥]{0,4})\s*(长发|短发|马尾|高马尾|束发|半束|披发)")
EYE_RE = re.compile(r"([一-龥]{0,3})\s*(?:眼眸|眼睛|瞳|眼)")

GROUPS = [
    ("数量实体", None),
    ("配色", None),
    ("服装部件", None),
    ("材质", None),
    ("方位元素", None),
    ("比例/外貌", None),
]


def _counts(text: str) -> set[str]:
    out = set()
    for a, b, c in COUNT_RE.findall(text):
        out.add(f"{a}{b}{c.strip()}")
    for a, b in COUNT_EN_RE.findall(text):
        out.add(f"{a} {b.strip()}")
    return out


HAIR_EYE_CLAUSE = re.compile(r"(发|眼眸|瞳|眼)")
HAIR_EYE_COLORS = {"银白", "墨黑", "玄黑", "冰蓝", "琥珀", "绯红", "暗紫", "暗赤", "纯白"}


def _colors(text: str) -> set[str]:
    """优先抽"主色/辅色/配色"声明句；没有声明时退回全文，但排除发色/瞳色所在小句。"""
    decl = "，".join(COLOR_DECL_RE.findall(text))
    if decl:
        return set(COLOR_NAME_RE.findall(decl))
    clauses = [c for c in re.split(r"[。；;，,\n]", text) if not HAIR_EYE_CLAUSE.search(c)]
    got = set(COLOR_NAME_RE.findall("，".join(clauses)))
    return got


def _parts(text: str) -> set[str]:
    return {p for p in CLOTH_PARTS if p in text}


def _materials(text: str) -> set[str]:
    return {m for m in MATERIALS if m in text}


def _orient(text: str) -> set[str]:
    return {f"{a}·{b}" for a, b in ORIENT_RE.findall(text)}


def _proportions(text: str) -> set[str]:
    out = set()
    for v in RATIO_RE.findall(text):
        out.add(f"{v} 头身")
    for m in HAIR_RE.finditer(text):
        pre = m.group(1)
        pre = "" if pre.endswith(("的", "长", "白", "黑")) and pre else pre
        out.add((pre + m.group(2)).strip())
    for m in EYE_RE.finditer(text):
        pre = m.group(1)
        if pre and pre not in ("的", "双", "两", "大", "一"):
            out.add(pre + "眼")
    return out


EXTRACTORS = {
    "数量实体": _counts,
    "配色": _colors,
    "服装部件": _parts,
    "材质": _materials,
    "方位元素": _orient,
    "比例/外貌": _proportions,
}


def diff(old: str, new: str) -> dict:
    report = {}
    for group, fn in EXTRACTORS.items():
        a, b = fn(old), fn(new)
        report[group] = {
            "same": sorted(a & b),
            "changed": sorted(a ^ b) if (a & b) else [],   # 同组有交集时的差集
            "lost": sorted(a - b),
            "added": sorted(b - a),
        }
    return report


def drift_score(report: dict) -> int:
    """漂移分：丢失 + 新增的锚点总数。0 = 完全一致。"""
    return sum(len(v["lost"]) + len(v["added"]) for v in report.values())


def render(report: dict, as_json: bool = False) -> str:
    if as_json:
        return json.dumps({"drift": drift_score(report), "groups": report},
                          ensure_ascii=False, indent=2)
    lines = ["=== 锚点漂移核对 ===", ""]
    total = 0
    for group, v in report.items():
        lost, added, same = v["lost"], v["added"], v["same"]
        if not (lost or added):
            lines.append(f"[一致] {group}：{'、'.join(same) if same else '（两版都没写）'}")
            continue
        total += len(lost) + len(added)
        lines.append(f"[漂移] {group}")
        if lost:
            lines.append(f"        丢失（v1 有、v2 无）：{'、'.join(lost)}")
        if added:
            lines.append(f"        新增（v2 才出现）：{'、'.join(added)}")
        if same:
            lines.append(f"        保持：{'、'.join(same)}")
    lines += ["", f"漂移项：{total} 处"]
    if total == 0:
        lines.append("判定：锚点完全一致，可放心当作同一角色/同一套装的下一版。")
    elif total <= 2:
        lines.append("判定：轻微漂移——确认这些变化是本次**有意**改的；不是的话，把对应锚点段逐字复制回去。")
    else:
        lines.append("判定：显著漂移——这大概率已经不是同一套服装/同一个配置了。"
                     "先确认本次变量清单，再把未列入变量的锚点还原。")
    lines += ["", "（启发式抽取，只查『有没有变』，不判『变得对不对』）"]
    return "\n".join(lines)


# ---------------------------------------------------------------- 自测

CASES = [
    {
        "name": "服装漂移（轻装 → 长袍）",
        "old": "3:4 全身，玄幻女帝，冰蓝与银白配色，局部冰晶肩甲、护臂、腰封，恰好九条冰龙环绕，头顶正上方双层光环，7.2 头身。",
        "new": "3:4 全身，玄幻女帝，冰蓝与银白配色，裹身长袍、宽腰封，恰好九条冰龙环绕，头顶正上方双层光环，7.2 头身。",
        "expect_min_drift": 3,
    },
    {
        "name": "锚点未变（只改光）",
        "old": "3:4 全身，冰蓝与银白，冰晶肩甲、护臂、腰封，恰好九条冰龙，7.2 头身，左上柔光。",
        "new": "3:4 全身，冰蓝与银白，冰晶肩甲、护臂、腰封，恰好九条冰龙，7.2 头身，右后侧逆光。",
        "expect_max_drift": 0,
    },
    {
        "name": "数量漂移（九条 → 五条）",
        "old": "九条冰龙环绕，七头身，银白长发，冰蓝眼眸。",
        "new": "五条冰龙环绕，七头身，银白长发，冰蓝眼眸。",
        "expect_min_drift": 1,
    },
]


def self_test() -> int:
    failed = 0
    for c in CASES:
        rep = diff(c["old"], c["new"])
        d = drift_score(rep)
        ok = True
        if "expect_min_drift" in c and d < c["expect_min_drift"]:
            ok = False
        if "expect_max_drift" in c and d > c["expect_max_drift"]:
            ok = False
        print(f"[{'PASS' if ok else 'FAIL'}] {c['name']}  drift={d}")
        if not ok:
            failed += 1
            print(render(rep))
    print("")
    print(f"自测：{len(CASES) - failed}/{len(CASES)} 通过")
    return 0 if failed == 0 else 1


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="两版提示词的锚点漂移核对")
    p.add_argument("--old", help="上一版提示词文件")
    p.add_argument("--new", help="这一版提示词文件")
    p.add_argument("--json", action="store_true", help="输出 JSON")
    p.add_argument("--strict", action="store_true", help="有漂移则退出码 1（可接进流水线）")
    p.add_argument("--self-test", action="store_true", help="运行内置自测")
    args = p.parse_args(argv)

    if args.self_test:
        return self_test()
    if not (args.old and args.new):
        p.print_help()
        print("\n提示：两版提示词请用 --old / --new 传文件路径（长中文建议存文件）。")
        return 2
    try:
        old = open(args.old, encoding="utf-8").read()
        new = open(args.new, encoding="utf-8").read()
    except OSError as e:
        print(f"读取失败：{e}", file=sys.stderr)
        return 2

    rep = diff(old, new)
    print(render(rep, as_json=args.json))
    if args.strict and drift_score(rep) > 0:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

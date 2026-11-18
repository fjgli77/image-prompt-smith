# 真人定妆四视图：把一张照片锁成可用的设定卡

> 这份文件治的是**另一类事**：不是"设计一个新角色"，而是**"这个人不能变"**。
> 用户挂上一张真人照片，要的是影视前期的定妆四视图——四个角度必须是同一个人，脸不许被"优化"。

---

## 〇、触发与输入

**上传人物参考图本身就是启动信号。** 他把照片挂上来，哪怕一句话没说、或只说"做个设定图""能做成设定卡吗"，都直接按本流程跑。

**不要先反问"你想做成什么图"**——四视图就是他要的，问了只是把压力推回去。

| 情况 | 处理 |
|---|---|
| 一张正脸照 | 能做。**侧脸与背面只能是推断**，交付时点明 |
| 正脸 + 侧脸 + 全身各一张 | 最稳，四格都有事实依据 |
| 多张同一人不同角度 | 好，全部挂上，当作同一人的多角度证据 |
| 明显不是人像（风景 / 物体 / 插画） | 转到 `object-views.md`，或问一句要哪一个 |
| 明显是几个不同的真人 | **问一句用哪一个**，不要自行挑 |

除以上，**不做前置校验**：不查分辨率、不问用途、不问风格。

---

## 一、四格定义

一张图里 2×2 四格，四格等大，细分割缝：

| 位置 | 标签 | 内容 | 为什么这样定 |
|---|---|---|---|
| 左上 | `FACE FRONT` | 头肩特写，正面朝镜头，平静中性表情，眼睛睁开但不瞪 | 这张是"身份基准"，全片所有替换都回到这一格对脸 |
| 右上 | `FACE SIDE` | **同等头肩画幅**，干净侧面轮廓，表情与发型与左上一致 | 侧面给鼻梁、下颌角、耳朵位置——这三样是"像不像"的真正关键 |
| 左下 | `BODY FRONT` | 全身正面站姿，双臂自然垂于体侧 | 给身材比例、服装廓形、鞋型 |
| 右下 | `BACK` | 全身背面站姿，**与左下同一站位** | 给后脑发型、背缝、鞋跟高度 |

### 左下全身为什么要"面部低细节"

这是本文件最容易被误解的一条。

| 做法 | 后果 |
|---|---|
| 全身格也把脸画清楚 | 后期改服装、改姿态时，全身格的脸必然跟着动，和左上那一格对不上，反而制造矛盾 |
| **面部保持低细节、不做刻画** | 后期在这格上改什么都自由；需要脸时，从左上格贴过来 |

**写法**：`face left intentionally featureless and low-detail (reserved for later editing)`

> 这条**只适用人物**。动物、物体不要套——五官与毛发就是信息本身。

---

## 二、光：为什么必须是"单硬光 + 5200K + 无补光"

| 参数 | 取值 | 理由 |
|---|---|---|
| 主光 | **单支硬光，机位左前 45°** | 硬光才有明确明暗交界线，能看清颧骨、下颌、鼻梁的真实起伏。柔光会把这些抹平，等于把"结构信息"换成"好看" |
| 色温 | **5200K 中性** | 与日光、多数影棚灯平衡。后期调色从中性起点出发，往暖往冷都不费劲 |
| 补光 | **不打** | 补光会抬高暗部，暗部里恰恰藏着轮廓信息。影视定妆要的就是"半边脸在暗里" |
| 背景 | **浅灰无缝** | 中灰不抢主体、不反射色光。纯白会过曝边缘，纯黑会吃掉深色头发与深色衣 |
| 道具 | **无** | 任何道具都会被后续当成设定的一部分 |
| 阴影 | **只留地面自然接触阴影** | 需要它来判断"这个人站在地面上"，而不是浮着 |

**统一性**：四格的光位、色温、曝光**完全一致**。不一致的设定卡在后期对不上，等于废纸。

---

## 三、完整模板（原样粘，只允许加一行指认）

```text
IMAGE TASK: Convert the uploaded character reference image(s) into a 4-panel character sheet.
CRITICAL PRESERVATION OVERRIDE
The uploaded image(s) are the ONLY design source. Preserve EXACTLY: facial structure, eyes, nose,
mouth shape, hairline and hairstyle, age, skin tone and skin texture (real pores, natural stubble),
body proportion and weight, every garment detail (cut, fabric, seams, wear, hardware), footwear. NO
beautification, NO redesign, NO style drift, NO "improving" the face. The same person, four times —
one identity across all panels.
OUTPUT FORMAT: single image, 2x2 grid, four equal panels, thin gutters, small panel labels in corners:
"FACE FRONT / FACE SIDE / BODY FRONT / BACK".
PANEL 1 — TOP LEFT, FACE FRONT: head-and-shoulders close-up, face directly toward camera, calm
neutral expression, eyes engaged but relaxed.
PANEL 2 — TOP RIGHT, FACE SIDE: same head-and-shoulders scale, clean profile view, same
expression, same hair behavior.
PANEL 3 — BOTTOM LEFT, BODY FRONT: full-body standing pose, front view, face left intentionally
featureless and low-detail (reserved for later editing), weight natural, arms relaxed at sides.
PANEL 4 — BOTTOM RIGHT, BACK: full-body standing pose, rear view — hair from behind, garment
back seams, heel height, same standing spot as PANEL 3.
STUDIO SETUP (all four panels identical): seamless light gray studio background, single hard key light at
45° camera-left, 5200K neutral tone, NO fill light, no set dressing, no props. Only natural contact shadows
on the floor.
QUALITY: photographic character sheet for film production, even exposure, accurate fabric weave,
matte skin, real pores, no gloss. Clean, clinical, production-use.
AVOID:
- FACE: no beauty-filter skin, no glossy TV-drama complexion, no idol makeup, no plastic skin, no face slimming, no enlarged eyes, no skin smoothing
- BODY: no pose change between panels, unneeded accessories, no height change
- LIGHT: no ambient color spill, no rim-light drama
```

**除"§五 图号指认"那一行外，模板正文不增删、不翻译、不改写。**
用户要的是一份可复用的一致配方，改写等于换配方。

---

## 四、负向词怎么放

多数站内出图工具**只有一个正向 prompt 字段**，没有独立 negative 输入框。

| 平台情况 | 处理 |
|---|---|
| 只有正向字段 | 把下面的负面串**接在模板最后**，保留英文原样 |
| 有独立 negative 字段（SD / ComfyUI） | 负向单独填，正向里删掉 `AVOID` 整段 |
| 只认 `--no`（Midjourney） | 写成 `--no beauty filter, plastic skin, face slimming, ...` |

负面串（可直接粘）：

```text
beauty filter, glossy tv-drama skin, idol makeup, plastic skin, face slimming, enlarged eyes, skin smoothing, pose variation, extra accessories, height change, ambient color spill, rim light, dramatic lighting, CG, illustration, 3d render, text, watermark, logo
```

---

## 五、图号指认（挂多张图时必加一行）

模型对"参考哪张图干什么"是模糊的。挂多张时，在模板**正文之前**加：

```text
REFERENCE: 图1 = the sole identity and appearance source. Any additional images (图2, 图3) are the SAME person from other angles, used only to complete facial features, hairstyle and garment details.
```

**这句话在防什么**：防模型把图 2、图 3 理解成"另一个人"，然后在四格里混着画。
它的本质是 `references/12-reference-and-multiframe.md` §四那段"职责声明"的英文定妆版——
**"只取什么 / 完全不取什么 / 目标是什么"**三段的压缩形态。

中文平台写法：

```
图1 是唯一的外貌与身份来源；图2、图3 是同一个人的其他角度，只用来补五官、发型与服装细节，不是另外的人。
```

---

## 六、画幅与裁切

| 情况 | 处理 |
|---|---|
| 用户指定了画幅 | **原样填**，不要换成"最接近"的 |
| 没指定 | **2×2 含两格全身 → 9:16 或 4:5**（每格是竖长条，全身站姿才容得下） |
| 未指定且平台默认 1:1 | 可以出，但每格会变方，全身格容易裁脚；被裁就建议换 9:16 再来一次，**由用户定** |
| 用户要单个视角的大图 | 拆成单张出，别在四格里挤 |

**为什么不是 16:9**：四格 2×2 用 16:9，每格是横向扁条，全身站姿必然裁到大腿。这是几何问题，不是偏好。

---

## 七、不做的事（止损纪律）

**不做**：前置校验｜出图后的自动验收｜自动重做。

用户不满意时，**先问是哪一类**：

| 他说 | 归因 | 改法 |
|---|---|---|
| 脸不像 | 参考图分辨率不足，或模型把"保真"理解成"美化" | 加强 `CRITICAL PRESERVATION OVERRIDE` 段，并把 `NO beautification` 前置；换更高分辨率的参考图 |
| 画风漂了（变成 CG / 插画） | 风格默认先验太强 | 负面里把 `CG, illustration, 3d render` 前移；正向加 `photographic, on-location real photography` |
| 布局错了（不是 2×2 / 多一格） | 格数没封顶 | 加 `exactly four panels, no fifth panel` |
| 四格不是同一人 | 参考图被当成多个人 | 补 §五 的图号指认行 |
| 光不一致 | 没说"四格同光" | 加 `identical exposure and white balance across all four panels` |

**只重做一次，并说明这轮改了什么。** 同一缺陷二次仍不行就停下，如实说明并给可选路径（换参考图 / 改做三视图 / 只出正脸一张）。
**不要连续重画烧额度。**

---

## 八、批量

默认**一次一个角色**。

用户明确说"批量""我有好几个人"时，**每人单独生成一次、逐人交付**——不要拼进同一张图（拼了就是平均分配，谁都像一半）。

---

## 九、与其他文件的分工

| 要 | 去 |
|---|---|
| 非人主体（车 / 衣服 / 枪 / 手办）四视图 | `object-views.md` |
| 不锁真人、要设计新角色的三视图 | `image-types.md` §9–§10 + `view-specs.md` |
| 角度写法与画幅口径 | `view-specs.md` §〇·〇 |
| 参考图职责声明（三段式完整版） | `references/12-reference-and-multiframe.md` §四 |
| 参考图污染（哪些图不能当参考） | `references/12-reference-and-multiframe.md` §三 |
| 要进建模（要正交、要地标线） | `modeling-handoff.md`——**定妆照不是建模图**，别混 |

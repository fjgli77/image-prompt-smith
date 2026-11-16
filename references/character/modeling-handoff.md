# 建模交付：AI 图与 3D 之间那条线

> 建模师视角写的一份"交接规范"。
> 一句话：**AI 给的是设计意图，不是资产。** 分不清这一点，下游会拿着 AI 图问你"为什么布线全是乱的"。

---

## 一、先定可用度：AI 出图的三级

| 级 | 名称 | 能干什么 | 不能干什么 | 典型产出 |
|---|---|---|---|---|
| **C** | 概念级 | 定造型方向、给美术看 | 一切工程用途 | 立绘、氛围图、KV |
| **B** | 参考级 | 建模师照着搭大型、对比例 | 不能量、不能贴图、不能绑 | 三/五视图、转面、服装拆解 |
| **A** | 准工程级 | 可当 Image Plane 直接对位 | **仍不可直接绑定** | 正交三视图 + 地标线 + 色卡 + 尺度表 |

> **现有 skill 里"生产交付级"这个词要打个折**：真正可绑定的资产必须经过人工重拓扑。
> AI 能给到的是 **A 级参考**——已经很值钱（省 2–3 天造型探索），但别承诺"能直接进引擎"。

**判级口诀**：有没有正交、有没有地标线、有没有尺度数字、有没有色值。四个都有 = A 级。

---

## 二、三视图的六个工程条件（缺一不可用）

| # | 条件 | 提示词要写什么 | 不写的后果 |
|---|---|---|---|
| 1 | **真正交** | `orthographic projection, no perspective foreshortening, camera at infinite distance` | 带透视，量不准，Image Plane 对不上 |
| 2 | **同一姿态** | `identical A-pose across all views` | 各视图姿态不同，无法对位 |
| 3 | **同一比例尺** | `identical height, feet aligned to one baseline` + 地标线 | 各格高矮不一，比例作废 |
| 4 | **同一光照** | `flat even lighting from front, no dramatic shadow` | 一侧有强投影，看不出结构 |
| 5 | **无遮挡** | `arms away from body, hair clear of eyes, no cape covering torso` | 手插兜、发盖眼、披风挡身 = 这块没画 |
| 6 | **分开的视图** | `evenly spaced, thin grey divider, plain background` | 视图重叠，切不开 |

**"写了 orthographic 就够了吗？"不够。** 模型会把 orthographic 当风格词，照样给你透视。
必须三条一起写：`orthographic` + `no perspective foreshortening` + `flat even lighting`。

---

## 三、姿态规范（A-Pose 的准确写法）

T-Pose 好量但不利于看肩部造型；A-Pose 更接近绑定姿态。**给建模用 A-Pose。**

```
A-Pose：双臂自然下垂并向外张开 15–45°，手肘微屈不锁死；
手掌朝内（拇指朝前），五指自然分开，指间距不小于一指宽，不交叉不并拢；
双腿与肩同宽，脚尖朝前，膝盖不锁死；下颌微收，视线平视前方。
```

| 项 | 正确 | 错误（建模师会退回） |
|---|---|---|
| 手臂角度 | 15–45° | 贴身体（看不到腋下）/ 90°（T-pose 但没声明） |
| 手掌朝向 | 朝内或朝下 | 朝后（手腕扭转，无法对位） |
| 手指 | 分开，指距 ≥1 指 | 并拢 / 交叉 / 握拳 / 插兜 |
| 腿部 | 与肩同宽 | 交叉站 / 一条腿弯曲（重心偏移） |
| 头部 | 平视，下颌微收 | 歪头 / 低头 / 仰头 |

**为什么手指要分开**：绑定时手部权重是按指缝分的。指头并拢或交叉的图，建模师只能猜，最后手部动画一定穿。

---

## 四、头面部：绑定前的四条硬要求

```
中性表情（neutral expression）、闭嘴、双眼平视睁开、不笑不皱眉；
刘海不遮眼，眉眼完整可见；双耳完整露出，不被头发盖住；发际线清晰可见。
```

| 要求 | 原因 |
|---|---|
| 中性表情 | 表情 morph / blend shape 要从 neutral 起算；笑着的图没法当基准 |
| 闭嘴 | 口型 viseme 需要闭口基型 |
| 眼睛平视睁开 | 眼球朝向要对位；半闭眼无法定瞳位 |
| 发际线清晰 | 头发建模的起点；糊住就只能编 |
| 耳完整 | 耳朵是全脸最容易被头发吃掉的部分，缺了要凭空补 |

> 表情页（P4）另出，**不要和转面页混**。转面页一旦带表情，比例就对不准。

---

## 五、拓扑友好：不能写拓扑，但可以避免"反拓扑设计"

AI 出不了布线。但**它出的造型会决定好不好布线**。提示词里能做的是"避开建模师最恨的五类设计"：

| 反拓扑设计 | 为什么难 | 改成 |
|---|---|---|
| 跨关节的密集横向褶皱 | 肘/膝要环形 loop，横向褶会把 loop 打断 | `loose folds above and below the elbow, clean surface at the joint` |
| 横穿关节的硬质饰物/绑带 | 权重无法分段 | 让饰物在关节上下分段，或写成软质 |
| 极细镂空 / 满身刺绣 | 只能烘贴图，做不出几何 | 改"织纹印花"或"只在局部刺绣" |
| 头发糊成一整块 | 无法分片、无法做动力学 | `hair in distinct clumps with clear separation` |
| 手指并拢 / 手部被遮挡 | 权重与指缝无法分 | 五指分开，或明确"手不入画" |

**一句话**：给建模用的图，**造型要"块面清楚、可拆分"**，不要"细节密到只能当贴图"。

---

## 六、服装分层：必须能拆开

建模与绑定要求服装是**可分层的壳**，不是"一整块布"：

```
分层写法：贴身层（内搭）/ 中间层（外套）/ 外层（披风、罩衫）/ 配件（腰带、护腕、挂饰）
每层写清覆盖边界：袖口到前臂中段、裤脚盖住靴口 2cm、裙摆至膝上 10cm。
```

| 要写 | 例子 |
|---|---|
| 覆盖边界 | `sleeve ends at mid-forearm`、`hem falls 10cm above the knee` |
| 层与层的关系 | `coat worn open over the inner shirt` |
| 与皮肤的关系 | `collar exposes the collarbone`、`cuffs leave the wrists bare` |
| 硬质件的位置 | `shoulder plate sits on the deltoid, not crossing the joint` |

**穿模高发区**（提示词要主动避开）：腋下、肘内侧、胯部、膝后、领口。
写 `loose fit at the armpit and inner elbow` 比事后修模型便宜。

---

## 七、发型建模口径

```
发片/发束，不用单缕：
hair built from distinct clumps (not single strands), visible part line,
hairline clearly defined, volume at the crown, bangs stop above the eyebrows
```

| 项 | 写法 |
|---|---|
| 结构 | `distinct clumps`（分片）/ `strand-based`（细发丝，适合 3D 动漫） |
| 发际线 | 必须可见，位置写清（额前/鬓角/后颈） |
| 刘海 | `stop above the eyebrows`（不压眼） |
| 后脑 | `volume at the back of the skull`（否则后视图是扁的） |
| 长度 | 写到具体位置（`mid-back` / `waist-length`） |

---

## 八、材质与色指定

### 8.1 建模要的是"数值意图"，不是"看起来像"

| 项 | 写法 | 别写 |
|---|---|---|
| 基色 | `base color #2C3E50, muted navy` | `蓝色` |
| 明暗三段 | `#3A4E62 highlight / #2C3E50 base / #1B2733 shadow` | — |
| 粗糙度 | `roughness 0.7, matte` / `roughness 0.15, polished` | `亮亮的` |
| 金属度 | `metalness 1.0, brushed` / `metalness 0, fabric` | `金属感` |
| 透明 | `transmission 0.9, ior 1.45` | `透明` |

### 8.2 三渲二 / 3D 动漫：反而要"去 PBR"

```
flat base color with clear color zones, no grunge maps, no roughness variation,
clean AO only in creases, no specular breakup
```

三渲二建模最怕拿到"写实脏贴图"：凹凸、粗糙变化、过深 AO 进了三渲二材质只会显脏。
**贴图控制在 2048 以内，颜色分区清楚比细节多重要。**

---

## 九、尺度：把比例换成数字

建模按 **1 unit = 1 m** 建。提示词里给一句换算，建模师能省半天：

```
身高 168cm，7 头身 → 头高约 24cm；肩宽 40cm（约 1.65 头宽）；
臂展 ≈ 身高 168cm；脚长 24cm；膝高 46cm。
```

| 项 | 常用值 |
|---|---|
| 头高 | 身高 ÷ 头身比 |
| 肩宽 | 男性 ≈ 2 头宽，女性 ≈ 1.6 头宽 |
| 臂展 | ≈ 身高 |
| 脚长 | ≈ 头高 |
| 膝高 | ≈ 身高 × 0.27 |

---

## 十、AI 做不到的七件事（写进交付说明，别让下游误会）

1. **真拓扑**：布线、四边面、极点位置
2. **UV 展开**：只能给"哪块是什么颜色"，不能给展开图
3. **绑定权重**：蒙皮、骨骼、关节形变
4. **表情 morph / 口型 viseme**：只能给"表情长什么样"，不能给形变目标
5. **布料解算**：只能给静止形态，动力学要另做
6. **严格的多角度一致**：AI 的背面是"猜"的，不是转过去的
7. **可量测的尺寸**：像素比例 ≠ 世界单位

> 所以正确流程是：**AI 出 A 级参考 → 建模师重拓扑 → 三渲二/写实材质 → 绑定**。
> 不要跳过第二步去要求"AI 直接出可绑定模型"。

---

## 十一、建模向提示词模板（整段可抄）

```
角色建模参考图，character model reference sheet，16:9 横版，写实风格
（按项目替换：三渲二 / 国漫半写实 / 全 3D 写实）。
五视图水平排列：正面、左侧面、背面、3/4前视、头部特写，仅此 5 格，不增加任何额外画格。
orthographic projection, no perspective foreshortening, camera at infinite distance,
flat even lighting from the front, no dramatic shadow, plain light grey background.

姿态：identical A-Pose across all views，双臂外张 30°，手肘微屈，
手掌朝内，五指自然分开、指距一指宽；双腿与肩同宽，脚尖朝前；
下颌微收，平视前方，中性表情，闭嘴，双眼睁开。

比例：身高 168cm，7 头身；肩宽约 1.65 头宽；脚底对齐同一水平线，
头顶、眼线、肩线、腰线、髋线、膝线、脚底七条水平地标线贯通全图。

服装分层：内层白色交领衫、中层深蓝短外套、外层无披挂；
袖口止于前臂中段，下摆至髋下 12cm，领口露出锁骨；腋下与肘内侧留松量。

发型：hair in distinct clumps, visible part line, hairline clearly defined,
bangs stop above the eyebrows, volume at the back of the skull.

材质：matte wool (roughness 0.7)、brushed silver (metalness 1.0)、
smooth stylized skin, no pores。

【外貌锚点：<逐字复制>】
不出现文字、logo、水印、地面阴影、场景元素。
```

---

## 十二、交付自查（建模师会逐条看）

- [ ] 写了 `orthographic` + `no perspective foreshortening`
- [ ] 各视图姿态一致（同一 A-Pose）
- [ ] A-Pose 手臂 15–45°，手指分开，手掌朝内
- [ ] 中性表情、闭嘴、平视、眉眼可见
- [ ] 刘海不压眼、双耳露出、发际线可见
- [ ] 有七条水平地标线
- [ ] 有身高与头身比（能换算数字）
- [ ] 服装分层且覆盖边界写清
- [ ] 关节处没有横跨的硬物与密集褶
- [ ] 纯色底、无地面阴影、无场景元素、无文字
- [ ] 色值给了十六进制或三段明暗
- [ ] 交付说明里写清"AI 图不可直接绑定"

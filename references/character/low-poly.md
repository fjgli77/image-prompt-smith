# 低多边形：面数预算法

> 依据：高部《ローポリで極めるキャラクターモデリング》的"轮廓/剪影/色块/平面化"路线，
> 交叉 polylusion（面数分配实测）、Jon Jones（细节级别一致性）、PromptAtlas（面片语法）。
>
> 一句话：**低模不是"面少"，是"面要花在眼睛会去的地方"。**
> 面数均分的低模，看起来永远廉价——不是因为少，是因为没有重点。

---

## 零、为什么单独开一份

`character-styles.md` 里"低模/极简"只占四行词，不够用。原因是低模有**三条硬约束**，任何一条错都救不回来：

| 约束 | 高模可以靠什么遮掩 | 低模没有 |
|---|---|---|
| 剪影 | 毛孔、缝线、单根发丝 | 只剩形状 |
| 配色 | 贴图细节、材质层次 | 只剩三块颜色 |
| 面片方向 | 细分曲面糊平 | 每条边都在明暗里露出来 |

所以低模是**形状语言的极限测试**：`aesthetics.md` 的六轴在低模上不是"建议"，是"全部家当"。

---

## 一、面数预算：不均分才好看

典型低模角色 **200–1000 三角面**（手游低模 500–1500）。**预算怎么分，决定好不好看。**

| 部位 | 预算占比 | 理由 | 提示词写法 |
|---|---|---|---|
| **头与脸** | 最高，40–50% | 玩家第一眼看这里 | `dense small facets across the head and face` |
| **手** | 高于预期 | 持物、交互、动作最容易被注意到 | `five separated fingers with visible facet edges` |
| **肩 / 髋 / 肘 / 膝** | 中 | 形变区，面不够弯曲就折 | `enough facets at the shoulder and hip to bend cleanly` |
| **躯干** | 极低 | 可以被一件外套概括 | `torso as a beveled box with large flat planes` |
| **腿** | 低 | 管状 + 膝盖一个折点 | `legs as tapered tubes with a single facet at the knee` |
| **脚** | 最低 | 通常在画面下缘或被地面吃掉 | `feet as simple wedges` |
| **配件** | 点缀 | 用来打破剪影，不堆量 | `one asymmetric accessory, minimal other props` |

### 三条铁律

1. **面数不许均分。** 每处密度一样 = 视觉上处处一样 = 没有视觉焦点。这是低模第一号廉价感来源。
2. **细节跟着视线走。** 第三人称视角下，后脑、肩、背反而比正面更常被看到——预算要给"看得最多的那面"，不是"最漂亮的那面"。
3. **同图内细节级别必须一致。** 一块 50 尺高的石头 24 面、旁边 3 尺的凳子 1000 面——假。除非那块石头是远景背景。

### 提示词怎么写"面数"

模型不懂"面数"，但懂**面片大小**。所以不要写 `low poly, 800 tris`，要写**哪密哪疏**：

```
头部与双手面片细密，躯干与腿部为大块平面；
面片大小随部位递减，不做均匀网格。
```
```
dense small facets at the head and hands, large flat planes on the torso and legs,
facet size scales with importance, not a uniform mesh
```

> **这条比任何 `low poly` 标签都有效** —— 它把"预算分配"这件建模师才懂的事，翻译成了模型能执行的描述。

---

## 二、剪影：低模唯一能用的信息

**填黑测试**在低模上是唯一标准：填成纯黑，还认得出是谁、在做什么吗？

高模靠细节区分角色；低模**只有形状**，形状得把活全干了。

| 形态 | 读出来的性格 |
|---|---|
| 宽肩 | 力量、可靠 |
| 细高 | 敏捷、轻盈 |
| 大头 | 风格化、喜剧、可爱 |
| 不对称 | 记忆点（低模最重要的东西） |

### 打破人形轮廓的四件附件

低模角色的辨识度几乎全靠"轮廓上的异物"：

```
帽子 / 披风 / 武器 / 异形发型
```
任选一件，**且只选一件**（两件以上会互相抵消，变成"装备很多的人"而不是"那个人"）。

```
distinctive silhouette break at the head and one shoulder,
one oversized asymmetric accessory, clean outline readable at thumbnail size
```

---

## 三、面片朝向就是形体

Jon Jones 那句最狠的话：**脸上翻一条边，就是"颧骨分明"和"脸胖"的区别。**

低模的面片不是"网格"，是**用三角面拼出来的雕塑**。每条边的走向都在暗示曲面：

| 部位 | 面片应该怎么走 | 提示词不能写"翻边"，但能写这个 |
|---|---|---|
| 额头 | 向上、向发际线收 | `facet edges flow upward across the forehead` |
| 颧骨 | 斜向下，形成一条硬的转折 | `a hard facet edge along the cheekbone` |
| 下颌 | 向耳朵方向 | `planar jaw with a single diagonal facet` |
| 鼻梁 | 一条竖向窄面 | `one narrow vertical facet for the nose bridge` |
| 肩 | 从颈根向外放射 | `facets radiating outward from the shoulder` |

### 三种面片语言（选一种，全图统一）

| 语言 | 面片特征 | 适合 | 提示词 |
|---|---|---|---|
| **硬折（angular）** | 大三角面、锐转折 | 科幻、机械、战斗 | `angular faceted geometry, hard facet edges, flat shaded` |
| **圆化低模（rounded low poly）** | 面少但转折圆 | 角色向、治愈 | `rounded low poly, softened facet transitions, still visibly faceted` |
| **晶体（crystalline）** | 长短面片混搭、锐利 | 幻想、魔法、Boss | `crystalline faceted body, sharp large planes, few small facets` |

**混语言 = 崩。** 一个角色身上同时有"大三角硬折"和"圆化过渡"，看起来像两个人拼的。

---

## 四、三色规则（没有贴图，颜色就是人格）

低模没有贴图承载信息，**颜色是仅次于剪影的性格工具**。

```
主色 60–70% + 次色 25–35% + 点缀色 5%
```

| 规则 | 说明 |
|---|---|
| **只三色** | 第四色开始就没有主次了。Superhot 全是红，Among Us 是单色身体 + 异色面罩 |
| **远处可辨** | 缩到 64px 还分得清两个角色，才算过关 |
| **明度差 > 色相差** | 远处先靠明暗分层，再靠色相；只靠色相会糊成一片 |
| **角色之间要对比** | 主角暖调，反派冷调；主角饱和，NPC 降饱和——**这是场景可读性的来源** |

```
three-color palette: dominant moss green, secondary warm cream, single rust accent,
strong value separation between the three, no gradient
```

---

## 五、光只干一件事：让面片生成明暗图案

低模的光不是为了"氛围"，是为了**把三角面读成形体**。

| 做法 | 原因 |
|---|---|
| **单一主光方向** | 多光源会把面片的明暗关系抵消掉，面片就"平"了 |
| **硬光 / 硬阴影** | 软光把转折糊掉，低模最怕这个 |
| **AO 克制** | AO 糊满 = 所有缝隙一样黑 = 面片读不出来 |
| **背景必须更简单** | 主体低模 + 复杂场景 = 双输，剪影立刻失效 |

```
single hard key light from upper left, crisp triangular shadow planes,
flat ambient fill, no soft gradient, simple neutral backdrop
```

### 中性光测试

把角色放到中性光下看一眼。**如果它在平光里"死"了，是剪影或配色的问题，不要用特效去遮。**

---

## 六、面数档位表（按用途选）

| 档 | 三角面 | 用途 | 头身比 | 面片语言 |
|---|---|---|---|---|
| 极简艺术向 | 200–500 | 艺术短片、图标、海报 | 5–7 | 硬折 / 晶体 |
| 手游低模 | 500–1500 | 移动端、独立游戏 | 5.5–7 | 圆化低模 |
| 桌面 / 主机低模向 | 1500–5000 | 风格化独立游戏、买量素材 | 6–7.5 | 硬折 |
| 高精度低模 | 5000–12000 | 需要近景的"低模风" | 7–8 | 硬折（小面片） |

> 提示词只写"风格档位 + 面片大小分布"，**不要写具体三角数**——模型不执行数字，只会把它当一个风格词。

---

## 七、成品块（整段抄）

### ① 中文（Seedream / 即梦）

```
低多边形风格角色，硬折面片，全身立绘，2:3。相机与腰部同高，50mm 镜头。
头部与双手面片细密，躯干与双腿为大块平面，面片大小按部位递减，不做均匀网格。
剪影在头部与单肩处有一处明显凸起（一顶异形帽），轮廓在缩略图尺寸仍可辨认；
四肢与躯干之间留出可见空隙，无相切轮廓。
三色配色：主色苔绿占七成，次色暖米占三成，点缀色锈红仅用于一条围巾。
单一硬光从左上方打入，形成清晰的三角面明暗块，环境补光平而不糊，无柔和渐变。
简单中性背景，画面中不出现文字、水印、多余物件。
```

### ② 英文（MJ / Flux / SD）

```
low poly character, hard faceted geometry, flat shaded, stylized 3D game character,
full body, 2:3, eye-level camera, 50mm lens,
dense small facets on the head and hands, large flat planes on the torso and legs,
facet size scales with importance, not a uniform mesh,
distinctive silhouette break at the head and one shoulder, readable at thumbnail size,
clear negative space between arms and torso, no tangent contours,
three-color palette: dominant moss green, secondary warm cream, single rust accent,
strong value separation, no gradient,
single hard key light from upper left, crisp triangular shadow planes, flat ambient fill,
simple neutral backdrop, no text, no watermark, no extra props
```

**隔离反向**：

```
smooth subdivision, photorealistic pores, dense micro detail, noisy topology,
uniform mesh density, gradient shading, soft airbrush, cluttered background,
lace, embroidery, single hair strands, thin wire details, floating fragments
```

---

## 八、八个崩坏点

| 现象 | 根因 | 改法 |
|---|---|---|
| 看起来像"高模降采样" | 写了 `low poly` 但没写面片分区 | 补"头手密、躯干腿疏" |
| 廉价感 | 面数均分 | 同上；并砍掉一半配件 |
| 剪影认不出 | 没有打破人形轮廓的附件 | 加一件（帽/披风/武器/异形发型） |
| 面片像马赛克滤镜 | 只是给写实图加了多边形滤镜 | 写 `flat shaded, large planar facets`，并禁 `photorealistic` |
| 颜色脏 | 四色以上 + 渐变 | 砍到三色，禁 gradient |
| 面片读不出形体 | 多光源 / 软光 / AO 糊满 | 单一硬光 + 平补光 |
| 手上糊成一团 | 手在低模上是第二大坑 | `five separated fingers with visible facet edges` 或藏手 |
| 同一图里细节级别不一 | 配件细节比主体高 | 统一级别，或把配件降级为一个大平面 |

---

## 九、八项自检

- [ ] 写了面片密度的**分区**（哪密哪疏），不是一句 `low poly`
- [ ] 面数不均分，头与手最密
- [ ] 有一件打破人形轮廓的附件，且只一件
- [ ] 缩略图尺寸下剪影可辨
- [ ] 面片语言三选一，全图统一
- [ ] 三色以内，且有明度差
- [ ] 单一主光 + 硬阴影，没有软渐变
- [ ] 背景比主体简单

---

## 十、和其他文件的关系

| 要写什么 | 读哪份 |
|---|---|
| 形状 / 剪影 / 体块 / 夸张幅度 | `aesthetics.md`（低模必须先把这页吃透） |
| 低模的**面数与面片** | **本文件** |
| 低模属于哪个风格家族 | `character-styles.md` §二「低模 / 极简」 |
| 低模的渲染介质写法 | `render-styles.md` |
| 低模要交给建模 / 直接生成 3D | `modeling-handoff.md` + `text-to-3d.md` |

**顺序**：先在 `aesthetics.md` 定形状，再回本文件分配面数。**低模没有第二次机会——第一次剪影不对，就是不对。**

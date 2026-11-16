# 纯文字一致性工作流（不依赖参考图）

**本技能的首选路径。** 不喂参考图、不做 LoRA、不训模型——**只靠一段写死的文字锚点，让同一角色在多图、多角度、多场景、多风格里保持是同一个人。**

参考图是"外挂"，纯文字是"内功"。内功练好了，任何平台、任何模型、任何端口都能用（很多国产模型 / 网页版 / 手机 App 根本不支持参考图）。

> 铁律：**能不用参考图就别用。** 参考图只作为"锦上添花"的可选增强（见第七节），核心一致性永远靠文字锚点。

---

## 一、为什么纯文字能锁住角色

AI 没有记忆，但它有**确定性**：同样的提示词 + 同样的种子 → 几乎相同的图。这就给了纯文字路线三个抓手：

| 抓手 | 原理 | 用法 |
|---|---|---|
| **逐字复制** | 锚点段一字不改 → 激活同样的 token 序列 | 锚点块单独成段，跨图原样粘贴 |
| **固定种子** | 同种子同提示词 → 构图与五官高度稳定 | 系列图固定 seed |
| **特征加权** | 权重词强化关键特征 | 三不变特征加权重 |

**把锚点表当成"文字版 LoRA"**：你写的不是描述，而是一段**代码**。改一个词就等于改了角色的基因。

---

## 二、七大锁定手段（按重要性排序）

### 1. 锚点块逐字复制（第一重要）

把角色锚点写成**独立成段、格式固定**的文本块，每条提示词**原样粘贴**，一个标点都不改：

```
CHARACTER ANCHOR (do not alter):
19-year-old East Asian girl, oval face, delicate features,
almond-shaped ice-blue eyes with double eyelids, straight thin brows,
small button nose, soft pink lips, small beauty mark under right eye,
silver-grey long wavy hair with center part and side bangs,
slim elegant build, 170cm, 7.5-head-tall.
```

**为什么有效**：模型对**固定位置、固定格式**的重复内容会形成稳定激活。锚点块放**提示词最前面**（权重最高位），并用 `CHARACTER ANCHOR (do not alter)` 这种"指令式"框标，模型会优先守住。

### 2. 三不变特征 + 唯一识别串（第二重要）

从锚点里再挑 **3 个最特殊的特征**，组成一个**短到不可能被忽略**的识别串，紧跟在锚点块之后重复一次：

```
Signature features (must appear in every image):
ice-blue almond eyes + silver-grey wavy hair + beauty mark under right eye.
```

- 特征**越具体越稳**：`beauty mark under right eye` >> `beauty mark`。
- 特征**要有区分度**：别选"黑发大眼"（几亿张图都有），要选"银灰卷发/异色瞳/左泪痣/右眉疤"。
- **一张图只留 1–3 个**特殊标记，多了会互相打架。

### 3. 固定种子（跨图锁构图）

同一种子 + 同一提示词 = 同一张图。系列图做法：

```
图1（定妆）: [锚点块] + [正面全身]  --seed 12345
图2（换场景）: [锚点块一字不动] + [新场景]  --seed 12345
图3（换角度）: [锚点块一字不动] + [侧面]  --seed 12345
```

- 想**脸部完全一致**：种子固定 + 只改场景段。
- 想**姿态不同但脸一致**：种子改，锚点块不动（靠文字锁脸）。
- SD 用固定 seed；MJ 用 `--seed`；Seedream/即梦多数不支持种子，靠锚点块硬扛。

### 4. 固定词序与句式（防漂移）

**同一个特征，永远用同一个写法。** 别这次写 `silver-grey hair`、下次写 `grey-silver hair`、再下次写 `silver hair`——模型会当成三种不同的头发。

建锚点表时就把英文定稿，之后**只复制不重写**。

### 5. 特征加权（把关键特征"顶上去"）

支持的平台给三不变特征加权重：

- SD/NovelAI：`(ice-blue almond eyes:1.2), (silver-grey wavy hair:1.15), (beauty mark under right eye:1.3)`
- MJ：无需权重，靠 `::` 分隔或前置位置
- Seedream/豆包：重复强调，如"她的银灰色波浪长发和冰蓝色杏眼要保持一致"

> 权重别超 1.3，否则五官会"焊死"变形。

### 6. 负面锁定（防漂到"另一个人"）

反向词里明确禁止**换脸/换发/换装**：

```
different face, different person, changed hairstyle, changed hair color,
changed eye color, changed outfit, inconsistent features,
mole missing, missing beauty mark, mismatched clothing
```

这条是纯文字路线**最容易被忽略却最有效**的一招——直接告诉模型"不许变"。

### 7. 一次多视图 / 分格生成（廉价一致性）

多视图本身就带一致性约束（同一张图里角色必须统一）：

- **一图多格**（三/四视图）：模型在同一画布内会尽量统一角色，一致性天然较高，但格数越多越崩。
- **分格生成**（更稳）：固定锚点块，只换视图词（正面/侧面/背面），逐张生成后拼版。

---

## 三、纯文字三步法

### Step 1 — 建立锚点表（定稿，之后只复制）

按 `appearance-anchors.md` 的模板填，**英文定稿**。这一步是整个流程的地基，**花时间最多的应该在这里**。

```markdown
## 角色锚点表 — <角色名>

### 锚点块（逐字复制，永不改动）
CHARACTER ANCHOR (do not alter):
<年龄性别种族>, <脸型>, <眼型+瞳色>, <眉>, <鼻>, <唇>, <特殊标记>,
<发型发色>, <身形+身高+头身比>, <默认服装套装>.

### 三不变特征（Signature）
- 特征1：<最特殊的一个>（如：冰蓝杏眼）
- 特征2：<发色发型>（如：银灰波浪长发）
- 特征3：<标记>（如：右眼下泪痣）

### 识别串（紧跟锚点块重复一次）
Signature features: <特征1> + <特征2> + <特征3>.

### 服装锚点（逐字复制）
<上衣>, <下装>, <鞋>, <配饰>.
```

### Step 2 — 纯文字定妆（出第一张"标准脸"）

用锚点块 + 最简单的构图（正面、中性表情、纯色背景、全身或半身），出一张满意的定妆图。

- 提示词**只保留锚点块 + 构图 + 风格 + 光照**，不要有场景、动作、情节干扰。
- 这张图是"标准答案"，后续所有图都对照它检查。
- 不满意就**微调锚点表**（改一个词），重出——直到定妆图满意为止。

### Step 3 — 文字回读迭代（把满意的图"翻译回"文字）

得到满意的定妆图后，**不要存下来当参考图用**，而是：

1. **观察**：图里角色的发型弧度、瞳色深浅、装饰位置等细节，和你的文字是否一致？
2. **补词**：把图上满意但你文字里没写的细节**补进锚点表**（如发现刘海是三七分，就加 `side-swept bangs, 3:7 part`）。
3. **校准**：把文字里但图上没体现的词，加强权重或换个说法。
4. **固化**：锚点表更新后**冻结**，之后所有图都用这一版。

> **这就是纯文字路线的核心循环：写词 → 出图 → 看图 → 改词 → 冻结。** 迭代 2–3 轮，锚点表就成了一副稳定的"文字模具"。

---

## 四、纯文字提示词模板（可直接用）

### 通用模板

```
【锚点块 · 逐字复制】
CHARACTER ANCHOR (do not alter):
<锚点表内容>

【识别串 · 重复强调】
Signature features: <特征1> + <特征2> + <特征3>.

【本次变量 · 只改这里】
<动作> + <场景/视角> + <表情>

【风格块 · 从 render-styles.md 抄】
<3D写实/2D动画/Q版等风格块>

【光照】
<统一光照>

【画质】
8K, ultra-detailed, sharp details, consistent character design
```

### 三视图（纯文字）

```
角色三视图设定稿，character turnaround sheet，同一角色并排三个完整全身立绘：
左：正面视角；中：正侧面90度视角；右：背面视角。

【锚点块 · 逐字复制】
19-year-old East Asian girl, oval face, almond-shaped ice-blue eyes,
straight thin brows, small button nose, soft pink lips,
small beauty mark under right eye, silver-grey long wavy hair with center part,
slim elegant build, 170cm, 7.5-head-tall,
wearing white lace corset top and silver-blue sheer chiffon overlay with ribbon,
high-slit skirt, crystal strappy high heels.

【识别串】Signature features: ice-blue almond eyes + silver-grey wavy hair + beauty mark under right eye.
【三视图铁律】三格人物身高比例完全一致、脚底对齐同一水平线、服装造型完全一致。
【风格】<风格块>
【背景】纯白背景，无阴影投地，等距排列，细灰分隔线。
【光照】左上45度均匀柔光。
【画质】8K，全身完整，锐利细节。
```

### 跨场景一致性（纯文字）

```
【与上一张图完全相同的锚点块 · 逐字复制】
CHARACTER ANCHOR (do not alter): <原样粘贴，一个标点都不改>
Signature features: <原样粘贴>.

【本次变量 · 只改场景与动作】
她走在傍晚雨后的城市街道上，霓虹灯倒映在湿漉漉的路面，微微回眸看向镜头，表情平静。
电影感写实光照，深夜蓝紫色调，半身构图，竖版 2:3。

【风格】<与前图完全相同的风格块>
【画质】8K，角色与设定保持一致。
```

> **关键**：跨场景那张，**只改"本次变量"段，锚点块和识别串一个字都不动**。这是纯文字一致性的全部秘密。

---

## 五、纯文字 × 风格切换

同一角色出 3D 版、2D 版、Q版（**全部纯文字，不喂图**）：

1. **锚点块不动**（脸型/瞳色/发型/标记/服装）——这是身份。
2. **风格块整段替换**——这是渲染方式。
3. **头身比跟着风格改**（写实 7.5 头 ↔ Q版 3.5 头）——这是唯一允许动的比例。
4. **识别串照旧保留**，保证 Q版也能认得出是同一人。

```
3D版：【锚点块】+【识别串】+ 3D rendered, PBR, subsurface scattering, UE5, 7.5-head-tall
2D版：【锚点块】+【识别串】+ 2D anime, cel shading, flat colors, clean lineart, 7-head-tall
Q版：【锚点块】+【识别串】+ chibi, super-deformed, big head small body, 3.5-head-tall, designer toy
```

---

## 六、反向提示词（纯文字一致性专用）

```
different face, different person, changed hairstyle, changed hair color,
changed eye color, changed outfit, inconsistent features, mole missing,
missing beauty mark, mismatched clothing, inconsistent skin tone,
morphing face between images
```
中文：`换脸, 变人, 发型变了, 发色变了, 瞳色变了, 服装不一致, 特征丢失, 泪痣消失, 系列图不像同一人`

---

## 七、参考图：可选增强，不是必需

> **纯文字已经够用。** 只有在追求"像素级复刻"（如商用交付、影视级一致性）时，才叠加参考图。参考图是**加速度**，不是**发动机**。

需要叠加时（顺序：先文字，后参考图）：

| 平台 | 增强手段 | 说明 |
|---|---|---|
| MJ | `--cref [url] --cw 80` | 文字描述仍是主体，cref 只补身份 |
| SD/ComfyUI | IP-Adapter weight 0.65–0.75 | 同上；纯文字路线下可将权重降到 0.5 |
| Seedream/即梦 | 上传参考图 + 文字分工 | 文字写明"保持锚点不变" |

**铁律不变**：即使加了参考图，**锚点块也必须写全**。参考图负责"像"，文字负责"稳"，两者叠加才最强；只有文字也不会差。

---

## 八、一致性自查评分表

出图后逐项打分（每项 1 分，低于 6 分就回退改锚点）：

| # | 检查项 | 通过 |
|---|---|---|
| 1 | 脸型与锚点一致 | ☐ |
| 2 | 眼型与瞳色一致 | ☐ |
| 3 | 发型、发长、发色一致（尤其背面视图） | ☐ |
| 4 | 三不变特征全部出现 | ☐ |
| 5 | 服装部件、层次、闭合方式一致 | ☐ |
| 6 | 配色一致（主/辅/强调色守住） | ☐ |
| 7 | 多角度下肩线/身高/脚底线对齐 | ☐ |
| 8 | 风格与系列前图一致 | ☐ |
| 9 | 光照方向统一 | ☐ |
| 10 | 整体"是同一人"的直觉判断 | ☐ |

**10 分 = 可直接用于系列图；8–9 分 = 微调锚点表；≤7 分 = 重建锚点表或换措辞。**

---

## 九、纯文字一致性速查（背下来）

| 手段 | 一句话 |
|---|---|
| 锚点块 | 独立成段，**逐字复制**，放最前 |
| 识别串 | 3 个特殊特征，紧跟锚点块重复一次 |
| 固定种子 | 同种子同提示词 = 同图 |
| 固定词序 | 同特征永远同一写法，别改同义表述 |
| 特征加权 | 关键特征 1.15–1.3，别超 |
| 负面锁定 | 反向词写"不许换脸换发换装" |
| 只改一个变量 | 每次迭代只动一处，其余冻结 |
| 三步法 | 建表 → 定妆 → 回读改词 → 冻结 |

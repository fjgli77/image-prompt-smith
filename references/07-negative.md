# 07 反向词与隔离矩阵

> **反向词不是越多越好。** 20 个精准反向 > 200 个万能反向。
> 反向的作用是**堵住这个模型的坏习惯**，不是罗列世界上所有丑东西。

---

## 〇、先判：这次该用反向、正面穷举，还是两个都用

历史上"独立负向框"和"正面穷举替代反向"两条策略并排讲，读者会双轨叠加（既有 `no text` 又有"画面无文字"）。**先按下表定一种主策略。**

| 平台有没有真负向字段 | 主策略 | 辅策略 | 不要做 |
|---|---|---|---|
| **有**（SD / ComfyUI、通义万相、Ideogram 的 negative） | **独立负向框** | 关键约束在正向再写一句结构描述 | 不要把负向内容塞进正向当 `no xxx` |
| **弱**（MJ 的 `--no`、Seedream/即梦的末尾排除项） | **正向穷举为主** | 末尾补 ≤6 个排除词 | 不要给 MJ 塞 30 条 `--no`，会稀释主体 |
| **无**（Flux 多数实现、GPT Image 部分版本） | **纯正面穷举** | 只写"画面里有什么"，不写"没有什么" | 不要写 `no text`——会被当正向词 |

### 三种图型的默认排除项（照抄即可，不要扩写）

| 图型 | 必排 | 可排 | 别排 |
|---|---|---|---|
| **角色立绘 / 设定稿** | 文字、水印、多余肢体、手指畸形 | 格号/箭头（多格时）、多余配饰 | 不要排"阴影/高光"——会把光也排掉 |
| **产品 / 电商** | 文字、logo、多余物体、杂乱背景 | 反光过曝 | 不要排"reflection"——玻璃质感靠它 |
| **海报 / KV** | 乱码文字、二维码、水印 | 多余元素 | 不要排"negative space"——留白要它 |

> **记忆句**：**有负向框就用框，没框就写"有什么"，写得越具体越不需要说"没什么"。**

---

## 一、按平台写反向

| 平台 | 写法 | 示例 |
|---|---|---|
| SDXL / ComfyUI | 独立 negative 字段 | `text, watermark, extra fingers, plastic, oversaturated` |
| Midjourney | `--no` 参数 | `--no text, watermark, extra objects` |
| Flux | 正向否定句（无 negative） | `The frame contains no lettering. All surfaces are blank.` |
| Nano Banana Pro | 末尾"禁止"段 | `禁止：不得出现文字、水印；不得添加其他物体；不得改变主体形状` |
| GPT Image 2 | 正向禁令句 | `Do not include any text, logos, or people.` |
| Seedream 5 / 即梦 | 末尾排除项 | `画面中不出现文字、水印、其他物体，主体形状不得改变` |
| 通义万相 | 独立负向框 | 同 SD 写法，中文亦可 |

> ⚠️ **最常见错误**：在正向里写 `no text` / `no watermark`。SD 会理解成"要 text 和 watermark"。

---

## 一·五 正面穷举：比反向更强的排除法

> 来自 `libtv-video-agent` 的实测：**负面指令很弱，甚至"提名字就召唤"**（"别想大象"效应）。
> 写 `禁止出现狗`，狗反而更容易出现；连写三版都改不掉，换成"有且只有"一次就清爽。

**原理**：否定式要在模型内部先构建那个物体再擦掉；白名单式直接规定画面里有什么，没给其他东西留位置。

| 弱写法 | 强写法 |
|---|---|
| `不要出现狗` / `no dog` | `画面里有且只有：女主、漂浮姿态、蓝色海水、珊瑚` |
| `不要杂乱` | `画面中只有三件物品：…、…、…` |
| `不要有人` | `空旷无人的空间，只有一张桌子和一把椅子` |
| `不要多余的杯子` | `桌面上只有一只米白陶瓷杯` |

**写法公式**

```
画面里有且只有：〔元素1〕、〔元素2〕、〔背景〕。
除上述之外不出现任何其他生物、人物、道具，构图干净、主体明确。
（通篇不再提那个不想要的元素的名字。）
```

**用哪个**

- 单一元素反复出现（多一只手、多一只动物、多一个人）→ **正面穷举 + 数量铁律**（见 12）
- 一类质感跑偏（塑料感、过曝、糊）→ **反向词**更有效
- 平台没有独立负向（Flux / GPT Image / Seedream）→ **只能正面穷举**

---

## 二、基础反向库（分五组，按需取 3–6 个）

### 组 1｜技术瑕疵（几乎总要）

```
lowres, blurry, out of focus, jpeg artifacts, noisy, pixelated, distorted, warped,
deformed, bad anatomy, extra limbs, extra fingers, fused fingers, malformed hands,
cropped, cut off, watermark, signature, username, text, logo
```

中文：`低分辨率、模糊、失焦、噪点、变形、肢体错乱、多余手指、裁切、水印、签名、文字、标志`

### 组 2｜质感崩坏

```
plastic look, waxy skin, oversmooth, over-retouched, airbrushed, doll-like,
flat lighting, dull colors, gray cast, HDR halos, oversaturated, chromatic aberration
```

中文：`塑料感、蜡感皮肤、过度磨皮、喷枪感、平光、发灰、HDR 光晕、过饱和`

### 组 3｜风格串味

```
anime, cartoon, illustration, painting, 3d render, CGI, sketch, vector, clipart,
comic, cel shading, chibi, doll, toy
```

> **这组是"隔离反向"，按主风格反着写**：主风格是摄影就全选；主风格是插画就选摄影类词（`photo, realistic, DSLR`）。

### 组 4｜内容多余

```
cluttered, busy background, extra objects, duplicate, multiple subjects,
text overlay, banner, frame, border, collage, split screen
```

中文：`杂乱、背景繁复、多余物体、重复、多主体、文字覆盖、边框、拼贴、分屏`

### 组 5｜氛围跑偏

```
oversaturated, neon, lens flare, heavy vignette, fog, smoke, rain, sunset,
dramatic shadows, high contrast
```

> 这组是**"不要什么氛围"**时用。夜景图反向里写 `bright daylight`；白天图反向里写 `night, neon`。

---

## 三、隔离矩阵（主风格 → 必加的反向）

| 主风格 | 必加隔离反向 | 因为 |
|---|---|---|
| 写实摄影 | `anime, cartoon, illustration, 3d render, painting, CGI` | 模型天然爱加"艺术化" |
| 二次元 | `photo, photorealistic, 3d render, DSLR, realistic skin` | 会漂成半写实 |
| 3D 渲染 | `2d, flat, illustration, sketch, hand-drawn` | 会漂成插画 |
| 平面设计 | `photo, 3d, realistic texture, depth of field` | 会漂成照片 |
| 国风 | `western fantasy, anime, neon, 3d render` | 会漂成西幻 |
| 极简 | `cluttered, ornate, busy, many objects, pattern` | 会填满画面 |
| 复古胶片 | `digital, HDR, crisp, modern, oversharpened` | 会变"数码味" |
| 夜景 | `daylight, bright sun, blue sky` | 会变白天 |
| 白天 | `night, neon, dark, moonlight` | 会变夜景 |
| 白底产品 | `background texture, props, shadow of other objects, gradient background` | 会加背景 |
| 无人图 | `person, people, human, hands, face` | 会塞人 |

---

## 四、按行业/场景的反向配方

| 场景 | 反向配方 |
|---|---|
| 电商主图 | 组 1 + 组 2 + 组 4 + `person, hands, props, colored background` |
| 人像写真 | 组 1（重点 hands/face）+ `over-retouched, waxy, plastic, anime` |
| 产品暗调 | 组 1 + 组 2 + `flat lighting, gray background, cluttered` |
| 食物 | 组 1 + `plastic food, fake, unappetizing, gray, cold tones` |
| 建筑空间 | 组 1 + `distorted perspective, tilted horizon, fisheye, people` |
| 信息图 | 组 1（重点 text 之外）+ `photo, realistic, depth of field` |
| 海报 | 组 1 + `watermark, stock photo look, cluttered, busy` |
| 游戏/资产 | 组 1 + `perspective distortion, shadow, background`（要正交无影时） |
| 国风 | 组 1 + `western, anime, neon, 3d render, oversaturated` |

---

## 五、反向的边际效应（什么时候停）

| 反向词数量 | 效果 |
|---|---|
| 0–5 | 只堵最要命的（文字、水印、手） |
| 6–15 | **甜点区** |
| 16–30 | 开始互相抵消，有时让画面变平庸 |
| 30+ | 模型进入"什么都不敢画"的状态，出图呆板 |

**判断标准**：如果你说不出"这个反向是堵哪个具体坏习惯"，就删掉它。

---

## 六、三个高级技巧

### 1. 反向也要成对写

想让画面没有"戏剧感"，写 `dramatic lighting, high contrast, cinematic`；  
但模型可能转而给你"平淡无光"，所以**正向要补** `soft directional light, gentle contrast`。  
**反向删掉什么，正向就要补上替代品。**

### 2. 隔离反向要放在反向字段最前

SD 的 negative 前 5 个词权重最高。把"防串味"的词放最前：

```
negative: anime, cartoon, illustration, 3d render, lowres, blurry, watermark, text
```

### 3. 用"正向排除"代替反向（自然语言模型）

Flux / GPT Image / Seedream 不认 negative，改写成**描述空状态**：

| 想排除 | 别写 | 改写 |
|---|---|---|
| 不要文字 | `no text` | `所有表面均为空白，无任何字迹` / `blank, unmarked surfaces` |
| 不要人 | `no people` | `空旷无人的空间` / `an empty space with no figures` |
| 不要多余物体 | `no extra objects` | `画面中只有这一件物体` / `a single object alone in frame` |
| 不要杂乱 | `not cluttered` | `极简、单一主体、干净背景` |

---

## 七、联想触发词：好端端写出"破败感"的原因

有些词本身没错，但会触发模型的社会联想滤镜。写"农村""砖房""90 年代""老房子"，出图常自动加：墙皮脱落、裸露砖墙、污渍、裂缝、杂乱。

| 触发词 | 常被加上的东西 |
|---|---|
| 农村 / 乡下 / 老家 | 破败、脏污、灰暗、杂乱 |
| 90 年代 / 复古 / 老 | 泛黄、霉斑、低饱和过度 |
| 简陋 / 便宜 / 经济 | 廉价塑料感、变形 |
| 赛博 / 未来 | 过量霓虹、满屏招牌、脏乱 |
| 高级 / 奢华 | 金色、大理石、过度反光、假欧式 |

**解法三步**（与正面穷举同一思路）：

1. **删掉触发词**，不写"农村砖房"，改写成"一栋被好好打理的房子"
2. **正面描述你要的样子**：`干净白墙、清漆木柜、墙上挂历与相框、暖色台灯、整洁地面`
3. **加硬负面兜底**：`禁止墙皮脱落、禁止裸露砖墙、禁止污渍、禁止裂缝`

**氛围（年代感、夜晚、怀旧）改用光线和具体陈设表达，不要用会触发滤镜的词。**

同一逻辑适用于"高级感"→ 别写高级，写低饱和 + 单一强调色 + 大面积负空间。

---

## 八、反向词常见错误清单

- ❌ 正向里写 `no xxx`（SD 会反向理解）
- ❌ 反向里写 `beautiful, good quality`（反向是"不要什么"，写正向词等于压制质量）
- ❌ 反向里写矛盾组合（`dark, bright`）→ 互相抵消
- ❌ 给 MJ 写 `negative prompt:` 段落 → 无效，只有 `--no`
- ❌ 反向词比正向还长 → 画面呆板
- ❌ 用反向去改构图（`not centered`）→ 反向不能控制布局，只能排除元素

# 人物风格体系（决定"这个人看起来是什么调性"）

> **和 `render-styles.md` 的分工，先分清，否则会写重、写漂：**
>
> - **`render-styles.md` = 渲染介质**：这张图是 3D 还是 2D？是赛璐璐还是厚涂？是照片还是像素？——回答"**用什么手段画**"。
> - **`character-styles.md`（本文件）= 人物风格家族**：这个人是电影级写实还是风格化？是日系二次元还是美漫？是国潮还是赛博朋克？——回答"**这个人属于哪种美术调性**"。
>
> 两者是**乘法关系**，不是二选一。举例：
> - "3D写实 + 电影化写实家族" = 《最后生还者》那种次世代写实
> - "3D赛璐璐 + 二次元家族" = 《原神》那种三渲二
> - "2D厚涂 + 国潮家族" = 国风游戏宣传图
> - "2D平涂 + 潮流卡通家族" = 治愈系盲盒贴纸
>
> **写提示词时两段都要给**：先写【人物风格族】再写【渲染介质块】。只给一个必漂。

---

## 一、人物风格的三个坐标（选风格 = 三个轴各选一个）

很多人说"风格"时把三件事混在一起，导致提示词互相打架。拆成三个轴就清楚了：

| 轴 | 回答的问题 | 取值 |
|---|---|---|
| **① 风格家族** | 写实度与夸张度在哪一档？ | 电影化写实 / 风格化写实 / 动画式三维 / 二次元 / 绘画感 / 美漫 / 潮流卡通 / 国潮 / 低模极简 / 像素 |
| **② 渲染介质** | 用什么手段画？ | 见 `render-styles.md`（3D写实/3D卡通/Q版/2D赛璐璐/2D厚涂/超写实/像素/水墨…） |
| **③ 主题情绪** | 世界观的调性是什么？ | 暗黑 / 治愈 / 赛博朋克 / 蒸汽朋克 / 废土 / 奇幻 / 都市现代 / 怀旧复古 / 太空歌剧 |

**组合公式：**

```
【风格家族】+【渲染介质】+【主题情绪】+【角色身份】
```

例：
```
半写实风格化（家族）+ 3D 渲染（介质）+ 赛博朋克（情绪）+ 女性义体佣兵（身份）
```

> **致命错误**：只在**一个轴**上写词，或两个轴互相冲突（如"写实解剖 + Q版头身比"）。同画面造型夸张度必须统一——这是风格混合失败的头号原因。

---

## 二、风格家族表（第一眼识别点 + 关键设计规则）

> 每行给"**第一眼先看什么**"——这是写提示词时最该抓的那件事。

| 风格家族 | 第一眼观察点 | 造型规则 | 色彩规则 | 适合 | 代表作品 |
|---|---|---|---|---|---|
| **电影化写实** | 人体、材质、表演、摄影 | 服从解剖，不做任何夸张 | 服从环境光逻辑 | 3A 大作、影视化游戏 | 最后生还者 / 荒野大镖客2 / Alan Wake 2 |
| **风格化写实** | 真实体积如何被比例/轮廓/颜色重新设计 | 真实体积 + 夸张比例与轮廓 | 高识别度配色，色块干净 | 竞技游戏、耐看 IP | 守望先锋 / 堡垒之夜 / Dota 2 |
| **动画式三维** | 表情、姿势、拉伸、动画友好形体 | 夸张表情、圆润形体、可拉伸 | 明快高饱和 | 合家欢、平台跳跃 | 双人成行 / 马力欧奥德赛 / 麻布仔 |
| **二次元 / 赛璐璐** | 脸部光照、描边、色影、关键姿势 | 比例优化（6–7头身）、面部高度简化 | 高饱和、纯度一致、投影偏冷紫 | 手游、卡牌、番剧 | 原神 / 崩坏 / Guilty Gear |
| **绘画感三维** | 笔触化材质、大色块、细节频率 | 手绘笔触覆盖 3D 造型 | 低饱和偏油画色调 | 幻想题材、氛围向 | Diablo III / Sea of Thieves |
| **美漫 / 欧美卡通** | 粗犷线条、网点、高对比 | 先剪形后填色，轮廓极强 | 高对比明暗 + 黑白 | 竞技、美式 IP | 无主之地 / Hi-Fi Rush / 蜘蛛侠平行宇宙 |
| **潮流卡通 / 治愈** | 圆润造型、柔和配色、可爱但精致 | 圆角、短肢、大眼但不 SD | 低饱和马卡龙 / 奶油色 | 模拟经营、社交、周边 | 蛋仔派对 / 星布谷地 / 动物森友会 |
| **国潮 / 东方幻想** | 结构线优先、纹样、留白 | 传统纹样 + 现代剪裁重构 | 低饱和中性 + 小重点色 | 仙侠、武侠、国风卡牌 | 斩妖 / 黑神话 / 永劫无间 |
| **低模 / 极简** | 每个折面、负形、有限色板 | 极少面数、几何化 | 极有限的色板 | 独立游戏、艺术向 | 纪念碑谷 / Journey / A Short Hike |
| **像素 / HD-2D** | 原生分辨率、色板、轮廓 | 网格对齐，逐格设计 | 有限调色板 | 复古、独立 | 信使 / 八方旅人 / 星露谷 |

---

## 三、主题情绪表（世界观调性）

> **主题情绪是"调味料"**，可以叠加到任意风格家族上。搜索热度极高但最容易被当成"风格"乱用的就是这一类。

| 情绪/主题 | 视觉规则（写词用） | 关键色 | 提示词 |
|---|---|---|---|
| **暗黑** | 高对比低明度、材质粗糙、压迫感构图 | 黑/暗红/深灰 | `dark fantasy, grim atmosphere, low-key lighting, desaturated moody palette` |
| **治愈** | 柔和光、圆润形体、留白 | 奶油白/浅木色/粉绿 | `cozy healing atmosphere, soft warm light, pastel palette, gentle mood` |
| **赛博朋克** | 霓虹 + 镜面反射 + 潮湿街道 | 洋红/青/紫/荧光绿 | `cyberpunk, neon magenta and cyan, wet reflective surfaces, high contrast night city` |
| **蒸汽朋克** | 齿轮、管道、黄铜、维多利亚 | 黄铜/棕色/皮革色 | `steampunk, brass gears, victorian industrial, leather and copper, warm amber light` |
| **废土** | 破败材质、尘土、拼凑装备 | 沙土黄/锈红/灰 | `post-apocalyptic wasteland, scavenged gear, dust and rust, harsh sunlight` |
| **日式奇幻** | 清新艳丽、萌系、明亮 | 高饱和清新色 | `japanese fantasy, bright vivid colors, whimsical and cute, soft cheerful palette` |
| **都市现代** | 利落剪裁、真实面料、日常光 | 中性色 + 单一强调色 | `urban modern, clean tailoring, contemporary streetwear, natural city light` |
| **怀旧复古** | 年代感服装、胶片质感 | 褪色暖调 | `retro vintage, 1980s fashion, film grain, faded warm tones` |
| **太空歌剧** | 金属盔甲、能量、宏大 | 银白/蓝/橙光 | `space opera, sleek metallic armor, energy glow, cinematic sci-fi grandeur` |

> **不要只写"暗黑""赛博朋克"这种形容词就算完**——要补上表里的**视觉规则**（色相/明度/反射/材质），否则模型只加一层滤镜，出不来氛围。

---

## 四、九大风格家族的提示词块（直接整段抄）

### 1. 电影化写实
```
cinematic realism, grounded realistic character design, physically accurate anatomy,
photographic material response, subtle micro-expression, natural imperfect skin,
shot like a film still, naturalistic lighting, muted realistic color grading
```

### 2. 风格化写实（最推荐的"耐看型"）
```
stylized realism, semirealistic character design, realistic volume with stylized proportions,
exaggerated silhouette and shapes, designer shape language, bold readable color blocking,
highly recognizable IP character design, clean appealing forms
```
> 关键词是 `stylized proportions + readable silhouette`——真实感做底座，比例和轮廓做设计。

### 3. 动画式三维
```
stylized 3D animation character, animation-friendly shapes, exaggerated expressive face,
squash-and-stretch appeal, rounded simplified forms, big expressive eyes,
appealing caricature proportions, playful personality readable at a glance
```

### 4. 二次元 / 赛璐璐
```
anime character design, japanese anime aesthetic, optimized proportions (6-7 head-tall),
simplified facial features, sharp nose line and chin, symbolic highlights,
uniform saturation control, cool-toned shadows, key pose appeal
```
> **两条铁律**：① 简化要**全画面一致**（面部高度简化配写实盔甲必割裂）；② 投影**偏冷或偏紫**，不是单纯压暗。

### 5. 绘画感三维 / 手绘质感三维
```
painterly 3D character, hand-painted texture work, visible brushstroke material,
large color blocks with controlled detail frequency, illustrative shading,
atmospheric painted look, stylized surface treatment
```

### 6. 美漫 / 欧美卡通
```
american comic style character, bold thick outlines with slight jitter, halftone dot texture,
high contrast lighting, graphic shapes, heroic silhouette-first design,
ink and cel hybrid, dynamic comic book energy
```

### 7. 潮流卡通 / 治愈
```
trendy stylized cartoon character, soft rounded shapes, short stylized limbs,
cute but refined design, soft pastel macaron palette, smooth matte surfaces,
cozy warm atmosphere, designer toy appeal, cheerful gentle mood
```

### 8. 国潮 / 东方幻想
```
guochao / oriental fantasy character design, traditional chinese pattern motifs,
modern re-tailored silhouette, structural line priority, generous negative space,
low saturation neutral with small accents of vermilion and gold,
elegant cultural depth, ink-wash influenced color gradation
```

### 9. 低模 / 极简
```
low poly stylized character, minimal faceted geometry, flat shaded polygons,
strong readable silhouette, extremely limited palette, abstract simplified forms
```
> 这一块只解决"像不像低模"。**面数怎么分配、哪密哪疏、面片朝向怎么走**，见 `low-poly.md`——低模的成败在预算分配，不在风格词。

---

## 五、风格选择决策表（按用途选）

| 用途 | 推荐风格家族 | 配套渲染介质 | 主题情绪 |
|---|---|---|---|
| 3A 游戏 / 影视化宣传 | 电影化写实 | 3D 写实 / 超写实 | 暗黑 / 废土 / 太空歌剧 |
| 竞技游戏 / 长线 IP | 风格化写实 | 3D 卡通 | 都市现代 |
| 手游 / 卡牌 / 乙女 | 二次元 | 2D 赛璐璐 / 2D 厚涂 | 日式奇幻 / 都市现代 |
| 合家欢 / 休闲 | 动画式三维 / 潮流卡通 | 3D 卡通 | 治愈 |
| 周边 / 潮玩 / 盲盒 | 潮流卡通 | Q版潮玩 | 治愈 |
| 仙侠 / 武侠 / 国风 | 国潮 | 2D 厚涂 / 水墨 | 东方幻想 |
| 科幻 / 机甲 / 末世 | 风格化写实 | 3D 写实 / 2D 厚涂 | 赛博朋克 / 废土 |
| 独立游戏 / 艺术向 | 低模 / 像素 | 像素 / 极简 | 怀旧复古 |
| 动画番剧角色设定 | 二次元 | 2D 赛璐璐 | 日式奇幻 |
| 品牌吉祥物 / 社交头像 | 潮流卡通 | 3D 卡通 / Q版 | 治愈 |

---

## 六、风格混合的规则（想要"国潮 + 赛博朋克"这种复合风格时）

多风格混合是常见需求，但**必须指定主风格**：

1. **主风格决定底层规则**（造型夸张度、光影策略、比例）。
2. **次风格只影响局部元素**（纹样、配色、配件）。
3. **判断冲突**：如果两个风格在**造型夸张度**上冲突（写实解剖 + Q版头身比），混合必失败——最底层的变量无法折中。

| 风格 | 造型 | 色彩 | 光影 | 细节密度 |
|---|---|---|---|---|
| 国风 | 结构线优先 | 低饱和中性 + 小重点色 | 平面化、留白 | 集中在纹样 |
| 二次元 | 比例优化 | 高饱和、纯度一致 | 色块化、边缘强化 | 关键部位集中 |
| 写实 | 服从解剖 | 服从环境逻辑 | 物理正确 | 均匀丰富 |
| 赛博朋克 | 写实为主 | 高饱和人工色相 | 高对比 + 强反射 | 光源与破败并存 |

**复合示例**（主风格=风格化写实，次风格=国潮，情绪=赛博朋克）：
```
stylized realism as primary style (base rules: realistic volume, readable silhouette),
guochao secondary motifs (traditional pattern details on costume trim),
cyberpunk mood (neon reflection light as accent), unified proportion language
```

---

## 七、风格隔离反向词（防串味）

在提示词末尾按目标风格选一行加进反向：

| 目标风格 | 隔离反向词 |
|---|---|
| 电影化写实 | `cartoon, anime, stylized exaggeration, chibi, illustration` |
| 二次元 | `photorealistic, 3D render, western cartoon, realistic skin texture, harsh realism` |
| 美漫 | `anime, soft airbrush, photorealistic, cute pastel` |
| 潮流卡通 | `realistic proportions, grimdark, horror, gore, harsh contrast` |
| 国潮 | `western fantasy armor, cyberpunk neon overload, anime school uniform` |
| 暗黑 | `cheerful, bright pastel, cute cozy, sunny` |

---

## 八、风格快查（复制即用）

```
电影化写实   cinematic realism, photographic material response, naturalistic lighting
风格化写实   stylized realism, stylized proportions, readable silhouette, IP design
动画式三维   stylized 3D animation, squash-and-stretch, appealing caricature
二次元      anime character design, 6-7 head-tall, cool-toned shadows, key pose
绘画感三维   painterly 3D, hand-painted texture, large color blocks
美漫        american comic, bold outlines, halftone dots, high contrast
潮流卡通     trendy cartoon, rounded shapes, pastel macaron, cozy mood
国潮        guochao, traditional motifs, structural line priority, vermilion accent
低模        low poly, faceted geometry, limited palette, strong silhouette
```

**主题情绪快查：**
```
暗黑      grim, low-key, desaturated moody palette
治愈      cozy, soft warm light, pastel, gentle
赛博朋克   neon magenta+cyan, wet reflective, high contrast night
蒸汽朋克   brass gears, victorian industrial, warm amber
废土      post-apocalyptic, dust and rust, harsh sunlight
都市现代   clean tailoring, contemporary streetwear, natural light
```

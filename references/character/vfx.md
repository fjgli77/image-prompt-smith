# 特效层：把物理法则写成指令

> 全网检索后的第二版。核心判断来自多个来源的交汇：
> **特效提示词不是"描述画面长什么样"，而是"描述一个事件怎么发生"。**
> 只写最终状态的提示词，得到的是一张"凝固的海报"——爆炸像贴在天空上，烟像挂着的棉花。

---

## 一、三条总原则

### 1. 写事件，不写状态

| 状态（废） | 事件（有效） |
|---|---|
| 一团火 | 火从木质横梁底部点燃，向上舔舐，边缘卷曲成黑色焦边 |
| 魔法爆炸 | 尘土从撞击点向外环状点燃，冲击波卷过松散碎屑，余烬映亮沉降的薄雾 |
| 烟雾 | 稀薄的烟丝向上卷曲，被横风拉向右侧，在窗口光里变亮 |
| 粒子 | 稀疏火星斜向下飞散，落在湿石阶上瞬间熄灭 |

**每个词自带运动和密度**：「余烬」是飘的，「火花」是溅的，「浓烟」是翻滚的，「薄雾」是悬停的，「冲击波」是荡开的。**「火」只是颜色，「点燃」才是事件。**

### 2. 特效在语法上依附主体

这是防"特效吃掉画面"最有效的一招——**不要给特效单独开一句**：

| 特效独立成句（会吃掉画面） | 依附主体（构图保住） |
|---|---|
| 强烈的火花在画面中飞散 | 火花勾出她的侧脸轮廓 |
| 浓烟弥漫 | 烟从她身侧分开，露出一道侧影 |
| 光芒四射 | 光从剑刃溢到她的下颌与锁骨 |

**规则**：每个特效句里必须出现主体（人/物）或主体的部位。

### 3. 一层主特效 + 至多一层辅特效

三层以上必然互相打架。**主特效决定"这场戏在发生什么"，辅特效只提供质感。**

---

## 二、六族特效：每族写"动词 + 形态 + 参数"

### 2.1 光（最便宜、最有效）

| 类型 | 动词/形态 | 词块 |
|---|---|---|
| 轮廓光 | 勾边、切出、溢到 | `sharp rim light on the shoulder and jaw, fading into darkness` |
| 体积光 | 穿、切、浮 | `volumetric god rays slicing through dust, visible beam edge` |
| 星芒 | 衍射、锐利 | `sharp starburst, natural diffraction spikes`（**别用 rays**，会变成十字创可贴） |
| 辉光 | 溢出、包裹 | `restrained bloom around highlights, crisp core, fast light falloff` |
| 眼部发光 | 溢出到 | `faint glow in the irises, light spilling onto the cheekbone` |
| 环境溢色 | 染上、爬上 | `neon spill climbing the jaw and collar` |
| 反射光 | 拉出、铺开 | `elongated reflection on wet stone` |

**光效必须写三层**：主光（方向+色温）→ 辅助/轮廓光 → 环境反射光。少一层就"平"。

**三条防翻车**

- 全场**主光色 ≤2 种**，第三色只做点缀（颜色一多就脏）
- 发光必配 `高光保留细节，无纯白死白`（否则出白块）
- 星芒要"一大带六七小"，三十颗等大光源等于着火

### 2.2 粒子

**五要素**：种类 + 密度 + 粒径 + 方向 + 与主体交互。

| 要素 | 写法 |
|---|---|
| 种类 | 余烬 / 火星 / 光尘 / 灰烬 / 花瓣 / 雪 / 雨丝 / 水花 / 血雾 / 数据流 / 碎晶 |
| 密度 | `sparse`（可数）/ `medium` / `dense`（成雾） |
| 粒径 | `varying sizes, some bokeh-blurred` ← **必须写**，全一个尺寸像刷漆 |
| 方向 | 自下而上 / 斜向下 / 螺旋上卷 / 环绕主体 / 沿轮廓外扩 |
| 交互 | 在轮廓光里发亮 / 被身体推开 / 在皮肤上投细影 / 落在湿地面熄灭 |

**实测铁律（多来源一致）**

> **粒子词在一条提示词里最多出现一次。** 堆 `glowing particles + fireflies + floating sparks + bokeh` 四个词，十张糊七张——密度会叠加。
> 改法：只留一个粒子词 + `sparse` + 负向 `dense particles, cluttered`。

#### 粒子三层预算（比"加粒子"有效十倍）

同屏粒子必须**按粒径分工**，否则全糊成一层噪点。三层各管一件事：

| 层 | 粒径 | 数量 | 职责 | 词例 |
|---|---|---|---|---|
| **大** | 拳头到手掌 | 几十片 | **重量与碰撞**：有重力、会坠落、撞到东西弹起 | 碎石块、碎晶片、断裂瓦片、符文碎片 |
| **中** | 指甲到铜钱 | 几百个 | **方向与轨迹**：沿一条明确路径飞行、拖尾 | 火星、光屑、流萤、灰烬 |
| **小** | 粉尘级 | 上千点 | **空气与体积**：自发光、照亮周遭、填满景深 | 星尘、光雾、浮尘、雪雾 |

**三层缺一必崩**：只写大粒子 = 打翻的碎石堆；只写小粒子 = 全景蒙灰；只有中粒子 = 一道假光。

```
【单句写法】三层粒子：拳头大的碎晶数十片坠地弹起；指节大的火星沿剑脊拖尾；贴地光雾一层自发光。
```

#### 粒子要写物理，不写"发光"

| 有物理 | 没物理 |
|---|---|
| 有重量，坠落、撞地弹起、二次炸开 | 悬在原地发光 |
| 有惯性，沿轨迹拖尾、急停时向前扑 | 均匀铺满画面 |
| 被气流带偏，绕过人物身体 | 直接穿过身体 |
| 命中点向外喷，随后衰减 | 一直保持同样密度 |

**光溢出（最常被漏的一条）**：粒子/能量必须照亮环境，否则像贴上去的贴图。

```
【错】剑身发出金色光芒，周围有粒子
【对】剑身金光向外溢出，照亮右臂内侧与下颌，地面落下一圈淡金色光斑，人物影子被光推着向外倒
```

#### 粒子专用反向

`random particle directions, uniform particle size, flat depth, excessive glow, particle storm, particles covering face, particle overlay` ——
**"粒子大小均匀 / 方向随机"是最常见的两种崩**，必须进反向段。

#### 不遮脸（几乎必崩的一处）

粒子一旦飘到脸前，五官就被吃掉。三种写法保脸：

1. **写保护区**：`粒子避让面部，面部前方留空`
2. **写层次**：`粒子位于人物身后与画面边缘，人物与镜头之间无粒子`
3. **写机位**：`粒子在焦外，面部实焦`

> 与铁律"写了的部位模型一定画"同理：**没写保护区，模型默认让粒子铺满整个画面。**

### 2.3 介质（烟 / 雾 / 水 / 火 / 尘）

介质最吃**形态词**，光写名词必翻车：

| 介质 | 别写 | 写成 |
|---|---|---|
| 烟 | `smoke` | `thin wisps of smoke curling upward, dragged to the right by crosswind` |
| 雾 | `fog` | `low-lying fog rolling slowly, parting around the legs` |
| 火 | `fire` | `flames flickering upward, heat shimmer distorting the air above` |
| 水 | `water` | `white foam exploding upward on impact, then sheeting off the rock` |
| 尘 | `dust` | `dust motes drifting in the light beam`（**性价比最高的一组词**） |
| 雨 | `rain` | `rain streaks at 15°, breaking on the shoulder line, vertical motion blur` |

**介质层数 ≤2**：雾 + 烟 + 雨 + 尘 四层齐上，画面必糊。

### 2.4 能量与冲击

| 类型 | 词块 | 必配因果 |
|---|---|---|
| 气浪 | `air distortion ring expanding outward, dust pushed away` | 衣摆/头发必须动 |
| 冲击波 | `concentric shockwave ring, semi-transparent boundary` | 地面碎屑被推开 |
| 地裂 | `cracks radiating from the feet, molten light in the fissures` | 重心下沉 |
| 电弧 | `thin branching arcs crawling along the forearm` | 皮肤/金属有反光 |
| 残影 | `motion afterimage trailing the arm, 30% opacity` | 必须有运动方向 |
| 碎裂 | `debris suspended mid-air, small stones and dry leaves` | 有来源（被什么打碎） |

### 2.5 形变（溶解 / 消散 / 聚合）

| 类型 | 词块 |
|---|---|
| 粒子化解体 | `the silhouette dissolving into particles from the edges inward` |
| 聚合成形 | `dust spiraling inward and assembling into a shape` |
| 燃烧殆尽 | `edges charring and curling, ash lifting off` |
| 冰晶生长 | `frost branching across the surface in sharp dendrites` |

**形变最忌"全图一起变"**：写清起点（从边缘/从脚下/从伤口）、传播方向、残留物。

### 2.6 服饰特效（附着在衣服上的那一类）

> 这一类最容易被漏掉：它既不是"粒子"，也不是"光效"，而是**长在布料/刺绣/甲片上的效果**。
> 玄幻法袍、机甲战衣、发光礼服全靠它。**关键是"附着位置"——不写位置，模型会糊满全身。**

| 类型 | 写法 | 附着点必写 |
|---|---|---|
| 光缕游走 | `thin threads of light travelling along the hem` | 沿哪条线（裙缘/袖摆/前襟） |
| 符文亮起 | `runes igniting one after another across the sleeves` | 从哪亮起、往哪走 |
| 织纹自发光 | `woven pattern faintly glowing from within the fabric` | 整片 / 局部 |
| 衣摆能量化 | `the hem dissolving into drifting embers` | 从下往上多少 |
| 材质渐变 | `fabric gradient shifting from silk to crystal at the shoulders` | 过渡带位置 |
| 甲片反光 | `metal scales catching a cold rim light along the shoulder line` | 哪一片、什么光 |

**三条写法约束**：

1. **只在一处起效**：`光缕沿裙缘游走` 比 `全身发光` 稳定十倍。全身发光 = 过曝 + 看不清剪影。
2. **必须有主体或部位**：`光纹顺着她的腰线爬上袖口`（依附主体，见 §一.2）。
3. **亮度要约束**：`发光但布纹仍可见，不死白`——否则布料细节全被烧掉。

**中英对照速查**：

```
光缕沿裙缘游走        thin light threads travelling along the hem
符文在袖口依次亮起     runes igniting one by one across the cuffs
织纹自内透光          the weave glowing faintly from within
裙摆化灰              the hem crumbling into drifting ash
肩甲冷冽反光          shoulder plates catching a cold rim light
```

**反向**：`glow everywhere, blown-out fabric, uniform emissive, white-clipped light, pattern lost in bloom`

---

## 三、把特效写成时间线（三段句）

```
① 成因：什么触发了它
② 发展：它怎么运动、卷起什么、照亮什么
③ 消散：它怎么减弱、留下什么
```

示例（战斗）：

```
① 剑锋落地的瞬间，石阶从撞击点裂开；
② 气浪贴着地面向外荡开，卷起碎石与干叶，火星斜向下飞散；
③ 烟尘缓缓沉降，余烬在湿石上明灭两下即灭。
```

示例（仙侠）：

```
① 掌心灵力汇聚，先聚成一粒亮点；
② 光向外扩散成环形光柱，衣袂被向上的气流掀起，皮肤映出青色反光；
③ 光柱边缘渐淡，只余少量光尘上浮。
```

**"之前、当时、之后"三段齐了，画面才读得真。** 只有"当时"就是海报。

---

## 四、六个可量化参数（不写就被随机）

| 参数 | 写法 | 不写的后果 |
|---|---|---|
| 密度 | `sparse` / `medium` / `dense` | 糊成雪花屏 |
| 粒径 | `varying sizes, some bokeh-blurred` | 像刷漆，全同尺寸 |
| 方向 | 斜下 30° / 自下而上 / 环绕 | 随机方向，像失重 |
| **尺度锚** | `一个街区的冲击波` / `萤火虫大小的火星` | 默认变屏保比例 |
| 层数 | 介质 ≤2 层，光效 3 层 | 糊成一片 |
| 速度 | 缓 / 疾 / 凝滞（或 `slow drift` / `rapid burst`） | 动感不可控 |

**尺度锚是最被低估的一条**：不锚定，"巨大爆炸"和"小火苗"在模型眼里没区别。

---

## 五、动态模糊（唯一稳的写法）

```
background motion blur, subject in sharp focus
```

- **全图写 `motion blur`，十张里只有两张主体还立得住**
- 方向可指定：`radial blur`（爆炸/冲刺）、`horizontal linear blur`（横移）、`vertical motion blur`（雨丝、下落）
- 速度线 `speed lines` 会把画风拖向漫画/线稿，照片系慎用
- 光轨 `light trails` 必须配 `long exposure` 语境

---

## 六、静态图里的"闪烁感"（三个来源）

| 来源 | 写法 |
|---|---|
| 噪声 | `subtle film grain, analog noise`（让亮部不均匀） |
| 疏密 | 一颗大光源带六七颗小的（比三十颗等大好得多） |
| 方向统一 | 所有光晕往同一侧偏（一侧偏=有风；四面都闪=着火） |

---

## 六·五、体积感：三条物理条件（不写就永远是"贴纸特效"）

### 1. 体积光必须有介质，否则出不来光柱

模型不会凭空算散射——**你得先告诉它"空气里有东西"**。

| 无效（只有光源） | 有效（给了介质） |
|---|---|
| 明亮的阳光从窗户照进来 | 强烈晨光切过积尘的窗，重度体积散射，光束里浮尘清晰可见，强烈明暗对比 |

关键词：`dust motes in light beam` / `heavy volumetric scattering` / `sunbeams visible in the haze`

> 这也是量测数据里"性价比最高、几乎不翻车"的一组词——**因为它是唯一能强制模型去算光在介质里怎么走的写法。**

### 2. 流体要写三个属性，不是四个形容词

```
粘度（thick / ethereal / dense）
湍流与速度（swirling / violent / crawling / slow-motion）
与光的交互（refraction / backlighting / self-illumination）
```

只写"浓烟滚滚"——模型给你一团灰色棉花。三个属性写齐，它才知道该往哪个方向解。

### 3. 镜头缺陷才是真实感来源

干净的画面像渲染图，**有缺陷的画面才像摄影**。三件套：

```
anamorphic lens flare（水平蓝色变形光斑）
shallow depth of field, 85mm f/1.4（写清镜头物理，不写"背景虚化"）
slight chromatic aberration on the edges（边缘轻微色差）
```

**代价**：三件套全上会抢主体。**主特效片最多用两件**，且光斑不要压在脸上。

---

## 七、风格适配矩阵

| 风格 | 允许 | 禁止 |
|---|---|---|
| 写实摄影 | 尘埃、薄雾、雨丝、轮廓光、地面反射 | 法术光、粒子爆发、发光纹路 |
| 电影感 | 体积光、薄雾、雨、克制辉光 | 满屏粒子、饱和撞色光 |
| 3D 动漫 / 三渲二 | 分层粒子、硬边光效、能量形变 | 过量体积雾（会脏）、真实焦散 |
| 2D 赛璐璐 | 硬边光效、色块状粒子、速度线 | 半透明柔和辉光（破坏平涂） |
| 国漫半写实 | 三层粒子、流光、法术光 | 2D 粗描边 |
| 水墨 | 墨点、飞白、留白气流 | 霓虹、电弧、彩色粒子 |
| 赛博朋克 | 霓虹溢色、数据流、电弧、湿地反射 | 暖调柔光、自然花瓣 |

**越界即"串味"**：写实人物 + 发光法阵 = 半张照片半张游戏，模型只能折中。

---

## 八、八套场景配方

### 仙侠（R3）
```
主：环形灵气光柱自脚下升起，青色半透明，边缘柔化
辅：稀疏光尘上浮，在轮廓光处发亮
因果：上升气流掀起广袖与发丝，皮肤映出青色反光
约束：脸无粒子遮挡；高光保留细节
```

### 战斗（R3）
```
主：气浪贴地向外荡开，卷起碎石与干叶
辅：火星斜向下飞散，落点处地面裂纹发光
因果：衣摆与头发被冲击推起，重心下沉
约束：烟尘不许盖住脸，主体轮廓清晰
```

### 赛博夜景（R2）
```
主：霓虹青紫从右侧溢色，爬上侧脸与衣领
辅：数据流粒子斜向上飘，湿地面拉出长反射
因果：面部保留一点暖色补光，不做全脸发蓝
约束：主光色 ≤2 种
```

### 治愈（R1）
```
主：柔光包裹，无明确光源方向
辅：稀疏花瓣横穿画面，两点萤火在轮廓光里发亮
因果：发丝被微风带起一缕
约束：留白 ≥30%，不堆粒子
```

### 雨中夜戏（R2）
```
主：雨丝 15° 斜落，在肩线与伞面截断并溅起细水花
辅：地面湿反射拉长霓虹倒影
因果：衣物肩部深色浸湿，发梢滴水
约束：雨用 vertical motion blur 定方向，主体 sharp focus
```

### 废墟尘烟（R2）
```
主：建筑倒塌后的尘幕从右向左缓慢推进
辅：dust motes 在穿窗光柱里浮动
因果：尘幕压暗远处，近处人物被轮廓光切出
约束：介质 ≤2 层
```

### 火场（R3）
```
主：火从底部点燃，向上舔舐，热浪扭曲背景
辅：余烬斜向上飘，映亮烟雾底部
因果：脸被暖橙光从下方照亮，衣物边缘焦黑卷曲
约束：火不遮脸部；烟不糊成一团
```

### 解体/消散（R2）
```
主：身影从边缘向内解离为粒子，粒子带原色
辅：少量粒子向上飘散并渐隐
因果：粒子在地面投下细影，最后一点粒子熄灭
约束：核心躯干最后消散，保证仍能认出是谁
```

---

## 九、实测崩坏表（含"十张干净率"）

| 现象 | 根因 | 改法 | 干净率参考 |
|---|---|---|---|
| 粒子糊成雪花屏 | 多个粒子词叠加 | 只留一个粒子词 + `sparse` + 负向 `dense particles` | 3/10 → 7/10 |
| 光溢出到背景 | 缺 falloff 与暗底 | `crisp core, fast light falloff, dark background` | 5/10 → 8/10 |
| 烟堵在主体前 | 只写 smoke | `thin wisps of smoke curling upward, parting around the subject` | 4/10 → 7/10 |
| 主体跟着糊 | 全图 motion blur | `background motion blur, subject in sharp focus` | 2/10 → 6/10 |
| 星芒像十字创可贴 | 用 rays | 改 `sharp starburst, natural diffraction` | — |
| 粒子像雪片 | 尺寸单一 | 加 `varying sizes, some bokeh-blurred` | — |
| 颜色脏 | 光源色太多 | 全场限两种主光色 | — |
| 特效变白块 | 无高光约束 | `高光保留细节，无纯白死白` | — |
| 爆炸像贴纸 | 只写状态 | 补成因 + 消散 | — |
| 烟雾挂棉花 | 缺形态动词 | 补 `curling / rolling / parting` | — |
| 特效穿模 | 缺交互 | 加"在轮廓光里发亮/被身体推开" | — |
| 光效边缘锯齿 | CFG 过高 | SD 系光效题材 CFG 5.5–6 | — |

---

## 十、平台差异

| 平台 | 对特效词的响应 | 建议 |
|---|---|---|
| **Seedream 5 / 即梦** | 中文形态词响应好；对"事件句"理解强 | 用中文三段句写；粒子只写一个词 |
| **Nano Banana Pro** | 能吃长结构化指令，物理描述越细越好 | 用七段式：主特效/辅粒子/环境交互/镜头 |
| **Midjourney v7** | 短句 + 氛围词；堆词会糊 | 特效只留 2–3 个词，靠 `--style raw` 压 MJ 味 |
| **SDXL / ComfyUI** | 标签 + 权重；CFG 敏感 | 光效 CFG 5.5–6；粒子层可单独出再合成 |
| **Flux** | 字面理解，否定弱 | 用正面穷举替代负向 |

---

## 十一、反向词（特效专用）

```
overexposed glow, blown-out white highlights, particles covering the face,
dense particles, cluttered particles, muddy colors, color banding,
flat fire, floating debris without cause, abrupt disappearance,
cartoonish explosion, glow everywhere
```

中文：`过曝光晕、纯白死白、粒子遮挡面部、粒子过密、颜色发脏、色带、扁平的火、无来由漂浮物、特效突然消失、卡通化爆炸、全屏泛光`

---

## 十二、十二项自检

- [ ] 特效写成了**事件**（成因/发展/消散），不是状态
- [ ] 每个特效句里都有主体（防淹没）
- [ ] 只有一层主特效 + 至多一层辅特效
- [ ] 粒子词只出现**一次**，且给了密度与粒径
- [ ] 有尺度锚（街区大 / 萤火虫大）
- [ ] 有环境交互（照亮什么、压弯什么、被什么分开）
- [ ] 光效三层齐（主光/轮廓/反射）
- [ ] 介质 ≤2 层，主光色 ≤2 种
- [ ] 动态模糊写了"主体清晰"
- [ ] 与主风格不冲突（对照矩阵）
- [ ] 写了体积光就写了介质（`dust motes in light beam`），否则没有光柱
- [ ] 流体写了粘度 + 湍流速度 + 与光交互三者，镜头缺陷至多两件

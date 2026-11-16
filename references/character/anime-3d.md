# 3D 动漫人物：六条路线与专用词法

> 这一份补 `render-styles.md` 没覆盖的那条轴：**"3D 的动漫人物"到底有几种**。
> 很多人写"3D 动漫"，模型给他一个塑料手办；写"二次元 3D"，给他一张贴纸。
> 原因是**"3D 动漫"是六条互斥的路线，不是一种风格**。

---

## 一、五条路线（先认路，再写词）

| 路线 | 一眼可辨 | 影子怎么画 | 头身比 | 典型用途 |
|---|---|---|---|---|
| **① 全 3D 写实** | 像游戏 CG，看不出"动画感" | 物理体积光、柔和过渡 | 7.5–8 | 虚拟人、CG 宣传图 |
| **② 三渲二（cel-shaded 3D）** | 3D 的立体 + 2D 的色块 | **一到两档硬边**，无渐变 | 6.5–7.5 | 国漫、动态海报 |
| **③ 国漫半写实（原神/崩铁向）** | 五官精致、材质华丽、光影有层次 | 体积光 + 手绘感过渡 | 7–7.5 | 游戏立绘、国潮 KV |
| **④ 皮克斯/迪士尼卡通** | 圆润、弹性、夸张表情 | 柔和物理光照 + SSS | 5.5–6.5 | 合家欢、IP 形象 |
| **⑤ 风格化手绘 3D** | 有笔刷感的多边形块面 | 大色块明暗，手绘边缘不齐 | 6–7 | 艺术短片、绘本动画 |
| **⑥ UE 影视级玄幻 CG** | 真人级渲染 + 动漫化精致五官，像国产玄幻剧 CG | 影视级物理光照（Lumen）+ SSS，但有动漫骨相 | 7–7.5 | 玄幻剧 CG、游戏 CG 预告 |

**判定口诀：写死影子写法 = 写死流派。**

- 赛璐璐 → `hard-edged cel shading, two-tone shadow, no gradient`
- 皮克斯 → `volumetric physical lighting, subsurface scattering, ambient occlusion in creases`
- 国漫半写实 → `painterly shading, cinematic key light, rim light on hair edges`
- 手绘 3D → `broad graphic shadow masses, painterly value transitions, irregular painted edges`
- UE 影视级玄幻 → `Lumen global illumination, subsurface scattering skin, filmic tone mapping, sculpted anime features`

**只写"3D 动漫"= 让模型在五条路线里随机抽。** 必须点名路线。

---

## 二、3D 动漫人物的七段结构

比 2D 多两段（建模语义、渲染语义），这两段是"像 3D"的关键：

```
① 路线锚（cel-shaded 3D / Pixar 3D / semi-realistic anime 3D）
② 建模语义（拓扑干净、无可见多边形、圆润有机体块）
③ 比例锚（头身比 + 肩宽 + 腿长 + 手部简化度）
④ 五官结构（按 3D 写法，不按 2D 五层）
⑤ 服装与发型（分层 + 材质 + 发束分组）
⑥ 渲染语义（SSS / toon spec / 描边 / AO / 轮廓光）
⑦ 隔离反向（防漂成 2D、写实、Q版、手办）
```

**两段建模/渲染语义的现成词**：

```
clean edge loops, subdivision surface topology, no visible polygons, rounded organic forms
matte plastic skin with subsurface scattering, soft specular highlights on cheeks and nose
path-traced render, ambient occlusion in creases, rim light, cinematic depth of field
```

> 注意：这类"建模术语"只在**大模型**上有效（MJ v6+ / Nano Banana / Seedream 5 / GPT Image）。
> SD 系会当噪声，改用 LoRA + 权重；小模型直接忽略。

---

## 三、比例锚（不写就往可爱漂）

> **头身比以 `render-styles.md` §一「头身比唯一表」为准**，下表只是路线侧的"其他必写项"补充。
> 单独说"3D"时默认 7.5–8；**只有说了"动漫 / 三渲二 / 国漫"才落到 6.5–7.5**。

| 路线 | 头身比 | 其他必写 |
|---|---|---|
| 全 3D 写实 | 7.5–8 | `realistic human proportions` |
| 国漫半写实 | 7–7.5 | `slender build, long legs, narrow shoulders` |
| 三渲二 | 6.5–7.5 | `clean silhouette, simplified hands` |
| 皮克斯卡通 | 5.5–6.5 | `stylized cartoon proportions, large head ratio` |
| 风格化手绘 3D | 6–7 | `angular faceted forms, simplified geometric anatomy` |
| Q 版 / 潮玩 | 2.5–4 | `super-deformed, big head small body` |

**手要单独处理**：3D 动漫的手最容易糊成一团。写 `simplified hands, five fingers, visible knuckles`，或者干脆**藏手**（拢袖、背手、插兜、持物）。

---

## 四、3D 动漫的五官词法（和 2D 不是一套）

2D 写"眼睛五层、鼻子一个点、嘴靠下唇阴影"；3D 写"体块、转折、受光"。

| 部位 | 2D 写法（不要用在 3D） | 3D 写法 |
|---|---|---|
| 脸 | 脸型线条、下颌线 | `planar facial structure`（面部分块）、`soft rounded jaw`、`cheekbone volume` |
| 眼 | 眼型/虹膜/瞳孔/高光/下眼睑五层 | `large expressive eyes with sculpted eyelids`、`iris with radial gradient`、`two specular highlights`、`upper lash as solid geometry` |
| 鼻 | 一个点 / 一条线 / 斜向阴影 | `small rounded nose with soft tip highlight`、`no visible nostril detail`（动漫化简） |
| 嘴 | 下唇阴影给厚度 | `soft lips with subtle volume`、`corner shadow` |
| 皮肤 | 平涂 + 腮红 | `subsurface scattering skin`、`soft specular on nose and cheek`、`subtle blush gradient` |
| 头发 | 发束分组 + 游离发 | `strand-based hair`、`hair clumps with rim light`、`soft shadow from bangs on forehead` |
| 描边 | 粗黑线（赛璐璐） | `thin dark outline on silhouette only`（三渲二）/ `no outline`（皮克斯） |

**两个高频错误**

1. 把 2D 的"眼睛五层"写进 3D 动漫 → 模型往平涂漂，立体感全丢。
2. 写"皮肤纹理、毛孔、绒毛" → 3D 动漫不是写实，一写毛孔就变真人。改 `smooth stylized skin, no pores`。

---

## 五、五个成品块（整段抄，改主体即可）

### ① 三渲二（国漫/动态海报）

```
3D cel-shaded anime character, toon rendering, clean 3D model with hard-edged
two-tone shadow, no gradient, flat color blocks with thin dark outline on silhouette,
6.5–7 head proportion, clean silhouette, simplified hands,
large expressive eyes with sculpted eyelids and two specular highlights,
strand-based hair with rim light, matte fabric with crisp fold edges,
directional key light 45° with crisp shadow terminator, ambient occlusion only in creases
```

反向：`soft gradient shading, volumetric haze, photorealistic skin, pores, plastic toy, chibi`

### ② 国漫半写实（原神/崩铁向，游戏立绘）

```
semi-realistic anime 3D character, Chinese gacha game illustration aesthetic,
refined facial features with painterly shading, elaborate fantasy outfit with layered
fabric and metal trim, 7–7.5 head proportion, slender build,
subsurface scattering skin, cinematic key light plus rim light on hair and shoulders,
volumetric atmosphere, high production value, clean readable silhouette
```

反向：`flat cel shading with thick outline, cartoon, chibi, photorealistic pores, plastic toy, low-poly`

> **交付稿把 "Genshin Impact" 这类作品名换成上面这串参数**（理由见 image-prompt-smith `references/11-style-block.md` 第五节）。

### ③ 皮克斯 / 迪士尼卡通

```
Pixar-style 3D animation character, stylized 3D proportions, 6-head-tall,
rounded sculptural forms, smooth organic body, large expressive eyes,
subsurface scattering on skin, squash-and-stretch facial features,
cinematic three-point lighting with rich color grading, global illumination,
tactile inviting world, high detail fabric texture, path-traced render
```

反向：`anime 2D, cel shading, flat color, photorealistic pores, uncanny, gritty, dark horror`

### ④ 风格化手绘 3D（笔刷块面感）

```
stylized 3D painterly animation, hand-painted character rendering,
angular faceted form construction, planar facial structure, simplified geometric anatomy,
broad graphic color masses, visible painterly surface treatment, irregular painted edges,
controlled brush texture, semi-matte painted materials, deliberately non-photorealistic,
clean readable silhouette, warm directional sunlight, gentle ambient occlusion, soft bloom
```

反向：`NO photorealism, NO glossy CGI, NO clean plastic 3D, NO anime lineart, NO cel-shading flat colors, NO watercolor`

### ⑤ 全 3D 写实（虚拟人/次世代）

```
photorealistic 3D character, next-gen game CG, Unreal Engine 5 render,
PBR materials, subsurface scattering skin, fine vellus hair and pores,
realistic eyes with catchlight, global illumination, cinematic rim light,
7.5–8 head proportion, path tracing, shallow depth of field
```

反向：`anime, cartoon, cel shading, flat color, stylized proportions, sticker, plastic toy`

---

### ⑥ UE 影视级玄幻 CG（国产玄幻剧 / 游戏 CG 预告）

> **这一条是「全 3D 写实」与「国漫半写实」的交叉产物**：渲染语义走①（PBR / GI / SSS），
> 五官逻辑走③（雕刻眼睑、虹膜径向渐变、简化鼻翼）。五条路线里没有一条对得上，所以单列。

```
cinematic UE5 CG render of a Chinese fantasy character, film-grade production still,
Lumen global illumination with volumetrics, subsurface scattering skin,
filmic tone mapping, physically based hair with strand-level specular,
sculpted anime features: large eyes with defined eyelids, iris radial gradient,
two specular highlights, simplified nose with soft tip highlight, thin upper lash as geometry,
7–7.5 head proportion, elongated silhouette, layered silk costume with subsurface fabric,
subtle rim light separating the figure from atmosphere,
fine airborne dust in light shafts, shallow depth of field, no visible polygons
```

**影子写法**：`Lumen GI + SSS + filmic tone mapping`（渲染层）＋ `sculpted anime features`（五官层）。
**只写前者 → 出真人**；**只写后者 → 出塑料游戏模型**。**两层必须同时给。**

反向：`photorealistic pores, real human skin texture, cel shading flat colors, chibi, plastic toy, low-poly, game HUD`

| 与其他路线的区别 | 差异点 |
|---|---|
| vs ① 全 3D 写实 | ①写"真人毛孔与绒毛"，⑥必须 **禁毛孔**、五官是雕刻化动漫骨相 |
| vs ③ 国漫半写实 | ③是手绘感过渡（painterly shading），⑥是**影视物理光照**（Lumen/filmic），更像实拍 |
| vs ② 三渲二 | ②要硬边两档，⑥要连续过渡 + 真实反射 |

---

## 六、即梦 / Seedream 的三大硬伤与修正句式

实测最常出的三个问题，以及可直接粘的修正段（中文平台直接吃）：

### 硬伤 1：面部崩坏（两眼大小不一、鼻子歪、唇厚不均）

```
人物面部五官比例正确：两眼大小一致，瞳孔位置对称，左右眼瞳孔中心连线与水平线夹角小于 2 度；
鼻子居中，鼻梁中点在两眼中心正下方；嘴唇闭合时上下唇厚度相等，嘴角高度一致；
耳上缘与眉平齐，下缘与鼻底平齐。删除所有"美貌/可爱/帅气/漂亮"类形容词，只保留结构词。
```

### 硬伤 2：手部畸形（六指、粘连、拇指位置错）

```
手部结构正确：手指数量五根，中指最长，拇指最短；拇指位于手掌侧面，与食指夹角 30–45 度；
其余四指并排且有缝隙；每根手指三个关节，关节处皮肤有褶皱；
指甲为长方形带圆弧，长度占末节一半。手部只写静止状态（自然下垂、轻握、平放），不写复杂手势。
```

### 硬伤 3：光影平铺（像手电筒正面直射）

```
光影有明确方向：删除"柔光/明亮/自然光/漂亮光"等词，改为具体光源——左侧 45° 光 / 右侧光 /
侧逆光 / 顶光；写明阴影落点：鼻右侧有三角形阴影、颧骨下方有暗区、下巴下方有投影；
写明色温：5500K 日光、3200K 暖光、6500K 冷白；写明光比 1:3（柔和）到 1:6（立体）。
```

> 同一条思路可移植到任何中文平台：**把形容词换成结构、数量、角度、色温**。

---

## 七、3D 动漫的八个崩坏点

| 现象 | 根因 | 改法 |
|---|---|---|
| 出成塑料手办 | 只写 3D + 没有皮肤/布料的材质语义 | 加 `subsurface scattering` + `matte fabric` + 真实反射 |
| 出成 2D 平涂 | 用了 2D 词（描线/五层眼/水彩） | 删 2D 词，换 `planar facial structure` + 体积光 |
| 出成 Q 版 | 没写头身比 | 写死 `6.5–7 head proportion` + 反向 `chibi, super-deformed` |
| 出成真人 | 写了毛孔/绒毛/真实皮肤 | 改 `smooth stylized skin, no pores`；反向 `photorealistic, pores` |
| 四不像（半写实半平涂） | 两条路线词混写 | 只留一条路线的影子写法，另一条全删 |
| 脸歪眼斜 | 缺结构约束 | 上第六节修正段 1 |
| 手糊成一团 | 手是全模型最难部位 | 藏手 / 写五指标 / 局部重绘 |
| 画面发灰 | 只有 AO 没有主光方向 | 补主光方位 + 光比，`ambient occlusion only in creases` |
| 玄幻 CG 出成真人 | 只写了 UE/Lumen，没写动漫五官 | 补 `sculpted anime features, no pores` |
| 玄幻 CG 出成塑料手办 | 只写了动漫五官，没写影视光照 | 补 `Lumen GI, filmic tone mapping, SSS` |

---

## 八、平台差异（3D 动漫专用）

| 平台 | 写法 | 注意 |
|---|---|---|
| **Seedream 5 / 即梦 / 豆包** | 中文，结构句 + 具体数值 | 中文原生最强；"3D 动漫"要写"3D 三维卡通建模 + 国风三维动画渲染" |
| **Nano Banana Pro** | 英文结构化长指令 | 能吃建模/渲染术语，多视图一致性最好 |
| **Midjourney v7** | 英文短句 + 建模语义 | 写 `--style raw` 更少 MJ 味；参数以官方为准，别抄旧版 `--v 6.6` |
| **SDXL / ComfyUI** | 标签 + 动漫底模 + LoRA | 建模术语当噪声；靠 LoRA 定路线，权重 0.6–0.9 |
| **Flux** | 完整英文句 | 字面理解强，别堆咒语 |

**模型选择**：要"国漫 3D 半写实 + 中文可控"→ Seedream；要"多视图同一角色"→ Nano Banana Pro；要"皮克斯质感 + 艺术性"→ MJ 或 SD+LoRA。

---

## 九、与写实/2D 的隔离反向矩阵

| 你的路线 | 必加反向 |
|---|---|
| 三渲二 | `soft gradient shading, volumetric haze, photorealistic skin, pores, plastic toy, chibi` |
| 国漫半写实 | `flat thick outline, cartoon, chibi, pores, plastic, low-poly` |
| 皮克斯卡通 | `anime 2D, cel shading, flat color, pores, uncanny, horror, gritty` |
| 风格化手绘 3D | `photorealism, glossy CGI, clean plastic, anime lineart, watercolor` |
| 全 3D 写实 | `anime, cartoon, cel shading, flat color, stylized proportions, sticker` |

**通用三件套**（所有 3D 动漫路线都该带）：`no visible polygons, clean silhouette, no text`

---

## 九·五、要真建模时的三条口径（建模师补充）

如果这张 3D 动漫图是要交给建模的，加三条与"好看"无关、但决定能不能落地的东西：

### 1. 三渲二要"去 PBR 脏信息"

```
flat base color with clear color zones, no grunge maps, no roughness variation,
clean AO only in creases, no specular breakup
```

写实纹理（凹凸、粗糙变化、过深 AO）进了三渲二材质只会显脏。**贴图控制在 2048 以内，颜色分区清楚比细节多重要。**

### 2. 低模/游戏向要写面数意图

```
game-ready silhouette, clean quad-friendly forms, no ultra-thin protrusions,
armor pieces separable from the body
```

避免：极细镂空、密布刺绣、镂空蕾丝、单根发丝——这些只能当贴图，做不出几何。

### 3. 关节与手仍按建模规范走

3D 动漫最常见的返工是"手是张开摆拍姿态、衣服褶子横穿肘部"。加一句：

```
A-Pose, arms 30° from torso, palms inward, fingers separated;
loose folds above and below the elbow, clean surface at the joint
```

> 完整规范见 `modeling-handoff.md`；部位级约束见 `body-parts.md` 第十二节。

---

## 十、一张自检表

- [ ] 点名了六条路线中的哪一条（不是"3D 动漫"四个字）
- [ ] 头身比写死
- [ ] 影子写法与路线一致（硬边 / 体积 / 色块）
- [ ] 有材质语义（SSS / matte / 金属反射）而不是只有"3D 渲染"
- [ ] 没混 2D 词（描线、五层眼、水彩、网点）
- [ ] 手要么写死五指标，要么藏起来
- [ ] 有隔离反向（防 Q 版、防真人、防塑料）
- [ ] 图内无文字（3D 模型的贴图文字最容易崩）

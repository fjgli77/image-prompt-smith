# 渲染风格矩阵（决定"出的是哪种图"）

**这是 3D / 2D / 动漫 / Q版 的总开关。** 很多模型默认往"可爱Q版"漂（因为训练集里讨喜的图多），如果提示词里不给**明确的渲染流派词 + 明确的比例锚点 + 明确的反向隔离词**，你要"3D写实"它会给你"Q版3D"，你要"2D动画"它会给你"Q版贴纸"。

出图前先在这一页选一行，然后做三件事：**① 抄风格块 ② 抄头身比 ③ 抄隔离反向词**。三件缺一件都会漂。

---

## 一、风格决策表（先选流派，再选细分）

| 用户可能说 | 流派 | 头身比 | 参照系（给模型的"锚"） |
|---|---|---|---|
| 3D、CG、建模、次世代、虚幻、写实建模 | **3D 写实渲染** | 7.5–8 头身 | AAA 游戏宣传图、虚幻5 |
| 3D 可爱、皮克斯、迪士尼、卡通 3D | **3D 卡通渲染** | 5.5–6.5 头身 | Pixar / Disney / 迪士尼 |
| Q版、可爱、大头、萌、贴纸、潮玩、盲盒 | **Q版 / 潮玩** | 2.5–4 头身 | 泡泡玛特、盲盒手办 |
| 2D 动画、日系、赛璐璐、番剧、动画截图 | **2D 动画赛璐璐** | 6.5–7.5 头身 | 日本 TV 动画、京阿尼 |
| 2D 厚涂、原画、概念设定、半写实 | **2D 厚涂/概念** | 7–8 头身 | 游戏原画、美术设定集 |
| 韩国条漫、网漫、半写实美型 | **韩系半写实** | 7–7.5 头身 | Naver 网漫 |
| 真人、照片、写真、虚拟人、真实感 | **超写实真人** | 7.5–8 头身 | 商业摄影、Metahuman |
| 像素、复古、8bit、游戏像素 | **像素风** | 按需 | 复古游戏 sprite |
| 国风、水墨、工笔、仙侠 | **中国风** | 按需 | 国画、仙侠原画 |
| 美漫、欧美卡通、DC/Marvel 风 | **欧美漫画** | 7–8 头身 | 美漫封面 |

> **歧义词要反问一次**：用户说"画个3D"——是**写实3D**（像真人/游戏CG）还是**卡通3D**（像皮克斯）？两者差别巨大。说不清时默认给**3D 写实渲染**并说明可切卡通。

---

## 二、九大风格块（直接整段复制）

### 1. 3D 写实渲染（次世代 / CG）

```
3D rendered character, photorealistic 3D model, next-gen game CG,
Unreal Engine 5 render, subsurface scattering skin, physically based rendering (PBR),
detailed skin texture with pores and fine vellus hair, realistic eyes with catchlight,
soft global illumination, cinematic rim light, 8K, ray tracing, depth of field
```
- **关键**：必须写 `subsurface scattering`（皮肤透光）+ `PBR` + `Unreal Engine/octane`，否则皮肤像塑料。
- **头身比**：`7.5-head-tall, realistic human proportions`（**必写**，否则模型往可爱漂）。
- **隔离反向词**：`anime, cartoon, chibi, cel shading, flat color, sticker, plastic toy`
- 代表模型：MJ 写实、Seedream 3D、SDXL RealVisXL、Flux 写实 LoRA。

### 2. 3D 卡通渲染（皮克斯 / 迪士尼）

```
3D cartoon character, Pixar-style 3D animation, Disney animation style,
stylized 3D proportions, big expressive eyes, smooth rounded forms,
soft subsurface scattering, stylized hair clumps, soft rim light,
global illumination, movie-quality 3D render, 8K
```
- **关键**：`stylized proportions + big expressive eyes` 定可爱度；不要写 realistic。
- **头身比**：`6-head-tall, stylized cartoon proportions`。
- **隔离反向词**：`photorealistic, realistic skin, anime 2D, cel shading, uncanny`
- 代表模型：MJ `--style 3d`、Seedream、Nijijourney 3D 向。

### 3. Q版 / 潮玩 / 盲盒（chibi）

```
chibi character, Q-version, super-deformed (SD), big head small body,
3.5-head-tall, cute round face, simplified features, large glossy eyes,
soft vinyl toy texture, designer toy collectible, blind box figure style,
clean studio product photography, soft even light, plain pastel background
```
- **关键**：`X-head-tall`（写死 2.5/3/3.5/4）是 Q 版不崩的唯一保险；`designer toy / blind box` 出潮玩质感。
- **隔离反向词**：`realistic proportions, tall, long legs, photorealistic, anime adult, mature`
- 用途：潮玩手办图、贴纸、表情包、游戏头像。

### 4. 2D 动画赛璐璐（日系番剧）

```
2D anime style, Japanese TV animation screenshot, cel shading,
flat colors with hard-edged shadows, crisp clean lineart, thick variable outlines,
flat lighting, anime key visual quality, studio anime production art
```
- **关键**：`cel shading + flat colors + hard-edged shadow` 三件套是赛璐璐的判定词，缺一个就变厚涂/3D。
- **头身比**：`7-head-tall anime proportions`。
- **隔离反向词**：`3D render, CGI, photorealistic, soft airbrush gradient, chibi`
- 搭配 Danbooru 标签最佳。代表：Animagine XL、Illustrious、NovelAI、Niji。

### 5. 2D 厚涂 / 游戏概念

```
2D digital painting, painterly rendering, semi-realistic concept art,
soft brushwork with visible strokes, volumetric lighting, soft shading,
detailed material rendering, cinematic composition, matte painting quality
```
- **关键**：`painterly + visible brush strokes + volumetric light`；不要写 cel/flat。
- **隔离反向词**：`cel shading, flat color, 3D render, chibi, thick outline`

### 6. 韩系半写实 / 网漫

```
Korean webtoon style, semi-realistic manhwa illustration, glossy rendering,
smooth gradient skin, refined delicate features, soft bloom,
elegant lineart, pastel color grading, romance webtoon key art
```
- **隔离反向词**：`3D render, chibi, harsh outline, western cartoon`

### 7. 超写实真人

```
ultra-photorealistic photograph, real human, 85mm lens, f/1.8 shallow depth of field,
natural skin texture with visible pores, subtle skin imperfections, realistic hair strands,
soft even studio light, neutral seamless backdrop, commercial photography
```
- **关键**：`visible pores + skin texture` 必写，否则塑料；`85mm / f/1.8` 拉真实度。
- **隔离反向词**：`anime, illustration, painting, 3D render, cartoon, chibi, smooth plastic skin`

### 8. 像素风

```
pixel art, 32x32 sprite style, limited palette, crisp pixels, no anti-aliasing,
retro game character, transparent background, sprite sheet
```
- **关键**：`no anti-aliasing + limited palette`，否则糊成马赛克油画。

### 9. 中国风水墨 / 工笔

```
Chinese ink wash painting, xuan paper texture, minimal color,
flowing expressive brush strokes, traditional guofeng style, elegant negative space
```
写实向变体：`Chinese traditional painting, gongbi fine brushwork, silk texture`

---

## 三、"只出Q版"的根因与根治

| 现象 | 根因 | 根治三连 |
|---|---|---|
| 要写实，出可爱娃娃 | 提示词没给头身比，模型默认可爱 | ① 写 `X-head-tall` ② 抄对应风格块 ③ 反向加 `chibi, cartoon` |
| 要2D动画，出3D | 缺赛璐璐判定词 | 加 `cel shading, flat colors, hard-edged shadow, clean lineart`；反向加 `3D render, CGI` |
| 要3D，出2D插画 | 缺渲染器词 | 加 `3D rendered, subsurface scattering, PBR, Unreal Engine, ray tracing`；反向加 `2D, illustration, flat color` |
| 脸像但风格飘 | 只换了"画风"形容词 | 画风段**整块替换**，锚点段一字不动（见 style-library 混搭） |
| 系列图风格不统一 | 各图风格词不同 | 风格块逐字复制，反向词也逐字复制 |

**一句话**：**风格 = 风格块 + 头身比 + 隔离反向词，三者一起换，不要只换形容词。**

---

## 四、风格 × 版式 组合矩阵

同一张档案海报，换风格等于换整张图的气质。推荐组合：

| 版式 \ 风格 | 3D写实 | 3D卡通 | Q版潮玩 | 2D动画 | 2D厚涂 |
|---|---|---|---|---|---|
| 单张立绘 | ◎ | ◎ | ◎ | ◎ | ◎ |
| 三/四视图 | ◎ 最稳 | ○ | ○ | ◎ | ○ |
| 档案海报 | ◎ 参考图同款 | ○ | ◎ 潮玩设定页 | ○ | ◎ |
| 表情差分 | ○ | ◎ | ◎ | ◎ | ○ |
| 表情包贴纸 | ○ | ◎ | ◎ | ◎ | △ |

> ◎最佳 ○可用 △不推荐。参考图那种"3D Character Design 档案海报"用 **3D写实 + 档案海报版式** 最接近。

---

## 五、跨风格一致性（纯文字，不喂图）

同一角色的多风格版本（"给我的角色出 3D 版和 2D 版"）：

1. **锚点块完全不动**（脸型/瞳色/发型/标记/服装）——这是身份，跨风格必须守住。
2. **只替换风格块 + 头身比**（写实 7.5 头 ↔ Q版 3.5 头）——这是唯一允许动的两处，但**三不变特征必须保住**（Q版也要认得出是同一人）。
3. **识别串照旧保留**：`Signature features: <特征1>+<特征2>+<特征3>` 在每个风格版本里都写一遍。
4. **固定种子**（支持的平台）：系列图固定 seed，风格切换只改风格段。
5. **推荐出图顺序**：先出 **3D 写实定妆**（信息最全），再靠纯文字降维到 Q版/2D——**全程不提参考图**，只换风格块。

> **不依赖参考图**：跨风格一致性同样靠"锚点块不动 + 只换风格段"实现，无需喂任何图。

---

## 六、风格快查（复制即用）

```
3D写实   3D rendered, PBR, subsurface scattering, UE5 render, 7.5-head-tall
3D卡通   3D cartoon, Pixar style, stylized proportions, soft GI, 6-head-tall
Q版潮玩  chibi, 3.5-head-tall, designer toy, blind box, soft vinyl
2D动画   2D anime, cel shading, flat colors, clean lineart, 7-head-tall
2D厚涂   digital painting, painterly, volumetric light, concept art
韩漫    Korean webtoon, semi-realistic, glossy, smooth gradient skin
超写实  ultra-photorealistic, 85mm f/1.8, visible pores, real skin texture
像素    pixel art, limited palette, no anti-aliasing, sprite
国风水墨 Chinese ink wash, xuan paper, flowing brush strokes, guofeng
```

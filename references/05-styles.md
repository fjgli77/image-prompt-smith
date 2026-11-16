# 05 风格族谱

> 每族给三样：**提示词块**（可直接抄）、**典型用途**、**隔离反向词**（防串味）。
> 铁律：**一次只选一族做主风格**。混搭时主族决定底层规则，副族只影响局部。
>
> **两个分层**：本文件是"快速词块"（单图够用）；要做**系列稿 / 需要跨图稳定**，改用
> `11-style-block.md` 的九槽区间块（光比、色温、焦段都给上下限，可机检越界）。
>
> **专名注意**：表中出现的工作室/导演名（吉卜力、MAPPA 等）在**探索稿**可用，
> **交付稿要转译成参数**（理由与对照表见 11 §五）。
>
> **3D 动漫人物另有一条轴**：主体是"一个 3D 动漫角色"时，"3D"不是一个词而是五条互斥路线
> （全3D写实 / 三渲二 / 国漫半写实 / 皮克斯卡通 / 风格化手绘3D），脸/眼/发/手另有专用词法。
> 见 `references/character/anime-3d.md`。

---

## 一、写实摄影族

### 1.1 商业产品摄影

```
商业产品摄影，无影棚柔光，主体居中偏上，f/8 全景深，地面自然接触阴影，材质真实
commercial product photography, seamless studio lighting, large softbox, crisp focus, natural contact shadow
```
**用途**：电商主图、详情页、KV  
**隔离反向**：`illustration, cartoon, 3d render, painting, plastic look, oversaturated, cluttered`

### 1.2 编辑/杂志摄影

```
杂志编辑大片，自然光，低饱和，浅景深，85mm，人物与环境有呼吸感
editorial photography, natural light, muted palette, shallow depth of field, 85mm
```
**用途**：品牌故事、生活方式内容  
**隔离反向**：`stock photo, stiff pose, over-retouched, studio backdrop`

### 1.3 纪实摄影

```
纪实摄影，35mm，可用光，轻微颗粒，构图不完美但真实
documentary photography, available light, 35mm, slight grain, candid framing
```
**用途**：新闻感、真实感叙事  
**隔离反向**：`posed, staged, studio lighting, perfect symmetry`

### 1.4 电影剧照

```
电影剧照，2.35:1，单一动机光源，大暗部，暗部保留细节，轻胶片颗粒
cinematic film still, anamorphic, single motivated source, deep shadows with detail, subtle grain
```
**用途**：叙事图、短剧参考、概念海报  
**隔离反向**：`flat lighting, sitcom look, overexposed, video look`

### 1.5 手机随手拍 / UGC

```
手机随手拍，轻微晃动，直出色彩，室内实用灯，未经修图
casual smartphone photo, slightly off-kilter, unedited colors, practical indoor light
```
**用途**：真实感种草、社媒原生内容  
**隔离反向**：`professional studio, perfect lighting, commercial polish, tripod steady`

---

## 二、插画与绘画族

| 子族 | 提示词块 | 用途 | 隔离反向 |
|---|---|---|---|
| **水彩** | `水彩插画，湿画法晕染，纸纹可见，留白透气` / `watercolor illustration, wet-on-wet bleeding, visible paper grain` | 绘本、文艺配图 | `digital vector, hard edges, 3d, photo` |
| **水粉/厚涂** | `水粉厚涂，笔触明显，色彩块面` / `gouache painting, visible brush strokes, flat color blocks` | 儿童、编辑插画 | `smooth gradient, airbrush, photo` |
| **编辑插画** | `编辑插画，概念化构图，几何化人物，双色限制` / `editorial illustration, conceptual, geometric figures, two-color palette` | 文章配图、观点表达 | `realistic anatomy, 3d, stock` |
| **线描/单色** | `单色线描，均匀线宽，大量留白` / `monoline line art, uniform stroke, generous white space` | 图标、极简配图 | `shading, color fill, texture` |
| **版画/Risograph** | `Risograph 印刷，可见网点，轻微套色错位，纸张肌理` / `risograph print, visible halftone dots, slight misregistration, paper texture` | 独立杂志、潮流海报 | `smooth gradient, glossy, digital` |
| **油画** | `古典油画，厚涂肌理，罩染层次，画布纹` / `oil painting, impasto, glazed layers, canvas weave` | 艺术感、历史题材 | `digital, flat, photo` |
| **素描/炭笔** | `炭笔素描，纸纹，明暗交界线清晰` / `charcoal sketch, paper tooth, clear core shadow` | 概念稿、过程感 | `color, digital paint, smooth` |

---

## 三、二次元 / 动漫族

| 子族 | 提示词块 | 用途 | 隔离反向 |
|---|---|---|---|
| 日系赛璐璐 | `日系动画赛璐璐，平涂上色，清晰描线，简单渐变` / `anime cel shading, flat colors, clean line art` | 番剧感、漫剧 | `3d render, photorealistic, painterly` |
| 厚涂二次元 | `厚涂二次元，笔触融接，光感强烈` / `painterly anime, blended strokes, strong rim light` | 游戏立绘、封面 | `flat color, cel shading, line art` |
| 韩漫/Webtoon | `韩式条漫风，柔和上色，细长眼型，干净背景` / `korean webtoon style, soft shading, clean background` | 条漫、恋爱题材 | `anime cel, chibi, 3d` |
| 美漫 | `美式漫画，粗墨线，强对比，网点阴影` / `american comic, bold ink, high contrast, halftone shadow` | 英雄题材 | `anime, soft shading, pastel` |
| 吉卜力式 | `吉卜力风格背景美术，手绘水粉感，饱和绿意，云层柔软` / `studio ghibli style background art, hand-painted gouache, lush greens, soft clouds` | 治愈场景 | `3d, photoreal, dark, cyberpunk` |
| 国漫/Q版 | `Q版三头身，圆润轮廓，糖果色` / `chibi, 3-head proportion, rounded shapes, candy colors` | 表情、周边 | `realistic proportions, mature, dark` |

> 人物细节（脸型、发色锚点、多视图）→ 转人物模式（`references/character/aesthetics.md`）。

---

## 四、3D / CG 族

| 子族 | 提示词块 | 用途 | 隔离反向 |
|---|---|---|---|
| 产品级 3D | `Octane 渲染，PBR 材质，全局光照，次表面散射，真实反射` / `octane render, PBR materials, GI, subsurface scattering` | 产品概念、KV | `illustration, flat, 2d` |
| 潮流 3D | `C4D 潮流 3D，圆润几何，糖果塑料质感，柔光棚拍` / `c4d trendy 3d, rounded geometry, candy plastic, soft studio light` | 社媒 KV、潮玩 | `realistic photo, gritty, matte` |
| 黏土/定格 | `黏土定格动画质感，指纹痕迹，微缩布景` / `claymation, fingerprint texture, miniature set` | 可爱、手作感 | `smooth plastic, photoreal, digital` |
| 低模/等距 | `低多边形，等距视角，平面化配色` / `low poly, isometric view, flat palette` | 科技插画、游戏 | `photoreal, high detail, organic` |
| 赛博 CG | `硬表面科幻，精密结构，发光缝隙，体积雾` / `hard-surface sci-fi, precision greebles, glowing seams, volumetric fog` | 概念设计 | `organic, soft, pastel` |
| 微缩场景 | `移轴微缩，景深极浅，模型质感` / `tilt-shift miniature, extreme shallow DOF` | 趣味叙事 | `full scale, flat perspective` |

---

## 五、平面设计族

| 子族 | 提示词块 | 用途 | 隔离反向 |
|---|---|---|---|
| 瑞士/国际主义 | `瑞士国际主义排版，无衬线网格，大量留白，红黑白` / `swiss international typographic style, grid, sans-serif, red-black-white` | 品牌、海报 | `ornate, decorative, gradient` |
| 包豪斯 | `包豪斯几何构成，原色三角圆方，非对称平衡` / `bauhaus geometric composition, primary colors, asymmetric balance` | 文化海报 | `photographic, realistic, ornate` |
| 扁平插画 | `扁平矢量插画，无描边，几何色块，轻微肌理` / `flat vector illustration, no outline, geometric shapes, subtle grain` | SaaS、PPT | `3d, photo, gradient mesh` |
| Y2K | `Y2K 千禧风，金属铬质感，气泡字，蓝紫渐变` / `y2k aesthetic, chrome metal, bubble type, blue-purple gradient` | 潮流、音乐 | `minimal, muted, vintage paper` |
| 孟菲斯 | `孟菲斯风格，活泼几何，撞色，波点条纹` / `memphis design, playful geometry, clashing colors, dots and stripes` | 活动、亲子 | `elegant, muted, realistic` |
| 粗野主义 | `粗野主义排版，超大字重，黑白高对比，故意不齐` / `brutalist layout, oversized type, black-white contrast, deliberate misalignment` | 独立文化、展览 | `delicate, symmetric, pastel` |
| 极简留白 | `极简主义，90% 留白，单一主体，柔和阴影` / `minimalism, 90% negative space, single subject, soft shadow` | 高端品牌 | `busy, ornate, colorful clutter` |

---

## 六、复古 / 印刷族

| 子族 | 提示词块 | 用途 | 隔离反向 |
|---|---|---|---|
| 70s 复古 | `1970 年代复古，暖橙棕，圆角字体，颗粒纸感` / `1970s retro, warm orange-brown, rounded type, grainy paper` | 咖啡、音乐 | `modern, clean, digital` |
| 宝丽来 | `宝丽来即时成像，边缘白框，褪色偏色，轻微漏光` / `polaroid instant photo, white border, faded colors, light leak` | 私摄影、纪念 | `crisp, HDR, studio` |
| 半调印刷 | `半调网点印刷，双色套印，纸张吸墨` / `halftone print, two-color overprint, ink absorption` | 报纸感、海报 | `digital gradient, glossy` |
| 老照片 | `银盐老照片，轻微划痕，边缘泛黄` / `vintage silver gelatin print, scratches, yellowed edges` | 年代叙事 | `digital, saturated, sharp` |

---

## 七、东方 / 国风族

| 子族 | 提示词块 | 用途 | 隔离反向 |
|---|---|---|---|
| 工笔重彩 | `工笔重彩，细线勾勒，矿物颜料，绢本底色` / `gongbi fine-line painting, mineral pigments, silk ground` | 国风海报、包装 | `oil painting, western, 3d` |
| 水墨 | `水墨写意，墨分五色，大片留白，宣纸渗墨` / `ink wash painting, five ink tones, vast negative space, rice paper bleed` | 文化、茶 | `colorful, photo, sharp edges` |
| 敦煌 | `敦煌壁画风，土红石青，斑驳剥落，飞天纹样` / `dunhuang mural, ochre and azurite, weathered flaking, flying apsara motifs` | 文旅、国潮 | `clean digital, western fantasy` |
| 新中式 | `新中式，月白与墨黑，留白构图，榫卯与格栅元素` / `new chinese style, moon-white and ink-black, negative space, lattice elements` | 高端品牌、空间 | `baroque, neon, cartoon` |
| 浮世绘 | `浮世绘，平涂色块，粗黑轮廓，波浪纹样` / `ukiyo-e, flat color, bold outlines, wave patterns` | 日式主题 | `3d, photoreal, gradient` |

**注意**：国风提示词里写**具体纹样名**（缠枝莲、回纹、云雷纹、海水江崖）比写"中国风"有效十倍。

---

## 八、潮流 / 亚文化族

| 子族 | 提示词块 | 用途 | 隔离反向 |
|---|---|---|---|
| 赛博朋克 | `赛博朋克，霓虹青紫，湿地面反射，密集招牌，雨夜` / `cyberpunk, neon cyan-magenta, wet reflections, dense signage, rainy night` | 科技、游戏 | `daylight, pastoral, minimal` |
| 蒸汽朋克 | `蒸汽朋克，黄铜齿轮，皮革护目镜，煤烟` / `steampunk, brass gears, leather goggles, coal smoke` | 奇幻、活动 | `clean digital, minimal` |
| 蒸汽波 | `蒸汽波，粉紫渐变，网格地平线，罗马雕塑，VHS 噪点` / `vaporwave, pink-purple gradient, grid horizon, roman bust, VHS noise` | 音乐、潮流 | `realistic, muted, natural` |
| 废土 | `废土，沙尘黄，锈蚀金属，拼接织物` / `post-apocalyptic wasteland, dust yellow, rusted metal, patched fabric` | 游戏、影视 | `clean, vibrant, suburban` |
| 暗黑哥特 | `暗黑哥特，烛光，黑纱，尖拱，低饱和冷调` / `dark gothic, candlelight, black lace, pointed arches, desaturated cool` | 悬疑、时尚 | `bright, cheerful, pastel` |

---

## 九、混合规则（唯一正确的写法）

```
主风格（决定底层渲染与解剖规则） + 副风格（只影响配色/元素/局部质感）
```

| ✅ 可行 | ❌ 必崩 |
|---|---|
| 写实摄影 + 赛博配色（照片 + 霓虹灯） | 写实摄影 + 二次元画风（同一画面两种底层规则） |
| 3D 渲染 + 国风元素（三维 + 榫卯纹样） | Q版头身比 + 写实解剖 |
| 版画风格 + 潮流配色 | 极简留白 + 满版元素 |
| 电影感光 + 插画材质（半写实） | 水墨 + 硬表面科幻（材质语言互斥） |

**写混合的句式**：

```
以【主风格】为底层，局部采用【副风格】的【具体元素】
```
例：`以商业产品摄影为底层，背景采用赛博朋克的霓虹青紫色溢光` —— 可以。  
例：`写实照片，但是动漫风格` —— 不行。

**八对底层互斥**（踩中必崩，完整表 + 原因见 `11-style-block.md` §四）：

硬光 × 柔光 ｜ 高反差 × 柔光装饰 ｜ 厚写实 × 动画平涂 ｜ 留白极简 × 大色块满幅
冷峻低照度 × 温暖高调 ｜ 颗粒胶片 × 零颗粒数字 ｜ 实拍皮肤 × 动漫五层眼睛 ｜ 精密机械秩序 × 手绘粗粝

---

## 十、风格选择决策表

| 用户信号 | 主风格 | 备选 |
|---|---|---|
| 卖货、要质感 | 商业产品摄影 | 产品级 3D |
| 讲故事、要情绪 | 电影剧照 | 纪实摄影 |
| 讲道理、要清楚 | 信息图 / 扁平插画 | 瑞士排版 |
| 要年轻、要传播 | 潮流 3D / Y2K | 孟菲斯 |
| 要高级、要克制 | 极简留白 / 杂志编辑 | 新中式 |
| 要文化、要东方 | 新中式 / 水墨 | 工笔重彩 / 敦煌 |
| 要可爱、要亲和 | 黏土定格 / 扁平插画 | 水彩 |
| 要酷、要科技 | 赛博朋克 / 硬表面 CG | 低模等距 |
| 要真实、要信任 | 纪实 / 手机随手拍 | 编辑摄影 |

---

## 十一、风格族与平台适配

| 风格族 | 最适合 | 不建议 |
|---|---|---|
| 写实摄影 | Seedream 5 / MJ `--style raw` / Flux | 老版二次元模型 |
| 二次元 | 动漫专用模型 / SDXL 动漫底模 | MJ（会带 MJ 味）/ GPT Image |
| 平面设计 | Seedream 5 / Ideogram / GPT Image | Flux（太写实） |
| 3D 渲染 | MJ / Seedream / Flux | 动漫底模 |
| 国风 | Seedream 5（中文语义优势） | MJ（纹样易糊） |
| 复古印刷 | MJ `--sref` / SDXL | Nano Banana（太干净） |

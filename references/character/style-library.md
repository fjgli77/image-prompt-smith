# 画风库（速查与混搭）

> **先读这两个文件，本文件是补充：**
> - `character-styles.md` — **人物风格族**（写实/风格化/二次元/美漫/潮流卡通/国潮…）+ 主题情绪。回答"这个人是什么调性"。
> - `render-styles.md` — **渲染介质块**（3D写实/3D卡通/Q版/2D赛璐璐/2D厚涂…）+ 头身比 + 隔离反向词。回答"用什么手段画"。
>
> **完整出图 = 人物风格族 + 渲染介质块，两段都要给。** 本文件只负责速查、混搭公式与一致性提醒。

换画风时**只替换画风段（风格族 + 介质块）**，其余段落一字不动，可快速产出同角色的多风格版本。

---

## 一、画风后缀词（速记版，完整块见 render-styles.md）

### 1. 日系赛璐璐 / 动画设定

```
anime character design sheet, cel shading, clean lineart, flat colors,
crisp black outlines, flat lighting, 2D anime style
```
代表模型：Animagine XL、Illustrious、Niji（MJ）、NovelAI V3。搭配 Danbooru 标签效果最好。

### 2. 韩系半写实 / 网漫

```
Korean webtoon style, semi-realistic, soft shading, glossy rendering,
smooth gradient skin, refined features, webtoon illustration
```
代表模型：SDXL 韩漫 LoRA、Seedream、即梦 3.1。适合恋爱漫、职场漫。

### 3. 欧美卡通 / IP 角色

```
stylized cartoon, bold clean black outlines, thick consistent line weight,
flat colors, limited palette of 5 colors, no gradients, vector-like
```
关键：**描边要粗且一致**（描边一虚角色就垮），**限色**（五六色封顶，渐变多显廉价）。代表：Disney/Pixar 风、扁平 IP。

### 4. 半写实游戏概念

```
semi-realistic game concept art, painterly texture, soft volume light,
detailed materials, cinematic composition
```

### 5. AAA 写实厚涂

```
AAA game concept art, digital painting, cinematic lighting,
high detail, realistic materials, subsurface scattering, 8k
```
代表模型：Midjourney 写实向、SDXL RealVisXL / Juggernaut。

### 6. 3D 渲染 / Pixar 风

分两支，**别混**：
- 写实 3D：`3D rendered, PBR, subsurface scattering, Unreal Engine 5, 7.5-head-tall`
- 卡通 3D：`3D cartoon, Pixar style, stylized proportions, soft GI, 6-head-tall`

代表模型：Midjourney `--style 3d`、Seedream 3D 风。完整块见 `render-styles.md`。

### 7. 像素风

```
pixel art, 16-bit sprite sheet style, limited palette,
crisp pixels, retro game character, transparent background
```
关键：像素风**必须限色 + 无抗锯齿**，否则糊。适合 sprite sheet。

### 8. 中国风水墨 / 工笔

```
Chinese ink wash painting, xuan paper texture, minimal color,
flowing brush strokes, traditional guofeng style, elegant negative space
```
写实向变体：`Chinese traditional painting, gongbi fine brushwork, silk texture`

### 9. Q版 / 潮玩 / 盲盒（chibi）

```
chibi character, Q-version, super-deformed, big head small body, 3.5-head-tall,
cute round face, large glossy eyes, designer toy collectible, blind box figure,
soft vinyl texture, product photography, pastel background
```
关键：**头身比写死**（2.5/3/3.5/4），反向加 `realistic proportions, tall, photorealistic`。完整块见 `render-styles.md`。

---

## 二、超写实真人像（商业级）

```
ultra-photorealistic, 85mm portrait lens, f/1.8 shallow depth of field,
natural skin texture with visible pores, soft even studio light,
neutral gray seamless backdrop, professional headshot
```
关键：**皮肤必须写 "visible pores / skin texture"**，否则塑料感；**镜头参数**（85mm、f/1.8）显著提升真实度。

---

## 三、风格混搭公式

```
[主体锚点] + [主风格族/介质的质感] + [次风格的构型或元素]
```

**主风格决定底层规则（比例、光影策略），次风格只影响局部**——见 `character-styles.md` 第六节。

例：`日系线稿 + 水墨上色`：
```
anime lineart combined with Chinese ink wash coloring, cel line with watercolor wash
```
例：`风格化写实（主）+ 国潮纹样（次）+ 赛博朋克光（情绪）`：
```
stylized realism as primary rule, guochao traditional motifs on costume trim, cyberpunk neon accent light
```

---

## 四、画风选择速查（风格族 + 介质 + 头身比）

| 用途 | 人物风格族 | 渲染介质 | 头身比 |
|---|---|---|---|
| 3A / 影视化 | 电影化写实 | 3D 写实渲染 / 超写实 | 7.5–8 头 |
| 竞技 / 长线 IP | 风格化写实 | 3D 卡通渲染 | 6–7 头 |
| 动画/漫画角色设定 | 二次元 | 2D 动画赛璐璐 | 7 头 |
| 条漫、女性向 | 二次元 / 韩系 | 韩系半写实 | 7 头 |
| 游戏原画、世界观 | 绘画感三维 / 国潮 | 2D 厚涂概念 | 7.5 头 |
| 仙侠、国风 | 国潮 | 2D 厚涂 / 水墨 | 按需 |
| 合家欢、周边 | 动画式三维 | 3D 卡通渲染 | 6 头 |
| 玩具、潮玩、盲盒、贴纸 | 潮流卡通 | Q版 / 潮玩 | 3.5 头 |
| 治愈系、模拟经营 | 潮流卡通 / 治愈 | 3D 卡通 / 2D 赛璐璐 | 5–6 头 |
| 科幻、机甲 | 风格化写实 | 3D 写实 / 2D 厚涂 | 7.5 头 |
| 独立游戏、复古 | 低模 / 像素 | 像素 / 极简 | 按需 |
| 真人写真、虚拟人 | 电影化写实 | 超写实真人像 | 7.5 头 |

---

## 五、画风一致性提醒

- **风格要同一**：系列图里画风段必须逐字相同，否则像换了作者。
- **负向隔离风格**：`--no realism`（要做动漫时）、反向词加 `photorealistic`（要做卡通时），防止风格串味。**完整隔离词表见 `render-styles.md` 与 `character-styles.md` 第七节。**
- **风格靠文字块锁**（首选）：把风格族 + 介质块整段逐字复制，跨图不改；`--sref` / Style LoRA / 风格参考图均为**可选增强**，非必需。
- **跨风格换头身比**：写实 7.5 头 ↔ Q版 3.5 头是允许变的；但三不变特征（脸型/瞳色/标记）必须保住。
- **跨风格换人物风格族**：只换风格族段，锚点段一字不动（如"二次元版"→"国潮版"，人脸与服装不变）。

## 相关文件

- `character-styles.md` — 人物风格族（写实/风格化/二次元/美漫/潮流卡通/国潮/低模）+ 主题情绪 + 混合规则
- `render-styles.md` — 渲染介质块 + 头身比 + 隔离反向词 + 介质×版式矩阵
- `character-asset-sheet.md` — 资产图套装的风格选择重点（三次元 vs 二次元差异）
- `outfit-design.md` — 服装搭配与配色规范（配色三公式也适用于风格定调）

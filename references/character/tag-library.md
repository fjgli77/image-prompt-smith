# 标签词库与参数建议

## 一、可替换标签词库

### 视图 / 排布

| 中文 | 英文关键词 |
|---|---|
| 三视图 | `character turnaround sheet, 3-view, front / side / back view` |
| 四视图 | `4-view character reference sheet` |
| 五视图 | `5-view turnaround` |
| 六视图 | `6-view orthographic character sheet` |
| 八视图 | `8-view character turnaround sheet, 360 degree turnaround` |
| 正交投影 | `orthographic projection, no perspective distortion` |
| 转面 | `character turnaround, rotation sheet` |
| 设计集页 | `character design sheet, model sheet, concept art sheet` |
| 角色档案海报 | `character profile poster, character design sheet, official character reference page, artbook layout` |
| **人物资产图** | `character asset sheet, production model sheet, studio reference board, turnaround plus callouts` |
| **资产图分页** | `construction sheet, proportion and silhouette chart, pose sheet, head study, costume construction sheet, extremities and props sheet, color model sheet, material study sheet, viseme chart, scale chart` |
| **服装拆解图** | `outfit breakdown sheet, costume breakdown, exploded clothing diagram, garment callouts` |
| **单品平铺图** | `coordinated outfit flat lay, clothing item breakdown, garments arranged by wearing position, no wearer` |
| **穿搭方案图** | `outfit lineup, wardrobe sheet, multiple outfits, character wardrobe variations, armor tier progression` |
| **配色规范图** | `color palette sheet, color model sheet, color swatches with hex codes` |
| **比例与剪影** | `proportion chart, head-count ruler, silhouette study, black silhouette thumbnails` |
| **口型图** | `viseme chart, mouth shape chart, phoneme mouths, lip sync reference` |
| 海报区块 | `profile table, quote text, expression reference, detail close-ups, outfit breakdown, color palette swatches, barcode, version label` |
| 装饰文字 | `decorative placeholder text, illegible labels, typographic layout` |
| 表情组 | `expression sheet, multiple expressions, expression chart` |
| 技术辅助线 | `horizontal guide lines, landmark alignment guides, technical annotation, blueprint style` |

### 主体 / 数量

| 中文 | 英文关键词 |
|---|---|
| 单人女性 | `1girl, solo` |
| 单人男性 | `1boy, solo` |
| 双人 | `2girls` / `2boys` / `couple` |
| 全身 | `full body, full body in frame, head to toe` |
| 半身 | `upper body, half body, waist up` |
| 胸像 | `bust shot, head and shoulders` |
| 头像 | `portrait, close-up face` |
| 七分身 | `cowboy shot, mid-thigh up` |

### 姿态

| 中文 | 英文关键词 |
|---|---|
| T字站姿 | `T-pose, arms out horizontally` |
| A字站姿 | `A-pose, arms slightly spread 30 degrees` |
| 自然站姿 | `natural standing pose, arms down, arms slightly away from body` |
| 双手叉腰 | `hands on hips` |
| 双手背后 | `arms behind back` |
| 坐着 | `sitting` |
| 行走 | `walking, mid-stride` |
| 回头 | `looking back over shoulder` |
| 动态姿势 | `dynamic action pose, motion blur` |

### 背景 / 排版

| 中文 | 英文关键词 |
|---|---|
| 纯白背景 | `pure white background, no ground shadow, simple background` |
| 浅灰背景 | `light gray background` |
| 米白背景 | `off-white background` |
| 中性影棚 | `neutral studio background, seamless backdrop` |
| 透明背景 | `transparent background, PNG` |
| 网格排版 | `grid layout, evenly spaced, thin gray divider lines, aligned at same height` |
| 场景背景 | `outdoors, indoors, city street, cafe interior, forest` |

### 光照

| 场景 | 关键词 |
|---|---|
| 设定稿（推荐） | `even soft front lighting, no harsh shadow` 或 `uniform studio lighting` |
| 单一主光 | `single key light from upper left 45 degrees` |
| 体积极光 | `soft volumetric light, rim light` |
| 电影级 | `cinematic lighting, three-point lighting, dramatic shadow` |
| 黄金时刻 | `golden hour, warm sunlight` |

### 画质

```
8K, ultra-detailed, sharp lineart, consistent proportions, full body in frame, high resolution, masterwork, best quality
```

Danbooru 权重写法（SD/NovelAI 类模型）：`(masterpiece:1.2), (best quality:1.1), (ultra-detailed:1.1)`

---

## 二、通用反向提示词

**多视图/设定图必备**，务必随正向提示词一起输出：

```
比例不一致, 身高不统一, 视角错乱, 凭空多肢体, 多手多脚, 手指畸形, 穿模, 背景杂点, 透视畸变, 裁切到脚, 裁切到头顶, 水印, 签名, 文字乱码, 模糊
```

英文版（部分模型只吃英文）：

```
inconsistent proportions, mismatched heights, confused viewpoints, extra limbs, extra arms/hands, deformed fingers, clipping, background noise, perspective distortion, cropped feet, cropped head, watermark, signature, garbled text, blurry, low quality
```

**一致性专用反向词**：

```
morphing face, different person between views, changed hairstyle, changed outfit, style change, inconsistent skin tone
```

**风格隔离反向词（按目标风格选，防串味）**：

| 目标风格 | 隔离反向词 |
|---|---|
| 3D 写实 | `anime, cartoon, chibi, cel shading, plastic toy, 2D illustration` |
| 3D 卡通 | `photorealistic, realistic skin, anime 2D, cel shading, uncanny` |
| Q版潮玩 | `realistic proportions, tall, long legs, photorealistic, mature, anime adult` |
| 2D 动画赛璐璐 | `3D render, CGI, photorealistic, soft airbrush gradient, chibi` |
| 2D 厚涂 | `cel shading, flat color, 3D render, thick outline, chibi` |
| 超写实真人 | `anime, illustration, painting, 3D render, cartoon, chibi, plastic skin` |

**档案海报专用反向词**：

```
garbled text, misspelled words, misaligned blocks, overlapping panels, inconsistent scale, cropped character, cheap layout
```

**人像专用反向词**：

```
deformed face, asymmetric eyes, bad anatomy, bad hands, missing fingers, extra fingers, fused fingers, long neck, cross-eyed, mutated hands
```

---

## 三、平台参数建议

### 通用构图比例

| 规格 | 比例 |
|---|---|
| 三视图 | 横构图 3:1 |
| 四视图 | 横 4:1 或 方图 1:1（2×2） |
| 五视图 | 横 5:1 或 4:1 |
| 六视图 | 4:3 或 3:2（2×3 网格） |
| 八视图 | 1:1 或 3:4（2×4 / 4×2 网格） |
| 人物设计图 | A2 竖版 ≈ 2:3 |
| 单人全身立绘 | 竖版 9:16 或 2:3 |
| 单人半身 | 4:5 或 1:1 |

### 采样（SD / ComfyUI）

| 项目 | 建议 |
|---|---|
| 步数 | 30–50（日系干净线稿可 40+） |
| CFG | 6–8（过低跑偏，过高僵硬） |
| 负面权重 | 1.0–1.3 |
| 分辨率 | 1024×1024（SDXL 基准，不要低于） |
| 采样器 | DPM++ 2M Karras |

### Midjourney

| 参数 | 作用 | 常用值 |
|---|---|---|
| `--ar` | 画幅 | 9:16 / 2:3 / 16:9 |
| `--cref [URL]` | 角色参考（V6 专用） | 固定人物 |
| `--cw` | 角色权重 | 30–80（低只锁脸，高连衣服姿势一起锁） |
| `--oref [URL]` | 全主体参考（V7） | 角色/道具/载具 |
| `--ow` | oref 权重 | 1–1000，默认 100 |
| `--sref [URL]` | 风格参考 | 固定画风 |
| `--sw` | 风格权重 | 100–300 |
| `--stylize` | 艺术化程度 | 100–400 |
| `--draft` | 草稿模式（v7，4倍速） | 快速探索构图 |

> 版本差异（关键）：`--cref` 仅 V6/Niji 6 支持；V7 用 `--oref`；V8.x 上 `--oref` 会回退到 V7 执行；Niji 7 两者都不支持，用 `--sref` + 文字描述替代。

### 即梦 / Seedream / 豆包

- 用**自然语言短句**，不要堆叠标签。
- 结构：主体 → 动作 → 环境 → 光照 → 构图 → 风格。
- **纯文字首选**：把完整锚点块（人物描述）写在最前，跨图逐字复用。
- 明确"保持不变"的部分："只换场景，保持她的脸、发型、瞳色不变"。
- 单个提示词控制在 600 英文词以内（过长会丢细节，脸恰恰在细节里）。
- 参考图（可选增强）：给每个图**分工**——"图1是人物，图2是服装，图3是街道"。**不支持参考图的版本，纯文字锚点完全够用。**

### 纯文字一致性要点（各平台通用）

| 手段 | MJ | SD/ComfyUI | Seedream/豆包 |
|---|---|---|---|
| 锚点块逐字复制 | ✓ 放最前 | ✓ 加权 | ✓ 写最前 |
| 固定种子 | `--seed 12345` | `seed: 12345` | 多数不支持，靠锚点硬扛 |
| 特征加权 | 靠 `::`/前置 | `(feature:1.2)` | 重复强调 |
| 负面锁定 | `--no different face` | 负面词框 | "不许换脸换发型" |

---

## 四、使用建议

1. **一致性（首选纯文字）**：锚点块逐字复制 + 识别串 + 固定种子 + 负面锁定，即可跨图锁人，无需参考图。单图多视图容易崩，追求精度时固定锚点、只替换视图词，逐张生成再拼版。
2. **必留关键词**：`turnaround`、`character sheet`、`model sheet`、`orthographic`、`character profile poster`。
3. **正交投影**：六视图含俯视/仰视时必须写 `orthographic projection`。
4. **统一光源**：设定稿推荐「左上45度均匀柔光」，避免各视角各打光导致拼接违和。
5. **风格块**：换画风时只替换「风格段」并同步头身比，锚点段不动，快速产出多风格版本。
6. **平台切换**：MJ 加参数、SD 用标签+加权、国产模型用自然语言；参考图均为可选增强。

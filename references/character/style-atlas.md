# 风格图鉴：一眼认出是哪一家

> `render-styles.md` 回答"是 3D 还是 2D"，`character-styles.md` 回答"什么美术调性"，
> 这一份回答第三个问题：**"具体是哪一家、哪条路线的味道"** —— 也就是能被模型命中的**流派级差异**。
>
> **用法**：先按 §一 选型，再抄对应格的关键词串。**一格只抄一串，别混两家。**

---

## 一、选型表（先定位，再看细节）

| 用户会怎么说 | 走哪一格 | 头身比 |
|---|---|---|
| 3D 动漫 / 国漫 / 玄幻 / 仙侠 / 原神风 | **A. 3D 国漫** | 7–7.5 |
| 皮克斯 / 迪士尼 / 合家欢 / 圆润可爱 | **B. 美式卡通 3D** | 5.5–6.5 |
| 梦工厂 / 穿靴子的猫 / 绘画质感 | **C. 绘画感 3D** | 6–6.5 |
| 蜘蛛侠平行宇宙 / 漫画感 / 抽帧 | **D. 漫画化 3D（NPR）** | 6.5–7.5 |
| 哪吒 / 大圣 / 中国神话 / 剧场动画 | **E. 中国剧场动画** | 6.5–7.5 |
| 日本 3D / 攻壳 / 最终幻想 / 赛博 | **F. 日式 3D** | 7.5–8 |
| 定格 / 黏土 / 手作 / 莱卡 | **G. 定格质感** | 5–6 |
| 次世代 / 3A / 虚拟人 / UE5 | **H. 全写实 CG** | 7.5–8 |
| 校园 / 青春 / 制服 / 日系插画 | **I. 校园青春** | 6.5–7 |
| 韩系 / 网漫 / 言情封面 | **J. 韩系半写实** | 7–7.5 |
| 赛博 / 霓虹 / 义体 | **K. 赛博朋克** | 7–7.5 |
| 西幻 / 骑士 / 城堡 / 龙 | **L. 西幻写实** | 7.5–8 |
| 国风 / 水墨 / 工笔 / 庭院 | **M. 国风绘画** | 按需 |

---

## 二、A｜3D 国漫（最高频，也是最容易写糊的一格）

**识别点**：五官精致、材质华丽、光影有层次，但**看得出是 3D 模型**——不是手绘，也不是真人。

### A1 半写实 3D 国漫（热血 / 战斗 / 年番）

```
semi-realistic 3D donghua, bold color grading, emissive energy VFX, glossy armor,
embroidered trim, stylized CG skin, character key visual, half-body hero shot,
cinematic ambient lighting, detailed material rendering
```

- **必写**：`bold color grading`（色彩分级浓）+ `emissive energy VFX`（自发光特效）
- **踩坑**：不写 `stylized CG skin` → 出真人脸；写了 `photorealistic` → 全身变塑料
- **负面**：`真人照片、明星脸、网红脸、画面分栏、多视角小图、画中画特写、裁切出画`

### A2 3D 国风（仙侠 / 古风女性向）

```
3D donghua, oriental fantasy character, film-grade CG render, PBR materials,
silk and gauze with visible weave, gold embroidery, jade ornaments,
soft volumetric light, atmospheric mist, stylized anime features, no pores
```

- **必写**：材质要具体（`silk / gauze / jade / gold trim`），否则出"通用古装"
- **踩坑**：写 `8K` 不增加质感，写 `silk weave, matte gold` 才有

### A3 冷灰废土 3D（工业感 / 材质化）

```
3D donghua in cold grey palette, material-driven rendering, desaturated grading,
weathered surfaces, industrial silhouette, hard key light, no warm saturation
```

- 适合：末世、机甲、废土宗门

### A4 UE 影视级玄幻（渲染走向 ①，五官走向 A1）

见 `anime-3d.md` 第 ⑥ 条。**渲染层与五官层必须同时给**，缺一层就出真人或塑料。

### 国漫的半写实五官（和 2D 不是一套）

| 部位 | 写法 |
|---|---|
| 骨相 | `narrow jaw with a defined chin, high cheekbones, small face` |
| 眼 | 瑞凤眼类：`phoenix eyes, outer corners lifted, amber iris, inner double lid` |
| 眉 | `thin brow, slightly arched, tapered tail` |
| 鼻 | `straight bridge, small tip, soft tip highlight` |
| 唇 | `thin lips, muted rose color, one corner slightly lifted` |
| 妆 | `cool-toned subtle makeup, clean eye corners, blood-toned lips` |
| 识别 | `a small flame-shaped mark under the left eye, a gold sigil between the brows` |

> **这张表的价值**：把"好看"翻译成**可执行的结构**。用户说"高级脸/仙气"，落到这里就是上面这几行。

---

## 三、B｜美式卡通 3D（皮克斯 / 迪士尼）

**识别点**：圆润、弹性、夸张表情；**角色与场景统一风格化**（这家的世界也卡通）。

```
Pixar-style 3D animation, stylized proportions, rounded sculptural forms,
squash-and-stretch facial features, soft subsurface scattering,
cinematic three-point lighting, rich color grading, path-traced render
```

- **头身比** 5.5–6.5；**必写** `squash-and-stretch`（弹性）
- **踩坑**：写 `detailed skin texture` → 出恐怖谷；写 `anime` → 串到国漫/日系
- **与梦工厂的分界**：皮克斯"角色与世界同一套风格"，梦工厂"卡通角色 + 写实环境"

---

## 四、C｜绘画感 3D（梦工厂现代 / 穿靴子的猫）

**识别点**：3D 体积 + 2D 笔触；**阶梯动画**（动作不平滑）；边缘有手绘感。

```
painterly 3D animation, stylized characters against realistic textured environments,
visible brush-like surface, graphic rim light, stepped animation feel,
bold saturated color, illustrated edge treatment
```

- **必写**：`painterly surface` + `graphic rim light`
- **区分**：与 `anime-3d.md` 的"⑤ 风格化手绘 3D"其实是同一族，这里补了**阶梯动画**这条静态图也能表达的特征
- **踩坑**：加 `smooth motion blur` → 抵消手绘感

---

## 五、D｜漫画化 3D（蜘蛛侠平行宇宙 / NPR）

**识别点**：3D 空间但**没有景深、没有动态模糊**；网点/色偏/分镜感。

```
comic-book 3D, non-photorealistic rendering, no depth of field, no motion blur,
halftone dots and slight color misregistration, ink-line accents,
graphic color blocking, dynamic comic framing
```

- **这条最反直觉**：`no depth of field, no motion blur` 是**特征**，不是缺陷
- **踩坑**：加 `cinematic bokeh` → 立刻变普通 CG
- 适合：潮流海报、游戏宣发、青年向 KV

---

## 六、E｜中国剧场动画（哪吒 / 大圣 / 神话）

**识别点**：东方神话造型 + 浓烈色彩 + **粒子/流体级特效** + 史诗构图。

```
modern Chinese feature animation, Chinese mythological design language,
dynamic flowing energy effects, dense saturated palette, epic wide composition,
stylized character design with strong silhouette, wuxia action staging
```

- **必写**：`dynamic flowing energy effects`——这家的招牌是特效的量与流动
- **踩坑**：只写 `Chinese style` → 出剪纸/年画；要写 `feature animation` + `mythological`
- **与 A 的分界**：E 更"电影/神话"，A 更"番剧/游戏立绘"

---

## 七、F｜日式 3D（攻壳 / 最终幻想 / 赛博）

**识别点**：高精度机械与材质、冷峻都市、写实比例（7.5–8），但保留日式五官。

```
Japanese 3D CG, high-fidelity mechanical detail, cool urban palette,
anime-styled faces on realistic bodies, holographic UI elements,
wet reflective surfaces, cinematic sci-fi lighting
```

- **必写**：`anime-styled faces on realistic bodies`（这是这家最独特的组合）
- **踩坑**：写 `photorealistic` → 出真人；写 `cel shading` → 串到三渲二

---

## 八、G｜定格质感（莱卡 / 黏土 / 手作）

**识别点**：材质有手工痕迹、光有微距感、**不完美**。

```
stop-motion aesthetic, handmade physical texture, clay or puppet materials,
visible fingerprints and seam lines, practical lighting, macro lens feel,
slightly imperfect surfaces
```

- **必写**：`visible fingerprints, seam lines`——"不完美"就是风格
- **踩坑**：写 `clean` / `polished` → 变塑料玩具渲染

---

## 九、H｜全写实 CG（次世代 / 虚拟人）

见 `render-styles.md` §二.1 与 `anime-3d.md` ⑤。

- **必写**：`subsurface scattering + PBR + visible pores and vellus hair`
- **反向**：`anime, cartoon, cel shading, stylized proportions, plastic toy`

---

## 十、I｜校园青春（校园风专用）

**识别点**：**逆光 + 制服款式 + 校园场景 + 空气感**。这四件缺一件就变证件照或影楼。

```
nostalgic youth anime style, backlit by golden afternoon sunlight streaming through windows,
navy sailor uniform with red ribbon and pleated skirt, knee-high socks,
classroom corridor with bulletin board and door plates, cherry blossom petals drifting,
soft bokeh, warm film-like grading
```

**三条命门（实测）**：

1. **光必须是侧逆光**：`backlit by golden afternoon sunlight`（色温 3200–3800K，光比 1:4）。写"自然光"= 死平光。
2. **制服必须写款式**：只写 `school uniform` 得到通用白衬衫；要写 `sailor uniform / blazer uniform + 领结/领带 + 百褶裙 + 袜型`。
3. **风格词用 `nostalgic youth anime`**，不要 `realistic`——后者往证件照跑。

**场景与道具**（选 2–3 件，别全上）：走廊、教室、天台、图书室、社办、樱花道、自行车棚、公告栏、黑板、课桌列。

**子风格**：

| 子风格 | 关键词 | 气质 |
|---|---|---|
| 90s 怀旧 | `90s anime aesthetic, grain, muted warm palette` | 回忆、胶片 |
| 新海诚式 | `makoto-shinkai-like light, dramatic clouds, lens flare` | 明亮、情绪化 |
| 清凉夏日 | `summer haze, cicada light, white shirt, short sleeves` | 少年感 |
| 雨天文艺 | `rain on windows, muted teal, wet asphalt` | 忧郁 |
| 热血社团 | `sports field, sweat and dust, low sun, dynamic pose` | 青春、燃 |

**踩坑**：写 `school` 两个字就完事 → 场景空、制服错、光死。**校园风是"四件套"风格，不是标签。**

---

## 十一、J｜韩系半写实（网漫 / 言情）

```
Korean webtoon style, semi-realistic manhwa illustration, glossy rendering,
smooth gradient skin, refined delicate features, soft bloom, elegant lineart, pastel grading
```

- **必写**：`glossy + smooth gradient skin`（这家最明显的手感）
- **踩坑**：加 `3D render` → 变成国漫；加 `harsh outline` → 变日漫

---

## 十二、K｜赛博朋克

```
cyberpunk, neon magenta and cyan, wet reflective surfaces, volumetric haze,
holographic signage, high-contrast night lighting, industrial detail
```

- **纪律**：**主光色只两种**（洋红 + 青）。第三种只做点缀
- **踩坑**：霓虹写满 → 颜色发脏；只写 `neon` 不给方向 → 平光

---

## 十三、L｜西幻写实（骑士 / 城堡 / 龙）

```
western fantasy realism, grounded medieval armor, weathered leather and steel,
overcast northern light, castle stone texture, atmospheric depth
```

- **必写**：`grounded` + `weathered`（不写就出游戏皮肤感）
- **踩坑**：写 `epic fantasy` 单独一个词 → 出通用游戏海报

---

## 十四、M｜国风绘画（水墨 / 工笔）

```
Chinese ink wash painting, xuan paper texture, minimal color,
flowing brush strokes, generous negative space, guofeng aesthetic
```

- 写实向变体：`gongbi fine brushwork, silk texture, mineral pigments`
- **踩坑**：混 `3D`/`CG` → 变"古风游戏宣传图"

---

## 十五、混搭禁区（两格不能同时写）

| 组合 | 为什么不行 |
|---|---|
| 皮克斯（B）+ 国漫半写实（A1） | 一个是圆润弹性、一个是精修骨相，比例语言冲突 |
| 漫画化 NPR（D）+ 电影级景深 | `no depth of field` 与 `cinematic bokeh` 直接互斥 |
| 定格（G）+ 高精度 CG | 手作痕迹与渲染精度互相抵消 |
| 国风绘画（M）+ 3D 渲染 | 一张图里既平涂又有体积光，必出四不像 |
| 校园青春（I）+ 暗黑赛博 | 光逻辑冲突（暖逆光 vs 霓虹冷光） |

**允许的混搭**：同一族内部的"风格 × 情绪"叠加（如 A1 + 暗黑、I + 雨天文艺）。
**规则**：**主风格定底层规则，次风格只影响配色与配件**（见 `character-styles.md` §六）。

---

## 十六、三件套速查（抄这一栏就够）

```
A1 半写实国漫  semi-realistic 3D donghua, bold color grading, emissive energy VFX, stylized CG skin
A2 3D 国风     3D donghua, silk and gauze, gold embroidery, jade, volumetric mist
B  皮克斯      Pixar-style 3D, squash-and-stretch, soft SSS, cinematic three-point light
C  绘画感 3D   painterly 3D, brush-like surface, graphic rim light, stepped animation feel
D  漫画化 NPR  comic-book 3D, no depth of field, no motion blur, halftone, ink accents
E  中国剧场    modern Chinese feature animation, flowing energy effects, epic wide composition
F  日式 3D     Japanese 3D CG, anime faces on realistic bodies, wet reflective surfaces
G  定格        stop-motion aesthetic, fingerprints and seams, macro lens feel
H  全写实 CG   PBR, SSS, visible pores, path-traced, cinematic rim light
I  校园青春    nostalgic youth anime, backlit golden afternoon light, sailor uniform, soft bokeh
J  韩系        Korean webtoon, glossy, smooth gradient skin, pastel grading
K  赛博        neon magenta+cyan, wet reflective, volumetric haze
L  西幻        grounded medieval armor, weathered steel, overcast northern light
M  国风        ink wash, xuan paper, mineral pigment, negative space
```

---

## 十七、自检（五项）

- [ ] 说得出是 A–M 的哪一格（不是"3D 动漫"四个字）
- [ ] 关键词串整串来自同一格，没有混两家
- [ ] 写了这一格的"必写项"（如 D 的 `no DOF`、I 的逆光）
- [ ] 没踩这一格的"踩坑项"
- [ ] 头身比与该格一致（见 §一）

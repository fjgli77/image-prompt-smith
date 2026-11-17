# 13 游戏概念设计：五类产出 × 五档画风

> 游戏美术和"插画"不是同一件事。插画交付给人看，概念设计交付给下游（建模、关卡、UI、外包、买量）。
> 画面可以糙，但**信息必须读得出来**。所以这份文档不追好看，追「读得懂 + 能复用」。

---

## 〇、先分清：什么时候来这份，什么时候去 09-recipes

| 用户要什么 | 去哪 |
|---|---|
| 一张场景氛围图 / 一张角色立绘 | `09-recipes.md` §14（单卡，最快） |
| 一个项目的成套概念（角色 + 场景 + 道具 + 图标 + 关卡） | **本文件**（五产出统一口径） |
| 角色要能进建模 | `character/modeling-handoff.md`（正交 + A-Pose + 地标线） |
| 只要一张三视图 | `character/image-types.md` §9 |

**判定句**：用户嘴里出现"我们项目""这套图""外包给谁做"——走本文件；只说"画一张"——走配方卡。

---

## 一、五类产出：一句话定生死

产出类型决定构图与信息密度，**写错这一句，后面全白搭**。

| 产出 | 必写规格句（可直接粘） | 画幅 | 光 | 信息要求 |
|---|---|---|---|---|
| **角色设定** | `character design sheet, front and side view, neutral A-pose, plain grey background` | 16:9 | 平光 | 剪影可读、服装结构可拆 |
| **场景氛围** | `wide establishing shot, atmospheric perspective, three clear depth layers` | 16:9 / 21:9 | 环境光 | 前中后景分层、尺度可判 |
| **道具立绘** | `isolated object, three-quarter orthographic view, material breakdown` | 1:1 / 16:9 | 平光 | 材质分区、磨损痕迹 |
| **图标素材** | `game icon, isolated centered subject, flat simple background, readable at 32px` | 1:1 | 平光 | 缩到小尺寸仍认得出 |
| **关卡俯视** | **二选一**：`top-down orthographic layout` 或 `isometric 2:1 layout` | 1:1 / 16:9 | 平光 | 动线可读、通路关系清楚 |

### 三条容易写错的

1. **图标必须写「缩到 32px 可读」**。不写，模型会堆碎细节；堆了碎细节，缩到 UI 里就是一团脏点。等价写法：`silhouette readable at small size, max 3 shape clusters`。
2. **道具要写「材质分解」而不是「很精致」**。道具概念的作用是告诉建模"这里是什么材质、多厚、怎么磨损"，`material breakdown: matte leather straps, tarnished brass buckles, chipped enamel` 才有用。
3. **关卡俯视里 `top-down` 与 `isometric` 是两个不能混的投影**。混着写会得到"既不俯视也不等距"的歪图，动线直接废。写死一个：
   - `top-down orthographic` — 正交正俯视，格子/通路关系最准，适合关卡布局
   - `isometric 2:1` — 等距斜视，有体积感，适合展示高低差与遮挡，**但不是精确布局**

---

## 二、五档画风：只能选一个

风格是**互斥**的。选两个 = 出一张两边都不像的图（见 `05-styles.md` 的八对互斥）。

| 画风 | 英文标签 | 造型特征 | 材质特征 | 常见误用 |
|---|---|---|---|---|
| **写实次世代** | AAA realistic game art, PBR materials | 解剖准确、比例近真人 | 有真实粗糙度与磨损，金属有氧化 | 写成 `photorealistic photo` → 变成摄影，失去"设计感" |
| **日式动漫** | cel shaded, clean lineart, flat color blocks | 头身比偏大、轮廓清晰 | 平涂为主，高光成块 | 与"3D 动漫"混写 → 出成三渲二（那是 `character/anime-3d.md`） |
| **美式卡通** | western stylized cartoon, bold simplified shapes | 夸张比例、剪影极简 | 少纹理，靠形与色 | 写成"迪士尼风" → 会被拉向幼态 3D |
| **暗黑幻想** | dark fantasy concept art, gritty weathered texture | 沉重、破败、结构复杂 | 做旧、锈蚀、污渍 | 只写 `dark` → 只是压暗，没有材质层面 |
| **赛博朋克** | cyberpunk aesthetic, neon accent lighting, wet reflective surfaces | 机能分割、硬边 | 湿反光、镀铬、全息 | 霓虹写太多 → 光盖住造型 |
| **国风水墨** | chinese ink wash, xieyi brushwork, negative space | 留白构图、笔意优先 | 墨色浓淡、宣纸渗化 | 与"国漫 3D"混 → 一个水墨一个 CG，必崩 |

**写法纪律**：风格标签 ≤3 个且同族。`dark fantasy + cel shaded` 这种跨族组合，只允许出现在**主题材 + 局部**的结构里（见 `character/genre-atlas.md` §零）。

---

## 三、光影四档（+1）：按氛围选，不按心情选

| 档 | 英文标签 | 落到画面是什么 | 适合 |
|---|---|---|---|
| **史诗逆光** | epic backlit silhouette, volumetric god rays | 主体成剪影，光从背后穿透 | 开场 CG、章节封面、大场景揭示 |
| **阴郁写实** | overcast diffused light, low contrast | 无明确阴影，色彩发闷 | 末日、悬疑、写实战争 |
| **霓虹夜景** | neon night lighting, colored rim lights, high contrast darkness | 彩色边缘光，暗部极暗 | 赛博、都市夜战 |
| **温暖黄昏** | warm golden hour light, long soft shadows | 长投影、暖橙、空气发金 | 怀旧、旅途、营地 |
| **冷峻月光** | cold moonlight, blue-grey ambient, hard rim | 冷蓝主调，边缘硬 | 奇幻夜战、密林、雪原 |

**唯一不能省的一句**：光必须有**来源**。写 `single hard key light from upper left`，别写 `beautiful dramatic lighting`——后者会让模型自由发挥，每张不一样。

---

## 四、三个可选维度（用户没说就替他定，并说明取了什么）

| 维度 | 取值 | 影响什么 |
|---|---|---|
| **配色倾向** | 高饱和对比 / 低饱和写实 / 单色调 + 强调色 / 互补色撞击 | 决定图能不能在缩略图里跳出来 |
| **材质重点** | 金属磨损 / 皮革织物 / 石材苔藓 / 全息塑料 / 木质陶土 | 决定下游建模的贴图方向 |
| **时代设定** | 中世纪 / 蒸汽朋克 / 现代都市 / 近未来 / 远古神话 | 决定道具形制与服装结构 |

**输出纪律**：补了哪几项，在提示词**前面用一句话交代**——"这轮按暗黑幻想定的，配色取了低饱和，材质重点放在金属磨损"。用户能据此判断要不要改。

---

## 五、IP 转译：这一节最值钱

用户说"要像《×××》那种感觉"——**不许写作品名，也不许写角色名**。

**理由**：模型对 IP 名的响应是不稳定的。轻则出个四不像，重则复刻出可识别的商标造型，商用直接踩线。

**做法**：把 IP 名拆成四要素，写要素不写名字。

| 拆解要素 | 问什么 | 写成什么 |
|---|---|---|
| **配色** | 主色是什么？强调色是什么？饱和度高低？ | `desaturated ochre with a single crimson accent` |
| **比例** | 头身比？四肢粗细？肩宽？ | `6.5-head proportion, broad shoulders, heavy gauntlets` |
| **材质** | 什么在反光？什么在做旧？ | `blackened steel plate, worn leather, no shine on cloth` |
| **笔触/工艺** | 厚涂还是平涂？线条粗细？颗粒感？ | `thick impasto brushwork, visible canvas texture` |

**改写示例**

```
❌ 要《巫师》那种感觉的猎魔人
✅ 一个中欧民俗奇幻世界的猎魔人：6.5 头身，宽肩厚甲，
   黑铁板甲有多处凹痕与锈迹，皮革绑带磨损发白，
   低饱和赭石主调配一点血红强调色，厚涂笔触可见画布颗粒，
   阴天散射光，光比 1:4。
```

**同理适用于**：动漫 IP（`像××那种番剧`）、影视（`像××电影的美术`）、画师名（`像××的画风`）。
一律转译成"配色 / 比例 / 材质 / 笔触"四要素。**画师名尤其不能写**——写名字等于要求复刻在世作者的风格。

---

## 六、质量词的真话（与铁律 3 对齐，别被旧教程带偏）

老教程的"必须包含"清单里有 `8k, highly detailed, masterpiece, best quality`。**这套在新一代模型上基本全废**，甚至有害。

| 平台 | 处置 |
|---|---|
| **SD 1.5 / SDXL 标签派** | 保留 2–3 个（`highly detailed, concept art`），别堆五个以上 |
| **Midjourney** | 一个都不要。MJ 把这类词当噪声，压掉画面张力 |
| **即梦 / Seedream / 豆包 / 万相** | 全部删。中文平台靠**部位与光位描述**给信息量 |
| **Flux / GPT Image / Nano Banana** | 全部删。写清"什么东西、什么材质、光从哪来"比堆形容词强 |

**真正提升"概念感"的三样**，比质量词有用得多：

1. **光的来源与光比**（`single hard key from 45° camera-left, 1:6 ratio`）
2. **材质的物理属性**（`matte, absorbs light` / `polished, sharp specular`）
3. **尺度参照**（`human figure occupies 1/8 of frame height`）

---

## 七、拼装：六句 + 一条完整示例

```
① 产出与规格：〔产出类型〕的〔必写规格句〕
② 画风：〔五档之一〕，〔≤2 个同族标签〕
③ 主体：〔是什么 + 关键结构 + 1 个识别点〕
④ 材质与世界观：〔材质重点 + 磨损方式 + 时代线索〕
⑤ 光与色：〔光档 + 来源 + 光比 + 配色倾向〕
⑥ 镜头与参数：〔景别 + 机位 + 焦段〕，〔画幅〕，画面中不出现任何文字与水印
```

**第 ⑥ 句不能省**。概念设计图不给焦段，模型会自己选——同一套设计，24mm 出成"广角小矮人"，85mm 出成"压缩扁片"，体量信息全废。

**示例（角色设定 · 暗黑幻想 · 沙漠游侠）**

```
16:9 角色设定图。dark fantasy concept art, character design sheet, front and side view, neutral A-pose, plain grey background。
写实厚涂笔触，可见画布颗粒；方形骨架，肩线平直，6.5 头身，肩膀加宽，手臂略长于常人。
一名沙漠游侠，双手各持一把弯刃短刀；头部缠亚麻头巾遮住下半张脸，只露一双琥珀色眼睛；
肩披磨破边的斗篷，胸前有皮革束带与三枚失去光泽的铜扣。
材质：沙磨过的粗糙皮革、氧化发暗的铜、布料边缘起毛；肩甲有几道浅凹痕。
阴天散射光，机位左前 45° 单硬主光，光比 1:4，低饱和赭石与炭黑主调，腰间一点暗红布条作唯一强调色。
50mm 平视，正面与侧面两视图等高并排，全身完整入画、脚不入画裁切，双臂与躯干之间留出可见空隙、无相切轮廓，八条地标线贯通。
画面中不出现任何文字、水印、标志。
```

**对照检查**：产出规格 ✓｜画风单一 ✓｜主体有识别点（双弯刃 + 遮面）✓｜材质具体到磨损 ✓｜光有来源与光位 ✓｜镜头焦段 ✓｜无 IP 名 ✓｜无 8k ✓

---

## 八、四条容易翻车的

| 翻车 | 原因 | 改法 |
|---|---|---|
| 角色设定出成单人立绘 | 没写 `design sheet, front and side view` | 补齐规格句；中文平台写 `正面与侧面两视图并排，同一姿态` |
| 场景概念没有纵深 | 只写"大场景" | 补三层：`前景岩壁 / 中景建筑 / 远景山脊`，并加 `atmospheric perspective` |
| 图标缩小就糊 | 细节太多 | 加 `max 3 shape clusters, silhouette readable at small size` |
| 关卡通路看不懂 | `top-down` 与 `isometric` 混写 | 选一个写死；布局用正交正俯视，展示用等距 |

---

## 九、与其他文件的分工

| 要 | 去 |
|---|---|
| 三视图 / 四视图的具体骨架 | `character/image-types.md` §9–§11 |
| 非人主体（道具 / 车辆 / 装备）四视图 | `character/object-views.md` |
| 角色要进建模 | `character/modeling-handoff.md` |
| 风格认不准是哪一家 | `character/style-atlas.md` |
| 题材世界观（赛博 / 废土 / 蒸朋…） | `character/genre-atlas.md` |
| 特效层（技能 / 大招 / 粒子） | `character/vfx.md` |

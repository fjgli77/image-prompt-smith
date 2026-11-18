# 03 平台方言矩阵

> **方言不是翻译。** 同一条需求换平台，要改四件事：语言、语序、权重语法、反向写法。
> 模型版本迭代很快，本表给的是**写法差异与心法**，具体参数以官方文档当日为准。

---

## 一、总表

| 平台 | 语言 | 语序 | 权重语法 | 反向 | 文字能力 | 建议长度 | 心法 |
|---|---|---|---|---|---|---|---|
| **Midjourney v7** | 英文优先 | 短句，主体最前 | `::` 分段权重；不吃 `(x:1.3)` | `--no xxx` | 中（英文短词） | 20–60 词 | 像写摄影brief，不像堆标签 |
| **SDXL / ComfyUI** | 英文 | 标签串 + 权重括号 | `(word:1.2)` `((word))` | 独立 negative 字段 | 弱 | 40–80 标签 | 精确控制，靠 negative 与 seed |
| **Flux.2 / Flux dev** | 英文 | 完整句，字面理解 | 不吃权重 | 无独立反向，写正向否定句 | 较强 | 30–80 词 | 说什么画什么，少写废话 |
| **Nano Banana Pro**（Gemini 3 Pro Image） | 中英皆可，英文更精确 | 结构化长指令（可分段/JSON） | 不吃权重 | 写"禁止项"段落 | 强 | 100–300 词 | 当需求文档写，可给约束清单 |
| **GPT Image 2** | 英文优先 | 自然语言指令 | 不吃权重 | 正向否定句 | 强 | 50–150 词 | 最擅长按指令改图，对话式迭代 |
| **Seedream 5.0 Pro**（即梦 / 豆包） | **中文原生** | 版式结构 → 形态 → 文案 → 位置 | 不吃权重 | 末尾排除项 | 强（中文优） | 60–150 字 | 当中文设计需求写，具体名称胜笼统 |
| **可灵 Kling Image 4.0** | 中文优先 | 主体 + 动作 + 场景 + 镜头 + 光 + 节奏 | 不吃权重 | **无独立框**，正向/负向混写 | 弱（后期叠） | 网页 ≤500 字符 | 像描述一张**已经拍好的照片**，不给评价词 |
| **通义万相** | 中文 | 自然语言 + 支持负向 | 弱 | 独立负向框 | 中 | 40–100 字 | 中文语义好，风格化强 |
| **Ideogram** | 英文 | 自然语言 + typography 指令 | 弱 | 弱 | **最强（排版）** | 30–80 词 | 赌文字就找它 |

---

## 二、逐个平台的改写法

### Midjourney v7

**要做**：
- 英文，短句，主语在前
- 用摄影/艺术专有名词（`Kodak Portra 400`、`Rembrandt lighting`、`editorial photography`）
- 参数放末尾：`--ar 3:4`、`--style raw`（更写实、少 MJ 味）、`--stylize 50–300`（越低越听话）、`--chaos 0–20`、`--no text, watermark`
- 一致性：`--sref <图URL>` 定风格，`--cref <图URL>` 定人，`--cw 0–100` 控制是否连衣服一起参考
- 复现：`--seed 12345`

**别做**：
- ❌ 堆 SD 标签（`masterpiece, best quality, 8k, ultra detailed`）→ MJ 会当噪声
- ❌ 用 `(word:1.3)` → 无效
- ❌ 写 `negative prompt:` → 无效，只有 `--no`

**示例改写**

需求：秋日咖啡海报主视觉

```
editorial still life photo, a ceramic cup of black coffee on a weathered oak table,
dried maple leaves scattered, autumn morning light raking from the left window,
warm amber and oat tones, 85mm lens, f/2.8, shallow depth of field,
generous empty space on the upper third --ar 3:4 --style raw --stylize 150 --no text
```

### MJ 附：电影外景剧照骨架（整段可粘）

用户要"电影剧照感 / 现场抓拍 / 写实人像"，且只要一条能直接粘的咒语时，用这套**固定系统**。
它把镜头、景别、画质、负向全部定死，只留三个变量：`{char}` `{env}` `{ratio}`。

```
Cinematic film still, documentary decisive moment shot, eye-level human perspective, 35mm full-frame cinema prime lens, rule of thirds composition, cinematic shallow depth of field, deep scene perspective, character framed from head to above the calves.
Character: {char}
Environment & Atmosphere: {env}
Natural physical lighting driven by scene ambient light, realistic shadow layering, accurate material reflection, subtle atmospheric haze, faint natural Tyndall effect, lifelike skin micro-texture, natural restrained facial expression.
Shot on ARRI Alexa Mini LF, natural 35mm film grain, authentic Kodak cinematic color grading, pure on-location real photography texture, photorealistic, high detail, --ar {ratio} --style raw
```

负向单起一行，**不塞进正向，也不加权重**（`--no` 已是负权重处理）：

```
--no deformed anatomy, distorted limbs, bad anatomy, unnatural body proportion, plastic skin, rubber mask, fake pores, CG rendering, 3D render, game screenshot, anime, illustration, painting, cartoon, oversaturated colors, exaggerated neon glow, blurry, ugly, disfigured, extra people, text, letters, logos, signs, symbols, watermarks, wrong framing, cut off awkwardly, cut above thighs only, cut below calves
```

**四条纪律**（这套骨架崩，几乎都崩在这四条）：

1. **景别固定「头到小腿以上」**——不裁在大腿，不裁到脚踝以下。因此画幅默认 **3:4**（竖向才容得下）。
   用户给 2:3 / 4:3 时，选清单里最接近的 3:4，**并在交付时说明替换了什么，不要静默改**。
2. **环境里必须点明主光源**（窗 / 灯 / 天光 / 水面反射）。"物理光照"是从场景里推出来的，场景不说光，这层就是空话。
3. **招牌与文字换无字等价物**。写"写着营业中的招牌"→ MJ 必出乱码；改成 `glowing light-bar signage`，只留光形不留字。
4. **不要在这一条上加 `8k, masterpiece`**。这套骨架靠胶片与镜头规格撑质感，堆质量词反而把 Kodak 调色压掉。


### Stable Diffusion / ComfyUI

**要做**：
- 英文标签，逗号分隔，**重要标签前移**
- 权重：`(frosted glass:1.2)`；范围 0.8–1.4，超 1.5 易崩
- 独立 negative 字段；负面词 15–30 个足够
- 采样：`DPM++ 2M Karras` / `Euler a`，steps 25–35，CFG 4–7
- 一致性：固定 seed + 固定 prompt 主体段 + IP-Adapter / ControlNet

**别做**：
- ❌ 写完整叙事句（权重会被平均掉）
- ❌ 把 `--ar` 写进正文
- ❌ 负向词写正向前缀（`no text` 放正向会被理解成"要 text"）

**示例**

```
positive:
editorial still life, (ceramic cup of black coffee:1.2), weathered oak table,
dried maple leaves, autumn window light from left, warm amber palette,
85mm, f/2.8, shallow depth of field, negative space upper third, film grain

negative:
text, watermark, logo, extra cups, clutter, oversaturated, plastic, blurry, lowres, deformed
```

### Flux（dev / pro / 2）

**要做**：
- 完整自然语言句，**字面理解**，别指望它脑补
- 要给具体：`a 35-year-old woman with a bob cut` 比 `a beautiful woman` 准
- 否定写正向：`a table with nothing on it` 而不是 `no objects`
- 文字渲染还不错，需要文字时用引号

**别做**：
- ❌ 权重括号、❌ `masterpiece` 类咒语、❌ 过长堆砌

**示例**

```
An editorial still life photograph of a single ceramic cup filled with black coffee
resting on a weathered oak table. Three dried maple leaves lie beside it. Low autumn
morning light enters from the left window and rakes across the wood grain. Warm amber
and oat color palette. Shot on an 85mm lens at f/2.8 with shallow depth of field.
The upper third of the frame is empty.
```

### Nano Banana Pro（Gemini 3 Pro Image）

**要做**：**当需求文档写**，允许分段、编号、清单。它指令跟随强，越结构化越准。

推荐七段式（官方风格）：

```
① 交付物  ② 主体  ③ 精确文案（引号）  ④ 构图与布局
⑤ 镜头与光照  ⑥ 必须保留的细节  ⑦ 禁止的改动
```

**示例**

```
交付物：一张 3:4 竖版秋季咖啡活动海报主视觉，2K。
主体：一只哑光米白陶瓷杯，盛黑咖啡，杯口有细微热气；三片干枯枫叶散落在做旧橡木桌面。
构图：主体位于画面中部偏左下，占宽 45%；上方 35% 保持纯净留白用于标题；右下角保留负空间。
镜头与光照：85mm，f/2.8，浅景深；左侧窗光 45° 侧逆，暖 3800K，光比 1:4。
保留细节：杯壁釉面细小开片、木纹节疤、叶脉纹理。
禁止：不得出现任何文字、字母、数字、logo、水印；不得添加其他杯具或人物；不得改变杯子形状。
```

### GPT Image（ChatGPT 出图 / gpt-image）

**它的强项不是"画得准"，是"听得懂"。** 指令跟随、数量与位置、局部编辑是三家最强，但它**没有负向框**，也没有参数。

#### 一、生成式：一句话用途 + 四段画面

```
一句用途（这张图干什么用）→ 主体与动作 → 构图与镜头 → 光与材质 → 排除项（正向化）
```

```
Create a 3:4 editorial still life for a coffee brand's autumn campaign:
one matte cream ceramic cup of black coffee on a weathered oak table, three dried
maple leaves beside it. Soft window light from the left, warm 3800K, shallow depth
of field, 85mm look. Keep the upper third of the frame empty. The surface stays clean
and unmarked; only the cup and leaves are present.
```

**为什么第一句要写用途**：它会把"商业产品图 / 社论配图 / 表情包"这些推理层调起来，出来的东西自动贴用途，比堆形容词有效。

#### 二、编辑式：七段（这是它真正的杀手锏）

改图时不要重写整段描述，按七段写：

| 段 | 写什么 | 例 |
|---|---|---|
| **① 动作** | remove / replace / add / recolor / restyle | `Replace the background behind the figure` |
| **② 目标** | 点名具体物体或区域 | `the grey wall behind her right shoulder` |
| **③ 外观** | 换成什么 | `with a plain light-grey studio backdrop` |
| **④ 几何** | 位置/尺度/透视/朝向 | `edge to edge, same perspective, horizon unchanged` |
| **⑤ 光照** | 匹配原图阴影、反射、色温 | `match the original soft side light and 5200K` |
| **⑥ 保真** | **必须不变的部分，逐项列出** | `Keep the face, hair, clothing, pose, camera angle and framing exactly the same` |
| **⑦ 用途** | 这张图给谁看 | `for a product page hero` |

**保真句是这套的核心**，照抄这句式：

```
Keep the character exactly the same: do not change the face shape, eyes, hairstyle,
clothing details, colors, proportions, camera angle, or position.
Change only the background.
```

**七段缺一就会"顺手美化"**——它会把脸也重画一遍，而且画得比原来"标准"，于是就不像了。

#### 三、别做

- ❌ 写 `negative prompt:` 或 `--no` → 无效，只有正向否定句
- ❌ 堆 `masterpiece, 8k` → 它按指令走，不看这些
- ❌ 一次改三处 → 会整张重绘；**一次一处，改完再改下一处**
- ❌ 依赖它写长文案 / 精确 logo → 文字能力有，但**长句与品牌标识仍不稳**，商业稿后期贴回

### Seedream 5.0 Pro（即梦 / 豆包）

**要做**：
- **中文直接写**，不用翻英文
- **版式优先**：先说版面结构，再说产品形态，再说精确文案（引号），再说位置规则，最后材质光照与排除项
- 中式元素给**具体名称**（"缠枝莲纹""月白釉""榫卯结构"），比"中国风"准得多
- 支持尺寸/比例参数与种子；文字渲染强，可赌中文短标题
- 支持空间标注式引导（框选/涂鸦）—— 有编辑器时优先用

**别做**：
- ❌ 权重括号；❌ 长篇英文；❌ 把"高级感"当风格词

**示例**

```
3:4 竖版秋季咖啡活动海报主视觉。版面上部 35% 为纯净留白，用于后期标题；下部为场景区。
一只哑光米白陶瓷杯盛着黑咖啡，杯口有细微热气，放在做旧橡木桌上，三片干枯枫叶散落左右。
左侧窗光 45° 侧逆入射，暖色 3800K，光比柔和，木纹与叶脉清晰可见。
色调为暖琥珀与燕麦色，低饱和。
画面中不出现任何文字、字母、数字、标志与水印，不添加其他杯具与人物。比例 3:4。
```

### 通义万相

- 中文自然语言，可用独立"负向提示词"框
- 风格化（国风/油画/水彩）表现好
- 中文文字能力一般，海报类仍建议后期叠字

### 可灵 Kling（Image 4.0）

**核心心法：像描述一张已经拍好的照片。** 不是提需求，是**复述你看到的画面**——位置、朝向、五官、服装、光位、镜头，一样一样铺开，一句评价词都不要。

#### 一、官方六段结构

```
主体 + 动作 + 场景 + 镜头 + 光 + 节奏
```

| 段 | 写什么 | 例 |
|---|---|---|
| 主体 | 外貌、服装、**在画面什么位置** | 年轻东亚女性，位于画面中央偏下 |
| 动作 | **一个**看得见的动作 | 背对画面，头部向左后方转动，面朝镜头 |
| 场景 | 地点 + 关键物件 | 老旧城区天台，斑驳水泥地，低矮白色护栏 |
| 镜头 | 景别 + 机位 + 焦段 + 景深 | 中焦，平视，近景平拍，中光圈中景深 |
| 光 | 方向 + 性质 + 色温 + 对比 | 45° 斜侧光，硬光，冷暖对比，整体偏暖 |
| 节奏 | 一张静图写"瞬间感" | 午后独自发呆时被镜头捕捉的一瞬 |

#### 二、官方式铺开顺序（照着写就不空洞）

```
① 位置 → ② 朝向与视线 → ③ 五官（脸型/肤色/身材）→ ④ 发型发色
→ ⑤ 服装（款式→图案→材质→贴合感）→ ⑥ 时间天气光位
→ ⑦ 镜头（焦段/机位/景别/景深）→ ⑧ 背景物件 → ⑨ 前景遮挡
```

这套顺序的价值：**它把"氛围"翻译成了可数的物件**。写完数一下 ⑧ 里点了几件东西，少于三件背景必空。

#### 三、抽象词必须换具体（官方明确列了这条）

| ❌ 官方不推荐 | ✅ 换成 |
|---|---|
| 高级感 / premium look | 侧逆光勾出轮廓，背景虚化，表面可见细腻哑光颗粒 |
| 复古感 / vintage feel | 泛黄墙面、家具边缘磨损、暖色白炽灯 |
| 中产家庭厨房 | 木纹橱柜、台面上有电饭煲与调料罐、冰箱门贴着便利贴 |
| 不要露出打电话的人的脸 | 人物以侧脸出现，正在通电话 |

**规律**：评价词换成"能看见什么"，否定句换成"正面描述你想要的"。

#### 四、参考图必须指派角色（不指派它会自己猜）

```
@图1 定义场景：保留其空间布局、陈设与光线。
@图2 定义女主角：保留其五官、发型与服装。
```

**只给图不说用途 = 结果不可控**，这是可灵官方文档点名的坑。

#### 五、负向与长度

- **没有独立负向框**：API 的 prompt 允许"正向与负向描述混写"，网页端同理 → 排除项写成一句 `画面中不出现任何文字、水印、第二个人物`
- **网页端 ≤500 字符**（比即梦的 800 还紧），API 端宽松得多但长了照样掉元素
- **图内文字弱**：海报文字一律后期叠，别赌

#### 六、完整示例（可直接改字）

```
3:4 竖版，中景人像。一位二十多岁的东亚女性站在老旧城区天台的水泥地上，
位于画面左侧偏下，身体朝向画面右侧呈半侧身，头部微抬，视线望向左上方天空，
表情安静疏离。圆润脸型，肤色自然偏暖，黑色齐耳短发，厚齐刘海。
身穿黑色无袖连衣裙，裙面有细小白色波点，领口带蕾丝与细褶，面料轻薄贴垂。
秋季晴天午后，自然光以 45° 斜侧硬光入射，投下斑驳光影，冷暖对比明显偏暖。
中焦镜头，略低于面部高度的轻微仰拍，中景深，背景略微虚化。
背景为灰白水泥墙与橙黄枝叶，前景一根暗红金属扶手斜向压角，不遮挡人物。
画面中不出现任何文字、水印与第二个人物。
```

### Ideogram

- 英文，专为 typography 优化；需要**图上真实排版**时首选
- 写法：`poster with the headline "AUTUMN COFFEE" in bold condensed sans-serif, centered in the lower third`
- 复杂中文仍不可靠

---

## 三、迁移改写清单（换平台必走）

把一条提示词从 A 平台搬到 B 平台，按顺序改：

1. **语言**：英文 ↔ 中文（Seedream 用中文更好）
2. **语序**：叙事句 ↔ 标签串 ↔ 版式蓝图
3. **权重**：删掉/加上 `(x:1.3)`
4. **反向**：独立 negative ↔ `--no` ↔ 正向否定句 ↔ 末尾排除段
5. **参数**：`--ar` ↔ 尺寸比例字段 ↔ 正文比例描述
   注意 **GPT Image 与可灵不是"参数式"平台**：比例写进正文（`3:4 竖版`），没有 `--ar`、没有权重
6. **长度**：MJ 砍到 20–35 词；**可灵网页端砍到 500 字符**；Nano Banana 可扩到 100 词
7. **能力补偿**：目标平台文字弱 → 删掉文字期望，改"假文字 + 后期"

**迁移完成的标准**：把两个版本并排读，**画面信息量一致，句法完全不像**。

---

## 四、平台选择速查

| 需求 | 首选 | 次选 |
|---|---|---|
| 赌画面内真实文字（英文） | Ideogram / GPT Image | Nano Banana Pro |
| 赌画面内真实中文 | Seedream 5.0 Pro | GPT Image（弱） |
| 人物多图一致性 | Nano Banana Pro（多图参考） | Seedream 5 Pro + seed |
| 复杂多物体排版（信息图） | Seedream 5.0 Pro | Nano Banana Pro |
| 写实摄影质感/肤色 | Seedream 5.0 Pro | MJ v7 `--style raw` |
| 精确构图控制 | SDXL + ControlNet | Flux + 参考图 |
| 艺术风格探索 | MJ v7 `--sref` | Flux |
| 快速草稿 | Nano Banana 2 Lite / Seedream Flash | MJ `--draft` |
| 按指令精细改图 | **GPT Image**（七段编辑式） | Nano Banana Pro |
| **中文写实人像 / 纪实生活感** | **可灵 Image 4.0** | Seedream 5.0 Pro |
| **中文 + 空间位置要求很具体** | **可灵**（位置/朝向写进正文） | Seedream |
| 中文语义理解 | Seedream / 通义万相 / 可灵 | — |

---

## 五、最容易翻车的七个方言坑

1. **把 SD 标签喂 MJ** → 出图平庸且油腻。MJ 要句子。
2. **给 Seedream 写英文长句** → 中文平台优势全废。
3. **给 Nano Banana 写 20 词短句** → 它有能力吃 300 词结构化指令，你浪费了。
4. **在 Flux 里写 `no text`** → 它可能真的画出 "no text" 字样。写 `the image contains no lettering` 或 `a plain blank surface`。
5. **跨平台只换语言不换语序** → 权重散掉，主体变淡。
6. **给可灵写"高级感 / 氛围感"** → 官方明确不推荐：它会把评价词当噪声。换成一串可数的物件与光位。
7. **给 GPT Image 编辑时不写保真项** → 它会把脸也"顺手美化"一遍，于是不像了。必须逐项列 `keep … exactly the same`。

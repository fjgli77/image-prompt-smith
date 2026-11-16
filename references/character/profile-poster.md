# 角色档案海报（Character Profile Poster · 展示级）

> **先分清本文件与 `character-asset-sheet.md`：**
> - **本文件 = 展示级**：给人看的角色资料页 / IP 定妆页 / 美术设定集内页。**好看、有设计感优先。**
> - **`character-asset-sheet.md` = 生产级**：给建模/绑定/动画/周边用的工程图套装。**信息完整、可测量、可复现优先。**
>
> 用户说"档案海报 / 资料页 / 角色设定页"→ 本文件；说"资产图 / 资产套装 / 设定图套装 / 生产交付图"→ `character-asset-sheet.md`。

对应参考图那种**「3D CHARACTER DESIGN」设定海报**：一整页把角色从「大立绘 → 档案字段 → 表情 → 细节特写 → 三视图 → 色卡」全部排完，像官方角色资料页 / IP 定妆页 / 美术设定集内页。

**这是本技能的高阶版式**，比单纯三视图信息量大得多，也更容易崩。核心心法：**一图直出拼不齐，就用"分块生成 + 本地拼版"**（见第四节）。

---

## 一、版式分区（照这张图记）

```
┌──────────┬──────────────┬─────┬─────┬─────┬────────┐
│ A 标题组  │  B 档案字段   │      │     │     │ F 细节 │
│ 大标题    │  角色档案表   │ C   │ C   │ C   │  特写列 │
│ 副标题    │  （姓名/身高/ │ FRONT│SIDE │BACK │ ────── │
│ 竖排标语  │   年龄/性别/  │     │     │     │ G 色卡 │
│ 英文短句  │   职业/性格/  │ 全身 │全身 │全身 │ ────── │
│          │   武器/外貌）  │ 立绘 │立绘 │立绘 │ H 版本 │
│ D 大立绘  │ ──────────── │     │     │     │  标签  │
│ （最大    │  E1 台词典     │     │     │     │ ────── │
│  主视觉） │  E2 表情参考4格 │     │     │     │ I 条形码│
│          │  E3 细节展示4格 │     │     │     │        │
│          │  E4 服装细节5格 │     │     │     │        │
└──────────┴──────────────┴─────┴─────┴─────┴────────┘
   左 1/4        中列 1/4      三视占中右 1/3      右栏 1/8
```

| 区 | 名称 | 内容 |
|---|---|---|
| A | 标题组 | 大标题（如 BLUE MIRAGE）+ 副标题（3D CHARACTER DESIGN）+ 竖排中文标语 + 英文短句 + 装饰星形 |
| B | 角色档案 | 姓名/身高/年龄/性别/职业/性格/武器/外貌 八字段 |
| D | 主视觉立绘 | 最大的人像（多为半身或 3/4 身），占据左侧或左中，是视觉中心 |
| E1 | 台词典 | 角色一句台词 + 签名（手写体） |
| E2 | 表情参考 | 4 格头像（冷却/微笑/生气/惊讶），下方各配小字 |
| E3 | 细节展示 | 4 格局部特写（眼部/唇部/耳饰/颈饰） |
| E4 | 服装细节 | 5 格服装单品拆解（上衣/腰饰/袖/裙/鞋） |
| C | 三视图 | FRONT / SIDE / BACK 全身立绘，等高等距，顶部有英文视角标注 |
| F | 三视图细节 | 右侧竖排特写（眼/额/耳/发/鞋），各配中文小标 |
| G | 色卡 | 一排色块（主色/辅色/强调色） |
| H | 版本标签 | 底部 LOGO 组（如 CHARACTER CONCEPT / NEXT GEN） |
| I | 条形码 | 左下或右下装饰条形码 + 编号 |

---

## 二、文字处理铁律（最容易翻车的地方）

**AI 画中文/长段英文必乱码。** 三条策略：

1. **假文字策略（推荐）**：提示词明确要求 `decorative placeholder text, illegible small text, lorem-ipsum-like labels`，让模型只画"像字的排布"，不画可读内容。成熟设定集海报常用此法。
2. **固定短词策略**：只保留模型能写对的**少数英文短词**——大标题、`FRONT / SIDE / BACK`、`CHARACTER PROFILE`、`DETAILS`。这些反复出现、抗乱码。
3. **后期加字策略（最强）**：出**无字纯净版**海报底（只说版式分区、不说文字），再用本地工具（Pillow / HTML）叠字。中文一类基本只能靠这个。见第五节模板。

> 参考图里中文档案字段（姓名 星澜 / 身高 170cm…）几乎一定是**后期排版**加的，不是模型一次画的。

---

## 三、三种产出路径

### 路径 A — 一图直出（快，适合 3D 模型 / Seedream）

一句话描述整页，接受一定混乱。适合 3D 渲染风（模型排布能力较强）：

```
完整角色设定海报，character profile poster / character design sheet，
一页包含全部区块，专业美术设定集排版：
左侧：角色大立绘（3/4身，主视觉，最大）+ 标题组 + 竖排标语；
中列：角色档案字段表 + 一句台词 + 4格表情参考 + 4格细节展示 + 5格服装细节；
中右：FRONT / SIDE / BACK 三视全身立绘，等高等距，顶部英文视角标注；
最右：竖排细节特写列（眼/耳/发/鞋）+ 底部色卡色块 + 版本标签 + 条形码。
【外貌锚点：<逐字复制锚点表>】
【服装：<逐字复制>】
【风格块：<从 render-styles.md 整段抄>】
版面：白色/浅蓝背景，细线分隔区块，区块对齐，装饰性星形图标点缀，
      文字为装饰性占位（decorative placeholder text），避免乱码。
光照：统一左上45度柔光。
画质：A2 竖版海报比例 ≈ 2:3，8K，印刷级细节。
```

> 路径 A 提示词**句子短、区块清**。切忌把每个区块写成长段，会让模型顾此失彼。

### 路径 B — 纯文字分块生成 + 本地拼版（最像参考图，推荐）

**这是复刻参考图的正确做法，且全程纯文字、不喂参考图。** 逐个区块单独出图（每块都用**同一份锚点块逐字复制**），保证每块质量，再拼版：

| 块 | 单独提示词要点 | 产出比例 |
|---|---|---|
| ① 三视图 | 用 view-specs 三视图规格，白底 | 3:1 |
| ② 表情参考 | expression-specs 四格，白底 | 4:1 |
| ③ 细节特写 | 局部特写（眼/唇/耳/颈），白底方图 | 每格 1:1 |
| ④ 服装拆解 | 单品平铺/特写，白底 | 每件 1:1 |
| ⑤ 主视觉立绘 | 半身/3/4身，竖版 | 2:3 |
| ⑥ 色卡 | 直接由 ⑤ 的主色提取，本地生成 | 横条 |

拼版用 **HTML 模板**（第六节）或 Pillow，对齐到第一节的分区图。**文字全部在拼版时叠加**，天然无乱码。

### 路径 C — 纯文字无字视觉版（最快拿到可交付底稿）

只出**五大视觉块**（主立绘 + 三视图 + 表情 + 细节 + 服装），不排文字，作为海报底。全程纯文字提示词。适合先看效果，也适合后续手动排版。

> **三条路径都不依赖参考图。** 所有区块共用同一份锚点块（逐字复制），靠文字锁住角色一致。参考图只在你追求像素级复刻时才作为可选增强叠加。

---

## 四、完整直出提示词模板（3D 写实档案海报 · 中文，适配 Seedream/即梦/豆包）

> 用法：替换 `<>` 内内容。这是**路径 A**，直接可粘。

```
完整角色设定海报，character profile poster，专业美术设定集内页排版，一页多区块：

【左侧主视觉区】占页面左侧约三分之一：超大角色半身立绘（3/4身，最大视觉主体），
左侧竖排大标题「<角色名英文>」，下方副标题「CHARACTER DESIGN」，旁边竖排中文标语，
底部手写体签名与英文短句，点缀装饰星形。

【中列档案区】上方「CHARACTER PROFILE」角色档案表，字段：姓名、身高、年龄、
性别、职业、性格、武器、外貌；其下一句角色台词（装饰性文字）；
再下 4 格表情参考（冷却、微笑、生气、惊讶）横向排列，每格下方小字；
再下 4 格局部细节特写（眼部、唇部、耳饰、颈饰）；
再下 5 格服装单品细节（上衣、腰饰、袖口、裙摆、鞋子）。

【中右三视图区】三格全身立绘水平排列，顶部英文标注 FRONT、SIDE、BACK，
三格人物高度完全一致、脚底对齐同一水平线、服装造型完全一致。

【右栏细节区】竖排 5 格局部特写（眼部、额头、耳部、发饰、鞋子），
下方一排色卡色块（主色/辅色/强调色），底部版本标签组与装饰条形码。

【角色设定】<外貌锚点逐字复制，如 19-year-old East Asian girl, oval face, blue-grey eyes,
soft elegant features, silver-grey long wavy hair with side part, 170cm, slim elegant build>
【服装】<如 白色蕾丝束胸上衣、银蓝色纱质外披、高开衩短裙、水晶系带高跟鞋、水晶颈饰与耳饰>

【渲染风格】<从 render-styles.md 抄 3D 写实块：3D rendered character, photorealistic 3D model,
Unreal Engine 5 render, subsurface scattering skin, PBR, realistic hair strands,
soft global illumination, cinematic rim light, 7.5-head-tall>
【版面】浅蓝白背景，区块之间细线分隔，整体对齐留白，高级杂志排版感。
【文字】所有小字为装饰性占位文字（decorative placeholder text, illegible）。
【光照】统一左上前方45度柔光，全页光照一致。
【画质】A2 竖版海报，≈2:3，8K 超高清，印刷级细节，边缘锐利。
```

---

## 五、负向与自查

**反向提示词（档案海报专用）**：

```
文字乱码, 中文错字, 拼写错误, 区块错位, 区块重叠, 比例不一致, 三视图高度不齐,
人物裁切, 多手多脚, 手指畸形, 水印, 签名乱码, 背景杂点, 颜色溢出, 廉价排版,
低分辨率, 模糊, 透视畸变
```
英文：`garbled text, misspelled words, misaligned blocks, overlapping panels, inconsistent scale, cropped character, extra limbs, deformed fingers, watermark, cheap layout, low resolution, blurry`

**出图自查**：

- [ ] 三视图三格高度/脚底线是否对齐？服装是否同款？
- [ ] 主视觉是否够大（视觉中心）？
- [ ] 表情 4 格是否同一张脸、同角度？
- [ ] 细节特写是否清晰、有信息量（不是纯重复）？
- [ ] 色卡是否与服装配色一致？
- [ ] 文字是否乱码？（乱码就走路径 B/C）
- [ ] 整页留白与对齐是否有"官方设定集"感？

---

## 六、拼版模板（路径 B 用 · HTML，无乱码）

把各区块图放同目录，改下面文件名，浏览器打开 → 截图 / 或转图。

```html
<!DOCTYPE html><html><head><meta charset="utf-8"><style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#f4f6fa;font-family:"Helvetica Neue",Arial,sans-serif;color:#3a4152}
.page{width:1600px;height:900px;background:#fff;display:grid;
  grid-template-columns:340px 380px 1fr 220px;gap:14px;padding:22px}
.col{display:flex;flex-direction:column;gap:10px}
h1{font-size:44px;letter-spacing:4px;color:#8ea2c8;line-height:1}
h2{font-size:12px;letter-spacing:2px;color:#8ea2c8;border-bottom:1px solid #d8e0ee;padding-bottom:4px}
.kv{display:grid;grid-template-columns:64px 1fr;font-size:12px;line-height:1.9}
.kv b{color:#9aa7bd;font-weight:400}
img{width:100%;display:block;object-fit:cover;background:#f0f3f8}
.row{display:grid;gap:6px}
.c4{grid-template-columns:repeat(4,1fr)}
.c3{grid-template-columns:repeat(3,1fr)}
.swatch{display:flex;height:26px}
.swatch i{flex:1}
.star{color:#a9bde0;font-size:18px}
</style></head><body><div class="page">

  <div class="col">
    <div class="star">✦</div>
    <h1>BLUE<br>MIRAGE</h1>
    <h2>3D CHARACTER DESIGN</h2>
    <p style="font-size:11px;line-height:1.8;color:#9aa7bd">
      蓝色幻境<br>梦与爱交织<br>海的叛逆少女
    </p>
    <img src="main-portrait.png" style="flex:1">
  </div>

  <div class="col">
    <h2>CHARACTER PROFILE</h2>
    <div class="kv">
      <b>姓名</b><span>星澜</span><b>身高</b><span>170cm</span>
      <b>年龄</b><span>19</span><b>性别</b><span>女</span>
      <b>职业</b><span>学生 / 音乐系</span><b>性格</b><span>温柔 / 清冷 / 偶尔火辣</span>
      <b>武器</b><span>吉他 / 音乐</span><b>外貌</b><span>银灰长发 / 蓝灰色眼睛</span>
    </div>
    <h2>表情参考</h2>
    <div class="row c4">
      <img src="expr-1.png"><img src="expr-2.png"><img src="expr-3.png"><img src="expr-4.png">
    </div>
    <h2>细节展示</h2>
    <div class="row c4">
      <img src="d1.png"><img src="d2.png"><img src="d3.png"><img src="d4.png">
    </div>
    <h2>服装细节</h2>
    <div class="row c4">
      <img src="c1.png"><img src="c2.png"><img src="c3.png"><img src="c4.png">
    </div>
  </div>

  <div class="col">
    <div class="row c3" style="flex:1">
      <div><div style="font-size:11px;letter-spacing:2px;color:#9aa7bd;text-align:center">FRONT</div><img src="front.png"></div>
      <div><div style="font-size:11px;letter-spacing:2px;color:#9aa7bd;text-align:center">SIDE</div><img src="side.png"></div>
      <div><div style="font-size:11px;letter-spacing:2px;color:#9aa7bd;text-align:center">BACK</div><img src="back.png"></div>
    </div>
  </div>

  <div class="col">
    <h2>三视图细节</h2>
    <img src="f1.png"><img src="f2.png"><img src="f3.png">
    <h2>色卡</h2>
    <div class="swatch"><i style="background:#0b0e16"></i><i style="background:#8ea2c8"></i>
      <i style="background:#c9d4e8"></i><i style="background:#eef1f7"></i></div>
    <h2>BLUE MIRAGE</h2>
    <p style="font-size:9px;color:#9aa7bd">CHARACTER CONCEPT<br>NEXT GEN</p>
    <div style="height:26px;background:repeating-linear-gradient(90deg,#2b2f3a 0 2px,#fff 2px 4px,#2b2f3a 4px 5px,#fff 5px 9px)"></div>
  </div>

</div></body></html>
```

---

## 七、版式变体

| 变体 | 变化 | 适合 |
|---|---|---|
| 经典档案页 | 如上，左立绘 + 中档案 + 右三视 | 官方设定集、IP 定妆 |
| 三视海报 | 去主立绘，三视放大占主位 | 建模参考、原画交付 |
| 潮玩设定卡 | Q版 + 盲盒风 + 色卡放大 | 潮玩、周边、盲盒 |
| 场景海报 | 主视觉换成带场景的半身，去掉细节格 | 宣传图、壁纸 |
| 极简白模 | 只留立绘 + 三视 + 色卡，大量留白 | 高级感、品牌向其 |

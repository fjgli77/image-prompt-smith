# 服装结构：从"穿了什么"到"怎么穿"

> `outfit-design.md` 管**搭配与交付图**（三色、版式、换装图），这一份管**单件服装怎么写准**。
> 服装失败的两种典型：**堆成一块布**（写得太多太泛）与**漂成默认款**（每轮重写，不是同一套衣服）。
>
> **一句话：服装要按"层"写、按"区"写、按"件"锁。**

---

## 一、分层四件法（复杂服装唯一稳的写法）

一次性写"一套华丽古装"→ 模型给你一团金属与布料的混合物。**拆成四层，它就会逐层画。**

```
内层（贴身）→ 中层（主结构）→ 外层（罩/披挂）→ 配饰（金属与挂件）
```

**示例（轻甲战装）**：

```
内层：贴身的深灰高领针织内衬，领口与手腕处露出一指宽。
中层：锁子甲短衫，环状纹理在肩部垂坠，下摆至髋。
外层：哑光黑钢胸甲，边缘錾刻云纹，肩甲分三段层叠，略有划痕与凹痕。
配饰：腰间三指宽皮革腰带 + 一枚方形玉扣；左腕皮质护腕镶银钉；右肩一枚兽首吞口。
```

**为什么有效**：模型对"层"有明确的空间概念（谁在谁上面、谁露出多少），对"一套"没有。

**四层各自必须写的槽位**：

| 层 | 必写 | 不许省 |
|---|---|---|
| 内层 | 覆盖到哪（领口/袖口露出多少）、材质、颜色 | 露出量——决定"有没有内搭感" |
| 中层 | 主结构（甲/袍/衣）、长度、闭合方式 | 长度（到髋/到膝/到踝） |
| 外层 | 披/罩/氅/纱、垂坠、风向 | 风向与垂坠 |
| 配饰 | 位置 + 件数（≤3） | 位置（腰/腕/肩/发） |

---

## 二、甲胄：三层递进（审计里的实测结论）

泛写"古代铠甲"，十张里八张糊成无名杂兵甲。**三步递进能把稳定率翻倍**：

```
① 甲种：层叠鱼鳞甲片 / 山文甲片 / 板甲 / 锁子甲 / 鳞札混编
② 纹路走向：甲片顺肩线向下压叠 / 横向环叠 / 放射状排列
③ 部件清单：兽头肩吞、三段式护臂、宽腰封、护心镜、胫甲
```

**成品句**：

```
层叠鱼鳞状甲片，甲片顺肩线向下压叠；双肩兽头吞口，三段式护臂，
宽腰封压住下缘，胸口一块圆形护心镜；哑光黑钢，边缘磨出亮边。
```

**一个真实踩坑（务必避开）**：

> 同时写「鳞片」和「铠甲」，模型会把**生物鳞片的长法**套到甲片上，腹部变成一节一节的蜈蚣壳。
> **改法**：删掉"鳞片"，只留 `鱼鳞状甲片`（带"甲"字）；反向加 `板块碎裂、条纹错乱、生物鳞片`。

**甲胄四条约束**：

| 约束 | 写法 | 原因 |
|---|---|---|
| 关节处不横压硬物 | `armor segments break above and below the elbow` | 否则绑定/动画必穿 |
| 甲片有厚度 | `each plate has visible thickness and a beveled edge` | 否则像贴图 |
| 磨损要有方向 | `scratches running diagonally, dents on the left pauldron` | 随机磨损显脏 |
| 金属只两处高光 | `specular only on the plate edges and the boss` | 否则满屏反光 |

---

## 三、幻想材质词表（日常材质不够用）

| 类 | 中文 | 英文 | 一句写法 |
|---|---|---|---|
| 冰 | 冰晶、霜面、半透冰片 | `ice crystal, frosted surface, translucent ice shards` | `faceted ice-crystal mantle, cold blue refraction at the edges` |
| 玉 | 玉、羊脂玉、青玉 | `jade, mutton-fat jade, celadon jade` | `polished jade plates with subsurface glow` |
| 玄铁 | 玄铁、乌金 | `blackened iron, dark steel` | `matte blackened iron, worn edges showing bright steel` |
| 鎏金 | 鎏金、错金 | `gilt, gold-inlaid` | `thin gilt trim only along the seams` |
| 薄纱 | 薄纱、烟纱、半透纱 | `sheer gauze, translucent chiffon` | `layered sheer gauze, edges catching light, body visible as silhouette` |
| 灵绸 | 灵绸、流云绸 | `spirit silk, cloud-flow silk` | `silk that flows like water, slight inner glow` |
| 鳞甲 | 分片鳞甲 | `overlapping scale plates` | 见 §二（**带"甲"字**） |
| 羽织 | 羽织、翎羽 | `feather weave, plumage` | `layered feather panels, barb lines visible` |
| 符文织锦 | 符文织锦 | `rune-woven brocade` | `abstract non-readable rune pattern woven into the fabric` |
| 能量衣料 | 半透能量衣、光织 | `semi-transparent energy fabric` | `a thin layer of light-formed fabric over the underlayer` |
| 兽皮/骨 | 兽骨、鳞皮 | `bone plates, scaled hide` | `bone segments strung along the shoulder line` |

**材质混搭纪律**：**一件主材 + 一件对比材 + 一件点缀材**。
例：`丝缎（主）+ 哑光金属（对比）+ 玉（点缀）`。三种以上的主材 = 视觉无重点。

### 3.1 材质三件套：主材质 + 质感修饰 + 光泽垂坠

**只写材质名 = 没写。** 单写 `silk` / `leather` 必出塑料或布贴图。

| 单写（必崩） | 三件套 |
|---|---|
| silk | `silk fabric, smooth lustrous surface, subtle sheen, flowing drape` |
| leather | `distressed leather, natural grain, satin finish with polished toe` |
| knitwear | `visible knit texture, ribbed cuffs, soft matte surface` |
| linen | `coarse linen weave, visible slubs, matte with crisp folds` |
| satin | `satin, high specular sheen, weighty folds pooling at the hem` |

**三件各管一件事**：材质名定身份，质感修饰定表面，光泽/垂坠定它与光的关系。

### 3.2 皮革四态（最实用的一张对照表）

同一种皮，四种处理，四种反光，四种崩法：

| 皮面 | 反光特征 | 写法 | 崩法 |
|---|---|---|---|
| **光面** | 整片柔光，边缘回弹 | `polished calf leather` | 反光过曝，像塑料 |
| **油蜡** | 哑中带油，光晕成片 | `oil-waxed leather, subtle sheen, pull-up effect` | 误写成 `waxed fabric`，出防水布感 |
| **漆皮** | 镜面，高光成条 | `patent leather, hard specular highlight` | 高光失控，整件变雨靴 |
| **磨砂/翻毛** | 不反光，看绒面过渡 | `matte nubuck, fine nap, short nap, soft falloff` | 被画成普通布面，皮感全失 |

**皮革想真，必须补"工艺痕迹"**：

| 痕 | 写法 | 作用 |
|---|---|---|
| 缝线 | `visible saddle stitching`（粗斜马鞍缝）、`contrast thread`（撞色线）、`double stitching` | 证明"这是一件成品"，不是一块料 |
| 磨损 | `worn edges`（边缘磨白）、`scuffed corners`（磕碰的角）、`creases at elbows`（肘弯褶） | 证明"用过" |
| 包浆 | `patina on the contact areas` | 高频接触处发亮，是高级感的来源 |

> **位置要点名**：缝线写在下摆/包盖边缘/袖口，磨损写在手肘/膝/鞋头。不点名 = 随机撒。

### 3.3 褶皱要写受力方向

`folds` 无效——模型知道有褶，不知道往哪折。

| 受力 | 写法 |
|---|---|
| 重力 | `gravity drapes, vertical folds pooling at the ankles` |
| 风 | `windblown folds, fabric pulled taut on the windward side` |
| 动作挤压 | `stress wrinkles at the armpit and elbow, compression folds at the waist` |
| 湿 | `wet fabric clinging, darker where it touches the skin` |

---

## 四、结构槽位清单（写完自查，缺一件就少一块设计）

| 部位 | 槽位 | 例 |
|---|---|---|
| **头** | 发冠/额饰/面帘/耳饰/头纱 | `silver filigree crown with a single blue gem, no tassels` |
| **颈肩** | 立领/披肩/肩甲/肩吞 | `high collar, structured pauldron on the left only` |
| **胸** | 主结构 + 装饰件 | `fitted breastplate with a vertical diamond setting` |
| **腰** | 腰封/腰带/腰链/挂件 | `three-finger-wide metal waist ring, engraved with beast motif` |
| **臂** | 袖型（广袖/窄袖/无袖/纱袖）+ 护臂 | `sheer black sleeves flaring at the wrist, bracer on the left` |
| **腿** | 裙/裤/开衩/腿环 | `front slit to mid-thigh over a longer inner skirt` |
| **足** | 靴/履/赤足 | `fitted black boots with gilt trim` |
| **披挂** | 披风/披帛/纱/拖尾 | `heavy brocade cloak spreading sideways-back, wind from the left` |

**写法顺序**：**从上到下 + 从内到外**。乱序写，模型最容易把腰饰画到胸口。

---

## 五、题材原型库（用户说一句，直接套一件）

| 原型 | 主结构 | 层次 | 配色套路 | 标志物 |
|---|---|---|---|---|
| **帝王战装（男）** | 长袍 + 分片胸甲 + 大氅 | 3 层 | 白/金 7:2 + 朱红 1 | 龙纹刺绣、玉带、发冠 |
| **帝王轻装（女帝）** | 贴身战衣 + 局部甲片 + 纱帛 | 3 层 | 冰蓝/银白 6:3 + 金 1 | 头顶双层纯光环、腰链、腿环 |
| **法袍 / 道袍** | 交领长袍 + 广袖 + 披帛 | 3 层 | 青/白 7:2 + 金 1 | 云纹袖口、玉佩、拂尘 |
| **剑修劲装** | 修身短打 + 护臂 + 束腰 | 2 层 | 月白/墨 6:3 + 银 1 | 剑鞘、束发、护腕 |
| **魔尊重甲** | 板甲 + 骨饰 + 披风 | 3 层 | 墨黑/暗紫 7:2 + 血赤 1 | 骨角肩饰、锁链、逆立发 |
| **妖姬轻装** | 纱衣 + 鳞片贴体 + 长尾摆 | 2–3 层 | 紫/黑 6:3 + 荧光绿 1 | 面纹、臂钏、赤足或高跟 |
| **圣女 / 神女** | 层叠长裙 + 披帛 + 圣带 | 3 层 | 白/浅金 7:2 + 天青 1 | 光轮、额印、手持圣器 |
| **校园制服** | 水手服 / 西装制服 + 领结 + 百褶裙 | 2 层 | 藏青/白 8:2 + 红 1 | 领结、校徽、及膝袜 |

**用法**：原型只给"骨架"。**具体到款式词必须补**——`school uniform` 出来的永远是通用白衬衫；
`navy sailor uniform with red ribbon and pleated skirt` 才出学生气。

---

## 六、女性玄幻轻装：覆盖分区写法（问题 7 的核心）

题材惯例里，女帝 / 妖姬 / 剑仙 / 魔女本就是**局部甲片 + 薄纱 + 配饰链**的组合。
问题不是"能不能写"，是**没有分区模板，模型就自由发挥成裹身长袍或廉价堆砌**。

### 6.1 八区四态：逐区锁定覆盖方式

**每区只选一个状态**：`裸` / `半透` / `贴体` / `甲片覆盖`。

| 区 | 常见取值 | 写法示例 |
|---|---|---|
| **肩颈** | 裸 / 甲片 | `bare shoulders with a single carved pauldron on the left` |
| **锁骨与上胸** | 裸 / 半透 | `open neckline to the collarbone, sheer panel across the upper chest` |
| **腰腹** | 贴体 / 裸一段 / 甲片 | `fitted corset waist, a narrow band of exposed midriff above the hip` |
| **后背** | 裸 / 半透 / 甲片 | `open back with a single spine chain` |
| **上臂** | 裸 / 臂钏 / 纱袖 | `bare upper arms with a jade armlet on the right` |
| **小臂** | 甲片 / 纱袖 / 裸 | `faceted ice bracer from wrist to mid-forearm` |
| **腿** | 贴体 / 半透 / 裸 | `form-fitting leggings with a high front slit, sheer outer layer` |
| **足** | 靴 / 履 / 赤足 | `knee-high boots with gilt edge` |

**成品骨架（轻装女帝）**：

```
贴身战衣为主结构（覆盖躯干与腿），外覆局部冰晶甲片：
左肩一片弧形肩甲、右小臂一段棱面护臂、腰间一圈鳞片腰封。
上胸为半透冰纱，透出内层结构但不露肤；肩颈裸露，右臂上臂戴一枚青玉臂钏。
后腰一条半透明冰晶披帛，向右后方飘起；腿侧一条细链连到腿环。
```

### 6.2 四条分寸规则（题材内，不廉价）

| 规则 | 做法 | 反面 |
|---|---|---|
| **重点只放一处** | 露肩 + 露腰 + 露腿只选一至两处作为"重心" | 处处露 = 没有设计，只剩堆砌 |
| **露的地方要"有结构"** | 裸露区由甲片/纱/链"框住"（`framed by a plate edge`） | 单纯"没布" = 廉价 |
| **透 ≠ 露** | 要"看得出层次"用半透：`sheer layer, silhouette visible, no skin detail` | 写"透明可见皮肤"会走向低俗，且平台易拒 |
| **金属只做点睛** | 金/银只在边缘、扣件、链 | 大面积金属 + 大面积露肤 = 影楼风 |

### 6.3 平台差异（同一套衣服，三种写法）

| 平台 | 稳妥写法 | 注意 |
|---|---|---|
| **即梦 / Seedream / 豆包** | 中文结构句 + 部位分区（本文 §6.1 直接可用） | 中文对"半透/贴体/甲片覆盖"响应好；避免单写"性感/暴露" |
| **MJ / Flux** | 英文服装术语：`fitted bodysuit, sheer overlay, segmented plate armor, bare shoulders` | 少用 `sexy` 一类词，用**结构词**替代 |
| **SDXL / ComfyUI** | 标签 + 权重，服装词靠前 | 露肤词权重过高会崩解剖，靠负面 `bad anatomy` 兜底 |

### 6.4 轻装配套特效（与服装打包，别分开写）

| 特效 | 附着点 | 写法 |
|---|---|---|
| 薄纱透光与飘向 | 披帛/纱袖 | `the sheer layer catching cold light, drifting to the right` |
| 符文/光纹游走 | 甲片边缘、腰封 | `light threads travelling along the plate seams` |
| 甲片/宝石辉光 | 护臂、额饰 | `the gem glowing faintly, a thin rim of light on the plate edge` |
| 灵力粒子 | 周身，向上 | `sparse frost motes rising from her shoulders` |
| 发丝与衣袂 | 长发、衣摆 | `hair and hem lifting in the same updraft` |

**一条纪律**：**发亮只留两处**（甲片边缘 + 一处配饰）。全身发光 = 剪影消失 + 过曝。

### 6.5 轻装的反向（写进反向段）

```
裹身长袍、层层叠叠的厚裙、全覆盖兜帽与面纱、全身大面积金属、
廉价夜店风、亮片反光、明显低俗的姿势、皮肤质感过度真实、
部位粘连、布料穿模、多余的裸露、结构混乱的甲片
```

> **分寸判据**：**"每个裸露区都被一件结构物框住"**——有框就是设计，没框就是堆砌。

---

## 七、服装锚点段（问题 8：跨轮次不一致的根治）

外貌锚点管脸，**服装锚点管衣服**。两者同级，**跨图逐字复制**。

### 7.1 模板（照抄，填空）

```
【服装锚点｜逐字复制】
主结构：<款式名>，<闭合方式>，<长度>
分层：内层<材质+露出口> / 中层<甲或衣> / 外层<披挂+风向>
部件：<护肩>、<护臂>、<腰封>、<靴>（各写位置与材质）
配饰：<3 件以内，写位置>
配色：主色 <色名> <占比>% / 辅色 <色名> <占比>% / 点缀 <色名> <占比>%
动态件：<披风/纱袖/飘带>，<飘向>，<受什么力>
标志：<1–2 个高辨识特征，如"黑金腰封 + 冰蓝分片胸甲">
```

### 7.2 三条冻结纪律

1. **冻结范围**：跨场景、跨角度、跨风格时，**服装锚点段与外貌锚点段一字不动**，只改"本次变量段"。
2. **禁止同义替换**：把"哑光黑钢"改成"磨砂黑金属"，模型会当成另一套甲。**逐字复制，包括形容词。**
3. **被否款式进反向**：用户否掉的旧款（长袍/大裙摆）写进反向段，否则下一轮会长回来。

### 7.3 部件级反向词（比泛称有效）

```
上衣款式改变、外套消失或变长、护臂消失、肩甲换边、腰封变细、
披风变长或变短、纱袖变成实袖、裙长改变、配色换色、配饰移位、
主色面积改变、出现未指定的第二套服装
```

**别再只写 `changed outfit`**——泛称对模型几乎没有约束力，**要按部件点名**。

### 7.4 两种方向的变量隔离（别搞反）

| 图型 | 变什么 | 锁什么 | 必写句 |
|---|---|---|---|
| **普通多视图 / 跨场景** | 角度、场景、动作 | **服装 + 外貌全锁** | `同一套服装，所有格款式、配色、配饰完全一致` |
| **换装图** | 服装 | 姿态、角度、光、发型 | `除服装外全部相同：同一姿态、同一角度、同一光照` |

---

## 八、八个服装崩坏点

| 现象 | 根因 | 改法 |
|---|---|---|
| 堆成一块布 | 一次写"一套华丽古装" | 拆成内/中/外/配饰四层 |
| 甲片变生物鳞 | 同时写"鳞片"+"铠甲" | 只写"鱼鳞状甲片"+ 反向"生物鳞片" |
| 长袍裹身（想要轻装） | 没写覆盖分区 | 用八区四态逐区锁 |
| 廉价堆砌 | 露肤处没有结构框 | 每区加"甲片/纱/链"框边 |
| 服装每轮变 | 服装段被重写 | 服装锚点段逐字复制 |
| 披风穿模 | 没写风向与垂坠 | `wind from the left, cloak spreading sideways-back` |
| 细节被布料吃掉 | 刺绣/镂空写太满 | 全身只留一处精细（袖口或前襟） |
| 三色变五色 | 配饰各自带色 | 配饰统一到点缀色 |

---

## 九、自检（九项）

- [ ] 按层写了（内/中/外/配饰），不是"一套"
- [ ] 甲胄走了三层递进（甲种/走向/部件）
- [ ] 材质一主一对比一点缀
- [ ] 八区都交代了覆盖方式（尤其轻装）
- [ ] 露肤区都被结构框住
- [ ] 发亮只两处
- [ ] 服装锚点段可逐字复制
- [ ] 动态件写了风向与受什么力
- [ ] 三色面积比写清了

---

## 十、与其他文件的关系

| 要写什么 | 读哪份 |
|---|---|
| 搭配、三色、精简上限、交付图版式 | `outfit-design.md` |
| 部位与体态（衣服下面的身体） | `body-parts.md` |
| 服饰特效（长在衣服上的光） | `vfx.md` §2.6 |
| 玄幻零件与光环位置 | `fantasy-elements.md` |
| 跨图一致性总则 | `text-only-consistency.md` + `consistency-workflow.md` |
| 场景与服装的材质呼应 | `scene-space.md` |

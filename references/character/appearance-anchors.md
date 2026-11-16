# 外貌锚点库

一致性的地基。AI 没有记忆，**描述颗粒度越细，留给模型自由发挥（瞎编）的空间越小，角色就越稳**。本文件提供锚点构建方法、可量化词表、锚点表模板。

---

## 一、锚点构建三原则

### 原则 1：三个不变特征

每个角色锁定 **3 个高识别度特征**，写进每一组提示词的**首位**，任何图都不改。好的锚点应是"扫一眼就认得出"的：

- 圆脸 + 杏仁眼 + 左眼下泪痣
- 高颧骨 + 鹰钩鼻 + 右眉骨旧疤
- 祖母绿瞳 + 鼻梁淡雀斑 + 自然微卷金棕发

### 原则 2：避开 AI 模糊词

审美形容词（beautiful / handsome / 美女 / 帅气）是几亿张训练图共有的描述，出 10 次得 10 个不同的人。**换成骨相与结构描述**：

| 禁用（模糊） | 替换（骨相） |
|---|---|
| beautiful / handsome | high cheekbones, sharp jawline, button nose |
| 大眼睛 | almond-shaped eyes, double eyelids, eye-to-face ratio 1:5 |
| 瘦 | slim build, narrow shoulders, long neck |
| 年轻 | smooth skin, round cheeks, youthful proportions (7-head-tall) |

### 原则 3：比例量化

用可量化的词锁五官与身体比例，AI 理解更准：

```
eye-to-face ratio 1:5, slim build, shoulder width medium,
7.5-head-tall proportions, leg-to-body ratio 1:1
```

---

## 二、五官锚点词表

### 脸型 face shape

| 中文 | 英文锚点 |
|---|---|
| 鹅蛋脸 | oval face |
| 圆脸 | round face |
| 瓜子脸 | heart-shaped face, pointed chin |
| 方脸 | square face, strong jawline |
| 长脸 | oblong face |
| 菱形脸 | diamond face, high cheekbones |
| 婴儿肥 | chubby cheeks, baby fat |

### 眼睛 eye shape

| 中文 | 英文锚点 |
|---|---|
| 杏眼 | almond-shaped eyes |
| 丹凤眼 | phoenix eyes, upturned corners (tsurime) |
| 下垂眼 | droopy eyes (tareme) |
| 桃花眼 | peach blossom eyes, smiling eyes |
| 单眼皮 | monolid eyes, single eyelid |
| 双眼皮 | double eyelids |
| 内双 | double eyelids, inner fold |
| 眯眼 | narrowed eyes |
| 圆眼 | round eyes, wide eyes |

### 瞳色 iris color

`amber eyes` · `golden pupils` · `emerald eyes` · `sapphire blue eyes` · `crimson red eyes` · `violet eyes` · `heterochromia`(异色瞳) · `starry eyes`(星瞳) · `glowing eyes`(发光瞳)

### 眉毛 eyebrow

`thick eyebrows`(浓眉) · `thin eyebrows`(细眉) · `arched brows`(挑眉) · `straight brows`(一字眉) · `slanted brows`(八字眉)

### 鼻型 nose

`button nose`(小巧鼻) · `high nose bridge`(高鼻梁) · `aquiline nose`(鹰钩鼻) · `snub nose`(翘鼻) · `straight nose`(挺直鼻)

### 嘴型 mouth

`full lips`(厚唇) · `thin lips`(薄唇) · `cupid's bow lips`(丘比特弓唇) · `small mouth`(小嘴) · `slightly parted lips`(微张唇)

### 特殊标记 distinguishing marks

`mole under left eye`(左眼下泪痣) · `freckles on nose bridge`(鼻梁雀斑) · `scar on right cheek`(右脸疤) · `beauty mark`(美人痣) · `birthmark`(胎记) · `blush`(腮红)

---

## 三、发型发色锚点词表

### 长度 length

`short hair`(短发) · `medium hair`(中发) · `long hair`(长发) · `very long hair`(及腰长发) · `waist-length hair`

### 发型 style

`straight hair`(直发) · `wavy hair`(波浪) · `curly hair`(卷发) · `twin tails`(双马尾) · `ponytail`(马尾) · `braid`(编发) · `bun`(丸子头) · `bob cut`(波波头) · `ahoge`(呆毛) · `side-swept bangs`(斜刘海) · `blunt bangs`(齐刘海) · `undercut`(剃边) · `messy hair`(凌乱)

### 发色 color

`black hair` · `jet black`(乌黑) · `silver hair`(银发) · `ash gray`(灰发) · `platinum blonde`(铂金) · `golden blonde`(金) · `chestnut brown`(栗棕) · `auburn`(赤褐) · `crimson hair`(绯红) · `pink hair` · `lavender hair`(薰衣草紫) · `gradient hair`(渐变) · `two-tone hair`(双色) · `multicolored hair`

---

## 四、身形比例锚点词表

**头身比（X-head-tall）是风格的开关，也是锚点的一部分**：写实 7.5–8 头、2D动画 6.5–7.5 头、3D卡通 5.5–6.5 头、Q版 2.5–4 头。**同一角色跨风格时允许改头身比，但三不变特征必须保住。**（各风格对应头身比详见 `render-styles.md`）

| 中文 | 英文锚点 |
|---|---|
| 纤细 | slim, slender, delicate build |
| 健美 | athletic, toned build |
| 健硕 | muscular, broad shoulders |
| 娇小 | petite, short stature |
| 高挑 | tall, long legs |
| 微胖 | curvy, plus-size |
| 头身比 | 7.5-head-tall（写实）/ 6-head-tall（3D卡通）/ 3.5-head-tall（Q版） |

身高用具体数字更稳：`168cm tall`、`approximately 5'7"`。

---

## 五、外貌锚点表模板

每次生成角色时先填这张表，之后**逐字复制**进每条提示词。

```markdown
## 角色锚点表 — <角色名>

| 项目 | 固定值（英文锚点） | 中文 |
|---|---|---|
| 性别年龄 | 18-year-old female | 18岁女性 |
| 脸型 | round face, oval jawline | 圆脸 |
| 眼睛 | almond-shaped amber eyes, double eyelids | 杏眼琥珀瞳，双眼皮 |
| 眉毛 | straight thin brows | 一字细眉 |
| 鼻/嘴 | button nose, full lips | 小巧鼻，厚唇 |
| 标记 | mole under left eye | 左眼下泪痣 |
| 发型发色 | silver waist-length straight hair, blunt bangs | 银灰及腰直发，齐刘海 |
| 身形 | slim build, 168cm, 7.5-head-tall | 纤细，168cm |
| 服装套装 | navy techwear cropped jacket, black high-waist shorts, chunky boots | 深蓝机能短外套+黑高腰短裤+厚底靴 |
| 识别物 | single silver ear cuff | 单只银耳夹 |

> 三不变特征：**round face + almond amber eyes + mole under left eye**
```

---

## 六、锚点使用铁律

1. **锚点块逐字复制**：换场景、换角度、换动作、换风格时，锚点段落一字不改（这是纯文字一致性的核心）。
2. **只改一个变量**：每次迭代只改一个维度（如只改外套长度），其余保持不动，否则无法判断哪项修正有效。
3. **颜色锚定到位置**：把"头发/眼睛/上衣/裤子/鞋子"分别锁定颜色，防止漂移。
4. **服装用部件+层次+闭合方式描述**：别写"漂亮裙子"，写"及膝百褶裙、腰部皮质束带、前开扣"。
5. **配饰做减法**：只保留 1-3 个高识别度锚点，小饰品越多越容易消失或错位。
6. **一张全身图先定妆**：先出一张满意的全身定妆图，**看图回读、把细节补进锚点表并冻结**，之后所有图都用这一版文字描述（不依赖参考图）。
7. **不依赖参考图**：全程纯文字锚点即可锁人；参考图仅作为可选增强（详见 `text-only-consistency.md`）。

# 表情与差分规格

表情是人物的灵魂。**笼统的情绪词（angry / happy）出图飘忽，必须把情绪拆解成肉眼可见的面部动作**。

> **两种用途，写法不同：**
> - **表情差分 / 表情包**（给人看）→ 本文件。
> - **资产图里的表情页**（给动画/绑定用，2×4 八格、头骨体积锁死、中性表情优先）→ `character-asset-sheet.md` P4。
> 口型图见 `character-asset-sheet.md` P11。

---

## 一、三层叠加微表情法

每条表情提示词由三层构成：

```
第一层：面部动作（嘴/眉/眼的肌肉动作）
第二层：情绪词（辅助理解）
第三层：眼神方向与情感
```

示例：`slightly parted lips, sad smile, eyes looking down with unshed tears`

### 禁用 vs 替换

| 禁用（笼统） | 替换（肉眼动作） |
|---|---|
| angry | flared nostrils, furrowed brows, clenched jaw |
| surprised | raised eyebrows, widened eyes, slightly open mouth |
| sad | trembling lips, reddened eyes, downcast gaze |
| happy | crinkled eye corners, raised mouth corners, bright eyes |
| disgusted | wrinkled nose, curled upper lip, squinted eyes |
| scared | wide eyes, pale face, slightly open trembling mouth |

### 眼神方向（决定画面张力）

| 中文 | 英文 |
|---|---|
| 与观众对视 | `eye contact with viewer, looking at viewer` |
| 失焦远望 | `looking into the distance with empty eyes` |
| 斜眼冷笑 | `side glance with a smirk` |
| 回眸 | `looking back over shoulder` |
| 垂眸 | `looking down, downcast eyes` |
| 仰视 | `looking up` |

提示词公式：`[嘴部动作] + [眉部动作] + [眼神方向与情感] + [微动作配合]`

**一句话记住**：别写"哭"，写"眼眶泛红嘴唇紧抿"。

---

## 二、五表情差分（标准表情组）

横向 5 格，同一角色、同一角度、同一光照，只有表情变化。

```
角色表情差分设定图，expression sheet，同一角色同一角度横向五格：
① 喜 happy — crinkled eye corners, raised mouth corners, bright eyes, looking at viewer
② 怒 angry — furrowed brows, flared nostrils, clenched jaw, glaring forward
③ 哀 sad — trembling lips, reddened eyes, downcast gaze, slight frown
④ 乐 laughing — closed eyes in crescent, wide open mouth laughing, head slightly tilted back
⑤ 惊 surprised — raised eyebrows, widened eyes, slightly open mouth, leaning back slightly
【外貌锚点：<逐字复制锚点表>】
【服装：<逐字复制>】
构图：五格胸部以上半身，面部大小一致、对齐同一水平线，格间细灰分隔线。
背景：纯白背景，无阴影投地。
画风：<与前序图完全一致>
光照：左上45度均匀柔光，五格完全一致。
画质：8K，面部细节锐利，表情差异清晰可辨。
```

---

## 三、表情包规格（九宫格 / 十二宫格）

适合做贴纸、聊天包。通常是**胸部以上 + 夸张表情**。

```
角色表情贴纸包，emoji sticker pack, 3×3 九宫格，同一角色九种夸张表情：
第一行：大笑、得意、嫌弃、害羞
第二行：生气、哭泣、震惊、无语
第三行：花痴、疲惫、坏笑、疑惑
【外貌锚点：<逐字复制>】
每格表情夸张、卡通化放大，角色辨识度保持一致。
背景：每格透明或纯色块，粗白描边，贴纸风格。
画风：<与前序图一致>，粗描边，鲜明配色。
画质：每格独立完整，网格对齐，1080×1080。
```

---

## 四、表情与一致性（纯文字）

- **锚点不能丢**：表情再夸张，三不变特征（脸型/眼型/标记）必须保留——把锚点块逐字复制在提示词首位。
- **只改表情段**：差分时只替换「表情层」，锚点块、服装、风格块、光照段落一字不动。
- **同一角度**：表情差分必须固定同一角度（多为正面或 3/4），否则无法比对。
- **固定种子**：支持的平台固定 seed，只换表情词，脸完全不漂。
- **生成策略**：一次出九宫格容易塌；追求质量时逐格生成（只换表情词），后期拼版。
- **不依赖参考图**：靠"锚点块 + 识别串 + 固定种子"即可让表情差分是同一张脸，无需喂图。

---

## 五、情绪强度词（辅助层）

`subtle` / `slightly` / `intense` / `extreme` / `restrained` / `exaggerated`

例：`slightly raised eyebrows`（微挑眉） vs `dramatically raised eyebrows`（夸张挑眉）。

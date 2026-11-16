# 从一句话到 3D 资产：text→3D 提示词

> 与 `modeling-handoff.md` 的分工，先分清：
>
> - **`modeling-handoff.md`** = 出一张**给建模师看的图**（正交三视图、A-Pose、地标线），人拿去照着建。
> - **本文件** = 写一段**直接喂给 3D 生成器的指令**（Meshy / Tripo / Hunyuan3D / Rodin），机器直接吐网格。
>
> 两者的评价标准完全不同：前者看"图够不够准"，后者看"**网格能不能用**"。

---

## 零、先判走哪条路

| 目标 | 路线 | 理由 |
|---|---|---|
| 只想看立体效果 / 快速试造型 | **text → 3D** | 一分钟出一个，代价是细节不可控 |
| 要还原某个具体角色 | **先出图 → image → 3D（多视图端点）** | 背面和侧面来自真实输入，不是编的 |
| 要绑骨做动画 | **先出 A-Pose 图 → 多视图 → image → 3D → 自动绑骨** | 姿态错了绑骨直接失败 |
| 要成品进引擎 | 任何 AI 输出**都必须重拓扑** | 见 §七 |

**核心判断：text→3D 的提示词不是"描述"，是"技术简报"。**

生图提示词可以写"唯美、氛围感强"；3D 提示词写这些等于没写。**少一个字段，生成器就自己填，而且填得比你想的保守——结果不可比、不可修。**

---

## 一、六层结构（照填，别跳）

```
① 对象：是什么 + 几个（单件，不要"一组"）
② 用途：game asset / product / AR preview / 3D print / concept asset
③ 几何：剪影 + 比例 + 关键部件 + 面数意图
④ 材质：一个部件一个材质族（此层最忌混）
⑤ 纹理：粗糙度 / 颜色 / 磨损 / 图案
⑥ 约束：不要什么（负向在 3D 里比生图更有效）
```

**填法示例（角色）**：

```
① 风格化人形机械师，单个角色
② game asset，要进 Unity 做主角
③ 紧凑体型，宽肩窄腰，大工具腰包形成右侧剪影凸起；四肢为独立管状件
④ 帆布（外套）、哑光烤漆金属（护腕）、皮革（腰包）
⑤ 帆布有轻微磨白，金属边缘露底漆，不做印花
⑥ 无场景、无底座、无漂浮件、无细长发丝、无文字
```

---

## 二、角色要能绑骨的五条件（硬要求，不是建议）

自动绑骨是 text→3D 最容易崩的一步。**下面五条写不全，绑骨一定失败或形变极差。**

| # | 条件 | 提示词要写什么 | 不写的后果 |
|---|---|---|---|
| 1 | **A-Pose** | `A-pose, both arms straight, angled about 55° down and out from the shoulders` | 手臂贴身 → 找不到肩关节 → 直接报错 |
| 2 | **四肢分离** | `a clear band of plain background visible between each arm and the torso along its whole length` | 手臂与躯干融合 → 网格粘连 → 拆不开 |
| 3 | **双腿留缝** | `visible gap between the legs` | 双腿熔成一片 → 无法分权重 |
| 4 | **关节不被遮挡** | `no long coat, no cape, no long skirt, no large accessories covering elbows, knees or hips` | 披风盖住关节 → 绑骨只能猜 |
| 5 | **单层服装 + 少配饰** | `simple single-layer clothing, minimal accessories` | 多层叠穿 → 生成成一整块布 |

> **为什么是 55° 而不是 30°**：手臂短的角色（Q 版、机械臂）在 30° 时，臂与躯干的间隙只有几个像素，自动绑骨识别不到。角度要按"能看见一条完整背景带"来定，不是照着 A-Pose 教科书抄。

### 明确避开的三类角色

| 类型 | 为什么是失败区 |
|---|---|
| **chibi / 超变形** | 头占身高 2/5、四肢粗短、连指手套手、几乎无颈——四肢与躯干像素级粘连，姿态估计直接 422 |
| **长发遮身** | 长发盖住肩与胸 → 躯干边界不可见 |
| **大裙摆 / 长披风** | 下半身完全被概括，腿部结构与步幅全部丢失 |

**这三类不是不能做，是要先改成"能绑的版本"再生成，绑完再加回装饰。**

---

## 三、几何：写形状，不写风格

Tripo 官方那句最有用：**描述形状与材质，而不只是风格。**

| 不要写 | 改写 |
|---|---|
| 一个奇幻宝箱 | 一个风格化奇幻宝箱，厚重比例，金属护角，雕刻木板，发光的蓝色宝石锁 |
| 未来感武器 | 短管能量步枪，枪身分三段，握把倾斜 15°，枪口有一个环形散热片 |
| 可爱小机器人 | 圆头 + 倒角方箱身体，头身比 1:2，两条短圆柱腿，一只手是夹具 |

**"风格词"只决定表皮，"形状词"决定网格。**

---

## 四、面数与拓扑口径

| 项 | 口径 | 说明 |
|---|---|---|
| **面数上限** | 300k 三角面 | Meshy 绑骨的硬上限，超了它自己报错 |
| **拓扑类型** | 先 **triangle** | 写 quad 会有一处歧义：300k 若按 quad 计，实际是 60 万三角面，一次生成白费 |
| **目标面数** | 手游 5k–15k｜桌面 30k–80k｜影视 150k+ | 按用途定，别一律求高 |
| **重网格时机** | **绑骨之前** | 权重是按顶点存的，绑完再减面等于白干 |
| **贴图分辨率** | basecolor 给到 4k | 它是唯一能撑过绑定的贴图，承载几乎全部观感 |
| **PBR** | 值得要 | 评审阶段看的是绑定前的资产，PBR 更接近最终观感 |

**一句话**：先 clean，再 remesh，最后 rig。顺序错了就是重做。

---

## 五、负向（3D 专用，和生图不是一套）

3D 生成器的负向比生图**更有效**——它的失败模式非常固定。

```
no background, no base plate, no text, no logo,
no extra limbs, no fused limbs, no floating parts,
no transparent material, no thin sheets, no tiny wires,
no long hair strands, no dense ornament, no motion
```

中文：

```
无场景、无底座、无文字、无 logo；无多余肢体、无融合肢体、无悬空部件；
无透明材质、无薄片结构、无细线结构；无长发单丝、无密集装饰、无动态姿态。
```

**最该加的三条**：`no floating parts`（悬空件导出即碎）、`no thin sheets`（薄片打印/绑定双杀）、`no fused limbs`（融合肢体 = 整个资产报废）。

---

## 六、六类失败与改法

| 现象 | 根因 | 改法 |
|---|---|---|
| **肢体融合**（手臂长进躯干） | 没要求四肢分离 | 加"臂与躯干之间有完整背景带"，重生成（重生成比重修便宜） |
| **薄片结构**（衣角、翅膀、披风） | 生成器把"薄"理解成"零厚度面" | 写 `solid volume, minimum thickness 2mm`，或干脆去掉 |
| **悬空件** | 配饰与大形分离 | 让配饰必须接触身体（`touching the shoulder, not floating`） |
| **正面密、背面空** | 单图输入的必然结果 | 走 multi-image 端点，喂正/侧/背三张 |
| **文字 / logo 乱码** | 生成器默认给物体加标识 | 负向写死 `no text, no logo` |
| **过度装饰** | 提示词里形容词太多 | 删掉一半形容词，加 `minimal details, large simple forms` |

---

## 七、三个平台的差别（2026 现状）

| 平台 | 关键机制 | 提示词注意 |
|---|---|---|
| **Meshy** | 有独立 Pose 选项（A/T）；multi-image 端点里**第一张图 = 正面**；auto-rig 有 300k 上限 | 图序不能乱；pose 用面板选，提示词里再写一遍做双保险 |
| **Tripo** | 姿态要在 **prompt 里自己写**；绑骨指南要求单层衣 + 少配饰 | 提示词必须含 A-pose、separated limbs、simple clothing |
| **Hunyuan3D / Rodin** | 吃长结构化简报，工程语响应好 | 六层结构照填，越具体越稳 |

**平台选择**：要"快出体积看造型"→ 任意；要"能绑骨"→ Meshy（有 pose 选项）或多视图 + Tripo；要"背面也真"→ 必须 multi-image，不要单图。

---

## 八、模板（整段可抄）

### ① 可绑骨的角色

```
A stylized humanoid mechanic, single character, stylized game-ready 3D asset for Unity.
Compact build, broad shoulders, narrow waist, oversized tool pouch creating a silhouette
break on the right hip; all four limbs are separate tubular forms.
A-pose: both arms straight, angled about 55 degrees down and out from the shoulders,
a clear band of plain background visible between each arm and the torso along its whole length,
visible gap between the legs.
Simple single-layer clothing: canvas jacket, matte painted metal bracers, leather pouch.
No long coat, no cape, no long skirt, no accessory covering the elbows, knees or hips.
Canvas with light wear, metal with edge chipping, no printed pattern.
Clean geometry, readable silhouette, balanced proportions, solid volume, minimum thickness 2mm.
No background, no base plate, no text, no logo, no floating parts, no fused limbs,
no thin sheets, no long hair strands, no motion.
```

### ② 只看造型的道具

```
A stylized low-poly fantasy treasure chest, single prop, game asset.
Heavy squat proportions, metal corner guards, carved wooden planks, a single blue gem lock.
Matte painted metal and aged wood, muted teal and warm brown with one cyan accent.
Broad planar faces, minimal small parts, readable from medium distance, centered pivot.
No background, no text, no logo, no thin sheets, no floating fragments, no ornament clutter.
```

---

## 九、交付话术（三句，别省）

生成完必须说清三件事，否则下游会误判：

1. **"这是概念网格，不是资产。"** AI 网格拓扑不可用，必须重拓扑。
2. **"面数与 UV 需要重做。"** AI 给的是形状，不是可上线的网格。
3. **"尺寸按 1 unit = 1 m 校对过。"** AI 输出常常没有真实尺度，进引擎前必须先校。

> 同一条原则见 `modeling-handoff.md` §十：**AI 做不到的七件事**。

---

## 十、自检

- [ ] 六层都填了（对象/用途/几何/材质/纹理/约束），没有只写风格
- [ ] 要绑骨的话，五条件全在（A-Pose 55° / 四肢分离 / 双腿留缝 / 关节不遮 / 单层衣）
- [ ] 写的是形状与部件，不是形容词
- [ ] 面数意图与用途匹配，拓扑写 triangle
- [ ] 负向含 `no floating parts / no thin sheets / no fused limbs`
- [ ] 已说明"AI 网格需重拓扑"，没承诺可直接上线
- [ ] 尺度可换算（1 unit = 1 m）

---

## 十一、和其他文件的关系

| 要写什么 | 读哪份 |
|---|---|
| 出一张给建模师看的正交三视图 | `modeling-handoff.md` |
| 低模的面数分配 | `low-poly.md` |
| 3D 动漫走哪条渲染路线 | `anime-3d.md` |
| 资产图型（34 种里 B 族） | `image-types.md` |
| 材质数值怎么写 | `modeling-handoff.md` §八 |

# 玄幻 / 战斗题材元素包

> 前面 24 份参考解决"人画得对不对"，这一份解决"**这个世界成不成立**"。
> 玄幻/仙侠/战斗题材的失败很少是脸的问题，是**世界缺件**：没有法相、没有光轮、没有法阵、没有灵气粒子，
> 只剩一个穿古装的人站在云里——那就是"通用游戏 CG"，不是玄幻。
>
> **一句话：玄幻味不是形容词堆出来的，是把"世界里的六类零件"写全。**

---

## 一、六类零件（缺两类就不像玄幻）

| 类 | 作用 | 缺了会怎样 |
|---|---|---|
| **① 法相 / 虚影** | 给"力量层级"一个可见的体量 | 人物再华丽也像普通人 |
| **② 光轮 / 背光** | 给"神圣/帝王"一个身份标识 | 皇帝和杂兵只差衣服 |
| **③ 法阵 / 地纹** | 把"施法"落到地面，接住人物 | 人像贴在背景上 |
| **④ 法器 / 武器** | 身份 + 动作的支点 | 手不知道在干什么 |
| **⑤ 灵气 / 粒子** | 让空气"有能量" | 空气是空的，像影楼 |
| **⑥ 天象 / 环境威压** | 给场面一个"事件" | 只有背景，没有"正在发生的事" |

**配置原则**：**一主两辅**。六类全上 = 视觉噪音；只上①+⑤ = 最常见也最稳的帝王/仙尊配置。

---

## 二、① 法相 / 虚影（体量与层级）

**法相不是"另一个人"**，是同一个角色的放大虚影。写错这三件，模型会画成"两个人在打架"。

| 必写 | 写法 | 不写的后果 |
|---|---|---|
| **同源** | `a colossal translucent projection of the same figure` | 出成另一个人 / 换了性别 |
| **倍数** | `roughly 20 times the character's height` | 尺度随机，可能比人小 |
| **半透明** | `semi-transparent, you can see the sky through it` | 出实体会挡住主体 |
| **姿态差** | `the projection raises one hand while the figure stands still` | 两个动作一样，读不出"召唤" |

**成品句**：

```
人物身后升起一具同源的半透明法相，约人物身高的 20 倍，
半透明到能透出后方云层；法相双臂环抱结印，人物本体静立不动。
```

```
a colossal semi-transparent dharma projection of the same figure rising behind her,
about 20 times her height, the sky visible through it,
the projection forming a seal with both hands while her body stays still
```

**三种法相变体**（按题材选一种，别混）：

| 变体 | 写法 | 适合 |
|---|---|---|
| 神女/仙尊 | `graceful female deity projection, flowing robes, lotus seat` | 仙侠、圣女 |
| 雷神/战神 | `armored war-deity projection, radiating energy lines` | 战斗、雷系 |
| 巨兽/兽形 | `beast-shaped projection with horns and layered scales` | 妖族、兽潮 |

---

## 三、② 光轮 / 背光（最容易被写错的一件）

**审计里真实踩过的坑：把"头顶光环"写成"身后轮盘"。** 这是两个完全不同的东西：

| 类型 | 位置 | 形态 | 写法 |
|---|---|---|---|
| **头顶光环** | 悬在头顶正上方，与人头 **不接触** | 细圆环，通常双层同心 | `a thin double-ring halo floating directly above the head, not touching it` |
| **背后光轮 / 法轮** | 在**身后**，与肩齐高或更高，正面可见其边缘 | 带辐条/纹饰的大圆盘 | `a large ornate wheel of light behind the shoulders, spokes radiating outward` |
| **背光 / 神光** | 贴着头/肩的柔光晕 | 无边界，渐变 | `soft radiant backlight blooming behind the head and shoulders` |
| **地轮 / 法阵** | 脚下地面 | 平铺圆形纹样 | `a circular spell array inscribed on the ground beneath the feet` |

**四条硬约束**：

1. **写位置 + 写"是否接触"**：`floating above the head, not touching` / `behind the shoulders, edge visible from the front`。
2. **写"是否实心"**：光环是"光"，不是金属环——`made of light, edges glowing, no physical rim`。想写金属环就说 `ornate metal ring`，别含糊。
3. **写"几层"**：`double-ring` / `three concentric rings`。不写就随机 1–3 层。
4. **写"纹饰有无"**：`plain, unadorned` / `engraved with cloud patterns`。**这一条决定"纯光环"还是"带纹轮盘"——用户否过一次就一定要写进正向词。**

**成品句**：

```
头顶正上方悬一枚双层纯光环，由光构成、边缘发亮、无金属实体，
环上无任何纹饰；光环与人头之间留出空隙，不接触。
背后不出现任何轮盘或法阵。
```

---

## 四、③ 法阵 / 地纹（把人物"接"到地上）

| 层 | 写法 | 作用 |
|---|---|---|
| 边缘 | `a circular array with a ring of runes at its rim` | 定大小与"人工感" |
| 内部 | `interlocking geometric lines, a triangle inside the circle` | 定风格（几何/符文/星象） |
| 状态 | `faintly glowing, edges still smoldering` / `fully ignited` | 定"刚施法"还是"正在施法" |
| 残光 | `残留余光未散，脚下石面被烤出裂纹` | **这一条最出效果**：让"事情刚发生" |

> **只写"脚下有法阵"= 得到一个贴图圆环。** 必须给"状态 + 残光"，它才有时间感。

---

## 五、④ 法器 / 武器（锁定项最高频的所在地）

审计里"权杖被否改回长枪"这种事，根因是**没有把武器写成结构清单**。

| 项 | 必写 | 例 |
|---|---|---|
| 形制 | 具体器物名 + 长度 | `a nine-foot spear` / `a folding fan` / `a double-headed staff` |
| 分件 | 2–4 个可指认部件 | `shaft, spearhead, cross guard, tassel` |
| 与手的接触 | 握在哪、哪只手、朝哪 | `gripped in the right hand at mid-shaft, tip angled down-right` |
| 材质与光 | 主材 + 发光位置 | `black iron shaft, silver blade, runes glowing at the base of the blade` |
| **不许变成什么** | 显式反向 | `it is a spear, not a staff, not a scepter, not a sword` |

**最后一行是审计的直接产物**：用户在视频提示词里写的就是「折扇必须清楚，是白色扇面、金色扇骨，不要变成剑」。
**把"不要变成 X"写进正向句尾**，比只放反向框有效——中文平台尤其如此。

---

## 六、⑤ 灵气 / 粒子（玄幻专用词表）

通用粒子词（火星/余烬/花瓣）在玄幻里不够，因为它们不带"能量"。

| 类型 | 中文 | 英文 | 关键参数 |
|---|---|---|---|
| 灵力光尘 | 灵力光尘、灵气碎片、灵光碎屑 | `spirit motes, drifting qi fragments` | 稀疏 + 大小不一 |
| 冰系 | 冰晶尘、冰屑、寒气结晶 | `frost motes, ice shards drifting` | 粒径小、向上/向外 |
| 雷系 | 电弧碎芒、雷痕拖影 | `arc fragments, lightning afterglow trailing` | 方向贴本体 |
| 火系 | 火屑、赤金余烬、星火 | `ember flecks, cinder sparks` | 向下飘落 |
| 暗系 | 魂火、黑雾粒、暗紫碎光 | `soul flames, dark violet particles` | 低亮度、贴地 |
| 金系 | 金色符纸、经文碎片 | `golden talisman papers, floating scripture fragments` | 有形状（纸片），不是光点 |
| 神圣 | 金色羽粒、光羽 | `golden feather motes` | 缓慢上浮 |

**两条玄幻专属纪律**：

1. **只留一种**。冰系 + 雷系 + 金色羽粒同时出现 → 变迪厅。一层主粒子 + 一层光效即可。
2. **粒子要跟"属性"一致**：冰系向上飘、火系向下落、雷系贴体拖、暗系贴地爬。**方向错了，属性就错了。**

---

## 七、⑥ 天象 / 环境威压（给"事件"）

| 事件 | 写法 | 光怎么配合 |
|---|---|---|
| **天劫压境** | `a spiraling thundercloud vortex directly overhead, the eye of the storm above her` | 云层内部放电，冷紫主光 |
| **万兽朝宗** | `a ring of beast silhouettes at every ridge, heads lowered` | 逆光剪影，不照亮细节 |
| **宗门殿宇** | `a vast temple hall receding into haze, columns marching into fog` | 纵深方向的光轴 |
| **古战场** | `a battlefield of broken banners and half-buried armor` | 低角度侧光，长影 |
| **秘境水潭** | `a still black pool reflecting a sky that is not the sky above` | 水面反射是主光来源 |
| **冰原深渊** | `a crevasse glowing faintly from below, frost columns rising` | 底光 + 上方冷光对冲 |

> **威压靠"尺度差"**：写清"人物的高度占画面 1/6，云层占 2/3"。不写尺度，天劫会变成一朵云。

---

## 八、中文专名 → 结构槽位（这块最容易翻车）

中文玄幻专名模型未必认得，**但结构词一定认得**。规则：**专名可留作氛围，结构必须另写一句。**

| 专名 | 模型可能画成 | 必须补的结构句 |
|---|---|---|
| 帝环 | 轮盘 / 金属齿轮 / 王冠 | `a plain double halo of light above the head, no spokes, no rim` |
| 法相 | 另一个人 / 巨大雕像 / 分身 | `semi-transparent projection of the same figure, 20x height` |
| 斗气 | 烟雾 / 火焰 / 光柱 | `thin energy vapor rising from the shoulders, faint colored edge` |
| 灵兽环绕 | 一群动物 / 宠物 | `three beast silhouettes circling at shoulder height, semi-transparent` |
| 分片鳞甲 | 生物鳞片长在身上 | `overlapping armor plates in fish-scale pattern, matte metal, segment lines visible` |
| 鎏金包边 | 全身金色 | `thin gold trim only along the plate edges` |
| 冰晶披风 | 透明塑料布 | `semi-transparent ice-crystal mantle, faceted planes, cold blue refraction` |
| 符文织锦 | 乱码文字 | `abstract glowing rune pattern, non-readable, woven into the fabric` |
| 罡气护体 | 泡泡 / 玻璃罩 | `a thin refractive energy shell hugging the body, edge only` |
| 九条冰龙 | 一条龙 / 九个头 | `exactly nine separate ice dragons, each a distinct silhouette, circling` |

**两条铁律**：

1. **可数实体必须写"恰好 N 个"**：`exactly nine`，并加 `no extra dragons`。模型对"九"极不稳定。
2. **符文/经文一律写"不可读"**：`non-readable abstract runes`。让模型写具体字符必崩（见 `06-text-in-image.md`）。

---

## 九、方位槽位（审计里"轮盘 vs 光环"混淆的根治）

**方位不是形容词，是一个坐标系。** 每个元素都要回答：**在哪、多高、朝哪、是否接触、谁在前。**

| 槽位 | 取值 | 例 |
|---|---|---|
| **相对人物** | 头顶正上 / 身后 / 肩侧 / 腰侧 / 脚下 / 身前 | `directly above the head` |
| **相对相机** | 在人物与相机之间 / 被人挡住 / 在人物背后可见 | `visible behind the shoulders from the front` |
| **高度** | 高于头顶 N 个头 / 与肩齐 / 与腰齐 / 贴地 | `one head-height above the head` |
| **接触** | 接触 / 悬空 / 穿身 | `floating, not touching` |
| **遮挡关系** | 不遮挡面部 / 不遮挡剪影 / 允许压住肩线 | `must not cover the face` |

**四类高频元素的方位规格**：

| 元素 | 标准方位写法 |
|---|---|
| 头顶光环 | `floating directly above the head, one head-height up, not touching` |
| 背后光轮 | `behind the shoulders, centered on the spine, edges visible from the front` |
| 环绕灵兽/龙 | `circling at shoulder height, in front of and behind the body alternately` |
| 法阵 | `on the ground beneath the feet, centered on the standing point` |
| 法相 | `rising behind and above the figure, its head above the frame or near the top edge` |
| 武器 | `in the right hand, gripped at mid-shaft, tip angled down and to the right` |

**一条反向兜底**（写进反向段）：

```
身后无轮盘、头顶无金属环、光环不带辐条、法相不遮挡人物面部
```

---

## 十、强度分档：restrained / epic（特效层数的两套阈值）

`vfx.md` 的"一层主 + 一层辅"是**克制档**，适合立绘与写真。**战斗 KV 需要另一套。**

| 档 | 适用 | 允许层数 | 关键约束 |
|---|---|---|---|
| **restrained（克制）** | 立绘、头像、写真、日常 | 主 1 + 辅 1 | 粒子一种；介质 ≤1 |
| **epic（史诗）** | 战斗 KV、CG 预告、封面 | 主 1 + 辅 2 + 环境 1 | 必须写"分层 + 遮挡 + 主光唯一" |

**epic 档的三条附加纪律**（不写这三条，多层必糊）：

1. **分层要报数**：`三层：主特效（雷）在人物与相机之间；辅特效（碎屑）在脚下；环境（云涡）在最远层`。
2. **主光仍只有一个**：多层特效不等于多光源。**主光色 ≤2**，其余用反射/溢色表现。
3. **脸部保护区**：`面部周围 15% 区域保持干净，任何特效不得进入`。

**epic 档的成品骨架**：

```
主体 → 主特效（贴体，颜色/形态/方向）→ 辅特效（脚下/身后，碎屑类）
→ 环境层（天象/云涡/兽潮剪影）→ 环境交互（照亮什么、压弯什么、映在什么上）
→ 主光（唯一）→ 面部保护区 → 镜头 → 排除
```

---

## 十一、六类零件的组合配方（按题材直接抄）

| 题材 | ①法相 | ②光轮 | ③法阵 | ④法器 | ⑤粒子 | ⑥天象 |
|---|---|---|---|---|---|---|
| **帝王 / 仙帝** | 可选（神女/帝影） | **头顶双层纯光环（必）** | 脚下地轮 | 权杖/帝剑 | 金色羽粒 | 祥云翻腾、宫殿远景 |
| **魔尊 / 妖皇** | 兽形法相 | 背后暗紫轮 | 血纹阵 | 长刀/骨杖 | 魂火贴地 | 黑雾翻涌、雷云压顶 |
| **剑仙** | 一般不用 | 不用 | 剑阵（多剑悬停） | 长剑 + 剑光 | 剑气碎芒 | 雪山/云海、寒雾 |
| **战斗术师** | 雷神法身 | 不用 | 脚下法阵余光 | 符环/折扇 | 雷痕拖影 | 古战场、兽潮剪影 |
| **圣女 / 神女** | 神女虚影 | 头顶柔光背光 | 莲台 | 圣器 | 光羽上浮 | 神殿柱廊、金色云隙 |
| **轻装女帝（问题 7）** | 神女法相 | **头顶双层纯光环** | 脚下冰纹阵 | 冰晶长枪 | 冰晶尘上浮 | 冰原深渊 + 云隙冷光 |

> **帝王/仙帝配方是最高频的一组**：光环 + 法阵 + 金色羽粒 + 祥云远景，四件齐了就"有帝王气"，
> 不需要再加第五件——**再加就开始糊。**

---

## 十二、八个玄幻专属崩坏点

| 现象 | 根因 | 改法 |
|---|---|---|
| 出成"通用游戏 CG" | 六类零件缺 3 个以上 | 按 §十一 配方补齐，至少 4 件 |
| 出成"塑料手办" | 只有法相/光环，没有材质与光照层级 | 补 SSS + 环境反射 + 主光方向 |
| 法相变成另一个人 | 没写"同源 + 半透明" | `semi-transparent projection of the same figure` |
| 光环变金属轮盘 | 没写"由光构成、无实体、无辐条" | 见 §三 成品句 |
| 光环压住头发 | 没写"不接触、留空隙" | `floating above the head, not touching` |
| 九条龙画成一条 | 没写"恰好 N 个"+ 逐个剪影 | `exactly nine separate dragons, each distinct` |
| 符文变乱码字 | 让模型写可读字符 | `non-readable abstract runes` |
| 多层特效糊成一片 | epic 档没写分层与面部保护区 | 见 §十 三条纪律 |

---

## 十三、自检（八项）

- [ ] 六类零件至少写了 4 件，且有 1 件是"主"
- [ ] 法相写了"同源 + 倍数 + 半透明 + 姿态差"
- [ ] 光环写了位置、是否接触、是否实心、几层、有无纹饰
- [ ] 法阵写了状态（刚施法/正在施法）+ 残光
- [ ] 武器写了分件 + 握持 + "不许变成什么"
- [ ] 粒子只有一种，方向与属性一致
- [ ] 可数实体写了"恰好 N 个"
- [ ] 天象写了尺度差（人物占画面多少）

---

## 十四、KV 出厂检查单（一张高信息密度的图，逐格对）

> 立绘漏一项只是"少点意思"，**KV 漏一项就是"不是这张图"**。
> 出图前按这张单子过一遍，缺哪格补哪格。

| # | 段 | 必须有的槽位 | 漏了会 |
|---|---|---|---|
| 1 | **主体** | 年龄 + 身份 + 体态 + 头身比 | 人像通用模特 |
| 2 | **脸** | 骨相（方/圆/尖）+ 眉眼 + 1 个识别特征 | 网红脸 |
| 3 | **服装** | 主结构 + 分层 + 覆盖分区 + 三色占比 | 一块布 |
| 4 | **法器** | 器物名 + 分件 + 握持 + "不是 X" | 换成默认武器 |
| 5 | **玄幻零件** | 六类里至少 4 件，其中 1 件为主 | 通用游戏 CG |
| 6 | **特效** | 层数报数 + 主辅分工 + 密度粒径方向 | 糊成一片 |
| 7 | **场景** | 前景 / 中景 / 远景 + 层间空气 + 尺度参照 | 背景贴纸 |
| 8 | **接触** | 脚与地面的接触阴影或倒影 | 人悬空 |
| 9 | **反光** | 至少一处环境光映在人物身上（写清部位） | 合成感丢失 |
| 10 | **光** | 唯一主光 + 光位 + 光比 + 色温 + 补光来源 | 平光、颜色发脏 |
| 11 | **镜头** | 景别 + 机位（仰/俯/平） + 焦段 + 人物占画面比例 | 构图随机 |
| 12 | **遮挡/保护区** | 背景不压剪影 + 特效不进面部 | 主体被吃掉 |
| 13 | **排除** | 文字/水印/格号 + 被否决项 | 旧设定长回来 |

**十三条过完还觉得空 → 不是"要加东西"，是某一格写得不够具体。**
最常见的三格虚：③服装（只写"华丽古装"）、⑦场景（只写"云雾仙山"）、⑪镜头（只写"好看的角度"）。

---

## 十五、与其他文件的关系

| 要写什么 | 读哪份 |
|---|---|
| 特效的时间线与事件化写法 | `vfx.md` §一 / §三（**本文件管"世界里有什么"，vfx 管"它怎么动"**） |
| 场景三层与题材场景包 | `scene-space.md` |
| 服装结构与轻装原型 | `costume-structure.md` |
| 3D 国漫/玄幻的渲染路线 | `anime-3d.md` ⑥ + `style-atlas.md` |
| 成套配方（立绘/KV/宗门） | `09-recipes.md` 第 19 卡起 |
| 锁定项与偏差核对 | `SKILL.md` 定向升级 + Step 0 |

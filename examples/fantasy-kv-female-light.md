# 完整走查：3D 玄幻女帝 · 轻装 · 战斗 KV

> 这个例子演示四件事同时成立：**锁定项写死 / 轻装分区 / 场景三层 / epic 分档特效**。
> 用到的文件：`fantasy-elements.md`（六类零件）、`costume-structure.md`（分层 + 覆盖分区）、
> `scene-space.md`（三层场景）、`style-atlas.md`（A2 3D 国风）、`vfx.md`（§2.6 服饰特效）。

---

## 一、用户原话

> 「3D 国漫玄幻女帝，冰系，要轻装、衣服少但华丽，头顶双层纯光环不要轮盘，
> 手上一柄冰晶长枪，九条冰龙环绕，场景要炸裂，竖版 KV。」

---

## 二、①·五 锁定项提取

| 清单 | 内容 | 去向 |
|---|---|---|
| **必须保留** | 冰系 / 轻装（露肤但不廉价）/ **头顶双层纯光环** / **冰晶长枪** / **恰好九条冰龙** / 竖版 | 正向锚点句 |
| **明确否决** | 身后轮盘、辐条、金属环、裹身长袍、大裙摆、权杖 | 正向"不是 X" + 反向段 |
| **可推断** | 场景（冰原深渊 + 云隙冷光）/ 光比（1:5）/ 镜头（50mm，略仰）/ 配色（冰蓝 6 : 银白 3 : 金 1） | 交付时标注 |

---

## 三、正向提示词（中文核心版，可直接粘）

```
3:4 竖幅，3D 国漫玄幻女帝战斗 KV，冰系，semi-realistic 3D donghua 质感。

【主体】二十七八岁成年女性，方正骨架、宽肩厚背，身高 7.2 头身；
脸型方圆、下颌线利落，剑眉上扬、眼尾略上挑、虹膜冰蓝、瞳中有细碎光点；
鼻梁直、唇偏薄且唇色冷调；神情不怒自威，视线压下前方。
银白长发半束，发冠为冰晶棱面、无流苏。

【服装·服装锚点｜逐字复制】
主结构：贴身冰蓝战衣，高领，前襟斜襟闭合，覆盖躯干与腿。
分层：内层深靛贴身织料（领口与手腕各露出一指宽）/ 中层贴身战衣带分片结构 /
外层无长袍、无大裙摆，仅一条半透明冰晶披帛自后腰垂落。
部件：左肩一片弧形冰晶肩甲 / 右小臂一段棱面护臂 / 腰间一圈鳞片腰封（鱼鳞状甲片，
顺腰线向下压叠）/ 膝下至踝的贴合战靴，边缘鎏金包边。
配饰：右臂上臂一枚青玉臂钏 / 腰侧一条细银链连到腿环 / 额间一枚冰晶额饰——共三件。
覆盖分区：肩颈裸露、上胸为半透冰纱（透出内层结构但不露肤）、腰腹贴体、
后背开至腰际并有一条脊链、上臂裸露、小臂甲片覆盖、腿为贴身层 + 高开衩、
足为战靴。裸露区边缘均由甲片或纱层框住。
配色：冰蓝 60% / 银白 30% / 鎏金 10%（金仅在甲片边缘与靴口）。
动态件：冰晶披帛，受上升气流影响向右后方飘起，末端碎裂成冰屑。

【玄幻零件】
① 光环：头顶正上方一枚双层纯光环，由光构成、边缘发亮、无金属实体、无辐条、无纹饰；
   高出头顶约一个头，与人头不接触。身后不出现任何轮盘或法阵轮盘。
② 法器：右手持冰晶长枪，枪身深蓝近黑、枪头半透明冰晶、枪长约为身高的 1.2 倍，
   右手握于枪身中段，枪尖斜指右下——不是权杖、不是法杖、不是剑。
③ 法阵：脚下冰纹法阵，边缘符文仍在发光，霜自阵纹向外爬出约两米。
④ 灵兽：恰好九条冰龙环绕，每条为独立的半透明冰质剪影、大小一致，
   在肩高位置环绕，部分在身前、部分在身后交错，不遮挡面部；不允许多出第十条。

【特效·三层（战斗 KV 档）】
主特效：寒气与冰晶尘自裙缘与枪尖向上升腾，稀疏、米粒大小、方向向上偏右，
在轮廓光里发亮；不遮挡面部。
辅特效：脚下冰屑与碎晶被气流卷起，贴地滚动；披帛末端持续碎裂成小冰片。
环境层：远景云涡在天空缓慢旋转，云隙间漏下冷光柱。
主光：右后方侧逆光穿过云隙形成体积光，光比 1:5，6500K 冷调；
面部由左前方微弱反射光提亮，暗部不死黑。主光色只两种（冷白 + 冰蓝）。
环境交互：冷光在冰晶肩甲与枪头上形成窄而亮的高光带（高光保留细节，不死白、
不出现纯白死白块）；霜沿战靴向上爬；披帛与长发被同一道上升气流带向右侧。
剪影：披帛与左臂之间留出可见空隙，无相切轮廓；长枪与身体之间留出空隙。

【场景·三层】
前景：画面左下角一根半透明冰柱压角，占 12%，不遮挡人物。
中景：人物立于冰原断崖边的平整冰台，冰台边缘有裂口与悬垂冰棱；身后三根冰蚀石柱。
远景：云海之上两座冰峰剪影，最远一座只占画面高度 1/8；天空为云涡与云隙。
层间：一层贴地寒雾，只在层与层之间，不进入人物周围一米。
地面：冰面有细裂纹与雾面反光，脚下柔和接触阴影 + 弱倒影。

【镜头】竖版全身偏大半身，相机略低于腰线、略仰 5°，50mm f/4，
人物占画面高度 68%；人物居中偏左，右侧留出云隙光柱。

【排除】画面中不出现任何文字、水印、标志、格号；不出现身后轮盘、金属光环、辐条、
裹身长袍、大裙摆、权杖、法杖、多余冰龙、多余配饰、皮肤过度真实质感、部位粘连、布料穿模。
```

---

## 四、英文版（MJ / Flux / SD）

```
semi-realistic 3D donghua key visual, ice-attribute female empress, 3:4 vertical,
7.2 head proportion, square sturdy build, broad shoulders, cold imposing gaze,
silver-white hair half-tied, faceted ice crown without tassels,

costume anchor: fitted ice-blue battle suit, high collar, diagonal closure,
inner dark indigo layer showing one finger-width at collar and wrists,
faceted ice pauldron on the left shoulder only, faceted bracer on the right forearm,
fish-scale plate waist ring overlapping downward, fitted boots with thin gilt trim,
jade armlet on the right upper arm, one thin silver chain to a thigh ring,
translucent ice mantle trailing to the back-right, ends crumbling into ice shards,
bare shoulders and upper arms, sheer panel across the upper chest showing the inner layer,
open back to the waist with a single spine chain, high front slit over fitted leggings,
palette: ice blue 60% / silver white 30% / gilt 10%,

a plain double-ring halo of light floating directly above the head, one head-height up,
not touching, made of light, no spokes, no rim, no ornament — not a wheel behind the back,
a crystalline ice spear in the right hand, gripped mid-shaft, tip angled down-right,
length about 1.2x body height — not a staff, not a scepter, not a sword,
exactly nine separate translucent ice dragons circling at shoulder height,
each a distinct silhouette, none covering the face, no extra dragons,
a frost rune array on the ground beneath the feet, edges still glowing, frost creeping outward,

VFX in three layers (battle KV tier): rising frost motes and ice dust from the hem and the spear tip,
sparse, rice-grain sized, drifting upward-right; ground ice shards rolling at her feet;
a slow vortex in the distant clouds with cold shafts of light breaking through,
one key light from behind-right at 1:5 ratio, 6500K, faint bounce from front-left on the face,
cold light forming a thin bright band along the ice pauldron and the spearhead, highlights retaining detail with no blown white,
frost climbing the boots, mantle and hair pulled to the right by the same updraft,
visible negative space between the mantle and the left arm, no tangent contours,

scene in three layers: a translucent ice column pressing the lower-left corner (12%, not covering her),
a flat ice ledge at the edge of a cliff with cracks and hanging icicles, three ice-eroded pillars behind,
two distant ice peaks in a sea of clouds, the farthest only 1/8 of the frame height,
one layer of ground frost mist only between layers, not around the figure,
soft contact shadow and faint reflection beneath the feet,
camera slightly below waist, 5° up, 50mm f/4, figure at 68% of frame height, off-centre left,

no text, no watermark, no logo, no panel numbers, no wheel behind the back,
no metal halo, no spokes, no wrap-around robe, no full skirt, no scepter, no staff,
no extra dragons, no extra accessories, no over-realistic skin, no fused limbs, no cloth clipping
```

---

## 五、反向词（独立负向框用）

```
身后轮盘, 金属光环, 辐条, 纹饰光环, 裹身长袍, 大裙摆, 权杖, 法杖, 剑, 多余冰龙, 第十条龙,
多余配饰, 皮肤毛孔, 过度真实皮肤, 部位粘连, 布料穿模, 手部畸形, 六指, 文字, 水印, logo,
低俗姿势, 影楼风, 塑料手办感, 过度泛光, 面部被粒子遮挡
```

英文：

```
wheel behind back, metal halo, spokes, ornate halo, wrap-around robe, full-length skirt,
scepter, staff, sword, extra dragons, tenth dragon, extra accessories, skin pores,
over-realistic skin, fused limbs, cloth clipping, bad hands, six fingers,
text, watermark, logo, cheap glamour look, plastic toy look, blown-out bloom, particles over face
```

---

## 六、机检结果

```bash
python scripts/prompt_lint.py --file prompt.txt --platform seedream \
  --purpose portrait --length long --energy epic
```

```
得分：100 / 100   [P0×0 P1×0 P2×0]   判定：可直接交付
```

---

## 七、这张图为什么能成立（四条可迁移的判断）

1. **锁定项用"不是 X"写死** —— 光环、长枪、龙的数量三处都是"正向描述 + 排他句"，
   这比只放反向框有效（中文平台尤其如此）。
2. **轻装靠"覆盖分区"而不是形容词** —— 八个区逐区写"裸/半透/贴体/甲片"，
   并给每条裸露区加"结构框住"，所以既有轻装感又不廉价。
3. **场景靠三层 + 接触** —— 前景压角、中景冰台、远景 1/8 冰峰，加贴地寒雾与接触阴影，
   人物才"站在"里面，而不是贴上去。
4. **epic 特效靠"分层报数 + 主光唯一 + 面部保护区"** —— 三层特效仍不糊，
   因为每一层都写了位置、方向、尺度，并且始终只有一个主光。

---

## 八、如果想改（定向升级示例）

| 用户说 | 只改哪一句 | 不许动 |
|---|---|---|
| 「换成火系」 | 属性词 + 配色 + 粒子类型（冰晶尘→赤金余烬，方向改向下） | 光环规格、龙的数量、服装结构 |
| 「光环再华丽一点」 | 只改光环句（加"三层同心 + 细密纹"） | 其余全部；且要说明"这会从纯光环变成纹饰环" |
| 「裙子长一点」 | 服装锚点"外层/腿"两处 | 分区表其余六区 |
| 「背景再炸裂」 | 环境层（云涡 → 天劫雷云 + 更多光柱） | 主光色仍只两种、面部保护区不变 |

# 鞋靴：四层结构写法

> 鞋在整套提示词里通常只占 2–6 个字（"黑色短靴"），然后模型自由发挥。
> 但鞋是全身图里**最先崩的三处之一**（另两处是手、发梢）。

---

## 一、四层结构（工业术语直接翻成提示词）

| 层 | 可写项 | 提示词写法 |
|---|---|---|
| **① 鞋面** | 前帮（vamp）、鞋头盖（toe cap）、后帮（quarter）、鞋口（collar）、鞋舌（tongue）、鞋眼（eyelets）、后跟稳定片（heel counter） | `suede toe cap, perforated vamp, padded collar` |
| **② 鞋底** | 内底（insole）、中底（midsole）、大底（outsole）、鞋跟（heel）、沿条（welt） | `gum outsole, stacked leather heel, visible welt stitching` |
| **③ 楦型** | 鞋头形状 + 跟高 | `almond toe, 6cm block heel`；方头 `square toe`、尖头 `pointed toe`、圆头 `round toe` |
| **④ 工艺状态** | 制法 + 使用痕 | `Goodyear welted, creased flex points, scuffed heel, salt stains` |

**只写 ① 就够出图，写全四层就够出"设定图"。**

---

## 二、靴筒高度（必须写死的一档）

| 写法 | 位置 |
|---|---|
| `ankle boots` | 到踝 |
| `mid-calf boots` | 到小腿中段 |
| `knee-high boots` | 到膝下 |
| `thigh-high boots` | 过膝 |
| `over-knee boots` | 膝上、接近大腿中段 |

> 只写 `boots`，模型默认给中筒，全身图里会把小腿比例吃掉。

---

## 三、闭合方式（不写就长出鞋带）

| 类型 | 写法 |
|---|---|
| 系带 | `lace-up with 5 pairs of metal eyelets` |
| 拉链 | `inner side zipper, no laces` |
| 松紧侧边 | `slip-on with elastic side gusset, no laces` |
| 搭扣 | `double buckle straps, no laces` |
| 一脚蹬 | `slip-on, laceless` |

**反向必须加**：`no lace where not specified` —— 这是鞋类最高频的崩坏。

---

## 四、三段式模板（单品图最好用）

```
① 主体：一双黑色切尔西靴
② 材质：光面小牛皮，弹性侧边拼接
③ 光影：棚拍顶光，水泥地面，产品图

→ a pair of black chelsea boots, polished calf leather with elastic side panels,
  studio top light on concrete floor, product shot
```

**顺序铁律**：主体 → 材质 → 光影。**风格词不许写在主体前面**——"油画质感的靴子"会把笔触糊到鞋型上，出来一双融化的靴子。

---

## 五、玄幻/古风鞋靴（与题材对接）

| 类型 | 写法 |
|---|---|
| 云履 | `layered cloth shoes, upturned cloud-patterned toe, white soles` |
| 战靴 | `armored greaves over leather boots, plated shin guard, iron toe cap` |
| 布靴 | `cloth boots with wrapped ankle ties, flat sole` |
| 木屐 | `wooden geta, two supporting teeth, cloth thong strap` |
| 赤足 | `barefoot, visible foot structure, no shoes`（**必须写明，否则自动加鞋**） |

> **赤足一定要写"no shoes"**：中式玄幻常见赤足设定，但模型默认补鞋。

---

## 六、崩坏点（5 条）

| # | 崩坏 | 根因 | 写法 |
|---|---|---|---|
| 1 | 鞋型融化 | 风格词写在主体前 | 风格词放最后或不写 |
| 2 | 靴子长出鞋带 | 没写闭合方式 | 写死 `slip-on / no laces` |
| 3 | 靴筒高度不对 | 只写 `boots` | 写 `ankle/mid-calf/knee-high/thigh-high` |
| 4 | 全身图脚被裁 | 画幅与格子形状冲突 | 2:3 竖版出全身；四格用 9:16 |
| 5 | 两只鞋不一样 | 没写"成对且对称" | `a matching pair, mirrored left and right` |

---

## 七、与其他文件的接口

- 配色：鞋算**点缀色 5–10%**（见 `outfit-design.md` §2），别给主色
- 袜/腿：过膝靴与 `thighhighs` 二选一，同时写会打架
- 拆解图：鞋在"服装分层"清单里必须单列一件，不能归进"下装"
- 建模：鞋底厚度与跟高要写数字，否则绑定后脚会陷进地面

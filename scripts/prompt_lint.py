#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""prompt_lint.py — 画面提示词机检

查六类问题：结构缺格 / 语义冲突 / 语法误用 / 画质词堆砌 / 动作过量 / 文字期望不匹配。
输出 P0（必改）、P1（建议改）、P2（可选）与 0-100 分。

用法:
    python prompt_lint.py --text "提示词" --platform mj --purpose poster
    python prompt_lint.py --file prompt.txt --platform seedream --json
    echo "..." | python prompt_lint.py --platform sd
    python prompt_lint.py --self-test

说明: 全部为启发式判断，命中后请人工复核。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field

# 控制台编码兜底（Windows GBK 终端）
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
    except Exception:
        pass


# ---------------------------------------------------------------- 词表

PLATFORMS = ["mj", "sd", "flux", "nano_banana", "gpt_image", "seedream", "wanx", "ideogram", "unknown"]

PURPOSES = ["poster", "cover", "ecommerce", "banner", "article", "avatar", "portrait", "infographic", "wallpaper", "asset", "turnaround", "character_sheet", "profile_page", "model3d", "general"]

# 需要显式画幅的用途
NEEDS_RATIO = {"poster", "cover", "ecommerce", "banner", "infographic", "wallpaper", "avatar", "portrait",
               "turnaround", "character_sheet", "profile_page"}

# 展示型设定稿：给人看的设定页，不是给下游用的资产图——建模五项对它不适用
SHOWCASE_PURPOSES = {"turnaround", "character_sheet", "profile_page"}

# 长度三档：short 给标签派 / standard 默认 / long 给长中文描述
LENGTH_TIERS = {
    "mj": (400, 700, 900),
    "sd": (900, 1500, 2000),
    "flux": (700, 1200, 1800),
    "nano_banana": (1200, 2500, 3500),
    "gpt_image": (800, 1500, 2200),
    "seedream": (600, 900, 1600),
    "wanx": (600, 900, 1600),
    "ideogram": (400, 600, 900),
    "unknown": (700, 1200, 3000),
}
LENGTH_TIER_IDX = {"short": 0, "standard": 1, "long": 2}

LIGHT_WORDS = [
    "光", "逆光", "侧光", "顺光", "顶光", "底光", "柔光", "硬光", "窗光", "体积光",
    "光比", "色温", "光影", "light", "lighting", "backlit", "backlight", "rim light",
    "softbox", "window light", "golden hour", "blue hour", "neon", "candlelight", "k ",
]
KELVIN_RE = re.compile(r"\b\d{4}\s*k\b", re.I)
LIGHT_DIR_RE = re.compile(
    r"((左|右|上|下)(侧|方|前|后|角)?[^。；;]{0,8}(光|打亮|打光|打入|投射|补光|入射|射入|照射))"
    r"|((光|光线|light)[^。；;]{0,8}(自|从|from)?\s*(左|右|上|下)(侧|方|前|后|角|上|下))"
    r"|((正面|背面|侧面|斜侧|前侧|顶部|底部)[^。；;]{0,4}(光|打光|照射))"
    r"|((from|toward|behind)\s+(the\s+)?(lower\s+|upper\s+|left|right|front|back|side))"
    r"|(\b(lower|upper)[- ](left|right)\b)",
    re.I,
)
CAMERA_RE = re.compile(r"\d{2,3}\s*mm\b|\bf/\d(?:\.\d+)?|\bf/\s*\d", re.I)

CAMERA_WORDS = [
    "特写", "近景", "中景", "全景", "远景", "大远景", "中近景", "俯拍", "仰拍", "平视",
    "鸟瞰", "顶视", "机位", "焦段", "镜头", "景深", "mm", "close-up", "closeup",
    "wide shot", "medium shot", "full shot", "low angle", "high angle", "top-down",
    "bird", "eye level", "f/", "aperture", "depth of field", "macro",
]

STYLE_WORDS = [
    "风格", "写实", "摄影", "插画", "水彩", "油画", "动漫", "二次元", "赛璐璐", "厚涂",
    "3d", "渲染", "极简", "复古", "国风", "水墨", "赛博", "蒸汽", "胶片", "版画",
    "扁平", "矢量", "电影感", "纪实", "editorial", "cinematic", "minimalist",
    "photorealistic", "illustration", "watercolor", "oil painting", "anime", "cel shading",
    "octane", "risograph", "bauhaus", "vector", "film grain", "polaroid",
]

RATIO_RE = re.compile(r"(?<![0-9])(\d+(?:\.\d+)?\s*[:：]\s*\d+(?:\.\d+)?)(?![0-9])")
AR_PARAM_RE = re.compile(r"--ar\s+\d+:\d+", re.I)
WEIGHT_RE = re.compile(r"\(\s*[^()]{1,60}:\s*\d+(?:\.\d+)?\s*\)|\(\(", re.I)
NEG_HEADER_RE = re.compile(r"(negative\s*prompt|反向提示词|负向提示词|排除项|禁止[:：])", re.I)
QUOTE_RE = re.compile(r"[\"“”'‘’「」『』《》][^\"“”'‘’「」『』《》]{1,60}[\"“”'‘’「」『』《》]")
SIZE_HIER_RE = re.compile(r"(字号|层级|font size|headline|主标题|副标题|1/3|1/2|最大)")

# "不要文字" 类句式（先剥离，避免与"要写字"混淆）
TEXT_FORBID_RES = [
    r"(画面中|画面内)?(不出现|不得出现|不要|无|没有|不含|避免)[^。；;，,]{0,10}(文字|字母|数字|字迹|文案)",
    r"no\s+(text|lettering|words|type|copy)",
    r"without\s+(any\s+)?(text|lettering|words)",
    r"blank\s+surface[s]?",
]

# "留出来给后期用" 类句式（不是要求图内写字，也先剥离）
TEXT_NEUTRAL_RES = [
    r"(供|用于|预留|留给|留出)[^。；;]{0,12}(排版|标题|文字|文案|口播)?",
    r"(for|reserved for)\s+(later\s+)?(typography|headline|text|caption)",
]

# "要写字" 类句式
TEXT_WANT_RES = [
    r"(写|放置|排版|添加|加上|印上|出现)[^。；;]{0,8}(文字|标题|文案|书名|标语|大字|几个字)",
    r"(文字|标题|文案|书名|标语)[^。；;]{0,8}(写|放|居中|位于|排版)",
    r"(标题|文案|书名)[^。；;]{0,12}(字|号)",
    r"\b(headline|title text|lettering|logo text|the words)\b",
]


# 多格图 / 参考图 / 套话相关
MULTI_RE = re.compile(
    r"(\d+\s*(格|视图|宫格|panel))|(三视图|四视图|五视图|六视图|八视图|九宫格|多视图|转面|turnaround|character sheet)",
    re.I,
)
CAP_RE = re.compile(
    r"(仅此|只有这|不超过|不增加|恰好|正好)\s*[0-9０-９一二三四五六七八九十两]*\s*(格|视图|个|处|张|幅)"
    r"|(only|exactly)\s+\d+\s+(panels|views|frames)"
    r"|no additional (panels|views)",
    re.I,
)
LABEL_RE = re.compile(
    r"(无格号|无箭头|无图注|无视图标签|无尺寸标注|无标注|no panel numbers|no arrows|no captions|no view labels|no labels)",
    re.I,
)
# 资产图型的专属禁忌（图型定了，光/材质/写法的规则就跟着定）
LIGHT_REF_RE = re.compile(r"(灯光参考|打光参考|光位参考|lighting\s*reference|light\s*setup)", re.I)
LIGHT_UNIFORM_RE = re.compile(
    r"((统一|一致|相同|同一)[^。；;，,]{0,6}(平光|光照|灯光|光位|照明))"
    r"|(flat even lighting[^。；;，,]{0,6}(统一|一致))", re.I)
LIGHT_VARY_RE = re.compile(r"(各不相同|光位不同|不同光位|四格分别|每格[^。；;，,]{0,6}不同|逐格|分别使用不同光)", re.I)
MATZONE_RE = re.compile(r"(材质分区|材质划分|材质标记|material\s*(zone|breakdown|id))", re.I)
MAT_PARAM_WORDS = ["roughness", "metalness", "ior", "次表面散射", "清漆",
                   "反射率", "金属度", "写实材质", "subsurface"]
ACTION_FREEZE_RE = re.compile(r"(动作冻结|相同动作|同一动作|冻结在|frozen\s+pose|identical\s+pose)", re.I)
SKELETON_RE = re.compile(r"(骨骼视图|骨骼参考|骨架参考|骨架图|关节参考|skeleton\s*(reference|view|overlay))", re.I)
RIG_WORDS = ["权重", "蒙皮", "绑定骨架", "骨骼层级", "控制器", "weight paint", "armature"]
RIG_RE = re.compile(r"\brig\b", re.I)
OUTFIT_SWAP_RE = re.compile(r"(换装图|多套服装|服装变体|outfit\s*(variant|swap|sheet))", re.I)
SAME_EXCEPT_RE = re.compile(
    r"(除服装外|只换衣服|仅服装不同|其余[^。；;，,]{0,10}(相同|一致|不变)"
    r"|姿态[^。；;，,]{0,8}(一致|相同|不变)|同一姿态)", re.I)

REF_RE = re.compile(
    r"((按|用|挂|喂|以|依据|参照)\s*[^。；;，,]{0,8}参考图)"
    r"|(参考图\s*[0-9０-９])"
    r"|(ref(erence)?\s*image)"
    r"|(image\s*[0-9])",
    re.I,
)
REF_ROLE_RE = re.compile(r"(只用来|只取|只作|仅取|只确定|不按这张图|完全不按|只用它|以上述图为唯一)", re.I)
COUNT_RE = re.compile(r"([2-9]|\d{2,}|[二两三四五六七八九十])\s*(只|个|人|件|位)[^，。；,;]{0,6}(猫|狗|人|杯|瓶|孩子|模特|主体|物品)")
TOTAL_RE = re.compile(r"(总数|严格等于|仅此|只有\s*[0-9一二两三四五六七八九十]|共\s*[0-9一二两三四五六七八九十])", re.I)

# 3D 动漫：五条互斥路线，写"3D 动漫"四个字等于没写路线
ANIME3D_RE = re.compile(r"(3\s*d|三维)[^。；;，,]{0,12}(动漫|二次元|anime|角色|人物)", re.I)
ROUTE_RE = re.compile(
    r"(cel[- ]?shad|toon\s*render|pixar|disney\s*3d|subsurface\s*scattering|sss"
    r"|painterly\s*shading|stylized\s*3d|semi[- ]realistic\s*anime|non[- ]photorealistic|\bnpr\b"
    r"|cartoon|chibi|赛璐璐|三渲二|次表面散射|半写实|卡通渲染|卡通|风格化\s*3d|q\s*版"
    r"|lumen|filmic|ue\s*5|unreal|影视级|玄幻\s*cg)",
    re.I,
)
SKIN_REAL = ["毛孔", "皮肤纹理", "绒毛", "pores", "vellus hair", "skin texture"]
SKIN_NEG_RE = re.compile(r"(无|没有|不见|no|without)\s*(毛孔|皮肤纹理|绒毛|pores|vellus hair|skin texture)", re.I)

# 特效层
VFX_PARTICLE = ["粒子", "光尘", "火星", "余烬", "尘埃", "花瓣", "落雪", "飞雪", "雪粒", "飘雪",
                "雨丝", "水花", "血雾", "数据流", "碎晶", "羽毛", "萤火状光点", "萤火般的光点",
                "particles", "embers", "sparks", "motes"]
VFX_DENSITY = ["稀疏", "中等密度", "密集", "可数", "成雾", "密度", "sparse", "dense", "medium density"]
VFX_LIGHT = ["轮廓光", "体积光", "辉光", "法术光", "溢色", "光晕", "色散", "发光", "剑光",
             "rim light", "volumetric", "bloom", "glow", "god rays", "lens flare"]
VFX_ENERGY = ["气浪", "冲击波", "地裂", "裂纹", "残影", "碎屑", "shockwave", "afterimage", "air distortion"]
VFX_CLOTH = ["衣摆上扬", "披风拖尾", "破损", "焦边", "湿透", "发光刺绣", "鳞甲", "fabric flowing",
             "torn hem", "wet fabric", "glowing embroidery",
             # 服饰特效：附着在服装上的过程性描述（不是独立粒子）
             "光缕", "游走", "纹路自发光", "符文游走", "衣摆能量化", "袍身流光", "渐变光纹",
             "沿袍身流动", "袖摆发光", "织纹发亮", "光纹沿", "energy threads", "glowing seams"]
VFX_MEDIA_WORDS = ["烟", "雾", "尘", "水汽", "热浪", "薄雾", "浓烟", "霾", "雨幕", "水雾",
                   "smoke", "fog", "mist", "haze", "steam"]
LIGHT_COLOR_WORDS = ["暖金", "冷蓝", "冰蓝", "青蓝", "橙", "洋红", "紫", "绿光", "暖黄", "冷白",
                     "金", "银白", "琥珀", "绯红", "荧光绿", "青紫"]
FACE_CLEAR = ["不遮挡面部", "不挡脸", "不入脸", "不在眼前", "面部清晰", "不覆盖面部",
              "no particles over the face", "face unobstructed", "not covering the face",
              "none covering the face", "no particle over the face",
              "面部周围保持干净", "面部周围干净", "无粒子进入", "keep the face clear",
              "不进人物脸部", "不进脸部", "不落到脸上", "不堆在脸前"]

# 角色服装与配饰（立绘最容易堆过头的地方）
CLOTH_LAYER_WORDS = ["外罩", "罩衫", "中衣", "内衬", "贴身层", "中层", "外层", "叠穿", "多层",
                     "夹层", "外袍", "里衣", "加一层", "内衬层"]
ACCESSORY_WORDS = ["肩饰", "腰饰", "腕饰", "发饰", "项饰", "耳饰", "臂钏", "手钏", "流苏",
                   "玉片", "银链", "挂坠", "佩环", "铃铛", "珠串", "缎带", "臂环"]
CLOTH_MAIN_WORDS = ["长裙", "法袍", "袍", "外套", "大衣", "铠甲", "战衣", "礼服", "罩袍", "披风"]
CLOTH_ATTACH = ["裙缘", "裙摆", "袖口", "袖摆", "衣摆", "袍身", "领口", "前襟", "肩线", "背部",
                "刺绣", "纹路", "织纹", "下摆", "腰带", "hem", "cuff", "collar"]
BACKDROP_WORDS = ["背景", "场景", "神域", "仙山", "宫殿", "废墟", "庭院", "神殿", "云海",
                  "background", "scene", "setting"]
FANTASY_WORDS = ["玄幻", "仙侠", "神域", "仙山", "神殿", "法神", "古风", "奇幻", "神阙",
                 "修真", "仙门", "魔域", "灵域"]

# 题材分族：同一张图跨两族以上，必须声明"主题材"（否则出四不像）
GENRE_FAMILIES = {
    "东方": ["玄幻", "仙侠", "古风", "宫廷", "武侠", "江湖", "民国", "和风", "和服",
             "东南亚", "异域", "国风", "修仙", "仙门"],
    "现代": ["都市", "通勤", "校园", "青春", "职场", "街头", "潮流", "运动", "竞技"],
    "未来": ["赛博朋克", "赛博", "科幻", "机甲", "星际", "太空", "废土", "末世", "末日"],
    "奇幻": ["西幻", "蒸汽朋克", "中世纪", "骑士", "城堡", "哥特", "童话", "神话",
             "克苏鲁", "吸血鬼", "魔法"],
    "亚文化": ["洛丽塔", "洋装", "y2k", "千禧", "赛博少女", "兽人", "拟人"],
    "年代": ["复古", "80s", "90s", "蒸汽波", "synthwave", "录像带"],
}
PRIMARY_GENRE_RE = re.compile(
    r"(主题材|主世界观|以[^。；;，,]{1,8}为主|主风格是|primary genre|main genre)", re.I)

# 可数实体（玄幻高频：九条龙、双环、数枚冰晶）——数量必须封顶，否则模型随意增删
COUNT_ENTITY_RE = re.compile(
    r"([0-9一二两三四五六七八九十数十百]+)\s*(条|只|枚|名|位|柄|座|层|重|道|颗|头|个)\s*"
    r"[^。；;，,]{0,6}(龙|凤|剑|兽|环|轮|晶|火焰|法相|分身|灵兽|羽|铃|珠)")
COUNT_CAP_RE = re.compile(r"(恰好|正好|仅|只|严格等于|exactly|only)\s*[0-9一二两三四五六七八九十百]*|不允许|不多出|不得多")

# 方位：光环 / 光轮 / 背光 / 法阵 混用（审计里真实事故：头顶光环被画成身后轮盘）
HALO_ABOVE_RE = re.compile(r"(头顶|正上方|头上)[^。；;，,]{0,12}(光环|光轮|光圈|halo)", re.I)
WHEEL_BEHIND_RE = re.compile(r"(身后|背后|背部)[^。；;，,]{0,12}(轮盘|法轮|光轮|圆盘|wheel|disc)", re.I)
HALO_SPOKE_RE = re.compile(r"(辐条|轮辐|纹饰环|雕纹环|spokes)", re.I)

# 服装锚点段
COSTUME_ANCHOR_RE = re.compile(r"(服装锚点|costume anchor)", re.I)
COSTUME_LAYER_RE = re.compile(
    r"(内层|中层|外层|贴身层|配饰[:：]|分层|inner layer|mid layer|outer layer|accessor)", re.I)
COLOR_DECL_RE = re.compile(r"(?:主色|辅色|点缀色?|配色)[^。；;，,]{0,30}", re.I)
LIGHT_COLOR_OK_RE = re.compile(
    r"(主光色只两种|两种主光色|主光色 ≤2|只两种主光|only two light colors|two light colors only)", re.I)
COLOR_NAME_RE = re.compile(r"(冰蓝|银白|玄黑|墨黑|月白|朱红|暗赤|鎏金|青玉|石青|天青|铁灰|暗铜|"
                           r"藏青|奶白|浅杏|雾蓝|暗紫|血赤|幽紫|荧光绿|琥珀|绯红|冷白|暖金|苔绿|暖米|锈红)")
LOCKED_OUTFIT_RE = re.compile(r"(同一套服装|服装完全一致|服装逐字一致|same outfit)", re.I)
SCENE_DEPTH = ["前景", "中景", "远景", "前中远", "层次", "纵深层", "层叠", "纵深",
               "foreground", "midground", "depth layers"]
PLAIN_BG_RE = re.compile(
    r"(纯色背景|纯白背景|浅灰背景|白色背景|无缝背景|中性背景|plain background|seamless|neutral backdrop|纯色底)",
    re.I)

# 角色动作（日常 + 战斗 + 仙侠；只收不会被名词误伤的词）
CN_VERBS = [
    "跑", "坐", "躺", "望", "挥", "抱", "吃", "喝", "笑", "哭", "握", "捧", "蹲", "扔",
    "迈步", "跃起", "举起", "举剑", "起身",
    # 角色/仙侠向的**身体动作**（升腾/游走/流转/垂落属于特效过程，不算动作，见 VFX 词表）
    "结印", "悬浮", "抬手", "侧身", "俯身", "倚靠", "回望", "托举", "踏", "掠",
]
EN_VERBS = [
    "walking", "running", "sitting", "standing", "holding", "looking", "flying",
    "falling", "pouring", "eating", "drinking", "smiling", "jumping", "throwing",
    "reaching", "pointing", "leaning", "climbing", "reading", "writing",
    "hovers", "floating", "summoning", "spreading",
]
VFX_HIER = ["主特效", "辅特效", "克制", "一层", "restrained", "only one effect", "subtle"]
HIGHLIGHT_OK = ["不死白", "保留细节", "无纯白", "高光有细节", "no blown", "retain detail", "controlled bloom"]
VFX_INTERACT = ["照亮", "投在", "投下", "压弯", "分开", "弹开", "溅", "熄灭", "映", "反射", "推开",
                "卷起", "爬上", "勾出", "切出", "casts", "illuminat", "parts around", "bounces",
                "splash", "ripples", "outlines", "lights up", "kicked up",
                "forming a band", "hugging", "climbing", "creeping", "pulled by", "catches",
                "catching", "lighting the"]
MOTION_BLUR = ["motion blur", "动态模糊", "拖影", "残影", "afterimage", "light trails"]
SUBJECT_SHARP = ["sharp focus", "主体清晰", "主体保持清晰", "subject in sharp focus", "subject stays sharp"]

# 建模交付向（多视图给 3D 用时的工程条件）
MODEL_RE = ["建模", "模型参考", "工程图", "blender", "rig", "绑定", "image plane", "对位"]
ORTHO_RE = re.compile(r"(orthographic|正交)", re.I)
POSE_RE = re.compile(r"(a[- ]?pose|t[- ]?pose|apose|tpose|中性站姿|双臂外张|arms\s+\d+[°度]?\s*away)", re.I)
LANDMARK_RE = re.compile(
    r"(baseline|地标|水平线|guideline|alignment line|脚底对齐|同一水平|同一基线|对齐同一"
    r"|脚底[^。；;，,]{0,6}头顶[^。；;，,]{0,4}(对齐|一致)|头顶[^。；;，,]{0,6}脚底[^。；;，,]{0,4}(对齐|一致)"
    r"|(各格|三格|四格|视图)[^。；;，,]{0,8}(等高|同高|一致))",
    re.I,
)
NEUTRAL_RE = re.compile(r"(neutral expression|中性表情|闭嘴|mouth closed|eyes open looking straight)", re.I)

# 中文数字（母语写作天然写"三格/四视图/八张"，必须归一化）
CN_NUM = "0-9０-９一二三四五六七八九十两"

# 低模：面数必须分区，且不许混高模细节
LOWPOLY_RE = re.compile(r"(低模|低多边形|low[- ]?poly|lowpoly|面数|三角面)", re.I)
FACET_BUDGET_RE = re.compile(
    r"(头部[^。；;，,]{0,12}(密|细)|头手[^。；;，,]{0,8}(密|细)|面片[^。；;，,]{0,10}(密|疏|大小|分区)"
    r"|dense (small )?facets|large flat planes|facet size|polygon density|面数分配|不均分|按部位递减)",
    re.I,
)
LOWPOLY_BAD = ["毛孔", "刺绣", "镂空", "单根发丝", "蕾丝", "渐变", "皮肤纹理",
               "pores", "embroidery", "lace", "single hair strand", "gradient shading"]
LOWPOLY_NEG_RE = re.compile(
    r"(无|没有|不出现|不做|no|without)\s*[^。；;，,]{0,4}(毛孔|刺绣|镂空|单根发丝|蕾丝|渐变|皮肤纹理"
    r"|pores|embroidery|lace|gradient)", re.I)

# text→3D / image→3D：技术简报，不是描述
T3D_RE = re.compile(
    r"(text[ -]?to[ -]?3d|text2?3d|img(en)?[ -]?to[ -]?3d|文生\s*3d|图生\s*3d"
    r"|生成\s*3d\s*模型|直接生成\s*3d|meshy|tripo|hunyuan\s*3d|rodin|3d\s*生成器)",
    re.I,
)
RIGGABLE_RE = re.compile(r"(绑骨|自动绑定|a[- ]?pose|t[- ]?pose|apose|tpose)", re.I)
LIMB_SEP_RE = re.compile(
    r"(四肢分离|肢体分离|手臂[^。；;，,]{0,12}(间隙|背景带|分开|离开)|背景带"
    r"|separated limbs|band of plain background|gap between the (arm|leg)|双腿留缝|visible gap between the legs)",
    re.I,
)
FLOAT_NEG_RE = re.compile(
    r"(无悬空|不悬空|无薄片|无融合|no floating|no thin sheet|no fused|no transparent|无透明)",
    re.I,
)

# 角色美学（书上的顺序：形状 → 剪影 → 体块 → 五官）
CHAR_SUBJECT = ["人物", "角色", "少女", "少年", "女孩", "男孩", "女性", "男性", "立绘", "character", "girl", "boy", "woman", "man"]
FULLBODY = ["全身", "full body", "full-body", "立绘", "standing figure", "全身像"]
SHAPE_WORDS = ["圆", "方", "三角", "几何形", "主形", "副形", "rounded", "angular", "blocky",
               "geometric", "shape language", "剪影", "silhouette"]
NEGSPACE = ["负空间", "空隙", "间隙", "gap between", "separation", "不粘连", "no tangent",
            "negative space", "臂与躯干", "分开"]

BEAUTY_CLICHE = [
    "九头身", "修长双腿", "完美五官", "网红脸", "顶级美女", "天使面孔",
    "绝世美女", "神颜", "超模脸", "零瑕疵肌肤", "黄金比例身材",
    "perfect features", "flawless skin", "model face",
]

AUTEUR_WORDS = [    "王家卫", "徐克", "袁和平", "张艺谋", "朴赞郁", "大卫·芬奇", "诺兰",
    "库布里克", "宫崎骏", "吉卜力", "新海诚", "今敏", "押井守", "MAPPA",
    "京阿尼", "韦斯·安德森", "塔可夫斯基", "黑泽明", "维伦纽瓦",
    "studio ghibli", "ghibli", "mappa", "wes anderson", "villeneuve",
    "kubrick", "nolan",
]

QUALITY_WORDS = [    "8k", "4k", "8 k", "uhd", "ultra detailed", "ultra-detailed", "ultra hd",
    "masterpiece", "best quality", "highly detailed", "extremely detailed",
    "hyper detailed", "hyperdetailed", "hdr", "super detailed", "sharp focus",
    "超清", "极致细节", "大师作品", "高清", "最高画质", "杰作",
]

# 空词分两档：纯夸赞（P1）与用户口语（P2）
FILLER_HARD = [
    "高级感", "高级", "唯美", "惊艳", "氛围感", "完美",
    "beautiful", "gorgeous", "stunning", "amazing", "high-end", "breathtaking", "epic",
]
FILLER_SOFT = [
    "大气", "有质感", "精致", "质感好", "清冷威严", "修长挺拔", "气质出众", "仙气",
    "premium feel", "aesthetic", "elegant", "refined",
]
FILLER_WORDS = FILLER_HARD + FILLER_SOFT  # 兼容旧引用

# 只收"不会被复合词误伤"的动作动词（写/读/看/拉/推/转 等在高频名词里出现，已剔除）
# 角色/仙侠向的动词表已扩充到下方「角色服装与动作」区，此处只留通用日常动词

# 混合风格词：本身合法（国漫半写实 / semi-realistic anime），判冲突前先剥离
HYBRID_STRIP_RE = re.compile(r"(半写实|半寫實|semi[- ]?realistic|semirealistic|semi realistic)", re.I)

# 冲突对: (名称, A 组, B 组, 提示)
CONFLICTS = [
    ("写实 vs 动漫",
     ["写实", "实拍", "photo", "photographic", "photorealistic", "realistic photo", "dslr"],
     ["动漫", "二次元", "赛璐璐", "anime", "cartoon", "chibi", "cel shading", "comic"],
     "同一画面不能同时走写实与动漫两套底层规则；只留一族（见 05 混合规则）"),
    ("白天 vs 夜晚",
     ["白天", "正午", "日光", "晴天", "daylight", "noon", "sunny", "blue sky", "bright sun"],
     ["夜晚", "夜景", "深夜", "午夜", "night", "midnight", "moonlight"],
     "时间矛盾会让模型随机选一个；统一时间，或改成明确时段（黄昏）"),
    ("逆光 vs 顺光",
     ["逆光", "backlit", "backlight", "rim light", "contre-jour"],
     ["顺光", "正面光", "front light", "flat lighting", "frontal light"],
     "光位互斥；保留一个主光，另一个改成补光"),
    ("广角 vs 长焦",
     ["广角", "wide-angle", "wide angle", "14mm", "16mm", "18mm", "24mm"],
     ["长焦", "telephoto", "135mm", "200mm", "300mm"],
     "焦段互斥会导致透视不可控；选一个（见 04 焦段表）"),
    ("微距 vs 大场景",
     ["微距", "macro", "大特写", "extreme close"],
     ["大远景", "鸟瞰", "extreme wide", "bird's eye", "birds eye", "aerial"],
     "景别跨度太大，模型会折中成模糊的中景"),
    ("极简 vs 繁复",
     ["极简", "minimal", "minimalist", "大量留白", "negative space"],
     ["繁复", "满版", "密集", "ornate", "baroque", "cluttered", "busy pattern"],
     "留白与满版互斥；'极简 + 元素很多' 必崩"),
    ("纯白底 vs 场景元素",
     ["纯白背景", "白色背景", "white background", "seamless white", "纯色背景"],
     ["树林", "街", "室内", "桌面场景", "forest", "street", "room", "landscape", "outdoor"],
     "电商白底要求无场景；要场景就换用途（场景图）"),
    ("3D vs 2D",
     ["3d 渲染", "3d render", "octane", "c4d", "blender", "cgi"],
     ["2d", "扁平", "flat design", "线描", "line art", "矢量", "vector"],
     "渲染介质互斥；参见 references/character/render-styles.md 的介质隔离思路"),
    ("无人 vs 有人",
     ["无人物", "无人", "no people", "empty room", "空旷无人"],
     ["一个男人", "一个女人", "人物", "人群", "person", "people", "girl", "boy", "man ", "woman "],
     "既要求无人又描述人；删掉人物描述或删掉'无人'"),
]

# 平台语法特性
NO_WEIGHT_PLATFORMS = {"mj", "flux", "nano_banana", "gpt_image", "seedream", "wanx", "ideogram"}
NO_AR_PLATFORMS = {"sd", "flux", "nano_banana", "gpt_image", "seedream", "wanx", "ideogram"}


# ---------------------------------------------------------------- 数据结构

@dataclass
class Issue:
    level: str          # P0 / P1 / P2
    kind: str           # 冲突 / 结构 / 语法 / 堆砌 / 动作 / 文字 / 长度
    msg: str
    hint: str = ""

    def as_dict(self) -> dict:
        return {"level": self.level, "kind": self.kind, "msg": self.msg, "hint": self.hint}


@dataclass
class Result:
    platform: str
    purpose: str
    length: int
    tier: str = "standard"
    issues: list[Issue] = field(default_factory=list)

    @property
    def score(self) -> int:
        p0 = sum(1 for i in self.issues if i.level == "P0")
        p1 = sum(1 for i in self.issues if i.level == "P1")
        p2 = sum(1 for i in self.issues if i.level == "P2")
        return max(0, 100 - 18 * p0 - 6 * p1 - 2 * p2)

    @property
    def counts(self) -> dict:
        return {lv: sum(1 for i in self.issues if i.level == lv) for lv in ("P0", "P1", "P2")}

    @property
    def verdict(self) -> str:
        s = self.score
        if s >= 90:
            return "可直接交付"
        if s >= 75:
            return "可交付，但请标注风险点"
        if s >= 60:
            return "先修 P0 再交付"
        return "建议重写（通常是结构问题，不是词的问题）"


# ---------------------------------------------------------------- 工具

def _ascii_word(k: str) -> bool:
    return all(ord(c) < 128 for c in k)


def find_terms(text: str, terms: list[str]) -> list[str]:
    low = text.lower()
    hits = []
    for t in terms:
        tl = t.lower()
        if _ascii_word(t):
            if re.search(r"(?<![a-z0-9])" + re.escape(tl) + r"(?![a-z0-9])", low):
                hits.append(t)
        else:
            if tl in low:
                hits.append(t)
    return hits


def has_any(text: str, groups: list[list[str]]) -> bool:
    return any(find_terms(text, g) for g in groups)


NEG_CUE = r"(?:无|没有|不含|不要|不出现|不添加|不写|不使用|禁止|避免|杜绝|no|without|avoid|not|free of)"
# 装饰/结构上下文：名词里含"雪/花/尘"等字但不构成特效（雪花扣、雪纹、花纹）
DECOR_SUFFIX = r"(?:纹|花纹|纹样|图案|扣|扣件|镶片|饰|饰片|刺绣|绣|贴花|纸|布|色)"


CLAUSE_SPLIT_RE = re.compile(r"[。；;，,\n]")


def strip_negated(text: str, terms: list[str], span: int = 4) -> str:
    """剔除否定式：按小句判断——一个小句里出现"无/不含/不出现/no"，该小句内所有目标词视为否定。

    比"否定词 + N 个字"的窗口式更稳：`不出现任何轮盘或法阵轮盘` 这种列举式也能整体剥掉。
    注意"、"不切分小句——`无文字、水印、logo` 里的三项应一起被否定。
    """
    parts = CLAUSE_SPLIT_RE.split(text)
    out = []
    for part in parts:
        if re.search(NEG_CUE, part, re.I):
            for t in terms:
                part = re.sub(re.escape(t), " ", part, flags=re.I)
        out.append(part)
    joined = "，".join(out)
    # 兜底：跨小句的"否定词 + 少量字 + 目标词"
    for t in terms:
        joined = re.sub(NEG_CUE + r"\s*[^。；;，,]{0," + str(span) + r"}" + re.escape(t),
                        " ", joined, flags=re.I)
    return joined


def find_affirmed(text: str, terms: list[str]) -> list[str]:
    """只返回被肯定表述命中的词（否定式、装饰后缀不算）。"""
    cleaned = strip_negated(text, terms)
    # 装饰上下文（雪花扣 / 雪纹 / 花纹）不算特效
    for t in terms:
        if len(t) <= 2:
            cleaned = re.sub(re.escape(t) + DECOR_SUFFIX, " ", cleaned)
    return find_terms(cleaned, terms)


# ---------------------------------------------------------------- 检查

def lint(text: str, platform: str = "unknown", purpose: str = "general",
         length: str = "standard", energy: str = "restrained") -> Result:
    text = (text or "").strip()
    res = Result(platform=platform, purpose=purpose, length=len(text), tier=length)

    if not text:
        res.issues.append(Issue("P0", "结构", "提示词为空", "至少给主体 + 场景 + 光"))
        return res

    low = text.lower()

    # 技术型图（分区/骨骼/灯光/正交）：目标是"能读"，不是"好看"，部分通用检查不适用
    tech_fig = bool(LIGHT_REF_RE.search(text) or MATZONE_RE.search(text)
                    or SKELETON_RE.search(text) or ORTHO_RE.search(text))

    # 3D 生成简报（text→3D / image→3D）：没有相机、没有画幅、没有打光，这三类结构检查不适用
    d3_brief = (purpose == "model3d")

    # 1) 结构缺格
    if not d3_brief:
        if not find_terms(text, LIGHT_WORDS) and not KELVIN_RE.search(text):
            res.issues.append(Issue("P1", "结构", "缺光段：没有光位/光质/色温",
                                    "补「光位 + 光质 + 光比 + 色温」，见 04 光位表"))
        elif not (
            LIGHT_DIR_RE.search(text)
            or find_terms(text, ["侧光", "逆光", "顶光", "顺光", "45", "90", "side light",
                                 "backlight", "rim light", "top light", "window light",
                                 "平光", "均匀光", "uniform light", "flat even", "even lighting"])
        ):
            res.issues.append(Issue("P2", "结构", "有光但无光位（只写了柔和/明亮）",
                                    "光位缺失 = 平光 = 廉价感；补『45° 侧光』这类方向词"))

    if not tech_fig and not d3_brief and not find_terms(text, CAMERA_WORDS) and not CAMERA_RE.search(text):
        res.issues.append(Issue("P1", "结构", "缺镜头段：没有景别/机位/焦段",
                                "补「景别 + 机位 + 焦段」，见 02 第 ⑦ 格"))

    if not tech_fig and not find_terms(text, STYLE_WORDS):
        res.issues.append(Issue("P1", "结构", "缺风格段：没有风格族/介质",
                                "至少给一个风格族词，见 05"))

    # 2) 画幅
    has_ratio = bool(RATIO_RE.search(text)) or bool(AR_PARAM_RE.search(text))
    if not has_ratio and not d3_brief:
        only_vertical = find_terms(text, ["竖版", "横版", "宽屏", "方形", "portrait orientation", "landscape orientation"])
        if only_vertical:
            res.issues.append(Issue("P0", "结构",
                                    f"画幅未量化：只写了『{only_vertical[0]}』",
                                    "改写成数字比例 3:4 / 16:9 / 1:1，模型不认形容词"))
        elif purpose in NEEDS_RATIO:
            res.issues.append(Issue("P0", "结构", f"缺画幅：用途为 {purpose} 但未给比例",
                                    "补比例（海报 3:4｜头图 2.35:1｜主图 1:1｜封面 9:16）"))
        else:
            res.issues.append(Issue("P1", "结构", "缺画幅比例", "补 3:4 / 16:9 等数字比例"))

    # 3) 语义冲突
    for name, a, b, hint in CONFLICTS:
        if name.startswith("逆光") and LIGHT_REF_RE.search(text):
            continue  # 灯光参考图本来就要求多光位并存（唯一例外）
        pair_text = HYBRID_STRIP_RE.sub(" ", text) if name.startswith("写实") else text
        hit_a, hit_b = find_affirmed(pair_text, a), find_affirmed(pair_text, b)
        if hit_a and hit_b:
            res.issues.append(Issue("P0", "冲突", f"{name}：『{hit_a[0]}』与『{hit_b[0]}』同时出现", hint))

    # 4) 平台语法
    if platform in NO_WEIGHT_PLATFORMS and WEIGHT_RE.search(text):
        res.issues.append(Issue("P0" if platform == "mj" else "P1", "语法",
                                f"{platform} 不吃权重括号 `(word:1.3)`",
                                "删括号；用词序前移来加权，或改用 SD"))
    if platform in NO_AR_PLATFORMS and AR_PARAM_RE.search(text):
        res.issues.append(Issue("P0", "语法", f"{platform} 不使用 --ar 参数",
                                "改成平台原生比例字段，或写进正文『3:4 竖版』"))
    if platform == "mj" and re.search(r"negative\s*prompt", low):
        res.issues.append(Issue("P0", "语法", "MJ 没有 negative prompt 字段",
                                "改用 `--no text, watermark`"))
    if platform == "sd" and not NEG_HEADER_RE.search(text) and len(text) > 60:
        res.issues.append(Issue("P1", "语法", "SD 未给反向字段",
                                "补独立 negative：text, watermark, deformed, blurry"))

    # 5) 质量词堆砌
    q = find_terms(text, QUALITY_WORDS)
    if len(q) >= 4:
        res.issues.append(Issue("P1", "堆砌",
                                f"画质词堆砌：{'/'.join(q[:6])} 共 {len(q)} 个",
                                "保留 ≤2 个；清晰度靠出图尺寸，不靠词（铁律 5）"))
    elif len(q) == 3:
        res.issues.append(Issue("P2", "堆砌", f"画质词偏多：{'/'.join(q)}", "保留 1–2 个即可"))

    # 6) 动作过量
    verbs = find_terms(text, CN_VERBS) + find_terms(text, EN_VERBS)
    if len(verbs) >= 3:
        res.issues.append(Issue("P1", "动作", f"动作过多：{len(verbs)} 个动词（{'、'.join(verbs[:6])}）",
                                "一张图只讲一个动作；其余拆图或改成状态描述（铁律 2）"))

    # 7) 空词（分两档：纯评价词 P1；"精致/大气"这类用户口语 P2，可要求结构化成词）
    hard_fillers = find_terms(text, FILLER_HARD)
    soft_fillers = find_terms(text, FILLER_SOFT)
    if hard_fillers:
        res.issues.append(Issue("P1", "结构", f"空词无法执行：{'、'.join(hard_fillers[:4])}",
                                "换成可测量词（低饱和/45° 侧逆光/85mm/f2.8），见 04 速查表"))
    if soft_fillers:
        res.issues.append(Issue("P2", "结构", f"口语评价词：{'、'.join(soft_fillers[:4])}",
                                "不是错，但模型不执行；可补一条结构描述（如『精致』→ 边缘干净、金属倒角 1mm）"))

    # 8) 文字期望（先剥离"禁止文字"句，再判断是否真要写字）
    stripped = text
    for fp in TEXT_FORBID_RES + TEXT_NEUTRAL_RES:
        stripped = re.sub(fp, " ", stripped, flags=re.I)
    forbids_text = stripped != text
    wants_text = any(re.search(wp, stripped, re.I) for wp in TEXT_WANT_RES)
    quotes = QUOTE_RE.findall(text)
    if wants_text and forbids_text:
        res.issues.append(Issue("P0", "文字", "既要求写文字又要求无文字",
                                "二选一：赌真文字（引号 + 层级）或转留白后期"))
    elif wants_text and not quotes:
        res.issues.append(Issue("P1", "文字", "提到文字但未用引号写出具体文案",
                                "文案逐字加引号 + 位置 + 层级 + 禁译，见 06"))
    if quotes and not SIZE_HIER_RE.search(text):
        res.issues.append(Issue("P2", "文字", "有文案但未给字号层级", "给主副标题比例（1 : 1/3）"))

    # 9) 多格图：封顶 + 标注层
    if MULTI_RE.search(text):
        if not CAP_RE.search(text):
            res.issues.append(Issue("P1", "多格", "多格图未封顶：只写了格数，没写『仅此 N 格』",
                                    "只写格数是下限不是上限，模型会补第 N+1 格（D41）"))
        if not LABEL_RE.search(text):
            res.issues.append(Issue("P1", "多格", "多格图未排除标注层：格号/箭头/图注会被画进图",
                                    "加『无格号、无箭头、无尺寸标注、无图注』（D43）"))

    # 9.5) 建模向多视图：四项工程条件
    if (MULTI_RE.search(text) and (find_terms(text, MODEL_RE) or ORTHO_RE.search(text))
            and purpose not in SHOWCASE_PURPOSES):
        if not ORTHO_RE.search(text):
            res.issues.append(Issue("P1", "建模", "多视图未写正交投影",
                                    "写 `orthographic projection + no perspective foreshortening + flat even lighting`"))
        if (not POSE_RE.search(text) and not SKELETON_RE.search(text)
                and not ACTION_FREEZE_RE.search(text)):
            res.issues.append(Issue("P1", "建模", "多视图未写 A-Pose / T-Pose",
                                    "只写『A-pose』不够：手臂外张 30° + 掌心朝内 + 五指分开 + 中性表情"))
        if not LANDMARK_RE.search(text):
            res.issues.append(Issue("P2", "建模", "多视图未写统一地标线",
                                    "加 `identical height, feet aligned to one baseline`"))
        if not NEUTRAL_RE.search(text) and not SKELETON_RE.search(text):
            res.issues.append(Issue("P2", "建模", "多视图未写中性表情/闭嘴",
                                    "表情 morph 与口型要从 neutral 起算，加 `neutral expression, mouth closed`"))

    # 9.6) 角色美学：形状语言 / 负空间 / 剪影
    if find_terms(text, CHAR_SUBJECT) and not tech_fig:
        if not find_terms(text, SHAPE_WORDS):
            res.issues.append(Issue("P2", "美学", "人物提示词未定形状语言（圆/方/三角）",
                                    "先定主形再写五官：形状定性格，五官只负责说清楚（见 aesthetics.md）"))
        if find_terms(text, FULLBODY) and not find_terms(text, NEGSPACE):
            res.issues.append(Issue("P2", "美学", "全身人物未写负空间",
                                    "加『肢体之间留出可见空隙，无相切轮廓』，否则手臂易粘躯干"))
        if (purpose == "asset" and purpose not in SHOWCASE_PURPOSES and find_terms(text, FULLBODY)
                and "剪影" not in text and "silhouette" not in text.lower()):
            res.issues.append(Issue("P2", "美学", "资产级全身图未提剪影可读性",
                                    "加 `readable silhouette`；剪影不过关的造型不适合作资产"))

    # 9.7) 灯光参考图：唯一允许"光不一致"的图型
    if LIGHT_REF_RE.search(text):
        if LIGHT_UNIFORM_RE.search(text) and not LIGHT_VARY_RE.search(text):
            res.issues.append(Issue("P1", "图型", "灯光参考图要求各格光位不同，却写了统一光照",
                                    "四格全写平光就成了一张图重复四次；保留姿态/背景/构图统一，逐格写明光位与光比"))

    # 9.8) 材质分区 / 配色图：要纯色分区，不要材质参数
    if MATZONE_RE.search(text):
        hit = find_terms(text, MAT_PARAM_WORDS)
        if hit:
            res.issues.append(Issue("P1", "图型", "材质分区图混入了材质参数（%s）" % "、".join(hit[:3]),
                                    "分区图要『每区单一平涂纯色、无渐变无纹理』；材质数值写进交付说明，不写进提示词"))

    # 9.9) 骨骼视图：AI 给的是关节位置参考，不是 rig
    if SKELETON_RE.search(text):
        hit = find_terms(text, RIG_WORDS)
        if hit or RIG_RE.search(text):
            res.issues.append(Issue("P1", "图型", "骨骼视图写了绑定/权重类术语",
                                    "AI 出不了 rig；只写关节球位置、骨段比例、脊柱曲线，绑定工作在 DCC 里做"))

    # 9.10) 换装图：必须锁死"除服装外全同"
    if OUTFIT_SWAP_RE.search(text) and not SAME_EXCEPT_RE.search(text):
        res.issues.append(Issue("P2", "图型", "换装图未锁死『除服装外全同』",
                                "加『同一姿态、同一角度、同一光照、发型妆容一致，只换衣服』，否则没法横向比较"))

    # 9.11) 低模：面数必须分区，且不许混高模细节
    if LOWPOLY_RE.search(text):
        if not FACET_BUDGET_RE.search(text):
            res.issues.append(Issue("P2", "低模", "低模未写面数分区（哪密哪疏）",
                                    "写『头与手面片细密、躯干与腿为大块平面』；密度均分是廉价感第一来源（见 low-poly.md）"))
        bad = find_terms(LOWPOLY_NEG_RE.sub(" ", text), LOWPOLY_BAD)
        if bad:
            res.issues.append(Issue("P1", "低模", f"低模混入了高模细节：{'、'.join(bad[:3])}",
                                    "低模没有贴图承载细节；改成大块平面 + 三色配色，反向加 pores, embroidery, lace"))

    # 9.12) text→3D：可绑骨条件与固定失败模式
    if T3D_RE.search(text) or purpose == "model3d":
        if not (RIGGABLE_RE.search(text) and LIMB_SEP_RE.search(text)):
            res.issues.append(Issue("P1", "3D生成", "3D 生成未写可绑骨条件（A-Pose + 四肢分离）",
                                    "写 `A-pose, arms 55° out, a clear band of background between arm and torso`，"
                                    "否则自动绑骨直接失败（见 text-to-3d.md）"))
        if not FLOAT_NEG_RE.search(text):
            res.issues.append(Issue("P2", "3D生成", "未排除悬空件/薄片/融合肢体",
                                    "加 `no floating parts, no thin sheets, no fused limbs`——3D 生成的三个固定失败模式"))

    # 9.13) 角色立绘：服装层数与配饰堆叠（立绘最容易堆过头，模型会照单全收）
    if find_terms(text, CHAR_SUBJECT) or find_terms(text, FULLBODY):
        layers = find_terms(text, CLOTH_LAYER_WORDS)
        if len(layers) >= 4:
            res.issues.append(Issue("P1", "服装", f"叠穿层数过多：{'、'.join(layers[:5])}",
                                    "立绘主件 ≤2 层 + 配饰 ≤3 件；层数越多越像一团布（见 outfit-design.md）"))
        acc = find_terms(text, ACCESSORY_WORDS)
        if len(acc) >= 5:
            res.issues.append(Issue("P1", "服装", f"配饰堆叠：{'、'.join(acc[:6])} 共 {len(acc)} 件",
                                    "挑 2–3 件留在剪影上，其余删掉或合成『同色系小饰』；配饰是剪影杀手"))
        elif len(acc) == 4:
            res.issues.append(Issue("P2", "服装", f"配饰 4 件：{'、'.join(acc)}", "建议收敛到 3 件以内"))
        cf = find_affirmed(text, VFX_CLOTH)
        if cf and not find_terms(text, CLOTH_ATTACH):
            res.issues.append(Issue("P2", "服装", f"服饰特效未写附着部位（{'、'.join(cf[:3])}）",
                                    "写清附在哪里：『光缕沿裙缘游走』『符文在袖口亮起』；不写位置会糊满全身"))

    # 9.14) 场景空泛（玄幻/仙侠最容易只给一句"云雾仙山"）
    if ((find_terms(text, CHAR_SUBJECT) or find_terms(text, FANTASY_WORDS))
            and find_terms(text, BACKDROP_WORDS) and not PLAIN_BG_RE.search(text)
            and not find_terms(text, SCENE_DEPTH)):
        res.issues.append(Issue("P2", "场景", "场景未分层（前 / 中 / 远景）",
                                "至少给两层：前景压角（云雾/碎石）+ 主景；只写『仙山背景』会被填成一张灰底"))

    # 9.14·五) 跨族题材混搭：必须声明主题材
    fam_hit = {}
    for fam, words in GENRE_FAMILIES.items():
        hit = [w for w in words if w in text]
        if hit:
            fam_hit[fam] = hit
    if len(fam_hit) >= 2 and not PRIMARY_GENRE_RE.search(text):
        detail = "；".join(f"{k}({'、'.join(v[:2])})" for k, v in fam_hit.items())
        res.issues.append(Issue("P2", "题材", f"跨题材混搭未声明主题材：{detail}",
                                "主题材定配色/材质/服装/场景，次题材只出现在指定局部（见 genre-atlas.md §四）"))

    # 9.15) 玄幻可数实体：数量必须封顶（九条龙写成"龙"会变一条，写"九条"又可能变十几条）
    # 单数（一枚/一个/单只）不需要封顶，只有 ≥2 才可能被加减
    ents = [e for e in COUNT_ENTITY_RE.findall(text) if e[0] not in ("一", "1", "单")]
    if ents and not COUNT_CAP_RE.search(text):
        sample = "、".join(f"{a}{b}{c}" for a, b, c in ents[:3])
        res.issues.append(Issue("P2", "数量", f"可数实体未封顶：{sample}",
                                "写『恰好 N 条/枚，不允许多出第 N+1 个』；模型对『九』这类数字极不稳定"))

    # 9.16) 方位：头顶光环 vs 身后轮盘（最易混，且用户否过一次就会反复长回来）
    halo_ok = bool(HALO_ABOVE_RE.search(strip_negated(text, ["轮盘", "法轮", "光轮", "圆盘"])))
    wheel_ok = bool(find_affirmed(text, ["轮盘", "法轮", "圆盘", "wheel", "disc"]))
    if halo_ok and wheel_ok:
        res.issues.append(Issue("P1", "方位", "头顶光环与身后轮盘同时被肯定描述",
                                "两者互斥：要么『头顶正上方的细环』，要么『身后的法轮』；"
                                "要否掉一个就写『身后不出现任何轮盘』（见 fantasy-elements.md §三）"))
    if halo_ok and HALO_SPOKE_RE.search(text) and not find_terms(text, ["无辐条", "不带辐条", "no spokes"]):
        res.issues.append(Issue("P2", "方位", "光环带辐条/纹饰：容易被画成法轮",
                                "纯光环写『无辐条、无纹饰、由光构成』；确要纹饰就说『纹饰环』并接受它像轮盘"))

    # 9.17) 服装锚点段：写了锚点就要可冻结（分层 + 配色 + 部件）
    if COSTUME_ANCHOR_RE.search(text):
        if not COSTUME_LAYER_RE.search(text):
            res.issues.append(Issue("P2", "服装", "服装锚点缺分层（内/中/外/配饰）",
                                    "没有分层的锚点冻结不住：模型会把『一套衣服』重画成另一套"))
        decl = "，".join(COLOR_DECL_RE.findall(text))
        colors = set(COLOR_NAME_RE.findall(decl or text))
        if len(colors) >= 4:
            res.issues.append(Issue("P2", "服装", f"服装配色超过三色：{'、'.join(list(colors)[:5])}",
                                    "主色 + 辅色 + 点缀色，三色封顶；第四色开始就没有主次"))
    # 多图/系列：写了服装但没锁"同一套服装"
    if MULTI_RE.search(text) and find_terms(text, CHAR_SUBJECT) and not LOCKED_OUTFIT_RE.search(text):
        cf_hit = find_affirmed(text, VFX_CLOTH + CLOTH_MAIN_WORDS)
        if cf_hit and not find_terms(text, ["换装", "多套服装", "outfit variant"]):
            res.issues.append(Issue("P2", "服装", "多视图未锁『同一套服装』",
                                    "普通多视图要锁服装、换装图才换服装：加『同一套服装，款式/配色/配饰完全一致』"))

    # 10) 参考图职责
    if REF_RE.search(text) and not REF_ROLE_RE.search(text):
        res.issues.append(Issue("P1", "参考图", "提到参考图但未声明职责",
                                "写清『只用来确定 X，衣服/背景完全不按这张图』（D44）"))

    # 11) 数量封顶
    if COUNT_RE.search(text) and not TOTAL_RE.search(text):
        res.issues.append(Issue("P2", "数量", "写了数量但未封顶",
                                "加『总数严格等于 N，不允许第 N+1 个、不允许分身』（D46）"))

    # 12) 通用美颜套话（会覆盖人物设定，优先级高于普通空词）
    cliche = find_terms(text, BEAUTY_CLICHE)
    if cliche:
        res.issues.append(Issue("P2", "套话",
                                f"通用美颜套话：{'、'.join(cliche[:4])}",
                                "套话会覆盖角色体态设定；但**用户显式点名时以用户为准**——"
                                "只需补一句结构描述（如『网红脸』→ 小V脸、直角鼻、宽双眼皮），不必删除"))

    # 13) 第三方专名（交付稿建议转译）
    auteur = find_terms(text, AUTEUR_WORDS)
    if auteur:
        res.issues.append(Issue("P2", "专名",
                                f"出现第三方作品/作者名：{'、'.join(auteur[:3])}",
                                "探索稿可留；交付稿应转译成参数（光比/焦段/颗粒/饱和度），见 11 §五"))

    # 13) 3D 动漫：路线与皮肤语义
    if ANIME3D_RE.search(text):
        if not ROUTE_RE.search(text):
            res.issues.append(Issue("P1", "3D动漫", "写了 3D 动漫但没点名哪条路线",
                                    "五条路线互斥（三渲二/国漫半写实/皮克斯/风格化手绘3D/全3D写实），"
                                    "用影子写法点名，见 references/character/anime-3d.md"))
        skin = find_terms(SKIN_NEG_RE.sub(" ", text), SKIN_REAL)
        if skin:
            res.issues.append(Issue("P1", "3D动漫", f"3D 动漫写了写实皮肤词：{'、'.join(skin[:3])}",
                                    "会往真人漂；改 smooth stylized skin, no pores，反向加 pores, photorealistic"))

    # 14) 特效层：层数、粒子密度、发光约束
    p_found = find_affirmed(text, VFX_PARTICLE)
    cloth_found = find_affirmed(text, VFX_CLOTH)
    cat_hits = [
        ("粒子", p_found),
        ("光效", find_terms(text, VFX_LIGHT)),
        ("能量", find_terms(text, VFX_ENERGY)),
        ("服饰特效", cloth_found),
    ]
    active = [(n, h) for n, h in cat_hits if h]
    max_cat = 4 if energy == "epic" else 3   # epic 档允许多一层（战斗 KV）
    if len(active) >= max_cat and not find_terms(text, VFX_HIER):
        names = "、".join(n for n, _ in active)
        res.issues.append(Issue("P1", "特效", f"特效类别过多：{names} 共 {len(active)} 类，未分主次",
                                "一层主特效 + 至多一层辅特效；三层以上必脏（见 references/character/vfx.md）"))
    if p_found and not find_terms(text, VFX_DENSITY):
        res.issues.append(Issue("P2", "特效", "写了粒子但没给密度/粒径",
                                "补『稀疏/中等/密集 + 细如尘/可见颗粒 + 方向 + 不遮挡面部』"))
    if find_terms(text, ["发光", "法术光", "剑光", "bloom", "glow"]) and not find_terms(text, HIGHLIGHT_OK):
        res.issues.append(Issue("P2", "特效", "有发光但未约束高光",
                                "加『高光保留细节，无纯白死白，辉光克制』，否则出白块"))

    # 粒子词**按词种**计数（同一词写两遍不是两个粒子；同字不同物更不该合并）
    n_kind = len(set(p_found))
    p1_at = 4 if energy == "epic" else 3
    if n_kind >= p1_at:
        res.issues.append(Issue("P1", "特效", f"粒子词种类 {n_kind} 种（{'、'.join(p_found[:4])}）：密度会叠加",
                                "只留一个粒子词 + sparse + 负向 dense particles, cluttered"))
    elif n_kind >= 2:
        res.issues.append(Issue("P2", "特效", f"粒子词 {n_kind} 种",
                                "克制档建议只留一个；epic 档可留两种主/辅，但要分层写清"))

    # 三约束：主光色 ≤2、介质 ≤2、粒子不遮脸
    light_clauses = [c for c in CLAUSE_SPLIT_RE.split(text) if ("光" in c or "light" in c.lower())]
    light_text = "，".join(light_clauses)
    light_colors = [c for c in LIGHT_COLOR_WORDS if c in light_text]
    if len(light_colors) >= 3 and not LIGHT_COLOR_OK_RE.search(text):
        res.issues.append(Issue("P2", "特效", f"主光色 {len(light_colors)} 种：{'、'.join(light_colors[:4])}",
                                "全场主光色限两种，第三色只做点缀，否则颜色发脏"))
    # 介质按"概念"去重：薄雾与雾是同一层，不能算两层
    media: list[str] = []
    for m in sorted(VFX_MEDIA_WORDS, key=len, reverse=True):
        if m in text and not any(m in f for f in media):
            media.append(m)
    if len(media) >= 3:
        res.issues.append(Issue("P2", "特效", f"介质 {len(media)} 层：{'、'.join(media[:4])}",
                                "介质 ≤2 层（烟/雾/尘/水汽/热浪），叠加会糊成一片"))
    if (p_found or media) and find_terms(text, ["面部", "脸部", "脸", "face"]) and not find_terms(text, FACE_CLEAR):
        res.issues.append(Issue("P2", "特效", "特效可能遮挡面部",
                                "加『粒子不遮挡面部、不在眼前堆积』，否则脸被吃掉"))

    # 动态模糊必须保主体清晰
    if find_terms(text, MOTION_BLUR) and not find_terms(text, SUBJECT_SHARP):
        res.issues.append(Issue("P1", "特效", "写了动态模糊但没保住主体清晰",
                                "改『background motion blur, subject in sharp focus』，否则主体一起糊"))

    # 特效要有环境交互（防"贴图感"）
    if find_terms(text, VFX_PARTICLE + VFX_ENERGY) and not find_terms(text, VFX_INTERACT):
        res.issues.append(Issue("P2", "特效", "特效缺环境交互",
                                "写『在轮廓光里发亮 / 被身体推开 / 压弯草丛 / 在皮肤上投细影』"))

    # 15) 长度（三档；轻微超出只提示，别为了过检删掉用户点名的设计细节）
    tier_idx = LENGTH_TIER_IDX.get(length, 1)
    limit = LENGTH_TIERS.get(platform, LENGTH_TIERS["unknown"])[tier_idx]
    if len(text) > limit:
        over = len(text) / limit
        lvl = "P1" if over > 1.5 else "P2"
        res.issues.append(Issue(lvl, "长度",
                                f"超出 {platform} {length} 档上限：{len(text)} > {limit}",
                                "换更长的一档交付（--length long），或先砍氛围句；"
                                "不要为了过检删用户点名的点缀细节"))

    # 10) 兜底提醒
    if not find_terms(text, ["不出现", "无文字", "无可读", "无任何", "no text", "no lettering",
                             "--no", "排除", "禁止", "无格号", "无标签"]):
        res.issues.append(Issue("P2", "结构", "未写任何排除/反向",
                                "至少排除：文字、水印、多余物体、变形"))

    # 排序：P0 → P1 → P2
    order = {"P0": 0, "P1": 1, "P2": 2}
    res.issues.sort(key=lambda i: order[i.level])
    return res


# ---------------------------------------------------------------- 输出

def render(res: Result, as_json: bool = False) -> str:
    if as_json:
        return json.dumps({
            "platform": res.platform,
            "purpose": res.purpose,
            "length": res.length,
            "tier": res.tier,
            "score": res.score,
            "verdict": res.verdict,
            "counts": res.counts,
            "issues": [i.as_dict() for i in res.issues],
        }, ensure_ascii=False, indent=2)

    c = res.counts
    lines = [
        "=== 提示词机检 ===",
        f"平台：{res.platform} ｜ 用途：{res.purpose} ｜ 长度：{res.length} 字（{res.tier} 档）",
        f"得分：{res.score} / 100   [P0×{c['P0']} P1×{c['P1']} P2×{c['P2']}]   判定：{res.verdict}",
        "",
    ]
    if not res.issues:
        lines.append("未发现问题。仍建议按 10-eval.md 的 30 项人工过一遍。")
    for i in res.issues:
        lines.append(f"[{i.level}] {i.kind}：{i.msg}")
        if i.hint:
            lines.append(f"        → {i.hint}")
    if c["P0"]:
        lines += ["", "⚠ P0 未清零不许交付；修完请重跑一次。"]
    lines += ["", "（启发式检查，命中后请人工复核）"]
    return "\n".join(lines)


# ---------------------------------------------------------------- 自测

SELF_TESTS = [
    {
        "name": "好词：产品摄影（应高分）",
        "text": ("商业产品摄影，一只磨砂琥珀玻璃精华瓶，立在浅米色洞石台面上，瓶身凝结细密水珠，"
                 "背景为暖灰墙面，极简风格，左侧 45° 大面积柔光加右侧轮廓光，光比 1:3，5600K，"
                 "85mm 镜头 f/5.6，略俯 15°，主体占画面 55%，右下留负空间，低饱和暖中性。"
                 "画面中不出现任何文字与标志。3:4"),
        "platform": "mj", "purpose": "poster", "expect_max_p0": 0,
    },
    {
        "name": "坏词：串味 + 堆砌 + 空词",
        "text": ("超写实摄影，一个唯美的动漫少女，8k, ultra detailed, masterpiece, best quality, hdr，"
                 "白天夜景都有，逆光正面光，高级感大气"),
        "platform": "mj", "purpose": "poster", "expect_min_p0": 2,
    },
    {
        "name": "语法：MJ 喂权重括号",
        "text": ("editorial photo of (a ceramic cup:1.3) on oak table, window light from left, "
                 "85mm f/2.8, 3:4 --ar 3:4"),
        "platform": "mj", "purpose": "general", "expect_code": "语法",
    },
    {
        "name": "语法：SD 喂 --ar",
        "text": ("product photo, ceramic cup, oak table, softbox left 45deg, 85mm, f/5.6, --ar 3:4"),
        "platform": "sd", "purpose": "general", "expect_code": "语法",
    },
    {
        "name": "文字：提文案没引号",
        "text": ("3:4 海报，秋日市集主视觉，暖黄串灯，45° 侧逆光，85mm，标题写秋日市集四个大字"),
        "platform": "seedream", "purpose": "poster", "expect_code": "文字",
    },
    {
        "name": "画幅：只写竖版",
        "text": ("竖版海报，咖啡杯，侧光，85mm 特写，写实摄影，暖调"),
        "platform": "seedream", "purpose": "poster", "expect_code": "结构",
    },
    {
        "name": "多格：未封顶 + 未排除标注",
        "text": ("画面为 4 格并排，每格一个全身视图，27 岁成年女性 6.5 头身，"
                 "左侧 45° 侧光，光比 1:4，5600K，85mm，写实摄影，3:4"),
        "platform": "nano_banana", "purpose": "asset", "expect_code": "多格",
    },
    {
        "name": "参考图：未声明职责",
        "text": ("参考图 1 是角色定版，请按它生成一张 3:4 海报，85mm 侧光，写实摄影，不出现文字"),
        "platform": "seedream", "purpose": "poster", "expect_code": "参考图",
    },
    {
        "name": "套话：九头身 + 网红脸",
        "text": ("3:4 人像，九头身，网红脸，顶级美女，85mm，45° 侧光，光比 1:3，写实摄影，无文字"),
        "platform": "sd", "purpose": "portrait", "expect_code": "套话",
    },
    {
        "name": "3D动漫：只写 3D 没写路线",
        "text": ("3D 动漫人物，少女，7 头身，站在窗前，85mm，侧光，3:4，无文字"),
        "platform": "seedream", "purpose": "portrait", "expect_code": "3D动漫",
    },
    {
        "name": "特效：多层叠加未分主次",
        "text": ("3:4 人物全身，7 头身，45° 侧光，85mm，写实摄影。"
                 "粒子：火星飞散；体积光；气浪扩散；衣摆上扬；剑光发光，高光有细节。"),
        "platform": "seedream", "purpose": "asset", "expect_code": "特效",
    },
    {
        "name": "建模：多视图缺正交与姿态",
        "text": ("角色建模参考图，四视图并排，正面、侧面、背面、3/4侧，仅此 4 格，"
                 "画面内无格号、无箭头、无图注。7 头身，85mm，侧光，3:4"),
        "platform": "seedream", "purpose": "asset", "expect_code": "建模",
    },
    {
        "name": "美学：人物无形状语言与负空间",
        "text": ("3:4 全身立绘，少女，鹅蛋脸，柳叶眉，凤眼，85mm，45° 侧光，写实摄影，无文字"),
        "platform": "seedream", "purpose": "portrait", "expect_code": "美学",
    },
    {
        "name": "图型：灯光参考图写了统一平光",
        "text": ("16:9 灯光参考图，4 格横排，仅此 4 格。同一角色正面半身，"
                 "四格统一平光，光比 1:3，浅灰背景。无格号、无箭头、无文字"),
        "platform": "seedream", "purpose": "asset", "expect_code": "图型",
    },
    {
        "name": "图型：材质分区图混入材质参数",
        "text": ("1:1 材质分区图，同一角色正面，纯色分区标记：上身深墨绿、下身浅灰。"
                 "外套 roughness 0.7、金属件 metalness 1.0。orthographic，纯白背景。无文字"),
        "platform": "seedream", "purpose": "asset", "expect_code": "图型",
    },
    {
        "name": "图型：骨骼视图写了绑定权重",
        "text": ("16:9 骨骼视图，三格横排，正面侧面背面。半透明皮肤叠加骨骼，"
                 "标注骨骼层级与控制器，权重按 1.0 分配。orthographic，平光。无文字"),
        "platform": "seedream", "purpose": "asset", "expect_code": "图型",
    },
    {
        "name": "图型：换装图未锁死变量",
        "text": ("16:9 换装图，2 行 3 列共 6 格，仅此 6 格。角色展示六套服装："
                 "便服、正装、居家、运动、礼服、战斗装。浅灰背景，无格号、无文字"),
        "platform": "seedream", "purpose": "asset", "expect_code": "图型",
    },
    {
        "name": "低模：未分面数 + 混高模细节",
        "text": ("低模风格角色，low poly，全身立绘，三色配色，外套有刺绣细节与蕾丝镂空，"
                 "单一硬光从左上方，3:4，无文字"),
        "platform": "seedream", "purpose": "portrait", "expect_code": "低模",
    },
    {
        "name": "3D生成：缺四肢分离",
        "text": ("生成3D模型，风格化机械师，game asset，宽肩窄腰，帆布外套，"
                 "哑光金属护腕，无场景，无文字，无底座"),
        "platform": "unknown", "purpose": "model3d", "expect_code": "3D生成",
    },
    {
        "name": "多格：中文数字封顶应被识别",
        "text": ("三视图设定稿，三个全身立绘并排，仅此三格，不增加任何额外画格，"
                 "无格号、无箭头、无图注。画幅比例 3:4。左上45度柔光，平视机位，全身景别，中长焦，写实摄影。"),
        "platform": "seedream", "purpose": "turnaround", "expect_no_code": "多格",
    },
    {
        "name": "特效：雪花扣/雪花纹不算粒子",
        "text": ("三视图设定稿。仅此3格，无格号。画幅比例 3:4。左上45度柔光，平视机位，全身景别，写实风格。"
                 "裙面绣雪花纹，鞋头是六瓣雪花扣的水晶鞋。"),
        "platform": "seedream", "purpose": "turnaround", "expect_no_code": "特效",
    },
    {
        "name": "服装：三层叠穿 + 五件配饰",
        "text": ("3:4 全身立绘，少女，法袍，外罩纱袖，腰封，披帛，内衬层。"
                 "肩饰、腰饰、腕饰、流苏、银链俱全。左上45度柔光，85mm f/2，写实摄影，无文字。"),
        "platform": "seedream", "purpose": "portrait", "expect_code": "服装",
    },
    {
        "name": "图型：展示型设定稿不套建模五项",
        "text": ("三视图设定稿，三个全身立绘并排，仅此三格，无格号无箭头。orthographic，画幅比例 3:4。"
                 "左上45度柔光，平视机位，全身景别，写实摄影。"),
        "platform": "seedream", "purpose": "turnaround", "expect_no_code": "建模",
    },
    {
        "name": "冲突：否定式'无广角畸变'不算广角",
        "text": "3:4 全身，少女，写实摄影，左上45度柔光，眼平机位，中长焦85mm。无广角畸变，无文字。",
        "platform": "seedream", "purpose": "portrait", "expect_no_code": "冲突",
    },
    {
        "name": "玄幻：九条龙未封顶",
        "text": ("3:4 玄幻女帝，九条冰龙环绕，长剑，头饰三枚冰晶。"
                 "左上45度侧逆光，85mm，3D 国漫半写实，无文字。"),
        "platform": "seedream", "purpose": "portrait", "expect_code": "数量",
    },
    {
        "name": "玄幻：九条龙已封顶应放过",
        "text": ("3:4 玄幻女帝，恰好九条冰龙环绕，不允许多出第十条。"
                 "左上45度侧逆光，85mm，3D 国漫半写实，无文字。"),
        "platform": "seedream", "purpose": "portrait", "expect_no_code": "数量",
    },
    {
        "name": "方位：头顶光环与身后轮盘同时肯定",
        "text": ("3:4 玄幻女帝，头顶正上方一枚双层光环，身后一轮巨大法轮缓缓转动。"
                 "左上45度侧逆光，85mm，3D 国漫半写实，无文字。"),
        "platform": "seedream", "purpose": "portrait", "expect_code": "方位",
    },
    {
        "name": "方位：否掉轮盘后不报冲突",
        "text": ("3:4 玄幻女帝，头顶正上方一枚双层纯光环，由光构成、无辐条；"
                 "身后不出现任何轮盘。左上45度侧逆光，85mm，3D 国漫半写实，无文字。"),
        "platform": "seedream", "purpose": "portrait", "expect_no_code": "方位",
    },
    {
        "name": "特效：epic 档三种粒子不报 P1",
        "text": ("3:4 战斗 KV，主特效为冰晶尘与碎晶自脚下升腾，辅特效为余烬飘落，"
                 "分层写清主辅；三层特效；面部不遮挡。"
                 "右后侧逆光，光比 1:5，85mm，3D 国漫半写实，无文字。"),
        "platform": "seedream", "purpose": "portrait", "energy": "epic",
        "expect_no_p1_code": "特效",
    },
    {
        "name": "服装：锚点段缺分层",
        "text": ("3:4 全身立绘，少女。【服装锚点】深蓝短外套、黑色高腰短裤。"
                 "左上45度柔光，85mm，写实摄影，无文字。"),
        "platform": "seedream", "purpose": "portrait", "expect_code": "服装",
    },
    {
        "name": "题材：仙侠 + 赛博未声明主次",
        "text": ("3:4 全身，仙侠女修，义体左臂，赛博霓虹。"
                 "左上45度柔光，85mm，3D 国漫半写实，无文字。"),
        "platform": "seedream", "purpose": "portrait", "expect_code": "题材",
    },
    {
        "name": "题材：声明主题材后应放过",
        "text": ("3:4 全身，主题材为仙侠，次题材赛博仅左臂义体。"
                 "左上45度柔光，85mm，3D 国漫半写实，无文字。"),
        "platform": "seedream", "purpose": "portrait", "expect_no_code": "题材",
    },
]


def self_test() -> int:
    failed = 0
    for case in SELF_TESTS:
        r = lint(case["text"], case["platform"], case["purpose"],
                 case.get("length", "standard"), case.get("energy", "restrained"))
        p0 = r.counts["P0"]
        ok = True
        if "expect_max_p0" in case and p0 > case["expect_max_p0"]:
            ok = False
        if "expect_min_p0" in case and p0 < case["expect_min_p0"]:
            ok = False
        if "expect_code" in case and not any(i.kind == case["expect_code"] for i in r.issues):
            ok = False
        if "expect_no_code" in case and any(i.kind == case["expect_no_code"] for i in r.issues):
            ok = False
        if "expect_no_p1_code" in case and any(
                i.kind == case["expect_no_p1_code"] and i.level == "P1" for i in r.issues):
            ok = False
        flag = "PASS" if ok else "FAIL"
        if not ok:
            failed += 1
        print(f"[{flag}] {case['name']}  score={r.score} P0={p0} P1={r.counts['P1']}")
        if not ok:
            for i in r.issues:
                print(f"        {i.level} {i.kind}: {i.msg}")
    print("")
    print(f"自测：{len(SELF_TESTS) - failed}/{len(SELF_TESTS)} 通过")
    return 0 if failed == 0 else 1


# ---------------------------------------------------------------- CLI

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="画面提示词机检")
    p.add_argument("--text", help="提示词文本")
    p.add_argument("--file", help="从文件读取提示词")
    p.add_argument("--platform", default="unknown", choices=PLATFORMS)
    p.add_argument("--purpose", default="general", choices=PURPOSES)
    p.add_argument("--length", default="standard", choices=["short", "standard", "long"],
                   help="长度档位：short 标签派 / standard 默认 / long 长中文描述")
    p.add_argument("--energy", default="restrained", choices=["restrained", "epic"],
                   help="特效强度档：restrained 立绘/写真（默认）/ epic 战斗 KV 允许多一层")
    p.add_argument("--stdin", action="store_true",
                   help="从管道读入提示词（需显式开启；无参数时不再自动读 stdin，避免卡住）")
    p.add_argument("--json", action="store_true", help="输出 JSON")
    p.add_argument("--self-test", action="store_true", help="运行内置自测")
    args = p.parse_args(argv)

    if args.self_test:
        return self_test()

    text = args.text
    if args.file and args.file != "-":
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                text = f.read()
        except OSError as e:
            print(f"读取文件失败：{e}", file=sys.stderr)
            return 2
    # 只在显式要求时读 stdin（默认不读，避免无参调用挂住）
    if not text and (args.stdin or args.file == "-"):
        try:
            text = sys.stdin.read()
        except Exception:
            text = ""
    if not text:
        p.print_help()
        print("\n提示：长中文提示词建议用 --file 读文件，避免命令行转义；管道输入请加 --stdin。")
        return 2

    res = lint(text, args.platform, args.purpose, args.length, args.energy)
    print(render(res, as_json=args.json))
    return 0 if res.counts["P0"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

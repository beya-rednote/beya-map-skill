# Beya Three-Map Travel Skill

一个用于 Codex 的 Beya 风格旅行地图三图组 Skill。

输入一个国家和一个具体区域/城市，就生成三张统一风格的地图：

1. `世界地图 - 国家名`: 该国家在世界上的位置，目标国家高亮。
2. `国家名旅行区域地图`: 该国家的官方/常用旅行区域划分。
3. `区域或城市名旅行地图`: 某个区域或城市的具体旅行地图。

示例：

```text
用 $beya-world-map 做一套印度尼西亚三张旅行地图，第三张画巴厘岛。
```

## 固定风格

- 横版 4:3 为主
- 米白纸底
- 蓝色水彩海洋
- 浅黄绿色陆地
- 重点国家/区域/城市使用亮黄色高亮
- 使用 Beya 插画 Skill 的风格一：Quiet Geometry Poster
- 手写中文标签，少量英文辅助
- 信息清楚、留白充足、低饱和、高级手账感
- 避开 GIS、教材地图、几何贴纸、厚边框和 UI 卡片感

每一张图底部都必须有：

- 地图名字
- 一个小牙齿 logo
- `by beya`

## 安装

下载这个仓库后，把 `beya-world-map` 文件夹复制到你的 Codex skills 目录：

```text
~/.codex/skills/beya-world-map
```

最终结构应该是：

```text
~/.codex/skills/beya-world-map/
├── SKILL.md
├── agents/openai.yaml
├── references/world-highlight-style.md
└── scripts/build_map_set_prompts.py
```

然后重新打开 Codex 或开启一个新对话。

## 使用

```text
$beya-world-map 印度尼西亚 -- 第三张画巴厘岛
$beya-world-map 泰国 -- 第三张画曼谷
$beya-world-map 日本 -- 第三张画东京
```

也可以让 Codex 先生成三张图的标准提示词：

```bash
python3 beya-world-map/scripts/build_map_set_prompts.py 印度尼西亚 --area 巴厘岛
python3 beya-world-map/scripts/build_map_set_prompts.py Thailand --zh-country 泰国 --area 曼谷
```

## 文件

- `beya-world-map/SKILL.md`: Skill 主说明
- `beya-world-map/references/world-highlight-style.md`: 固定视觉风格和三图规则
- `beya-world-map/scripts/build_map_set_prompts.py`: 三张图提示词生成脚本

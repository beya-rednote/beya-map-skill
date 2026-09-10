# Beya World Map Skill

一个用于 Codex 的 Beya 风格世界地图 Skill。

输入国家名，就生成固定风格的水彩手绘世界地图：

```text
用 $beya-world-map 画 世界地图 - 泰国
```

它会保持统一模板，只变化：

- 标题里的国家名，例如 `世界地图 - 泰国`
- 被黄色高亮的国家
- 指向该国家的小黄标签

## 风格

- 横版 4:3
- 米白纸底
- 蓝色水彩海洋
- 浅黄绿色陆地
- 目标国家亮黄色高亮
- Beya 手写中文风格
- 标注七大洲、四大洋、少量大国名
- 避开 GIS、教材地图、几何贴纸、厚边框和 UI 卡片感

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
└── scripts/build_world_map_prompt.py
```

然后重新打开 Codex 或开启一个新对话。

## 使用

```text
$beya-world-map 世界地图 - 日本
$beya-world-map 世界地图 - 泰国
$beya-world-map 世界地图 - 法国
```

也可以让 Codex 先生成标准提示词：

```bash
python3 beya-world-map/scripts/build_world_map_prompt.py 泰国
python3 beya-world-map/scripts/build_world_map_prompt.py Thailand --zh-name 泰国
```

## 文件

- `beya-world-map/SKILL.md`: Skill 主说明
- `beya-world-map/references/world-highlight-style.md`: 固定视觉风格
- `beya-world-map/scripts/build_world_map_prompt.py`: 国家高亮世界地图提示词生成脚本

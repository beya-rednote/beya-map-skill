---
name: beya-world-map
description: Generate a fixed Beya-style watercolor world map with one highlighted country. Use when the user asks for "世界地图 - [国家]", "world map - [country]", a country-highlight world map, or a reusable Beya world map template where only the title country and yellow highlighted country change while layout, colors, labels, and handwriting style remain consistent.
---

# Beya World Map

## Purpose

Use this skill for one repeatable artifact: a landscape 4:3 Beya-style watercolor world map titled `世界地图 - {国家名}`, with exactly one country highlighted in warm yellow.

## Inputs

- Required: target country name in Chinese or English.
- Optional: output language for labels. Default to Chinese.
- Optional: extra countries to label. Default to the fixed major-country set.

If the country name is ambiguous, ask one short clarifying question. Otherwise infer the common sovereign country name and continue.

## Fixed Output Rules

- Canvas: landscape 4:3.
- Title: `世界地图 - {中文国家名}` centered at the top.
- Background: warm cream paper.
- Ocean: soft irregular watercolor blue wash, no hard rectangular panel.
- Other land: pale yellow-green watercolor fill.
- Target country: warm bright yellow watercolor highlight.
- Borders/coastlines: thin, soft, hand-traced feeling.
- Labels: original Beya handwritten Chinese style; loose, clear, light, not mechanical.
- Continents to label: 北美洲, 南美洲, 欧洲, 非洲, 亚洲, 大洋洲, 南极洲.
- Oceans to label: 太平洋, 大西洋, 印度洋, 北冰洋.
- Major countries to label by default: 加拿大, 美国, 巴西, 俄罗斯, 中国, 印度, 日本, 韩国, 澳大利亚. Add nearby context labels only if they help identify the highlighted country.
- Add one small yellow callout label pointing to the highlighted country, text exactly `{中文国家名}`.
- Signature: optional small `by beya` in the lower right.

## Workflow

1. Normalize the requested country to a Chinese display name and English geographic name.
2. Read `references/world-highlight-style.md`.
3. Generate the map as a bitmap illustration, not a programmatic GIS-looking map, unless the user explicitly asks for SVG/vector.
4. Use `scripts/build_world_map_prompt.py` to produce the final prompt when helpful:

```bash
python3 scripts/build_world_map_prompt.py 泰国
python3 scripts/build_world_map_prompt.py Thailand --zh-name 泰国
```

5. Use the generated prompt with image generation.
6. Check the result before delivering:
   - The target country is visibly yellow.
   - Other land is green and ocean is blue.
   - The title uses the requested country.
   - All seven continents and four oceans are labeled.
   - The image feels like watercolor travel notebook art, not GIS, atlas, infographic, or vector clipart.

## Do Not

- Do not redraw the world as crude polygon blobs.
- Do not use strong grids, thick black borders, UI cards, rounded map panels, heavy white text halos, or classroom atlas styling.
- Do not change the template style between countries.
- Do not overcrowd the map with too many labels.

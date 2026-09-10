---
name: beya-world-map
description: "Generate a fixed three-image Beya travel map set for one country: (1) world location map highlighting the country, (2) official/national travel-region map for that country, and (3) detailed travel map for one selected region or city. Use when the user asks for a Beya map set, three travel maps, world map plus country region map plus city/area travel map, or a reusable template where style stays consistent and only country/region/city content changes."
---

# Beya World Map Set

## Purpose

Use this skill for one repeatable three-image map set. For each destination country, create:

1. `世界地图 - {国家名}`: show where the country is in the world and highlight the whole country in yellow.
2. `{国家名}旅行区域地图`: show the country divided into official, government, tourism-board, or widely accepted national travel regions.
3. `{区域/城市名}旅行地图`: show a detailed travel map for one selected region or city inside that country.

Keep visual style consistent across all three images. Only change the destination facts, title, highlighted area, labels, and local travel details.

## Required Inputs

- Required: country name.
- Required for image 3: target region or city. If missing, ask which specific region/city to use for the third map.
- Optional: language. Default to Chinese labels, with English names only when helpful.
- Optional: official source preference for travel-region divisions.

If the user asks for only one or two of the three maps, produce only the requested subset while preserving the same style system.

## Shared Visual Rules

Follow `references/world-highlight-style.md` for the locked Beya style. Use Beya illustration skill Style 1 as the design base:

- Quiet Geometry Poster mood: clean editorial layout, restrained composition, premium muted colors, paper texture, simplified but recognizable forms, and lots of breathing room.
- Combine Style 1 with the supplied map demos: cream paper, watercolor or dry-pigment wash, soft blue water, pale yellow-green land, thin hand-traced borders, handwritten Chinese labels, and one clear warm-yellow focus.
- Do not imitate a named artist. Build an original Beya hand-drawn map language.

Every image must include a footer mark at the bottom:

- Map name, for example `世界地图 - 印度尼西亚`.
- A small tooth logo mark beside or near the map name.
- `by beya` as a small handwritten signature.

The footer should be subtle, clean, and consistent across the three images.

## Image 1: World Location Map

- Canvas: landscape 4:3.
- Title: `世界地图 - {国家名}` centered at the top.
- Background: warm cream paper.
- Ocean: soft irregular watercolor blue wash, no hard rectangular panel.
- Other land: pale yellow-green watercolor fill.
- Target country: warm bright yellow highlight.
- Add one small yellow callout label pointing to the target country, text exactly `{国家名}`.
- Label continents: 北美洲, 南美洲, 欧洲, 非洲, 亚洲, 大洋洲, 南极洲.
- Label oceans: 太平洋, 大西洋, 印度洋, 北冰洋.
- Label sparse major countries only: 加拿大, 美国, 巴西, 俄罗斯, 中国, 印度, 日本, 韩国, 澳大利亚. Add nearby context countries only if they help identify the highlighted country.

## Image 2: Country Travel Region Map

- Canvas: landscape 4:3 unless the user asks otherwise.
- Title: `{国家名}旅行区域地图`.
- Use the country's official, government tourism, or widely accepted travel-region divisions. If uncertain or time-sensitive, verify before finalizing.
- Keep the full country shape geographically recognizable.
- Divide regions with distinct low-saturation colors from the Beya palette.
- Use numbered rounded callout labels for each region when there are many regions.
- Add concise notes only when useful: landscape type, culture cue, gateway city, or travel planning role.
- Keep the design closer to a travel planning map than a government administrative map.

## Image 3: Region Or City Travel Map

- Canvas: choose landscape 4:3 by default, or portrait 3:4 if the city/route shape fits better.
- Title: `{区域/城市名}旅行地图`.
- Show practical travel geography: districts, coastline, main roads or route arrows, airports/stations/ports, key attractions, food/market areas, viewpoints, beaches, temples, museums, and day-trip clusters.
- Use a small set of hand-drawn icons only when they help scan the map.
- Keep labels sparse and readable. Do not turn the map into a dense guidebook page unless the user asks for a detailed poster.
- Highlight the selected region/city core in warm yellow or a stronger accent, while nearby context stays pale.

## Workflow

1. Normalize the country, region, and city names into Chinese display names and English geographic names.
2. For image 2, determine the authoritative or accepted travel-region divisions. Use official tourism/government sources when possible.
3. Read `references/world-highlight-style.md`.
4. Use `scripts/build_map_set_prompts.py` to draft the three image prompts when helpful:

```bash
python3 scripts/build_map_set_prompts.py 印度尼西亚 --area 巴厘岛
python3 scripts/build_map_set_prompts.py Thailand --zh-country 泰国 --area 曼谷
```

5. Generate the images as bitmap illustrations, not programmatic GIS-looking maps, unless the user explicitly asks for SVG/vector.
6. Check each image:
   - Correct title.
   - Correct yellow highlight.
   - Required map facts included.
   - Bottom footer includes map name, tooth logo, and `by beya`.
   - Style matches the same Beya paper/watercolor/Style 1 visual system across all three images.

## Do Not

- Do not produce only the world map when the user asked for the full three-image set.
- Do not make crude polygon continent blobs, classroom atlas maps, GIS dashboards, UI-card layouts, thick grids, or flat vector clipart.
- Do not overcrowd labels.
- Do not invent official travel-region divisions. If uncertain, verify or state that the region grouping is a practical travel grouping rather than official.

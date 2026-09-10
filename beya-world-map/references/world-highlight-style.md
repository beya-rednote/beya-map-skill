# Beya Three-Map Travel Style

## Locked Visual Direction

The output must resemble a soft Beya travel-notebook map series, using the Beya illustration skill's Style 1 as the base:

- Cream textured paper background.
- Quiet Geometry Poster restraint: clean editorial composition, simplified recognizable forms, muted premium palette, large breathable space.
- Soft blue watercolor or dry-pigment wash for ocean/water.
- Pale yellow-green land with subtle paper-print variation.
- Warm bright yellow for the main highlighted country/region/city.
- Thin olive-gray hand-traced coastlines, borders, roads, and callout lines.
- Sparse handwritten Chinese labels, airy spacing, light and human.
- Consistent footer on every image: map name + small tooth logo + `by beya`.

The style should feel like the user's demo maps: clear travel information on handmade paper, not a technical atlas.

## Locked Palette

- Paper: warm cream, around `#F7F0DD`.
- Ocean/water: soft watercolor blue, around `#9DDBEB`.
- Ocean text: deeper blue, around `#2F66B3`.
- Other land: pale yellow-green, around `#D4E57A`.
- Highlight: warm yellow, around `#F5D32E`.
- Ink: deep green-black, around `#1C362B`.
- Border line: muted olive green, thin and semi-transparent.
- Secondary region colors for image 2: muted teal, sage green, soft blue, lavender, terracotta, dusty pink, soft yellow.

Avoid saturated poster colors, neon yellow, glossy gradients, heavy black outlines, and flat vector fills.

## Typography

Use original Beya handwriting:

- Chinese title: loose, elegant, hand-written, dark green-black, not bold UI text.
- Map labels: lighter handwritten Chinese, readable but not typeset.
- Ocean labels: blue handwritten Chinese.
- Country/region/city labels: small handwritten Chinese.
- English place names: optional, smaller, compact, only when useful.

If an image model struggles with exact Chinese text, regenerate or simplify labels rather than accepting chaotic text.

## Footer Mark

Every generated image must include a bottom footer mark:

- Map name in handwritten Chinese.
- A small tooth logo mark. Make it a simple hand-drawn tooth outline, cream/white fill, thin dark green-black line, tiny enough to be a brand mark rather than decoration.
- `by beya` in a small handwritten signature style.

Place the footer along the bottom edge with comfortable margin. It must not compete with the map.

## Image-Specific Guidance

### 1. World Location Map

Show the whole world. Highlight the target country in yellow. Keep continents, oceans, and sparse large-country labels readable.

### 2. Country Travel Region Map

Show the target country at larger scale. Divide it into official, government tourism, or widely accepted travel regions. Use distinct low-saturation colors, numbered callouts if useful, and short travel-planning notes.

### 3. Region Or City Travel Map

Show the selected region/city at practical travel scale. Include key landmarks, transport points, attraction clusters, routes, coastline/water, district names, and a few hand-drawn icons. Keep it useful but airy.

## Prompt Template: Full Three-Image Set

Replace bracketed values:

```text
Create a consistent three-image Beya travel map set for [ZH_COUNTRY] / [EN_COUNTRY], in the same visual style across all images. Use Beya illustration Style 1 Quiet Geometry Poster as the base: cream textured paper, refined muted palette, handmade dry-pigment/watercolor texture, simplified but recognizable map forms, thin olive-gray hand-traced lines, airy editorial spacing, original loose Chinese handwritten labels, not a technical atlas and not flat vector clipart.

Image 1 title: “世界地图 - [ZH_COUNTRY]”. Landscape 4:3 world location map. Soft irregular blue watercolor ocean wash, pale yellow-green land, highlight the entire [EN_COUNTRY] territory in warm bright yellow. Label seven continents in Chinese: 北美洲, 南美洲, 欧洲, 非洲, 亚洲, 大洋洲, 南极洲. Label four oceans in blue Chinese handwriting: 太平洋, 大西洋, 印度洋, 北冰洋. Add sparse major country names in Chinese: 加拿大, 美国, 巴西, 俄罗斯, 中国, 印度, 日本, 韩国, 澳大利亚. Add a small yellow callout label pointing to [EN_COUNTRY] reading “[ZH_COUNTRY]”.

Image 2 title: “[ZH_COUNTRY]旅行区域地图”. Landscape 4:3 country travel-region map. Show [EN_COUNTRY] at country scale and divide it into official/government tourism or widely accepted travel regions. Use low-saturation region colors, handwritten region labels, optional numbered callouts, and concise travel-planning notes. Keep the country shape recognizable and useful for trip planning.

Image 3 title: “[ZH_AREA]旅行地图”. Travel map for [ZH_AREA] / [EN_AREA] inside [ZH_COUNTRY]. Show practical travel geography: districts or area clusters, coast/water if relevant, main routes, transport gateways, key attractions, viewpoints, food/market areas, and a few simple hand-drawn icons. Highlight the selected area/core in warm yellow and keep nearby context pale.

Each image must include a subtle bottom footer: the map name, a small hand-drawn tooth logo, and “by beya”. Keep all text readable, sparse, and handwritten. No heavy grid, no rounded map panel, no thick black outlines, no GIS look, no classroom atlas look, no infographic cards, no geometric sticker blobs, no imitation of any specific artist.
```

## Quality Bar

Reject and retry when:

- The output is not three images or does not clearly separate the three map purposes.
- A title is missing or uses the wrong country/area.
- The wrong country/region/city is highlighted yellow.
- The second map invents official travel regions without verification.
- The third map lacks practical travel detail.
- Any image misses the footer map name, tooth logo, or `by beya`.
- The style becomes a GIS map, classroom atlas, vector infographic, or crude polygon diagram.

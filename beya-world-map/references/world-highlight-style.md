# World Highlight Style

## Locked Visual Direction

The output must resemble a soft watercolor hand-drawn travel notebook world map:

- Cream textured paper background.
- Soft blue watercolor ocean wash with irregular feathered edges.
- Pale yellow-green continents with subtle watercolor variation.
- Thin olive-gray coastlines and country borders.
- One target country highlighted in warm bright yellow.
- Sparse Chinese handwriting labels, airy spacing, light and human.
- Title centered above the map: `世界地图 - {国家名}`.

This skill is a fixed template. Across maps, keep composition, palette, label set, and visual language consistent. Only change the title country, highlighted country, and callout location.

## Locked Palette

- Paper: warm cream, around `#F7F0DD`.
- Ocean: soft watercolor blue, around `#9DDBEB`, with slightly deeper blue labels.
- Other land: pale yellow-green, around `#D4E57A`.
- Target country: warm yellow, around `#F5D32E`.
- Ink: deep green-black, around `#1C362B`.
- Border line: muted olive green, thin and semi-transparent.

Avoid saturated poster colors, flat vector fills, neon yellow, and heavy black outlines.

## Typography

Use original Beya handwriting:

- Chinese title: loose, elegant, hand-written, dark green-black, not bold UI text.
- Map labels: lighter handwritten Chinese, readable but not typeset.
- Ocean labels: blue handwritten Chinese.
- Country labels: small handwritten Chinese.

If the image model struggles with text, still request correct text explicitly and regenerate rather than accepting missing continent/ocean labels.

## Prompt Template

Use this exact structure and replace bracketed values:

```text
A polished original Beya-style hand-drawn watercolor world map, landscape 4:3. Cream textured paper background, soft irregular blue watercolor ocean wash with feathered edges, pale yellow-green land masses with geographically recognizable world outlines, delicate thin hand-traced coastlines and country borders. Title centered at the top in original loose Chinese handwritten lettering: “世界地图 - [ZH_COUNTRY]”. Highlight the entire [EN_COUNTRY] territory in warm bright yellow watercolor while all other land remains pale yellow-green and oceans remain soft blue. Add one small yellow callout label pointing to [EN_COUNTRY] reading “[ZH_COUNTRY]”. Label all seven continents in Chinese handwriting: 北美洲, 南美洲, 欧洲, 非洲, 亚洲, 大洋洲, 南极洲. Label the four oceans in blue Chinese handwriting: 太平洋, 大西洋, 印度洋, 北冰洋. Add sparse larger country names in Chinese handwriting: 加拿大, 美国, 巴西, 俄罗斯, 中国, 印度, 日本, 韩国, 澳大利亚. Clean airy travel-notebook composition, refined watercolor texture, gentle hand-drawn map style, readable labels, no heavy grid, no rounded map panel, no thick black outlines, no GIS look, no classroom atlas look, no infographic cards, no geometric sticker blobs, not imitating any specific artist.
```

## Quality Bar

Reject and retry when:

- The country is not highlighted yellow.
- The wrong country is highlighted.
- The title is missing or uses the wrong country.
- The map becomes a flat vector atlas.
- Continents or oceans are missing.
- Text is chaotic or illegible enough to defeat the purpose.

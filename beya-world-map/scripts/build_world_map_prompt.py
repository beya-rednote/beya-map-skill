#!/usr/bin/env python3
from __future__ import annotations

import argparse


ALIASES = {
    "中国": ("中国", "China"),
    "日本": ("日本", "Japan"),
    "韩国": ("韩国", "South Korea"),
    "泰国": ("泰国", "Thailand"),
    "印度尼西亚": ("印度尼西亚", "Indonesia"),
    "印尼": ("印度尼西亚", "Indonesia"),
    "美国": ("美国", "United States"),
    "加拿大": ("加拿大", "Canada"),
    "巴西": ("巴西", "Brazil"),
    "俄罗斯": ("俄罗斯", "Russia"),
    "印度": ("印度", "India"),
    "澳大利亚": ("澳大利亚", "Australia"),
    "新西兰": ("新西兰", "New Zealand"),
    "马来西亚": ("马来西亚", "Malaysia"),
    "新加坡": ("新加坡", "Singapore"),
    "越南": ("越南", "Vietnam"),
    "菲律宾": ("菲律宾", "Philippines"),
    "英国": ("英国", "United Kingdom"),
    "法国": ("法国", "France"),
    "德国": ("德国", "Germany"),
    "意大利": ("意大利", "Italy"),
    "西班牙": ("西班牙", "Spain"),
    "埃及": ("埃及", "Egypt"),
    "南非": ("南非", "South Africa"),
}


def normalize(country: str, zh_name: str | None, en_name: str | None) -> tuple[str, str]:
    if zh_name and en_name:
        return zh_name, en_name
    if country in ALIASES:
        zh, en = ALIASES[country]
        return zh_name or zh, en_name or en
    return zh_name or country, en_name or country


def build_prompt(zh: str, en: str) -> str:
    return (
        "A polished original Beya-style hand-drawn watercolor world map, landscape 4:3. "
        "Cream textured paper background, soft irregular blue watercolor ocean wash with feathered edges, "
        "pale yellow-green land masses with geographically recognizable world outlines, delicate thin hand-traced "
        "coastlines and country borders. "
        f"Title centered at the top in original loose Chinese handwritten lettering: “世界地图 - {zh}”. "
        f"Highlight the entire {en} territory in warm bright yellow watercolor while all other land remains "
        "pale yellow-green and oceans remain soft blue. "
        f"Add one small yellow callout label pointing to {en} reading “{zh}”. "
        "Label all seven continents in Chinese handwriting: 北美洲, 南美洲, 欧洲, 非洲, 亚洲, 大洋洲, 南极洲. "
        "Label the four oceans in blue Chinese handwriting: 太平洋, 大西洋, 印度洋, 北冰洋. "
        "Add sparse larger country names in Chinese handwriting: 加拿大, 美国, 巴西, 俄罗斯, 中国, 印度, 日本, 韩国, 澳大利亚. "
        "Clean airy travel-notebook composition, refined watercolor texture, gentle hand-drawn map style, readable labels, "
        "no heavy grid, no rounded map panel, no thick black outlines, no GIS look, no classroom atlas look, "
        "no infographic cards, no geometric sticker blobs, not imitating any specific artist."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a Beya world-map country-highlight image prompt.")
    parser.add_argument("country")
    parser.add_argument("--zh-name")
    parser.add_argument("--en-name")
    args = parser.parse_args()
    zh, en = normalize(args.country, args.zh_name, args.en_name)
    print(build_prompt(zh, en))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

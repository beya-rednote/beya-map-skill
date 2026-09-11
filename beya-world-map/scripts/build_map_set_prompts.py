#!/usr/bin/env python3
from __future__ import annotations

import argparse


ALIASES = {
    "中国": ("中国", "China"),
    "日本": ("日本", "Japan"),
    "韩国": ("韩国", "South Korea"),
    "泰国": ("泰国", "Thailand"),
    "印度尼西亚": ("印度尼西亚", "Indonesia"),
    "印尼": ("印尼", "Indonesia"),
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


AREA_ALIASES = {
    "科莫多": ("科莫多", "Komodo"),
    "科莫多岛": ("科莫多", "Komodo"),
    "巴厘岛": ("巴厘岛", "Bali"),
    "雅加达": ("雅加达", "Jakarta"),
    "曼谷": ("曼谷", "Bangkok"),
    "东京": ("东京", "Tokyo"),
    "首尔": ("首尔", "Seoul"),
}


DEFAULT_REGION_COUNTS = {
    "印度尼西亚": "7",
    "印尼": "7",
}


def normalize(value: str, zh: str | None, en: str | None, aliases: dict[str, tuple[str, str]]) -> tuple[str, str]:
    if zh and en:
        return zh, en
    if value in aliases:
        default_zh, default_en = aliases[value]
        return zh or default_zh, en or default_en
    return zh or value, en or value


def shared_style() -> str:
    return (
        "Use Beya illustration Style 1 Quiet Geometry Poster as the base: cream textured paper, "
        "refined muted palette, handmade dry-pigment/watercolor texture, simplified but recognizable map forms, "
        "thin olive-gray hand-traced lines, airy editorial spacing, original loose Chinese handwritten labels, "
        "not a technical atlas and not flat vector clipart. Every image must include a subtle bottom footer: "
        "the map name, a small hand-drawn tooth logo, and “by beya”."
    )


def resolve_region_count(country_input: str, country_zh: str, region_count: str | None) -> str:
    if region_count:
        return region_count
    return DEFAULT_REGION_COUNTS.get(country_input) or DEFAULT_REGION_COUNTS.get(country_zh) or "[REGION_COUNT]"


def build_prompts(country_zh: str, country_en: str, area_zh: str, area_en: str, region_count: str) -> str:
    style = shared_style()
    title_1 = f"{country_zh} - 世界地图"
    title_2 = f"{country_zh} - {region_count}大旅行区域地图"
    title_3 = f"{country_zh} - {area_zh}旅行地图"
    return f"""# Beya three-map set prompts

## Image 1

Create image 1 of a consistent three-image Beya travel map set for {country_zh} / {country_en}. {style}

Title: “{title_1}”. Portrait 3:4 world location map. Soft irregular blue watercolor ocean wash, pale yellow-green land, highlight the entire {country_en} territory in warm bright yellow. Label seven continents in Chinese: 北美洲, 南美洲, 欧洲, 非洲, 亚洲, 大洋洲, 南极洲. Label four oceans in blue Chinese handwriting: 太平洋, 大西洋, 印度洋, 北冰洋. Add sparse major country names in Chinese: 加拿大, 美国, 巴西, 俄罗斯, 中国, 印度, 日本, 韩国, 澳大利亚. Add a small yellow callout label pointing to {country_en} reading “{country_zh}”. Bottom footer must include: “{title_1}”, small tooth logo, “by beya”.

## Image 2

Create image 2 of the same Beya travel map set for {country_zh} / {country_en}. {style}

Title: “{title_2}”. Portrait 3:4 country travel-region map. Show {country_en} at country scale and divide it into {region_count} official/government tourism or widely accepted travel regions. Use low-saturation region colors, handwritten region labels, numbered callouts, and concise travel-planning notes. Add a clean bottom detail strip or region cards when space allows, in the same handmade paper style. Keep the country shape recognizable and useful for trip planning. Bottom footer must include: “{title_2}”, small tooth logo, “by beya”.

## Image 3

Create image 3 of the same Beya travel map set for {country_zh} / {country_en}. {style}

Title: “{title_3}”. Portrait 3:4 travel map for {area_zh} / {area_en} inside {country_zh}. Show practical travel geography: districts or area clusters, coast/water if relevant, main routes or dotted route arrows, transport gateways, key attractions, viewpoints, food/market areas, and a few simple hand-drawn icons. If it is an itinerary map, add compact day/detail cards at the bottom in the same handmade paper style. Highlight the selected area/core in warm yellow and keep nearby context pale. Bottom footer must include: “{title_3}”, small tooth logo, “by beya”.

Global negatives for all three: no heavy grid, no rounded map panel, no thick black outlines, no GIS look, no classroom atlas look, no infographic cards, no geometric sticker blobs, no imitation of any specific artist.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Build prompts for a three-image Beya travel map set.")
    parser.add_argument("country")
    parser.add_argument("--area", required=True, help="Region or city for image 3")
    parser.add_argument("--zh-country")
    parser.add_argument("--en-country")
    parser.add_argument("--zh-area")
    parser.add_argument("--en-area")
    parser.add_argument("--region-count", help="Number for the country travel-region title, e.g. 7")
    args = parser.parse_args()

    country_zh, country_en = normalize(args.country, args.zh_country, args.en_country, ALIASES)
    area_zh, area_en = normalize(args.area, args.zh_area, args.en_area, AREA_ALIASES)
    region_count = resolve_region_count(args.country, country_zh, args.region_count)
    print(build_prompts(country_zh, country_en, area_zh, area_en, region_count))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

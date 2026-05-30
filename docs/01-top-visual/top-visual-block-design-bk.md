# Top Visual Block Design

Source: [Top/Profile design image](assets/top-section-design.png) and [wireframe image](../framework.png)

This document defines the top `profile block` in the wireframe. It is the first Top/Profile area visitors see on the public page.

## Goal

The Top/Profile block is the first impression of the site. It should immediately communicate:

- This is the Top/Profile area for 結萌ひまり.
- The site is a fan archive with memorial and preservation intent, while also functioning as a dashboard for the VTuber's activity record.
- The statistics should quickly show the shape of the VTuber's streaming and video activity.

## Wireframe Reference

In `docs/framework.png`, this block corresponds to the upper yellow `profile block`.

Main elements:

```text
profile block
|-- left: full-body main visual
|-- top/right: slanted name banner
|-- right: profile text area
`-- lower center: icons / channel links / expression variations
```

## Layout

Desktop layout:

- Use a two-column hero composition.
- Place the character main visual on the left.
- Place the profile panel on the right, including name, short profile copy, and links.
- Allow the name banner to overlap the upper area, echoing the slanted orange title shape in the wireframe.
- Place statistics below the profile content while keeping them visually connected to the Top/Profile block.

Mobile layout:

- Stack content vertically.
- Show the name and profile summary before longer statistics.
- Keep the main visual visible in the first viewport without pushing all text below the fold.
- Let statistics become a compact two-column or single-column grid.

## Required Content

| Content | Purpose | Source |
| --- | --- | --- |
| Name | Clearly identify the page subject | Static profile text |
| Main visual | Create the first visual anchor | `src/assets/profile/hero.png` or replacement asset |
| Short profile copy | Explain the archive purpose | Static profile text |
| X link | Link to the external identity source | Static URL |
| YouTube link | Link to the external channel | Static URL |
| Total videos | Show archive scale | `videos.length` |
| Playlist count | Show archive structure | Derived from `playlist` |
| Members-only count | Signal archive completeness | `isMembersOnly` or current transitional member field |
| Active period | Provide historical context | Derived from min/max `date` or static graduation data |

## Profile 靜態資料

Profile 文字與連結不應該 hardcode 在 `TopPage` 內。

檔案：

```text
src/data/profile.ts
```

規則：

- `name` 是橘色 banner 中的顯示名稱。
- `description` 是名稱 banner 下方的主要 profile 文案。
- `links` 用來驅動圓形 X/YT icons。
- `lastUpdated` 顯示在 top visual 區塊的右下角。
- `graduationDate` 可用於 active-period 顯示或未來的 profile 詳細資料。

## 隨機表情選擇

Top visual 區塊應顯示三張表情圖片。

行為：

- 每次進入或載入頁面時，從 `src/assets/profile/expressions/` 隨機選出三張不重複的圖片。
- 在同一次 render session 中保持選出的三張圖片穩定。
- 不要在每次 component re-render 時重新洗牌。
- 隨機選擇不需要在瀏覽器重新整理後持續保留。

[表情圖片資料夾](../../src/assets/profile/expressions/)

```text
src/assets/profile/expressions/
```

## Current Implementation Mapping

Current component:

- `src/components/TopPage/index.tsx`

## Visual Direction

Use the palette from [`../00-overview/product-design.md`](../00-overview/product-design.md):

| Role | Color |
| --- | --- |
| Main accent | `#E87FAB` |
| Soft background | `#FFEEF5` |
| Secondary pink | `#F9C8DC` |
| Main text | `#3D2B3D` |
| Muted text | `#7A5C7A` |
| Secondary accent | `#9B6FC8` |

Style notes:

- Keep the block warm, profile-like, and commemorative.
- Use the main visual as a strong first-viewport signal.
- Use small icon-style buttons for external links where possible.

## Interaction

Primary interactions:

- X link opens `https://x.com/RAG_Himari`.
- YouTube link opens `https://www.youtube.com/@raghimari`.

次要互動項目：

- 吸引觀眾回來：
  - 貓貓點擊器
    - 點擊貓貓會觸發計數器
    - 計數器是全網共通
      - Todo: 要怎麼在github page上實現共通計數？
    - Todo: 計數器的名子？
  - 表情解鎖器
    - 把表情分作N、R、SR、SSR等級，作為出現機率
    - Todo: 要怎麼讓使用者知道已經解鎖過哪些表情
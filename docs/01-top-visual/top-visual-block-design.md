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
|-- lower center: icons / channel links / expression variations
`-- lower stats: total videos, playlists, active period
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

## Acceptance Checklist

### Identity

- [ ] The Top/Profile block is rendered before the video/archive list section.
- [ ] The visible display name text is exactly `結萌ひまり`.

### Required Content

- [ ] A main visual image is rendered from `src/assets/profile/hero.png` or the configured replacement asset.
- [ ] The X link is visible.
- [ ] The YouTube link is visible.
- [ ] The total video count is displayed.
- [ ] The displayed total video count equals `videos.length`.
- [ ] The playlist count is displayed.
- [ ] The displayed playlist count equals the number of unique normalized playlist values.
- [ ] The members-only count is displayed.
- [ ] The displayed members-only count equals the number of videos where `isMembersOnly` or the transitional member field is true.
- [ ] The active period is displayed.
- [ ] The displayed active period is derived from min/max `date` or the configured graduation date.

### Statistics

- [ ] Each statistic has a visible label.
- [ ] Each statistic has a visible value.
- [ ] Statistics do not appear above the display name.
- [ ] Statistics do not visually dominate the main visual at desktop width `1280px`.

### Visual Direction

- [ ] The Top/Profile block uses `#E87FAB` for the main accent or name-banner accent.
- [ ] The Top/Profile block uses `#FFEEF5` as a soft background or background tint.
- [ ] Body/profile text uses `#3D2B3D` or another approved main text color from `product-design.md`.
- [ ] Secondary/supporting text uses `#7A5C7A` or another approved muted text color from `product-design.md`.

### Interaction

- [ ] Clicking the X link opens `https://x.com/RAG_Himari`.
- [ ] Clicking the YouTube link opens `https://www.youtube.com/@raghimari`.
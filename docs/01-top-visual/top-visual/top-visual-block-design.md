# Top Visual Block Design

Source: [Notion design document](https://www.notion.so/React-35254a9cebff81df8fc7c1fc381d26b4) and [wireframe image](../framework.png)

This document defines the top block in the wireframe: the first visual/profile area of the public page.

## Goal

The top block is the first impression of the site. It should immediately communicate:

- This is a 結萌ひまり archive/profile page.
- The site is a memorial/archive-style fan project, not a generic video dashboard.
- Visitors can continue into video archive, tags, and related links.
- The profile and stats are trustworthy because they are based on the curated `videos.json` dataset.

## Wireframe Reference

In `docs/framework.png`, this is the upper yellow `profile block`.

Main elements:

```text
profile block
├── left: full-body main visual
├── top/right: slanted name banner
├── right: profile text area
├── lower center: icons / channel links / expression variations
└── lower stats: total videos, playlists, active period
```

## Layout

Desktop layout:

- Use a two-column hero composition.
- Left side: main visual of the character.
- Right side: profile panel with name, short copy, and links.
- Name banner may overlap the upper area to echo the wireframe's slanted orange title shape.
- Stats sit below the profile content, visually connected to the top block.

Mobile layout:

- Stack content vertically.
- Name and profile summary appear before long stats.
- Main visual remains visible in the first viewport, but should not push all text below the fold.
- Stats can become a compact two-column or single-column grid.

## Required Content

| Content | Purpose | Source |
| --- | --- | --- |
| Name | Clear subject identity | Static profile text |
| Main visual | First visual anchor | `src/assets/profile/hero.png` or replacement asset |
| Short profile copy | Explain the archive purpose | Static profile text |
| X link | External identity link | Static URL |
| YouTube link | External channel link | Static URL |
| Total videos | Archive scale | `videos.length` |
| Playlist count | Archive structure | Derived from `playlist` |
| Members-only count | Data completeness signal | `isMembersOnly` or current transitional member field |
| Active period | Historical context | Derived from min/max `date` or static graduation data |

## Current Implementation Mapping

Current component:

- `src/components/TopPage/index.tsx`

Current data:

- Receives `videos: Video[]`.
- Computes total video count from `videos.length`.
- Computes members count from `video.isMembers || video.isMembersOnly`.
- Computes total hours from `duration`.
- Uses `src/assets/profile/hero.png` as the main visual.

Gaps from this design:

- Text is currently affected by mojibake and must be repaired before final polish.
- Playlist count is not shown in the top block yet.
- Active period is not shown yet.
- The current layout is a general hero, not yet the wireframe-specific composition with a slanted name banner.
- Icons/channel links are limited to X and YouTube.

## Visual Direction

Use the palette from `../../00-overview/product-design.md`:

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
- Avoid making the first view look like an admin dashboard.
- Use the main visual as a strong first-viewport signal.
- Stats should support the profile, not dominate it.
- Use small icon-style buttons for external links where possible.

## Interaction

Primary interactions:

- X link opens `https://x.com/RAG_Himari`.
- YouTube link opens `https://www.youtube.com/@raghimari`.
- Optional future links: lit.link, Twitch, sub X account, recreated pages.

Secondary navigation:

- A CTA can scroll to `#videos`.
- A CTA can scroll to `#tag-searcher`.

Accessibility:

- Main visual image needs meaningful alt text.
- External links must use `target="_blank"` and `rel="noreferrer"`.
- Stats should use semantic labels, for example `dl`, `dt`, and `dd`.
- Text must remain readable on mobile and desktop.

## Data Rules

Derived values should be computed from `videos` when possible.

Recommended helpers:

- `videoCount`: `videos.length`
- `playlistCount`: unique playlist names after normalizing `string | string[]`
- `membersOnlyCount`: count of videos where `isMembersOnly` is true; during migration also accept `isMembers`
- `activePeriod`: earliest date to graduation date, or earliest to latest video date
- `totalHours`: sum of non-null `duration`, rounded for display

Avoid hardcoding derived stats unless the data source is intentionally frozen for a release.

## Implementation Checklist

- Repair mojibake in TopPage visible strings.
- Confirm the final display name text.
- Add playlist count to the stats area.
- Add active period or graduation date.
- Decide whether total hours stays in the top block or moves to analytics.
- Add visual treatment for the name banner.
- Check responsive layout at desktop and mobile widths.
- Confirm image framing of `src/assets/profile/hero.png`.
- Verify build with `npm run build`.

# Profile Block Design

Source: [Profile design image](assets/profile-section-design.png) and [wireframe image](../framework.png)

This document defines the `Profile` block in the wireframe. It is the first Profile area visitors see on the public page.

## Goal

The Profile block is the first impression of the site. It should immediately communicate:

- This is the Profile area for 結萌ひまり.
- The site is a fan archive with memorial and preservation intent, while also functioning as a dashboard for the VTuber's activity record.
- The statistics should quickly show the shape of the VTuber's streaming and video activity.

## Wireframe Reference

In `docs/framework.png`, this block corresponds to the upper yellow `Profile` block.

Main elements:

```text
Profile block
|-- left: full-body main visual
|-- right:
  |-- slanted name banner
  |-- profile text area
  |-- active period
  |-- x/Youtube Link
  |-- expression images
  `-- statistics
```

## Layout

Desktop layout:

- Use a two-column first-view composition.
- Place the character main visual on the left.
- Place the profile panel on the right, including name, short profile text, and links.
- The right-column content order follows the structure shown in the Wireframe Reference.
- Allow the name banner to overlap the upper area, echoing the slanted orange title shape in the wireframe.

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
| X link | Link to the official external identity source | Static URL |
| YouTube link | Link to the official external channel | Static URL |
| Total videos | Show archive scale | `videos.length` |
| Members-only count | Signal archive completeness | `isMembersOnly` or current transitional member field |
| Total hours | Show archive volume | Sum of `duration`, rounded to hours |
| Active period | Provide historical context | Derived from min/max `date` or static graduation data |

## Profile Static Data

Profile text and links should not be hardcoded in `TopPage`.

File:

```text
src/data/profile.json
```

Rules:

- `name` is the display name in the orange banner.
- `description` is the main profile copy under the name banner.
- `links` drive the official X / YT icons.
- `links` only include official SNS entry points for Profile. Do not put `Recreated Pages` content here.
- `debutDate` may be used later as the start date for the active period.
- `graduationDate` can be used for active-period display.

## Boundary of Profile Links in Profile block

- Profile links are the official links shown in the Profile block.
- They help visitors to make a quick jump to official SNS page.
- The function of these links / pages is different from links / pages in `Recreated Pages` block.

## Other Static Data

File:

```text
src/data/site.json
```

Rules:

- `lastUpdated` is shown at the lower-right side of the Profile block.

## Random Expression Selection

The Profile block should show three expression images.

Behavior:

- On each page entry or page load, randomly pick three different images from `src/assets/profile/expressions/`.
- Keep the three selected images stable during the same render session.
- Do not shuffle again on every component re-render.
- The random choice does not need to persist after a browser refresh.

[Expression image folder](../../src/assets/profile/expressions/)

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
- These links should not be reused as Recreated Pages items.

## Future Ideas

- Bring visitors back:
  - Cat clicker
    - Clicking the cat starts a counter.
    - The counter is shared by all visitors.
      - Todo: Decide how to make a shared counter on GitHub Pages.
    - Todo: Decide the counter name.
  - Expression unlocker
    - Group expressions by N, R, SR, and SSR levels, and use them as appearance rates.
    - Todo: Decide how to show users which expressions they have unlocked.

## Checklist

[Checklist](./profile-checklist.md)

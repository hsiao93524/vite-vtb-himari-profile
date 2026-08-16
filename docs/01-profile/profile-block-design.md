# Profile Block Design

Source: [Profile design image](assets/profile-section-design.png) and [wireframe image](../framework.png)

This document defines the `Profile` block in the wireframe. It is the first Profile area visitors see on the public page.

## Scope

This block covers the first-view identity area for 結萌ひまり.

This block includes:

- Character main visual and expression images.
- Display name and short profile copy.
- Current official X and YouTube links.
- Activity period.
- High-level archive statistics for videos, members-only videos, and total hours.
- `lastUpdated` display from shared site metadata.

This block does not include:

- Video search, video filters, table/gallery views, or detailed video metadata.
- X / Twitter tag search entry points.
- Fanart gallery or fanart collection behavior.
- Recreated Pages, historical links, Litlink, Twitch, old X accounts, or sub-account history.
- Future interactive ideas such as counters or expression unlock systems, unless they become part of the current implementation scope.

Profile links should stay limited to the current official X account and YouTube channel. Historical or preserved links belong to `Recreated Pages`.

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

### Desktop layout or Behavior

- Use a two-column first-view composition.
- Place the character main visual on the left.
- Place the profile panel on the right, including name, short profile text, and links.
- The right-column content order follows the structure shown in the Wireframe Reference.
- Allow the name banner to overlap the upper area, echoing the slanted orange title shape in the wireframe.

### Mobile layout or Behavior

- Stack content vertically.
- Show the name and profile summary before longer statistics.
- Keep the main visual visible in the first viewport without pushing all text below the fold.
- Let statistics become a compact two-column or single-column grid.

## Required Content

| Content | Purpose | Source |
| --- | --- | --- |
| Name | Clearly identify the page subject | Static profile text |
| Main visual | Show the character as the first visual signal | `src/assets/profile/hero.png` or replacement asset; `hero` means the character image asset |
| Short profile copy | Explain the archive purpose | Static profile text |
| X link | Link to the official external identity source | Static URL |
| YouTube link | Link to the official external channel | Static URL |
| Total videos | Show archive scale | `videos.length` |
| Members-only count | Signal archive completeness | `isMembersOnly` or current transitional member field |
| Total hours | Show archive volume | Sum of `duration`, rounded to hours |
| Active period | Provide historical context | Derived from min/max `date` or static graduation data |

## Details

### Naming Boundary

- `Profile` is the block name and section name.
- `profile` is the block-level section id, page anchor, and publication section identity.
- `hero` only means the character main visual asset, such as `src/assets/profile/hero.png` or a local `heroImage` variable.
- Do not use `hero` to name the whole Profile block, its section id, or its publication section id.

### Profile Text And Links

The Profile block shows the display name, short profile copy, and current official links.

- The display name appears in the name banner.
- The profile copy appears below the name banner.
- Official X and YouTube links appear near the expression images.
- These links are only current official Profile links.
- Historical or preserved links belong to `Recreated Pages`.

Data shape is defined in [Profile Data Design](./profile-data-design.md).

### Last Updated Display

The Profile block shows the shared site data snapshot date as supporting text.

- The text appears near the lower-right side of the Profile block.
- The text should stay secondary and should not compete with the name, main visual, or statistics.

The value comes from shared site metadata. Profile only defines how this text is displayed.

### Expression Image Behavior

The Profile block shows three expression images.

- Pick three different expression images on page load.
- Keep the selected images stable during the same render session.
- Do not shuffle again on every component re-render.
- The random choice does not need to persist after a browser refresh.

Asset folder and implementation details are defined in [Profile Data Design](./profile-data-design.md).

### Visual Direction

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

These ideas are not part of the current implementation scope.

- Cat clicker
  - Clicking the cat starts a counter.
  - The counter is shared by all visitors.
  - Research needed: Decide how to make a shared counter on GitHub Pages.
  - Research needed: Decide the counter name.
- Expression unlocker
  - Group expressions by N, R, SR, and SSR levels, and use them as appearance rates.
  - Research needed: Decide how to show users which expressions they have unlocked.

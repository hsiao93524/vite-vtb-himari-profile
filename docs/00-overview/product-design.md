# Product Design

Source: [Notion design document](https://www.notion.so/React-35254a9cebff81df8fc7c1fc381d26b4)

This document is the repository-side product design reference for the React web version. Use the Notion page as the working draft, and keep this file aligned with implementation decisions that affect the codebase.

## Document Role

This file answers three questions:

1. What kind of site is this project building?
2. Which page blocks and user interactions are in scope?
3. Which decisions are already fixed, and which specifications still need design detail?

Related detailed documents:

- [Data Model](data-model.md): `videos.json` schema and data migration rules.
- [Data Flow](data-flow.md): current React data flow and hook/component boundaries.
- [Roadmap](roadmap.md): implementation phases and release readiness.
- [Top Visual Block Design](../01-top-visual/top-visual-block-design.md): detailed Top/Profile UI design.
- [Top Visual Data Design](../01-top-visual/top-visual-data-design.md): Top/Profile data requirements.

## Project Summary

Build a one-page React site for the VTuber archive/profile of 結萌ひまり and publish it on GitHub Pages.

The site should work as a fan-made profile and archive page. It collects public channel/profile information, organizes preserved video metadata, and provides entry points to tags, fanart, and recreated historical pages.

| Item | Content |
| --- | --- |
| Target VTuber | 結萌ひまり |
| Affiliation | Re:AcT Gaming |
| X | <https://x.com/RAG_Himari> |
| YouTube | <https://www.youtube.com/@raghimari> |
| Graduation date | 2026-04-27 |
| Video count | 279, based on `videos.json` |
| Members-only videos | 76 |
| Playlist count | 28 |

## Design Goals

- Preserve profile and archive information in a static site that can be hosted on GitHub Pages.
- Make the page readable as a memorial/profile page first, then usable as a video archive.
- Keep data and UI boundaries explicit so later sections can be implemented in phases.
- Avoid requiring a backend for the initial release.

## Page Structure

The page is divided into five major blocks.

| Order | Block | Purpose | Main Content |
| --- | --- | --- | --- |
| 1 | Profile | First-view identity and summary | Main visual, short profile, channel links, total videos, playlist count, active period |
| 2 | Video Analyze | Archive exploration | Stream type charts, collaboration analysis, full video archive, detail/search mode |
| 3 | Tag Block | Tag discovery and external search | Related tags and X/Twitter search handoff |
| 4 | Fanarts | Fanart preview | Horizontal carousel, auto-scroll, pause-on-hover, left/right controls |
| 5 | Recreated Pages | Preserved historical material | Litlink, YouTube, Twitch, Twitter, sub-Twitter page candidates |

## Interaction Design

### Primary Navigation

- The site is a single-page experience.
- Section-level navigation should scroll to the relevant block instead of opening separate pages.
- CTA buttons in the Top/Profile block should support these targets:
  - `#videos`
  - `#tag-searcher`

### Video Archive

- Video Analyze should support both overview charts and detailed archive browsing.
- Expected visualizations:
  - Bar chart for major stream categories.
  - Pie/cake chart for composition summary.
  - Bubble chart for collaboration or tag distribution.
- Detail/search behavior can refer to [videos_check.html](../ref/videos_check.html), but the final UI should be adapted for the public-facing React page.

### Tag Search

- Tag clicks should open an X/Twitter search page for that tag.

### Fanart Preview

- Intended UI is a horizontal carousel.
- Auto-scroll should run only when the user is not hovering or interacting.
- Hover should pause movement.
- Left/right controls should remain available for manual navigation.

### Recreated Pages

- Recreated pages should expose preserved local material without implying official ownership.
- Public/private boundaries must be decided before publishing any recreated or archived content.

## Wireframe And Assets

- [Wireframe PNG](../framework.png)
- [Original wireframe workbook](../design.xlsx)
- Figma source: [結萌ひまり 卒業アルバム - Wireframe](https://www.figma.com/design/qRIG39WtxY0JosIujPBGd7)

## Visual Tokens

| Usage | Color |
| --- | --- |
| Deep pink | `#E87FAB` |
| Pale pink | `#FFEEF5` |
| Mid pink | `#F9C8DC` |
| Dark text | `#3D2B3D` |
| Muted text | `#7A5C7A` |
| Purple | `#9B6FC8` |
| Green | `#6BAD6B` |
| White | `#FFFFFF` |

## Component Design

```text
src/
├── components/
│   ├── TopPage/          # Main visual, profile, and stats
│   ├── VideoTable/       # Dense table view
│   ├── VideoGallery/     # Thumbnail card view
│   ├── TagSearcher/      # Categorized X/Twitter tag search links
│   ├── VideoAnalytics/   # Charts: bar, bubble, pie
│   ├── FanartPreview/    # Fanart preview/gallery
│   └── RelatedLinks/     # Related and recreated links
├── data/
│   └── videos.json
├── hooks/
│   └── useVideos.ts
└── App.tsx
```

## Technology Choices

| Area | Choice | Reason |
| --- | --- | --- |
| Framework | React + Vite + TypeScript | Keep the app simple and static |
| Styling | Custom CSS in current repo | Current implementation does not use Tailwind |
| Charts | Recharts or equivalent React chart library | Better fit for future chart work |
| Data source | Static `videos.json` | No backend required for early phases |
| Deploy | GitHub Pages | Free static hosting |
| Future data sync | Google Sheets API | Possible later automation path |

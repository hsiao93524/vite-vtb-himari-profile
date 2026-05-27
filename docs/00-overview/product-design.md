# Product Design

Source: [Notion design document](https://www.notion.so/React-35254a9cebff81df8fc7c1fc381d26b4)

This document is the repository snapshot of the product design for the React web version. Use the Notion page as the working draft, and use this file as the implementation reference inside the codebase.

## Project Overview

Build a one-page React site for the VTuber archive/profile of 結萌ひまり and publish it on GitHub Pages.

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

## Page Structure

The page is divided into five major blocks.

1. Profile
   - Main visual, short profile, channel links, and core stats.
   - Stats include total videos, playlist count, and active period.

2. Video Analyze
   - Shows the major stream types, collaboration targets, and the full video archive.
   - Expected visualizations: bar chart, pie chart, and bubble chart.
   - Includes a detail/search mode similar to `docs/ref/videos_check.html`.

3. Tag Block
   - Lists related tags.
   - Tag clicks should open an X/Twitter search page for that tag.

4. Fanarts
   - Shows fanart fetched or linked by a specific X/Twitter tag.
   - Intended UI: horizontal carousel, auto-scroll when not hovered, pause on hover, left/right controls.

5. Recreated Pages
   - Recreates deleted or historical pages from locally preserved material.
   - Candidate targets: Litlink, YouTube, Twitch, Twitter, and sub-Twitter pages.

## Wireframe Assets

- [Wireframe PNG](framework.png)
- [Original wireframe workbook](design.xlsx)
- Figma source: [結萌ひまり 卒業アルバム - Wireframe](https://www.figma.com/design/qRIG39WtxY0JosIujPBGd7)

## Color Palette

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
│   ├── TagSearcher/      # Tag search, filter, and X/Twitter handoff
│   ├── VideoAnalytics/   # Charts: bar, bubble, pie
│   ├── FanartPreview/    # Fanart preview/gallery
│   └── RelatedLinks/     # Related and recreated links
├── data/
│   └── videos.json
├── hooks/
│   └── useVideos.ts
└── App.tsx
```

| Previous idea | Final component | Notes |
| --- | --- | --- |
| TopPage | TopPage | Main profile block |
| VideoTable | VideoTable + VideoGallery | User can switch between table and gallery |
| FilterBar | TagSearcher | Integrated into tag/filter entry |
| PlaylistNav | Tag/filter behavior | Playlist is handled as filtering data |
| New | VideoAnalytics | Bar, bubble, and pie/cake charts |
| New | FanartPreview | Fanart preview block |
| New | RelatedLinks | Related/recreated links |

## Technology Choices

| Area | Choice | Reason |
| --- | --- | --- |
| Framework | React + Vite + TypeScript | Keep the app simple and static |
| Styling | Custom CSS in current repo | Current implementation does not use Tailwind |
| Charts | Recharts or equivalent React chart library | Better fit for future chart work |
| Data source | Static `videos.json` | No backend required for early phases |
| Deploy | GitHub Pages | Free static hosting |
| Future data sync | Google Sheets API | Possible later automation path |

## Open Specifications

These need more detail before implementation.

- Video filters: exact filter list, sort order, pagination or no pagination.
- VideoTable and VideoGallery switch behavior and default view.
- TagSearcher logic: AND/OR behavior, partial match, and difference between site filter vs X/Twitter search.
- FanartPreview API policy: X/Twitter API auth, rate limits, cache strategy, fallback when API is unavailable.
- Recreated Pages: `.mhtml` conversion, static delivery, iframe/modal approach, and public/private content boundary.
- GitHub Pages: repository name, base path, custom domain, and GitHub Actions deployment.


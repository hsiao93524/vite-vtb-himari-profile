# Product Design

This document is the overview design document for the project.

## Document Role

Use this document as the overview reference for the project. It explains the site scope, the five main blocks, the current example dataset, and the design choices that affect the whole page.

## Project Summary

Build a simple frontend-only archive and profile site for VTubers. This project currently uses Himari as the example profile and dataset, and is published on GitHub Pages.

The site should work as a fan-made profile and archive page that can be adapted for different VTubers. It organizes public profile information, activity data, video metadata, tag search entry points, fanart content, and recreated or archived related pages.

**Example VTuber Profile:**

| Item | Content |
| --- | --- |
| Example VTuber | 結萌ひまり |
| Affiliation | Re:AcT Gaming |
| X | <https://x.com/RAG_Himari> |
| YouTube | <https://www.youtube.com/@raghimari> |
| Graduation date | 2026-04-27 |
| Video count | 279, based on `videos.json` |
| Members-only videos | 76 |
| Playlist count | 28 |

## Design Goals

- Make it easy for fans or VTubers to build a simple profile and archive site.
- Keep the first release frontend-only and easy to host on GitHub Pages.
- Start with dummy or static data, and keep the option open for a future backend.
- Preserve profile and archive information as static content in the first release.
- Keep data and UI boundaries explicit so later sections can be implemented in phases.

## Page Structure

The page is divided into five major blocks.

| Order | Block | Purpose | Main Content |
| --- | --- | --- | --- |
| 1 | Profile | First-view identity and summary | Main visual, short profile, official SNS links, total videos, members-only count, total hours, active period |
| 2 | Video Analyze | Activity data analysis | Stream type charts, collaboration analysis, full video archive, detail/search mode |
| 3 | X Tag Searcher | Quick access to related tag search results on X / Twitter | Prepared tags, category display, X / Twitter search handoff |
| 4 | Fanarts | Fanart preview | Horizontal carousel, auto-scroll, pause-on-hover, left/right controls |
| 5 | Recreated Pages | Preserved historical material | Litlink, YouTube, Twitch, Twitter, sub-Twitter page candidates |

## Block Titles And Descriptions

For future expansion, each main block title and purpose are provided by JSON.
This section defines that JSON only. The detailed data for each block is defined in that block's own design document.

These shared blocks are currently defined in [block-descriptions.json](../../src/data/block-descriptions.json).

JSON shape:

```json
{
  "[id]": {
    "label": "string",
    "desc": "string"
  }
}
```

Rules:

- Each top-level id in the shared block description JSON means one main block.
- Internal data fields and item ids are defined in each block's own design document.
- `label` is the block title shown on the page. It may be an empty string when the block design does not show a shared block title.
- `desc` explains what the block is for, what users can do there, and whether the content is public or limited. It may be an empty string when the block design does not show a shared block description.
- If `label` is an empty string, `desc` is not shown even when `desc` has text.

Current spec:

- There are five main blocks. Their ids are:
  - `profile`: `Profile`
  - `videoAnalyze`: `Video Analyze`
  - `tagSearcher`: `X / Twitter Tag Searcher`
  - `fanarts`: `Fanarts`
  - `recreatedPages`: `Recreated Pages`

## Wireframe

![profile-section-design](assets/01-framework.png)

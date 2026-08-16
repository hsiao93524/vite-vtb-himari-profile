# Profile Data Design

This document defines the Profile block preview, current `profile.json`, and related shared data needed by the `Profile` component.

## Block Titles And Descriptions

Notes:

- The character profile text inside the `Profile Static Data` also uses `description` as key, but it is not the block function description.
- The `Profile` block itself does not show shared `label` or `desc`.
- When the `profile` entry is added to `src/data/block-descriptions.json`, it should keep the same shared block shape and leave both fields empty.
- The shared block `label` / `desc` entry belongs to `src/data/block-descriptions.json`, not `src/data/profile.json`.

Expected shared block entry:

```json
{
  "profile": {
    "label": "",
    "desc": ""
  }
}
```

## Data Source

The Profile block uses Profile-owned assets and data, video-derived statistics, shared site metadata, and planned shared block text:

- Profile visual assets in `src/assets/profile/`.
- Profile static data in `src/data/profile.json`.
- Video-derived statistics from `src/data/videos.json` through `src/hooks/useVideos.ts`.
- Shared site metadata: `lastUpdated` from `src/data/site.json`.
- Shared block title/description data: `src/data/block-descriptions.json`.

### Asset Folder

In this document, `hero` means the character main visual asset. It is smaller than the full `Profile` block and should not be used as the Profile block id, page anchor, or publication section id.

[Main visual image](../../src/assets/profile/hero.png)

```text
src/assets/profile/hero.png
```

Current files:

| File | Size |
| --- | --- |
| `expression-01.jpg` | 360 x 360 |
| `expression-02.jpg` | 360 x 360 |
| `expression-03.jpg` | 360 x 360 |
| `expression-04.jpg` | 360 x 360 |
| `expression-05.jpg` | 340 x 340 |
| `expression-06.jpg` | 360 x 360 |
| `expression-07.jpg` | 360 x 360 |
| `expression-08.jpg` | 360 x 360 |
| `expression-09.jpg` | 360 x 360 |
| `expression-10.jpg` | 360 x 360 |
| `expression-11.jpg` | 342 x 342 |
| `expression-12.jpg` | 338 x 360 |
| `expression-13.jpg` | 360 x 360 |
| `expression-14.jpg` | 360 x 360 |
| `expression-15.jpg` | 360 x 360 |

- Image sizes are not all the same.
- Most images are `360 x 360` squares.
- The UI should place these images in fixed square frames and use `object-fit: cover`.
- Do not use the original image size to decide the layout.

Render rule:

```css
.expression-image {
  width: 152px;
  height: 152px;
  object-fit: cover;
}
```

### Random Expression Selection

Implementation:

```ts
const expressionImages = [
  expression01,
  expression02,
  expression03,
  // ...
]

function pickRandomExpressions(images: string[], count = 3) {
  return [...images].sort(() => Math.random() - 0.5).slice(0, count)
}

const selectedExpressions = useMemo(
  () => pickRandomExpressions(expressionImages, 3),
  [],
)
```

If stable test results are needed later, replace `Math.random()` with a seeded shuffle helper.

### JSON Shape

Current data file: `src/data/profile.json`.

Profile static data shape:

```json
{
  "name": "結萌ひまり",
  "description": "A zinnia spirit who connects people through good bonds. She woke up in a flower field and has unclear memories of being human.",
  "links": [
    {
      "label": "X",
      "shortLabel": "X",
      "href": "https://x.com/RAG_Himari",
      "kind": "x"
    },
    {
      "label": "YouTube",
      "shortLabel": "YT",
      "href": "https://www.youtube.com/@raghimari",
      "kind": "youtube"
    }
  ],
  "debutDate": "2025-04-19",
  "graduationDate": "2026-04-27"
}
```

Current shared site metadata used by Profile:

```json
{
  "lastUpdated": "2026-07-14"
}
```

### Field Rules

#### Profile Static Data Fields

Rules:

- `profile.json` is imported by the `Profile` component.
  - `name` stores the display name.
  - `description` stores the character profile text shown in the Profile block.
  - `links` stores the official Profile links.
    - `links.label` stores the full display label.
    - `links.shortLabel` stores the short label for compact UI.
    - `links.href` stores the target URL.
    - `links.kind` stores the link type used by the UI.
  - `debutDate` stores the debut date.
  - `graduationDate` stores the graduation date.
- `links` only stores the current official X account and YouTube channel. It is different from Recreated Pages data.
- Date fields use `YYYY-MM-DD`.

#### Shared Site Metadata Used By Profile

Rules:

- `site.json` is shared site-level metadata, not Profile-owned data and not the shared block description source.
- Profile currently reads `lastUpdated` from `src/data/site.json`.
- `lastUpdated` is shown by the Profile block as secondary supporting text.
- If more site-level fields are added, define the canonical schema in an overview or shared data document.
- Date text should use `YYYY-MM-DD` unless a display format helper is added later.

#### Statistics Fields

Statistics are loaded from `src/data/videos.json` through `useVideos`, then calculated inside the `Profile` component.

Current Profile statistics:

| Label | Meaning | Source |
| --- | --- | --- |
| `VIDEOS` | Total archive video count | `videos.length` |
| `MEMBERS` | Members-only video count | `video.isMembers || video.isMembersOnly` |
| `HOURS` | Total stream/video hours | Sum `duration`, then convert seconds to hours |

Suggested helper logic:

```ts
export function getProfileStats(videos: Video[]) {
  const membersCount = videos.filter(
    (video) => video.isMembers || video.isMembersOnly,
  ).length
  const totalHours = Math.round(
    videos.reduce((total, video) => total + (video.duration ?? 0), 0) / 3600,
  )

  return {
    videos: videos.length,
    members: membersCount,
    hours: totalHours,
  }
}
```

Rules:

- Do not copy statistics into another static JSON file unless the design intentionally freezes a release snapshot.
- Future tests should not hardcode `279`, `76`, or `907` as assets imgs. They should calculate expected values from `videos.json`.
- The members-only count should reflect the current data. Use `isMembers` now, and also count `isMembersOnly` if it appears during schema migration.
- Keep playlist support for both `string` and `string[]`, because one video may belong to multiple playlists.

### Empty Data Rules

- If `description` is empty or missing, do not render an empty profile text area.
- If `links` is empty, do not render an empty official-link row.
- If shared `lastUpdated` is empty or missing, do not render blank last-updated text.
- If `videos.json` is empty, calculate statistics from the empty list and avoid hard-coded fallback values.
- If JSON syntax is invalid, treat it as a build or development error.

## Suggested Final Structure

```text
src/
|-- assets/
|   `-- profile/
|       |-- hero.png
|       `-- expressions/
|           |-- expression-01.jpg
|           |-- expression-02.jpg
|           `-- ...
|-- data/
|   |-- block-descriptions.json
|   |-- profile.json
|   |-- site.json        # shared site metadata
|   `-- videos.json
|-- hooks/
|   `-- useVideos.ts
`-- components/
    `-- Profile/
        `-- index.tsx
```

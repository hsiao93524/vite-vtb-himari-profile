# Profile Data Design

This document defines the Profile block preview and the data needed for the future `TopPage` implementation.

## Asset Folder

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
- The future UI should place these images in fixed square frames and use `object-fit: cover`.
- Do not use the original image size to decide the layout.

Render rule:

```css
.expression-image {
  width: 152px;
  height: 152px;
  object-fit: cover;
}
```

## Random Expression Selection

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

## Profile Static Data

Data shape:

```ts
export const profile = {
  name: '結萌ひまり',
  description:
    'Profile copy profile copy profile copy profile copy profile copy...',
  links: [
    {
      label: 'X',
      shortLabel: 'X',
      href: 'https://x.com/RAG_Himari',
    },
    {
      label: 'YouTube',
      shortLabel: 'YT',
      href: 'https://www.youtube.com/@raghimari',
    },
  ],
  graduationDate: '2026-04-27',
}
```

Rules:

- `links` stores the official Profile links.
- `links` only stores the current official X account and YouTube channel. It is different from Recreated Pages data.

## Block Titles And Descriptions

Notes:

- The character profile text inside the `Profile Static Data` also uses `description` as key, but it is not the block function description.
- The `Profile` block itself does not use `description` or `label`. To keep every block consistent, the JSON still keeps these fields and leaves them empty.

```json
{
  "profile": {
    "label": "",
    "desc": ""
  }
}
```

## Statistics Data

Statistics are loaded from `src/data/videos.json` through `useVideos`, then calculated inside `TopPage`.

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
- Future tests should not hardcode `279`, `76`, or `907` as assets imgs. They should compare against values derived from the current `videos.json`.
- The members-only count should reflect the current data. Use `isMembers` now, and also count `isMembersOnly` if it appears during schema migration.
- Keep playlist support for both `string` and `string[]`, because one video may belong to multiple playlists.

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
|   |-- profile.ts
|   `-- videos.json
|-- hooks/
|   `-- useVideos.ts
`-- components/
    `-- TopPage/
        `-- index.tsx
```

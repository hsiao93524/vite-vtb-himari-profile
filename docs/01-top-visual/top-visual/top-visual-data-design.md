# Top Visual Data Design

This document defines the data needed by the top visual/profile block preview and the future `TopPage` implementation.

## Asset Directory

Expression images are stored here:

```text
src/assets/profile/expressions/
```

Main visual image:

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

Conclusion:

- The image sizes are not all identical.
- Most images are square `360 x 360`.
- The future UI should render them inside a fixed square frame with `object-fit: cover`.
- Do not rely on raw image dimensions for layout.

Recommended render rule:

```css
.expression-image {
  width: 152px;
  height: 152px;
  object-fit: cover;
}
```

## Random Expression Selection

The top visual block should show three expression images.

Behavior:

- On each page entry/load, randomly select three unique images from `src/assets/profile/expressions/`.
- Keep the selected three stable during the same render session.
- Do not reshuffle on every component re-render.
- The random choice does not need to persist across browser refreshes.

Recommended implementation:

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

If deterministic testing is needed later, replace `Math.random()` with a seeded shuffle helper.

## Profile Static Data

Profile text and links should not be hardcoded inside `TopPage`.

Recommended file:

```text
src/data/profile.ts
```

Recommended shape:

```ts
export const profile = {
  name: '結萌ひまり',
  description:
    '個人介紹個人介紹個人介紹個人介紹個人介紹個人介紹個人介紹...',
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
  lastUpdated: '2026-05-05',
  graduationDate: '2026-04-27',
}
```

Rules:

- `name` is the display name in the orange banner.
- `description` is the main profile copy under the name banner.
- `links` drives the circular X/YT icons.
- `lastUpdated` is shown at the lower-right of the top visual block.
- `graduationDate` can be used for active-period display or future profile details.

## Statistics Data

Statistics should be derived from `src/data/videos.json` through `useVideos` or a helper function.

Current top visual stats:

| Label | Meaning | Source |
| --- | --- | --- |
| `VIDEOS` | Total archive video count | `videos.length` |
| `MEMBERS` | Members-only video count | `video.isMembersOnly || video.isMembers` |
| `HOURS` | Total streaming/video hours | Sum of `duration`, converted from seconds to hours |

Possible future stats:

| Label | Meaning | Source |
| --- | --- | --- |
| `PLAYLISTS` | Unique playlist count | Unique values from `playlist` |
| `ACTIVE` | Active period | Min `date` to graduation date or latest video date |

Recommended helper logic:

```ts
function toList(value: string | string[]) {
  return Array.isArray(value) ? value : [value]
}

export function getTopVisualStats(videos: Video[]) {
  const playlistCount = new Set(videos.flatMap((video) => toList(video.playlist))).size
  const membersCount = videos.filter(
    (video) => video.isMembersOnly || video.isMembers,
  ).length
  const totalHours = Math.round(
    videos.reduce((total, video) => total + (video.duration ?? 0), 0) / 3600,
  )

  return {
    videos: videos.length,
    playlists: playlistCount,
    members: membersCount,
    hours: totalHours,
  }
}
```

Rules:

- Do not duplicate stats as separate static JSON unless the design intentionally freezes a release snapshot.
- Tests should not hardcode `279`, `76`, or `907`; they should compare against values derived from the current `videos.json`.
- During the schema migration, support both `isMembers` and `isMembersOnly`.
- During the playlist migration, support both `string` and `string[]`.

## Suggested Final Structure

```text
src/
├── assets/
│   └── profile/
│       ├── hero.png
│       └── expressions/
│           ├── expression-01.jpg
│           ├── expression-02.jpg
│           └── ...
├── data/
│   ├── profile.ts
│   └── videos.json
├── hooks/
│   └── useVideos.ts
└── components/
    └── TopPage/
        └── index.tsx
```

## Test Checklist

### Data And Images

- [ ] Main visual `src/assets/profile/hero.png` is displayed.
- [ ] The screen shows exactly three expression images.
- [ ] The three expression images are unique.
- [ ] Reloading the page can show a different expression-image combination.
- [ ] Expression images with different source sizes are cropped into consistent square frames.
- [ ] Display name is `結萌ひまり`.
- [ ] Profile description is visible.
- [ ] `Last updated: 2026-05-05` is visible.
- [ ] `VIDEOS` value matches the current `videos.json` total count.
- [ ] `MEMBERS` value matches the current members-only count derived from `videos.json`.
- [ ] `HOURS` value matches the current total duration derived from `videos.json`.

### Desktop Layout

- [ ] Full-body main visual appears on the left.
- [ ] Name banner appears on the right.
- [ ] Name banner has a slanted shape.
- [ ] Name banner has diagonal stripe decoration on the right.
- [ ] Profile description appears below the name banner.
- [ ] X / YT icons appear to the left of the expression images.
- [ ] Three expression images are arranged horizontally.
- [ ] Three statistic circles are arranged horizontally.
- [ ] Last updated text appears at the lower-right.
- [ ] Overall composition is close to the 1280 x 720 reference layout.

### Mobile Layout

- [ ] Layout becomes a single column on mobile width.
- [ ] Main visual does not overflow the viewport.
- [ ] Name banner does not overflow.
- [ ] Profile description does not overlap other elements.
- [ ] Three expression images remain square.
- [ ] Statistic circles become vertically arranged.
- [ ] Last updated text remains visible.
- [ ] Page has no horizontal scrollbar.

### Links And Interaction

- [ ] X icon links to `https://x.com/RAG_Himari`.
- [ ] YT icon links to `https://www.youtube.com/@raghimari`.
- [ ] External links use `target="_blank"`.
- [ ] External links use `rel="noreferrer"`.

### Accessibility

- [ ] Main visual has alt text.
- [ ] Expression images have alt text.
- [ ] Social links have understandable `aria-label` values.
- [ ] Statistics use `dl`, `dt`, and `dd`.
- [ ] Main top visual section has an understandable `aria-label`.
- [ ] Text is readable against the background.

### Edge Cases

- [ ] Layout remains stable when expression source images have different dimensions.
- [ ] Longer profile description does not compress or overlap the stats area.
- [ ] Four-digit stat values remain readable inside statistic circles.
- [ ] Page does not collapse if one image fails to load.

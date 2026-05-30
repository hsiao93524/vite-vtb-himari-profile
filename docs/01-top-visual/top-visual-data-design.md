# Top Visual 資料設計

本文件定義 top visual/profile 區塊預覽，以及未來 `TopPage` 實作所需的資料。

## 資產目錄

[主視覺圖片](../../src/assets/profile/hero.png)

```text
src/assets/profile/hero.png
```

目前檔案：

| 檔案 | 尺寸 |
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

- 圖片尺寸並非全都相同。
- 多數圖片是 `360 x 360` 的正方形。
- 未來 UI 應該把這些圖片放在固定的正方形框內，並使用 `object-fit: cover`。
- 不要依賴原始圖片尺寸來決定 layout。

渲染規則：

```css
.expression-image {
  width: 152px;
  height: 152px;
  object-fit: cover;
}
```

## 隨機表情選擇

實作：

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

如果之後需要 deterministic testing，請用 seeded shuffle helper 取代 `Math.random()`。

## Profile 靜態資料

資料形狀：

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
  graduationDate: '2026-04-27',
}
```

## 統計資料

統計資料應該透過 `useVideos` 或 helper function，從 `src/data/videos.json` 推導出來。

目前 top visual 統計：

| Label | 意義 | 來源 |
| --- | --- | --- |
| `VIDEOS` | archive 影片總數 | `videos.length` |
| `MEMBERS` | members-only 影片數 | `video.isMembersOnly || video.isMembers` |
| `HOURS` | 直播/影片總時數 | `duration` 加總後從秒換算成小時 |

建議 helper 邏輯：

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

規則：

- 除非設計上刻意凍結某個 release snapshot，否則不要把統計資料複製成另一份靜態 JSON。
- Tests 不應 hardcode `279`、`76` 或 `907`；應該與目前 `videos.json` 推導出的值比較。
- Schema migration 期間，同時支援 `isMembers` 與 `isMembersOnly`。
- Playlist migration 期間，同時支援 `string` 與 `string[]`。

## 建議最終結構

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
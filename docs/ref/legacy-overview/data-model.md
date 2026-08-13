# Data Model

Source: [Notion design document](https://www.notion.so/React-35254a9cebff81df8fc7c1fc381d26b4)

This document defines the intended `videos.json` schema and the migration direction from the current project data.

## Source Data Flow

```text
YouTube API
  -> fetch_himari.py
  -> 卒業アルバム.xlsx
  -> fetch_durations.py
  -> videos.json
  -> check.py
  -> videos_check.html
```

## Excel Fields

| Field | Description | Example |
| --- | --- | --- |
| `配信日 (YYMMDD)` | Stream date, six-digit format | `260130` |
| `タイトル` | Video title | |
| `URL` | Full YouTube URL | |

## Target JSON Schema

| Field | Type | Source | Notes |
| --- | --- | --- | --- |
| `id` | `string` | Generated | Playlist name plus sequence number |
| `date` | `string` | Excel conversion | `YYYY-MM-DD` |
| `title` | `string` | Excel conversion | |
| `url` | `string` | Excel conversion | |
| `videoId` | `string` | Extracted from URL | YouTube 11-character ID |
| `thumbnailUrl` | `string` | Generated from `videoId` | Can use local `/thumbnails/{videoId}.jpg` |
| `playlist` | `string[]` | Excel conversion | A video may belong to multiple playlists |
| `visibility` | `'public' \| 'unlisted' \| 'unavailable'` | YouTube API | `unavailable` means deleted, private, or otherwise API-inaccessible |
| `isMembersOnly` | `boolean` | Playlist/title rule | Replaces old mixed member flags |
| `duration` | `number \| null` | YouTube API | Seconds |
| `tags` | `string[]` | Manual or generated/reviewed | Category should be merged into tags |
| `collab` | `string[]` | Manual or generated/reviewed | Collaboration names |
| `note` | `string` | Manual | Optional stream notes |

Removed fields:

- `category`: merge into `tags`.
- `status`: no longer needed after graduation.
- `isDeleted`: replace with `visibility`.
- `isMembers`: replace with `isMembersOnly`.

## JSON Example

```json
{
  "id": "ggst-001",
  "date": "2026-02-12",
  "title": "【 #GGST 参加型】新しいGGST...",
  "url": "https://youtu.be/IGLsTjVzoL0",
  "videoId": "IGLsTjVzoL0",
  "thumbnailUrl": "/thumbnails/IGLsTjVzoL0.jpg",
  "playlist": ["初めてのGUILTY GEAR -STRIVE-"],
  "visibility": "public",
  "isMembersOnly": false,
  "duration": 7200,
  "tags": [],
  "collab": [],
  "note": ""
}
```

## Duplicate Video Policy

The same `videoId` can appear in multiple playlists. This is expected.

Decision:

- Store all playlists on one video as `playlist: string[]`.
- Keep duplicate detection by `videoId`.
- Playlist-based search can show the video as belonging to multiple playlists.
- Video-ID-based display should treat it as one video.

## Tag Policy

Phase 1:

- Generate candidate tags from video titles with scripts.
- Extract game names, event names, and collaboration patterns.
- Review generated tags manually before accepting them.

Phase 2:

- Consider a user-participation tag voting system.
- Tags may have scores.
- High-score tags are emphasized.
- Low-score tags are muted or hidden.
- User-proposed tags become official after passing a threshold.

## Collaboration Policy

- Extract `w/XXX` and similar title patterns with scripts.
- Review extracted names manually.
- Future user completion can be considered after the base archive is stable.

## Current Migration Gap

As of the current repository state:

- `src/data/videos.json` still uses `playlist` as a string.
- `category`, `status`, and `isMembers` still exist.
- `visibility` does not exist yet.
- `src/types/video.ts` still supports transitional fields.

Treat the schema above as the target state, not the current implementation state.


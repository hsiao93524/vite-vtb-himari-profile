# Roadmap

Source: [Notion design document](https://www.notion.so/React-35254a9cebff81df8fc7c1fc381d26b4)

The project should be published block by block instead of waiting for every feature to be complete.

Publication order:

1. Profile + TagSearcher
2. Video search/list
3. VideoAnalytics
4. Recreated pages
5. Fanarts

## Phase 1: Data Foundation

Status: mostly complete in the original plan, but migration cleanup remains in this repo.

- Excel to JSON conversion script.
- HTML checker generation.
- `videos_check.html` validation workflow.
- Target JSON schema decision.
- `playlist` should become `string[]`.
- `status` should be removed.
- `category` should be merged into `tags`.
- VideoTable and VideoGallery switch behavior is accepted.

## Phase 2: First Public Release

Goal: establish the visual style and the main entry point.

Scope:

- Profile block.
- Tag entry.
- Base layout and shared visual language.

Tasks:

- Define final color system, background, accents, typography, spacing, and reusable component styles.
- Implement header or page navigation if needed.
- Implement profile content, main visual, core stats, and channel links.
- Implement static tag list.
- Tag click opens X/Twitter search.

Completion criteria:

- Page has a coherent visual style.
- Home/Profile block is usable.
- Tags are clickable and useful.

Release: first public release with Profile + TagSearcher.

## Phase 3: Video Searcher

Goal: make the archive actually searchable.

Scope:

- Video list.
- Basic title search.
- Date sorting.
- Table/gallery switch.
- Playlist filter.

Tasks:

- Connect `videos.json`.
- Implement VideoTable and VideoGallery.
- Implement search input and filters.
- Create tag/collab extraction script and populate reviewed values.

Completion criteria:

- User can find video records.

Release: second public release with VideoSearcher.

## Phase 4: VideoAnalytics

Goal: show the major streaming patterns visually.

Tasks:

- Analyze categories or tags.
- Analyze collaboration targets.
- Implement at least one useful chart first.
- Expand to bar, pie/cake, and bubble charts when the data is stable.

Completion criteria:

- At least one analysis visualization is correct and useful.

Release: third public release with VideoAnalytics.

## Phase 5: Recreated Pages

Goal: preserve historical page context.

Tasks:

- Test `.mhtml` to static HTML conversion.
- Decide how to serve recreated pages on GitHub Pages.
- Implement archive list.
- Implement modal or iframe display.
- Add Litlink, YouTube, Twitch, Twitter, and sub-Twitter targets if legally and technically acceptable.

Completion criteria:

- Recreated pages can be opened from the site without breaking the main archive.

Release: fourth public release with recreated pages.

## Phase 6: Fanarts

Goal: connect the archive to community content.

Tasks:

- Decide X/Twitter API usage and authentication.
- Define rate-limit and cache strategy.
- Implement FanartPreview carousel.
- Add auto-scroll, hover pause, and left/right controls.

Completion criteria:

- Fanart block can display relevant content or a stable fallback.

Release: fifth public release with Fanarts.

## High-Priority Open Items

- Define data rules before deeper analysis work.
- Migrate `playlist` to `string[]`.
- Replace `isDeleted` with `visibility`.
- Replace `isMembers` with `isMembersOnly`.
- Merge `category` into `tags`.
- Decide whether TagSearcher is a site filter, an X/Twitter search launcher, or both.
- Decide chart library before implementing advanced analytics.
- Decide deploy base path and GitHub Pages automation.


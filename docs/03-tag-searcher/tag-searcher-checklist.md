# Tag Searcher Acceptance Checklist

## Data Source

- [x] Tag Searcher reads tag entries from an independent JSON file.
- [x] The JSON file should be in `src/data/`.
- [x] The JSON has a top-level `categories` array.
- [x] Each category has `id`, `label`, and `tags`.
- [x] Category `description` is optional.
- [x] Each tag has `id`, `label`, and `query`.
- [x] Tag `description` is optional.
- [x] The JSON data follows the documented category model: official and unofficial.
- [ ] Category IDs are stable and unique across categories.
  - Note: This can be checked with the current mock data. Re-check after real API data is connected because ID stability depends on the final API rules.
- [ ] Tag IDs are stable and unique across all categories.
  - Note: This can be checked with the current mock data. Re-check after real API data is connected because tag IDs may come from the API or from a mapping rule.

## Required Content

- [x] The Tag Searcher block is visible when the JSON contains at least one visible tag.
- [x] Category labels must be visible.
- [x] Category descriptions are visible when provided.
- [x] Empty or missing category descriptions are not rendered.
- [x] Tag labels must be visible.
- [x] Tag descriptions are visible when provided.
- [x] Empty or missing tag descriptions are not rendered.
- [x] Tag display text uses `label`.
- [x] `label` and `query` can be different without breaking display or link generation.

## Layout

- [x] Categories are displayed as independent sections.
- [x] Tags are displayed under their category.
- [x] The UI treats categories generically and is not visually locked to only official/unofficial.
- [x] The tag label is visually identifiable as the clickable element.
- [x] The tag description is visually separate from the clickable tag label.
- [x] Categories without descriptions do not leave an empty description area.
- [x] Tags without descriptions do not leave an empty description area.

## Mobile Layout

- [ ] ~~The layout works without hover behavior.~~
  - Not applicable as a hover test because mobile devices do not support hover.
- [x] Tag descriptions are readable on mobile when provided.
- [x] Categories stack vertically on narrow screens.
- [x] Tag entries stack or wrap without creating horizontal scrolling.
- [x] The clickable tag label remains easy to tap on mobile.
- [x] Category descriptions are readable on mobile when provided.

## Interaction

- [x] Clicking a tag label opens a new browser tab.
- [x] X/Twitter search URL generation uses `query`.
- [x] The generated URL uses `https://x.com/search?q=${encodeURIComponent(query)}&src=typed_query`.
- [x] The generated URL does not add `&f=live` or other sorting/result-type parameters.
- [x] Only the tag label is clickable.
- [x] The tag description is not part of the link target.
- [x] Each tag uses one `query` string.
- [ ] ~~Tag search does not generate OR-combined or multi-query search strings.~~
  - Remove this item because OR-combined and multi-query search strings are outside the current spec.

## Empty Data Rules

- [x] A category with no tags is not displayed.
- [x] If all categories have no visible tags, the Tag Searcher block is not displayed.
- [x] Invalid JSON is treated as a build or development error, not as a runtime empty state.
  - Result: Removed a closing bracket, pressed F5, and the page did not render. Vite reported `expected ',' or '}' at line 52 column 3`.
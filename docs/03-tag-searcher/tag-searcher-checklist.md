# Tag Searcher Acceptance Checklist

## Data Source

- [ ] Tag Searcher reads tag entries from an independent JSON file.
- [ ] The JSON file should be in `src/data/`.
- [ ] The JSON has a top-level `categories` array.
- [ ] Each category has `id`, `label`, and `tags`.
- [ ] Category `description` is optional.
- [ ] Each tag has `id`, `label`, and `query`.
- [ ] Tag `description` is optional.
- [ ] The JSON data follows the documented category model: official and unofficial.
- [ ] Category IDs are stable and unique across categories.
- [ ] Tag IDs are stable and unique across all categories.

## Required Content

- [ ] The Tag Searcher block is visible when the JSON contains at least one visible tag.
- [ ] Category labels must be visible.
- [ ] Category descriptions are visible when provided.
- [ ] Empty or missing category descriptions are not rendered.
- [ ] Tag labels must be visible.
- [ ] Tag descriptions are visible when provided.
- [ ] Empty or missing tag descriptions are not rendered.
- [ ] Tag display text uses `label`.
- [ ] `label` and `query` can be different without breaking display or link generation.

## Layout

- [ ] Categories are displayed as independent sections.
- [ ] Tags are displayed under their category.
- [ ] The UI treats categories generically and is not visually locked to only official/unofficial.
- [ ] The tag label is visually identifiable as the clickable element.
- [ ] The tag description is visually separate from the clickable tag label.
- [ ] Categories without descriptions do not leave an empty description area.
- [ ] Tags without descriptions do not leave an empty description area.

## Mobile Layout

- [ ] The layout works without hover behavior.
- [ ] Tag descriptions are readable on mobile when provided.
- [ ] Categories stack vertically on narrow screens.
- [ ] Tag entries stack or wrap without creating horizontal scrolling.
- [ ] The clickable tag label remains easy to tap on mobile.
- [ ] Category descriptions are readable on mobile when provided.

## Interaction

- [ ] Clicking a tag label opens a new browser tab.
- [ ] X/Twitter search URL generation uses `query`.
- [ ] The generated URL uses `https://x.com/search?q=${encodeURIComponent(query)}&src=typed_query`.
- [ ] The generated URL does not add `&f=live` or other sorting/result-type parameters.
- [ ] Only the tag label is clickable.
- [ ] The tag description is not part of the link target.
- [ ] Each tag uses one `query` string.
- [ ] Tag search does not generate OR-combined or multi-query search strings.

## Empty Data Rules

- [ ] A category with no tags is not displayed.
- [ ] If all categories have no visible tags, the Tag Searcher block is not displayed.
- [ ] Invalid JSON is treated as a build or development error, not as a runtime empty state.

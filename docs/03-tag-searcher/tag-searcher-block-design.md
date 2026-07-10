# Tag Searcher Block Design

This document defines the Tag Searcher block. This block provides X/Twitter search entry points generated from prepared tag data.

## Scope

This block provides prepared tag links that open X/Twitter search results.

The block is responsible for turning each configured tag into an external X/Twitter search entry point.

## Layout

Tags are displayed as categorized groups.

Each category should be shown as an independent section with its own category label and optional category description. The initial data model uses official and unofficial categories, but the layout should treat categories generically so the design can support other category types later.

Each tag entry should show:

- The tag label.
- The tag description when provided.

Only the tag label is clickable. The description is explanatory text and is not part of the link.

## Mobile Behavior

The design must not depend on hover behavior. Descriptions should be visible inline when present.

On narrow screens, categories and tags should stack vertically.

## Interaction

Clicking a tag label opens a new browser tab.

The generated X/Twitter search URL format is:

```text
https://x.com/search?q=${encodeURIComponent(query)}&src=typed_query
```

No additional sorting or result-type parameter is added in the initial version.

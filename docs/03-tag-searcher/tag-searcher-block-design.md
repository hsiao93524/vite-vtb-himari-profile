# X Tag Searcher Block Design

This document defines the X Tag Searcher block. This block provides X / Twitter search entry points generated from prepared tag data.

## Scope

This block provides prepared tag links that open X / Twitter search results.

The block is responsible for turning each configured tag into an external X / Twitter search entry point.

This block does not control the site-side video tag filter or video list state. The internal React component can remain named `TagSearcher`.

## Wireframe Reference

This block corresponds to the third homepage block, `X Tag Searcher`.

Main elements:

```text
X Tag Searcher block
|-- section heading
`-- category groups
    |-- category label
    |-- optional category description
    `-- tag entries
        |-- clickable tag label
        `-- optional tag description
```

## Layout

Tags are displayed as categorized groups.

Each category should be shown as an independent section with its own category label and optional category description. The initial data model uses official and unofficial categories, but the layout should treat categories generically so the design can support other category types later.

Each tag entry should show:

- The tag label.
- The tag description when provided.

Only the tag label is clickable. The description is explanatory text and is not part of the link.

### Mobile layout or Behavior

The design must not depend on hover behavior. Descriptions should be visible inline when present.

On narrow screens, categories and tags should stack vertically.

## Required Content

| Content | Purpose | Source |
| --- | --- | --- |
| Section heading | Identify the block as X Tag Searcher | `src/data/block-descriptions.json` `tagSearcher.label` |
| Section description | Explain the X / Twitter search handoff | `src/data/block-descriptions.json` `tagSearcher.desc` |
| Category label | Group related X / Twitter search tags | `src/data/tag-searcher.json` category `label` |
| Category description | Explain the category when provided | category `description` |
| Tag label | Show the clickable search entry | tag `label` |
| Tag query | Generate the X / Twitter search URL | tag `query` |
| Tag description | Explain the tag when provided | tag `description` |

## Interaction

Clicking a tag label opens a new browser tab.

The generated X / Twitter search URL format is:

```text
https://x.com/search?q=${encodeURIComponent(query)}&src=typed_query
```

No additional sorting or result-type parameter is added in the initial version.

## Future Ideas

None for the current version.

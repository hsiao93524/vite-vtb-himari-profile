# 03 X Tag Searcher Docs

This folder contains the design documents for the third homepage block, `X Tag Searcher`. Its scope is limited to generating X / Twitter search entry points from prepared tag data. It does not cover site-side video filtering or AND/OR search conditions.

## Recommended Reading Order

1. [X Tag Searcher Block Design](tag-searcher-block-design.md)
   - Start here for purpose, screen scope, category display, mobile behavior, and X / Twitter search interaction.

2. [X Tag Searcher Data Design](tag-searcher-data-design.md)
   - Read this next for JSON structure, official/unofficial category definitions, tag fields, and empty-data rules.

3. [X Tag Searcher Checklist](tag-searcher-checklist.md)
   - Use this for final acceptance checks covering data source, required content, layout, mobile behavior, and interaction rules.

4. [X Tag Searcher Migration Checklist](tag-searcher-migration-checklist.md)
   - Use this while splitting the existing video tag filter from the X Tag Searcher external search handoff behavior.

## File Map

```text
docs/03-tag-searcher/
├── README.md
├── tag-searcher-block-design.md
├── tag-searcher-checklist.md
├── tag-searcher-data-design.md
└── tag-searcher-migration-checklist.md
```

## File Roles

| File | Role |
| --- | --- |
| `README.md` | Folder index and reading entry point. |
| `tag-searcher-block-design.md` | Draft UI, layout, and interaction specification for the X Tag Searcher block. |
| `tag-searcher-data-design.md` | Draft JSON schema, category definitions, and data rules for X Tag Searcher. |
| `tag-searcher-checklist.md` | Draft final acceptance checklist for X Tag Searcher implementation. |
| `tag-searcher-migration-checklist.md` | Draft migration checklist for splitting video tag filtering from X Tag Searcher. |

## Implementation Mapping

| Design Item | Current or Planned Location |
| --- | --- |
| X Tag Searcher component | `src/components/TagSearcher/` |
| Tag data JSON | `src/data/tag-searcher.json` |
| X / Twitter search URL builder | `buildXSearchUrl` in `src/components/TagSearcher/index.tsx` |

`TagSearcher` remains the internal component name. `X Tag Searcher` is the user-facing block name.

## Data Rules

- X Tag Searcher entries are managed by an independent JSON file.
- The JSON top level is `categories`.
- The initial categories are official and unofficial, but the UI must not be visually locked to those two categories.
- Each tag must include at least `id`, `label`, and `query`.
- `description` may be empty. When it is empty, no description text is shown.
- `label` is the user-facing display text. `query` is the search text used by the X / Twitter search URL.

## Relationship To Overview Docs

- Site direction: [`../00-overview/product-design.md`](../00-overview/product-design.md)
- Document map: [`../design-doc-map.md`](../design-doc-map.md)

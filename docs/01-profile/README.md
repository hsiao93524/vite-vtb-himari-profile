# 01 Profile Docs

This folder collects the design materials for the top `Profile` block on the home page.

## Purpose

- Define what the Profile block should show.
- Keep the Profile design image, source presentation, and acceptance checklist.
- Explain which images, text, links, and statistics the React implementation needs.
- Serve as the spec entry point before implementing `src/components/TopPage/`.
- Separate assets imported by the React app from preview assets used only by design docs.

## File Map

```text
docs/01-profile/
├── README.md
├── profile-block-design.md
├── profile-checklist.md
├── profile-data-design.md
├── profile-section-design.pptx
└── assets/
    └── profile-section-design.png
```

## Implementation Mapping

| Design Item | Current or Planned Location |
| --- | --- |
| Profile component | `src/components/TopPage/index.tsx` |
| Main visual image | `src/assets/profile/hero.png` |
| Expression images | `src/assets/profile/expressions/` |
| Profile static data | `src/data/profile.json` |
| Video-derived stats | `src/data/videos.json` + `src/hooks/useVideos.ts` |

## Asset Rules

- Images imported by the React app are stored in `src/assets/profile/`.
- Images used only for design docs or previews are stored in `docs/01-profile/assets/`.
- `profile-section-design.pptx` is the source design file, and `assets/profile-section-design.png` is the preview output.

## Relationship to Overall Design

- Site direction: [`../00-overview/product-design.md`](../00-overview/product-design.md)
- Doc map: [`../design-doc-map.md`](../design-doc-map.md)

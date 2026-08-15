# 01 Profile Docs

This folder collects the design materials for the top `Profile` block on the home page.

## Purpose

- Define what the Profile block should show.
- Set the Profile block as the first-view identity area for 結萌ひまり.
- Explain that the site is a fan archive with memorial and preservation intent.
- Present the block as both a profile area and a small activity dashboard.
- Use high-level statistics to show the shape of her streaming and video activity.
- Keep the Profile design image, source presentation, and acceptance checklist.
- Explain which images, text, links, and statistics the React implementation needs.
- Serve as the spec entry point before implementing `src/components/Profile/`.
- Separate assets imported by the React app from preview assets used only by design docs.

## Design Preview

![profile-section-design](./assets/profile-section-design.png)

## Recommended Reading Order

1. [Profile Block Design](profile-block-design.md)
   - Start here for purpose, layout, required content, visual direction, and interaction.

2. [Profile Data Design](profile-data-design.md)
   - Read this next for profile static data, asset rules, random expression selection, and video-derived statistics.

3. [Profile Checklist](profile-checklist.md)
   - Use this for final acceptance checks.

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

## File Roles

| File | Role |
| --- | --- |
| `README.md` | Folder index and reading entry point. |
| `profile-block-design.md` | UI, layout, visual direction, and interaction specification for Profile. |
| `profile-data-design.md` | Profile data, asset, and statistics rules. |
| `profile-checklist.md` | Final acceptance checklist for Profile implementation. |
| `profile-section-design.pptx` | Source design file. |
| `assets/profile-section-design.png` | Design preview image used only by docs. |

## Implementation Mapping

| Design Item | Current or Planned Location |
| --- | --- |
| Profile component | `src/components/Profile/index.tsx` |
| Main visual image | `src/assets/profile/hero.png` |
| Expression images | `src/assets/profile/expressions/` |
| Profile static data | `src/data/profile.json` |
| Video-derived stats | `src/data/videos.json` + `src/hooks/useVideos.ts` |
| Shared block text | `src/data/block-descriptions.json` `profile` entry after DYS-IMPL-07.01 |

## Asset Rules

- Images imported by the React app are stored in `src/assets/profile/`.
- Images used only for design docs or previews are stored in `docs/01-profile/assets/`.
- `profile-section-design.pptx` is the source design file, and `assets/profile-section-design.png` is the preview output.

## Relationship To Overview Docs

- Site direction: [`../00-overview/product-design.md`](../00-overview/product-design.md)
- Doc map: [`../design-doc-map.md`](../design-doc-map.md)

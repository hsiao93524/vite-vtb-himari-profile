# VTuber Archive & Profile Site

A fan-made archive and profile site for a VTuber, built as a personal frontend project.

## Overview

This project displays stream history, video archives, and channel information in a clean, browsable interface. Data is sourced from a structured JSON dataset and rendered with a custom UI.

## Tech Stack

- **React** + **TypeScript**
- **Vite**
- **CSS** (custom, no UI framework)

## Features

- Video archive browsing by playlist / category
- Channel profile display
- Responsive layout
- Data-driven rendering from a curated JSON dataset

## Publication Modes

This project publishes two versions at the same time:

- Public: `/vite-vtb-himari-profile/`
- HR: `/vite-vtb-himari-profile/hr/`

Section visibility is controlled in `src/config/publication.ts`.

- `public`: visible in both versions
- `wip-visible`: visible only in the HR version, with `[In progress]`
- `hidden`: hidden in both versions

Local development defaults to the public view. Use `?v=d` to show every
section with its visibility label: `[public]`, `[limit]`, or `[hidden]`.

Preview publication views without restarting the dev server:

```bash
http://localhost:5173/vite-vtb-himari-profile/
http://localhost:5173/vite-vtb-himari-profile/?v=h
http://localhost:5173/vite-vtb-himari-profile/?v=d
```

Build both versions into `dist/`:

```bash
npm run build:publications
```

Deploy publishes both versions:

```bash
npm run deploy
```

## Live Site

- [GitHub Pages](https://hsiao93524.github.io/vite-vtb-himari-profile/)
- [GitHub Pages deployments](https://github.com/hsiao93524/vite-vtb-himari-profile/deployments/github-pages)

## Design Docs

- [Design Doc Map](docs/design-doc-map.md)
- [Top Visual Docs](docs/01-top-visual/README.md)
- [Top Visual Block Design](docs/01-top-visual/top-visual-block-design.md)
- [Top Visual Data Design](docs/01-top-visual/top-visual-data-design.md)
- [Product Design](docs/00-overview/product-design.md)
- [Data Model](docs/00-overview/data-model.md)
- [Roadmap](docs/00-overview/roadmap.md)
- [Data Flow](docs/00-overview/data-flow.md)
- [Wireframe](docs/framework.png)
- [Original Wireframe Workbook](docs/design.xlsx)
- [Notion source](https://www.notion.so/React-35254a9cebff81df8fc7c1fc381d26b4)

## Background

Built as a side project to practice frontend development with React and TypeScript, as well as data pipeline work (Python scripts for fetching and structuring YouTube data via the YouTube Data API).

The supporting tooling includes:
- Python scripts for fetching video metadata and durations via the YouTube Data API v3
- Excel-based data management with `openpyxl`
- A browser-based data checker for validating the JSON dataset

## Status

Work in progress. Core UI and data pipeline are functional; additional features planned.

## License

Personal/fan project. Not affiliated with or endorsed by any talent agency.

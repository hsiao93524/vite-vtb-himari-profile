# VTuber Archive & Profile Site

A fan-made archive and profile site for a VTuber, built as a personal frontend project.

This is not an official site and is not affiliated with or endorsed by any talent agency.

## Overview

The site presents channel profile information, video archive data, fanart links, and related archive pages in a browsable frontend. The app is data-driven and currently reads its main video dataset from `src/data/videos.json`.

The main product blocks are planned around:

- Profile
- Video Analyze
- X Tag Searcher
- Fanarts
- Recreated Pages

For feature details, see the `docs/` folder.

## Tech Stack

- React
- TypeScript
- Vite
- Custom CSS

## Local Development

```text
npm install    # install dependencies
npm run dev    # start the local dev server
npm run build  # build the app
npm run lint   # run ESLint
```

## Publication Modes

Section visibility is controlled in `src/config/publication.ts`.

- `public`: visible in both versions
- `wip-visible`: visible only in the HR version, with `[In progress]`
- `hidden`: hidden in both versions

Local development defaults to the public view. Use `?v=d` to show every section with its visibility label: `[public]`, `[limit]`, or `[hidden]`.

Preview publication views without restarting the dev server:

```text
http://localhost:5173/vite-vtb-himari-profile/
http://localhost:5173/vite-vtb-himari-profile/?v=h
http://localhost:5173/vite-vtb-himari-profile/?v=d
```

## Project Docs

- [Product Design](docs/00-overview/product-design.md)
- [Wireframe](docs/00-overview/assets/01-framework.png)
- [Original Wireframe Workbook](docs/00-overview/design.xlsx)

## Live Site

- [GitHub Pages](https://hsiao93524.github.io/vite-vtb-himari-profile/)
- [GitHub Pages deployments](https://github.com/hsiao93524/vite-vtb-himari-profile/deployments/github-pages)

## Status

Work in progress. Core UI and data pipeline are functional, while product blocks and data schema cleanup are still being refined.

## License

Personal fan project. Not affiliated with or endorsed by any talent agency.

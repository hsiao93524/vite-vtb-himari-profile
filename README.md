# VTuber Archive & Profile Site

A fan-made archive and profile website for VTubers, developed as a personal frontend project.

Himari (結萌ひまり) is featured as the sample profile and dataset for demonstration purposes.

This website is unofficial and has no affiliation with, sponsorship from, or endorsement by Himari or any talent agency.

## Overview

This project aims to make it easy for fans or VTubers to build a simple profile and archive site. It is currently built as a frontend-only app, with a focus on organizing VTuber activity data and fan interaction content.

Planned data analysis includes:

- Video and stream frequency, categories, and ratios
- Frequent collaborators and closely related streamers

Fan interaction content includes:

- Quick access to related tag search results on X / Twitter
- Fanart post listings
- Recreated or archived related pages

The main product blocks are:

- Profile
- Video Analyze
- X Tag Searcher
- Fanarts
- Recreated Pages

For feature details, see the `docs/` folder.

## Publication Modes

Section visibility is controlled in `src/config/publication.ts`:

- `public`: visible in all publication views
- `wip-visible`: visible only in the portfolio view, marked as `[In progress]`
- `hidden`: hidden in all publication views

The public view is used by default during local development. Append `?v=d` to the URL to show all sections and their visibility labels: `[public]`, `[limit]` (= `wip-visible`), or `[hidden]`.

Preview publication views without restarting the development server:

```text
http://localhost:5173/vite-vtb-himari-profile/       # public view
http://localhost:5173/vite-vtb-himari-profile/?v=h   # portfolio view
http://localhost:5173/vite-vtb-himari-profile/?v=d   # debug view (all sections)
```

## Project Docs

For readers who want to learn more about the design and features of each section, please see the documents in [docs](./docs/).

## Live Site (`public` version)

- [GitHub Pages](https://hsiao93524.github.io/vite-vtb-himari-profile/)

## Local Development

```text
npm install    # install dependencies
npm run dev    # start the local dev server
npm run build  # build the app
npm run lint   # run ESLint
```

## Status

Work in progress. Core UI and data pipeline are functional, while product blocks and data schema cleanup are still being refined.

## License

Personal fan project. Not affiliated with or endorsed by any talent agency.

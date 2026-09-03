# VTuber Archive & Profile Site

A fan-made archive and profile site for VTubers, built as a personal frontend project.

This project uses Himari, a VTuber, as the example profile and dataset.

This is not an official site and is not affiliated with or endorsed by any talent agency.

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

Because the project is still in development, content is shown through section visibility controls. The site has two publication views: an SNS version and a portfolio version. The SNS version has already been shared on X / Twitter. Section visibility is controlled in `src/config/publication.ts`:

- `public`: visible in both the SNS version and the portfolio version
- `wip-visible`: visible only in the portfolio version, with sections marked as `[In progress]`
- `hidden`: hidden in both versions

Local development defaults to the public view. Use `?v=d` to show every section with its visibility label: `[public]`, `[limit]`, or `[hidden]`.

Preview publication views without restarting the dev server:

```text
http://localhost:5173/vite-vtb-himari-profile/
http://localhost:5173/vite-vtb-himari-profile/?v=h
http://localhost:5173/vite-vtb-himari-profile/?v=d
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

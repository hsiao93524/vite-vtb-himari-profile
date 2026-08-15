# Acceptance Checklist

## Identity

- [ ] The Profile block is rendered before the video/archive list section.
- [ ] The visible display name text is exactly `結萌ひまり`.
- [ ] The main visual from `src/assets/profile/hero.png` is displayed.
- [ ] Exactly three expression images are displayed.
- [ ] The three expression images are not repeated.
- [ ] A different set of expression images can appear after reloading the page.
- [ ] Expression images with different source sizes are cropped into consistent square frames.
- [ ] The Profile description is displayed.

## Desktop Layout

- [ ] The full-body main visual appears on the left.
- [ ] The name banner appears on the right.
- [ ] The name banner uses a slanted shape.
- [ ] The name banner has slash decoration on the right.
- [ ] The Profile description appears below the name banner.
- [ ] X / YT icons appear to the left of the expression images.
- [ ] The three expression images are arranged horizontally.
- [ ] The three statistic circles are arranged horizontally.
- [ ] The Last updated text appears at the lower-right corner.
- [ ] The overall composition is close to the 1280 x 720 reference layout.

## Mobile Layout

- [ ] At mobile width, the layout becomes a single column.
- [ ] The main visual does not overflow the viewport.
- [ ] The name banner does not overflow.
- [ ] The Profile description does not overlap other elements.
- [ ] The three expression images remain square.
- [ ] The statistic circles change to a vertical layout.
- [ ] The Last updated text remains visible.
- [ ] The page has no horizontal scrollbar.

## Required Content

- [ ] A main visual image is rendered from `src/assets/profile/hero.png` or the configured replacement asset.
- [ ] The X link is visible.
- [ ] The YouTube link is visible.
- [ ] The total video count is displayed.
- [ ] The displayed total video count equals `videos.length`.
- [ ] The members-only count is displayed.
- [ ] The displayed members-only count equals the number of videos where `isMembersOnly` or the transitional member field is true.
- [ ] The total hours count is displayed.
- [ ] The displayed total hours count equals the sum of `duration` rounded to hours.
- [ ] The active period is displayed.
- [ ] The displayed active period is derived from min/max `date` or the configured graduation date.
- [ ] `Last updated: 2026-xx-xx` is displayed.
- [ ] The `VIDEOS` value matches the current total count in `videos.json`.
- [ ] The `MEMBERS` value matches the members-only count derived from `videos.json`.
- [ ] The `HOURS` value matches the current total duration derived from `videos.json`.

## Statistics

- [ ] Each statistic has a visible label.
- [ ] Each statistic has a visible value.
- [ ] Statistics do not appear above the display name.
- [ ] Statistics do not visually dominate the main visual at desktop width `1280px`.

## Visual Direction

- [ ] The Profile block uses `#E87FAB` for the main accent or name-banner accent.
- [ ] The Profile block uses `#FFEEF5` as a soft background or background tint.
- [ ] Body/profile text uses `#3D2B3D` or another approved main text color from `product-design.md`.
- [ ] Secondary/supporting text uses `#7A5C7A` or another approved muted text color from `product-design.md`.

## Links and Interaction

- [ ] Clicking the X link opens `https://x.com/RAG_Himari`.
- [ ] Clicking the YouTube link opens `https://www.youtube.com/@raghimari`.

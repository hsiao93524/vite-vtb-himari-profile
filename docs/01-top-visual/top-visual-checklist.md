
# Acceptance Checklist

## Identity

- [ ] The Top/Profile block is rendered before the video/archive list section.
- [ ] The visible display name text is exactly `結萌ひまり`.
- [ ] 主視覺 `src/assets/profile/hero.png` 有顯示。
- [ ] 畫面剛好顯示三張表情圖片。
- [ ] 三張表情圖片不重複。
- [ ] 重新載入頁面時，可以出現不同的表情圖片組合。
- [ ] 不同來源尺寸的表情圖片會被裁切到一致的正方形框內。
- [ ] Profile description 有顯示。

## Desktop Layout

- [ ] 全身主視覺出現在左側。
- [ ] 名稱 banner 出現在右側。
- [ ] 名稱 banner 具有傾斜形狀。
- [ ] 名稱 banner 右側有斜線裝飾。
- [ ] Profile description 出現在名稱 banner 下方。
- [ ] X / YT icons 出現在表情圖片左側。
- [ ] 三張表情圖片水平排列。
- [ ] 三個統計圓形水平排列。
- [ ] Last updated text 出現在右下角。
- [ ] 整體構圖接近 1280 x 720 reference layout。

## Mobile Layout

- [ ] Mobile 寬度下 layout 變成單欄。
- [ ] 主視覺不會超出 viewport。
- [ ] 名稱 banner 不會超出。
- [ ] Profile description 不會與其他元素重疊。
- [ ] 三張表情圖片維持正方形。
- [ ] 統計圓形改成垂直排列。
- [ ] Last updated text 仍然可見。
- [ ] 頁面沒有水平捲軸。

## Required Content

- [ ] A main visual image is rendered from `src/assets/profile/hero.png` or the configured replacement asset.
- [ ] The X link is visible.
- [ ] The YouTube link is visible.
- [ ] The total video count is displayed.
- [ ] The displayed total video count equals `videos.length`.
- [ ] The playlist count is displayed.
- [ ] The displayed playlist count equals the number of unique normalized playlist values.
- [ ] The members-only count is displayed.
- [ ] The displayed members-only count equals the number of videos where `isMembersOnly` or the transitional member field is true.
- [ ] The active period is displayed.
- [ ] The displayed active period is derived from min/max `date` or the configured graduation date.
- [ ] `Last updated: 2026-xx-xx` 有顯示。
- [ ] `VIDEOS` 的值符合目前 `videos.json` 的總數。
- [ ] `MEMBERS` 的值符合從 `videos.json` 推導出的 members-only 數量。
- [ ] `HOURS` 的值符合從 `videos.json` 推導出的目前總 duration。

## Statistics

- [ ] Each statistic has a visible label.
- [ ] Each statistic has a visible value.
- [ ] Statistics do not appear above the display name.
- [ ] Statistics do not visually dominate the main visual at desktop width `1280px`.

## Visual Direction

- [ ] The Top/Profile block uses `#E87FAB` for the main accent or name-banner accent.
- [ ] The Top/Profile block uses `#FFEEF5` as a soft background or background tint.
- [ ] Body/profile text uses `#3D2B3D` or another approved main text color from `product-design.md`.
- [ ] Secondary/supporting text uses `#7A5C7A` or another approved muted text color from `product-design.md`.

## 連結與互動

- [ ] Clicking the X link opens `https://x.com/RAG_Himari`.
- [ ] Clicking the YouTube link opens `https://www.youtube.com/@raghimari`.
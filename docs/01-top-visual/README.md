# 01 Top Visual Docs

這個資料夾整理首頁最上方 `Top/Profile` 區塊的設計資料。範圍只包含第一眼看到的 profile visual block，不包含 Video、Tag、Fanart 或 Related Links 區塊。

## 目前用途

- 定義 Top/Profile 區塊要呈現什麼。
- 保存 Top 區塊設計圖與簡報原始檔。
- 說明 React 實作時需要哪些圖片、文字、連結與統計資料。
- 作為 `src/components/TopPage/` 實作前的規格入口。

## 建議閱讀順序

1. [Top Visual Block Design](top-visual-block-design.md)
   - 先看畫面結構、視覺方向、互動與目前實作差距。

2. [Top Visual Data Design](top-visual-data-design.md)
   - 再看資料來源、圖片資產、profile static data 與統計值規則。

3. [Top Section Design Preview](assets/top-section-design.png)
   - 對照實際設計圖，確認畫面構圖。

4. [Top Section Design Deck](top-section-design.pptx)
   - 原始簡報檔，保留給需要回溯設計來源時使用。

5. [Static HTML Preview](../../../top-visual-preview.html)
   - 根目錄的靜態預覽頁，用來快速看 Top/Profile 畫面方向。

## 檔案地圖

```text
docs/01-top-visual/
├── README.md
├── top-visual-block-design.md
├── top-visual-data-design.md
├── top-section-design.pptx
└── assets/
    └── top-section-design.png
```

## 實作對應

| 設計項目 | 目前或預計位置 |
| --- | --- |
| Top/Profile component | `src/components/TopPage/index.tsx` |
| Main visual image | `src/assets/profile/hero.png` |
| Expression images | `src/assets/profile/expressions/` |
| Future profile static data | `src/data/profile.ts` |
| Video-derived stats | `src/data/videos.json` + `src/hooks/useVideos.ts` |
| Static preview | `top-visual-preview.html` |

## 資產規則

- 會被 React app import 的圖片放在 `src/assets/profile/`。
- 只給設計書或預覽用的圖片放在 `docs/01-top-visual/assets/`。
- `top-section-design.pptx` 是原始設計檔，`assets/top-section-design.png` 是預覽用輸出。

## 實作前待確認

- 正式顯示名稱與 profile 文案。
- Top/Profile 是否要顯示 `VIDEOS / MEMBERS / HOURS`，或改成 `VIDEOS / PLAYLISTS / ACTIVE`。
- `totalHours` 是否保留在 Top 區塊，或移到 analytics。
- 表情圖是每次載入隨機 3 張，還是固定設計稿指定 3 張。
- 手機版是否保留完整主視覺，或使用裁切版。

## 與總設計書的關係

- 全站方向：[`../00-overview/product-design.md`](../00-overview/product-design.md)
- 資料模型：[`../00-overview/data-model.md`](../00-overview/data-model.md)
- 實作順序：[`../00-overview/roadmap.md`](../00-overview/roadmap.md)
- 文件地圖：[`../design-doc-map.md`](../design-doc-map.md)

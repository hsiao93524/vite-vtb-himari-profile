# 01 Top Visual Docs

這個資料夾整理首頁最上方 `Top/Profile` 區塊的設計資料。範圍只包含第一眼看到的 profile visual block，不包含 Video、Tag、Fanart 或 Related Links 區塊。

## 目前用途

- 定義 Top/Profile 區塊要呈現什麼。
- 保存 Top/Profile 的設計圖、簡報原始檔與驗收清單。
- 說明 React 實作時需要哪些圖片、文字、連結與統計資料。
- 作為 `src/components/TopPage/` 實作前的規格入口。
- 區分 React app 會 import 的資產，以及只給設計文件使用的預覽資產。

## 檔案地圖

```text
docs/01-top-visual/
├── README.md
├── top-visual-block-design.md
├── top-visual-checklist.md
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
| Profile static data | `src/data/profile.json` |
| Video-derived stats | `src/data/videos.json` + `src/hooks/useVideos.ts` |

## 資產規則

- 會被 React app import 的圖片放在 `src/assets/profile/`。
- 只給設計書或預覽用的圖片放在 `docs/01-top-visual/assets/`。
- `top-section-design.pptx` 是原始設計檔，`assets/top-section-design.png` 是預覽用輸出。

## 與總設計書的關係

- 全站方向：[`../00-overview/product-design.md`](../00-overview/product-design.md)
- 資料模型：[`../00-overview/data-model.md`](../00-overview/data-model.md)
- 資料流：[`../00-overview/data-flow.md`](../00-overview/data-flow.md)
- 實作順序：[`../00-overview/roadmap.md`](../00-overview/roadmap.md)
- 文件地圖：[`../design-doc-map.md`](../design-doc-map.md)

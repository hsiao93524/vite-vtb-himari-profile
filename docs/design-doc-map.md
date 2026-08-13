# Design Doc Map

這份文件是設計書地圖，用來快速判斷「要看哪一份文件」以及「文件之間的關係」。

## 快速入口

| 目的 | 先看 |
| --- | --- |
| 了解整個專案要做什麼 | [00-overview/product-design.md](00-overview/product-design.md) |
| 了解 Profile 畫面 | [01-profile/profile-block-design.md](01-profile/profile-block-design.md) |
| 了解 Profile 需要哪些資料 | [01-profile/profile-data-design.md](01-profile/profile-data-design.md) |
| 預覽 Profile 設計圖 | [01-profile/assets/profile-section-design.png](01-profile/assets/profile-section-design.png) |
| 看全頁 wireframe | [framework.png](framework.png) |

## 資料夾地圖

```text
docs/
├── README.md
├── design-doc-map.md
├── 00-overview/
│   └── product-design.md
├── 01-profile/
│   ├── README.md
│   ├── profile-block-design.md
│   ├── profile-data-design.md
│   ├── profile-checklist.md
│   ├── profile-section-design.pptx
│   └── assets/
│       └── profile-section-design.png
├── framework.png
├── design.xlsx
└── ref/
    ├── README.md
    ├── legacy-overview/
    │   ├── README.md
    │   ├── data-flow.md
    │   ├── data-model.md
    │   └── roadmap.md
    ├── chart_design.html
    ├── himari_archive_react_preview.html
    ├── videos_check.html
    └── python/
```

## 文件關係

```text
Notion design source
  -> 00-overview/product-design.md

Legacy overview notes
  -> ref/legacy-overview/README.md

framework.png / design.xlsx
  -> 01-profile/profile-block-design.md
      -> 01-profile/profile-data-design.md
      -> 01-profile/assets/profile-section-design.png

ref/python/
  -> videos.json generation and checking
  -> ref/videos_check.html
```

## 閱讀路徑

### 只想知道專案方向

1. [00-overview/product-design.md](00-overview/product-design.md)

### 要實作 Profile 畫面

1. [01-profile/profile-block-design.md](01-profile/profile-block-design.md)
2. [01-profile/profile-data-design.md](01-profile/profile-data-design.md)
3. [01-profile/assets/profile-section-design.png](01-profile/assets/profile-section-design.png)

### 要查看舊影片資料整理脈絡

1. [ref/README.md](ref/README.md)
2. [ref/legacy-overview/README.md](ref/legacy-overview/README.md)
3. [ref/videos_check.html](ref/videos_check.html)

## 文件定位

| 類型 | 位置 | 原則 |
| --- | --- | --- |
| 總設計 | `00-overview/` | 跨頁面、跨功能的核心設計與資料規則 |
| 單一區塊設計 | `01-profile/` 等 numbered folder | 專注於某個 UI block 的規格 |
| 原始草稿 | `design.xlsx`, `framework.png` | 保留設計來源，不直接當實作規格 |
| 參考資料 | `ref/` | 舊版 HTML、資料檢查、腳本與歷史參考 |
| 舊 overview | `ref/legacy-overview/` | 過舊的 data flow、data model 與 roadmap，只作參考 |
| 實際 app 圖片 | `src/assets/` | React 程式會 import 的圖片 |
| 文件用圖片 | `docs/**/assets/` | 只給設計書或預覽文件使用 |

## 維護規則

- 新增跨專案設計文件時，放進 `00-overview/`。
- 新增特定 UI 區塊設計時，建立下一個 numbered folder，例如 `02-video-block/`。
- 新增設計圖但不會被 React import 時，放在該設計資料夾的 `assets/`。
- 移動文件後，同步更新：
  - [README.md](../README.md)
  - [docs/README.md](README.md)

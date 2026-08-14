# Design Doc Map

這份文件是設計書地圖，用來快速判斷「要看哪一份文件」。

## 快速入口

| 目的 | 先看 |
| --- | --- |
| 了解整個專案要做什麼 | [00-overview/product-design.md](00-overview/product-design.md) |
| 了解 Profile 設計 | [01-profile/README.md](01-profile/README.md) |
| 了解 X Tag Searcher 設計 | [03-tag-searcher/README.md](03-tag-searcher/README.md) |
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
├── 03-tag-searcher/
│   ├── README.md
│   ├── tag-searcher-block-design.md
│   ├── tag-searcher-checklist.md
│   ├── tag-searcher-data-design.md
│   └── tag-searcher-migration-checklist.md
├── framework.png
└── design.xlsx
```

## 文件定位

| 類型 | 位置 | 原則 |
| --- | --- | --- |
| 總設計 | `00-overview/` | 跨頁面、跨功能的核心設計與資料規則 |
| 單一區塊設計 | `01-profile/` 等 numbered folder | 專注於某個 UI block 的規格 |
| 原始草稿 | `design.xlsx`, `framework.png` | 保留設計來源，不直接當實作規格 |
| 文件用圖片 | `docs/**/assets/` | 只給設計書或預覽文件使用 |
| 實際 app 圖片 | `src/assets/` | React 程式會 import 的圖片 |

## 維護規則

- 新增跨專案設計文件時，放進 `00-overview/`。
- 新增特定 UI 區塊設計時，建立 numbered folder，例如 `NN-feature-name/`。NN 為區塊順序。
- 新增設計圖但不會被 React import 時，放在該設計資料夾的 `assets/`。
- 移動文件後，同步更新：
  - [README.md](../README.md)
  - [docs/README.md](README.md)

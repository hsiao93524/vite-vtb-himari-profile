# Docs Index

這裡整理專案內的設計書、資料規格、roadmap、草圖與參考資料。

建議先從 `00-overview/product-design.md` 看整體方向，再看 Top 區塊設計與資料模型。

## 00 Overview

| 檔案 | 用途 |
| --- | --- |
| [00-overview/product-design.md](00-overview/product-design.md) | 主設計書快照，整理 Notion 的核心規格。 |
| [00-overview/data-model.md](00-overview/data-model.md) | 影片資料 schema 與資料清理方向。 |
| [00-overview/roadmap.md](00-overview/roadmap.md) | 實作階段、發布順序與高優先缺口。 |
| [00-overview/data-flow.md](00-overview/data-flow.md) | 目前 app 的資料流與 component 串接方式。 |

## 01 Top Visual

| 檔案 | 用途 |
| --- | --- |
| [01-top-visual/README.md](01-top-visual/README.md) | Top/Profile 區塊設計資料夾索引。 |
| [01-top-visual/top-visual-block-design.md](01-top-visual/top-visual-block-design.md) | Top/Profile 區塊的 UI 設計說明。 |
| [01-top-visual/top-visual-data-design.md](01-top-visual/top-visual-data-design.md) | Top/Profile 區塊的資料需求與欄位設計。 |
| [01-top-visual/top-visual-checklist.md](01-top-visual/top-visual-checklist.md) | Top/Profile 實作完成後的驗收清單。 |
| [01-top-visual/top-section-design.pptx](01-top-visual/top-section-design.pptx) | Top 區塊設計簡報原始檔。 |
| [01-top-visual/assets/top-section-design.png](01-top-visual/assets/top-section-design.png) | Top 區塊設計圖預覽。 |

### Top 區塊設計圖

![Top section design](01-top-visual/assets/top-section-design.png)

## 03 Tag Searcher

| 檔案 | 用途 |
| --- | --- |
| [03-tag-searcher/^README.md](03-tag-searcher/^README.md) | Tag Searcher 區塊設計資料夾索引。 |
| [03-tag-searcher/tag-searcher-block-design.md](03-tag-searcher/tag-searcher-block-design.md) | Tag Searcher 區塊的 UI、layout 與 X/Twitter 搜尋互動規格。 |
| [03-tag-searcher/tag-searcher-data-design.md](03-tag-searcher/tag-searcher-data-design.md) | Tag Searcher 使用的 JSON schema、分類定義與資料規則。 |
| [03-tag-searcher/tag-searcher-checklist.md](03-tag-searcher/tag-searcher-checklist.md) | Tag Searcher 實作完成後的驗收清單。 |
| [03-tag-searcher/tag-searcher-migration-checklist.md](03-tag-searcher/tag-searcher-migration-checklist.md) | 拆分影片 tag filter 與 X/Twitter Tag Searcher 行為的 migration checklist。 |

## Wireframe / 原始草稿

| 檔案 | 用途 |
| --- | --- |
| [framework.png](framework.png) | 全頁 wireframe 圖片預覽。 |
| [design.xlsx](design.xlsx) | 原始 wireframe Excel 草稿。 |

### 全頁 Wireframe

![Framework wireframe](framework.png)

## 參考資料

| 位置 | 用途 |
| --- | --- |
| [ref/README.md](ref/README.md) | `docs/ref/` 內容說明。 |
| [ref/chart_design.html](ref/chart_design.html) | 舊版分析圖設計參考。 |
| [ref/himari_archive_react_preview.html](ref/himari_archive_react_preview.html) | 舊版 React 風格預覽。 |
| [ref/videos_check.html](ref/videos_check.html) | `videos.json` 檢查報告 HTML。 |
| [ref/python/](ref/python/) | YouTube 資料取得、轉換、檢查與縮圖下載腳本。 |

## 外部來源

- [Notion source](https://www.notion.so/React-35254a9cebff81df8fc7c1fc381d26b4)
- [GitHub Pages](https://hsiao93524.github.io/vite-vtb-himari-profile/)
- [GitHub Pages deployments](https://github.com/hsiao93524/vite-vtb-himari-profile/deployments/github-pages)

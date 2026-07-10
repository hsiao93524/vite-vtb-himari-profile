# Tag Searcher Migration Checklist

這份清單用於將目前混合在 `TagSearcher` 裡的影片 tag 篩選功能拆分出去，並將 `TagSearcher` 改為獨立的 X/Twitter 搜尋入口，同時避免破壞既有的 Video Analyze 功能。

## 調查

- [ ] 確認目前 `TagSearcher` component 的 props、事件與顯示內容。
- [ ] 確認 `App.tsx` 傳入 `TagSearcher` 的資料與 callback。
- [ ] 確認 `useVideos` 提供的 `allTags`、`selectedTags`、`toggleTag` 與篩選流程。
- [ ] 確認影片 tag filter 如何影響 `filteredVideos`。
- [ ] 確認目前影片文字搜尋、playlist filter 與 tag filter 是否能同時使用。
- [ ] 記錄目前 Video tag filter 的操作步驟與預期結果，作為拆分後的比較基準。
- [ ] 確認現有 `.tag-list`、`.tag-pill` 等 CSS 是否同時被其他區塊使用。
- [ ] 確認 Tag Searcher 的 publication visibility 與 `In progress` 標記流程。

## 拆分

- [ ] 建立獨立的 Video tag filter component。
- [ ] 將目前 `TagSearcher` 的影片 tag 按鈕與選取狀態移到 Video tag filter component。
- [ ] 在 Video Analyze 區域接回 `allTags`、`selectedTags` 與 `toggleTag`。
- [ ] 確認 `useVideos` 的既有 tag filter 邏輯不需要因拆分而改變行為。
- [ ] 建立 Tag Searcher 專用 JSON 資料檔。
- [ ] 依 `tag-searcher-data-design.md` 定義 category 與 tag 資料。
- [ ] 將 `TagSearcher` 改為讀取獨立 JSON。
- [ ] 將 `TagSearcher` 改為依 category 顯示 tag。
- [ ] 讓 tag label 使用 `query` 產生 X/Twitter search URL。
- [ ] 讓 tag label 在新分頁開啟搜尋結果。
- [ ] 確保 description 不是連結的一部分。
- [ ] 加入 Tag Searcher 專用桌機與手機版樣式。
- [ ] 避免 Tag Searcher 新樣式改變 Video tag filter 的外觀或行為。

## 驗證

### Video Tag Filter 回歸

- [ ] Video tag filter 仍會顯示目前影片資料中的 tag。
- [ ] 點擊一個 video tag 後，影片結果只顯示符合條件的項目。
- [ ] 再次點擊已選取的 video tag 可以取消該條件。
- [ ] 多個 video tag 的既有選取行為沒有改變。
- [ ] `Clear` 可以清除 video tag、playlist 與文字搜尋條件。
- [ ] 影片文字搜尋仍可正常使用。
- [ ] Playlist filter 仍可正常使用。
- [ ] Table 與 Gallery 切換後仍保留目前篩選結果。
- [ ] 顯示的影片結果數量與實際篩選結果一致。

### Tag Searcher 功能

- [ ] Tag Searcher 使用獨立 JSON，而不是 `videos.json` 的 tag 清單。
- [ ] Category 與 tag 依 JSON 順序顯示。
- [ ] 有 description 的 tag 會顯示說明。
- [ ] description 留空或缺少時不顯示空白說明區域。
- [ ] 只有 tag label 可以點擊。
- [ ] 點擊 tag label 會開啟新分頁。
- [ ] 搜尋 URL 使用 `https://x.com/search?q=${encodeURIComponent(query)}&src=typed_query`。
- [ ] 日文、英文、空格、`#` 與引號等字元會正確 URL encode。
- [ ] 搜尋 URL 不會加入 `&f=live` 或其他排序參數。
- [ ] 空 category 不顯示。
- [ ] 所有 category 都沒有 tag 時，整個 Tag Searcher 區塊不顯示。

### 畫面與可用性

- [ ] 桌機版 category 與 tag 排版沒有重疊或溢出。
- [ ] 手機版 category 與 tag 可以垂直排列或換行。
- [ ] 手機版沒有水平捲軸。
- [ ] 手機版不依賴 hover 才能看到 description。
- [ ] Tag label 的點擊範圍足以在手機上操作。
- [ ] Video tag filter 與 X/Twitter Tag Searcher 在畫面與語意上可清楚區分。

### 自動檢查

- [ ] 執行 lint 並確認沒有錯誤。
- [ ] 執行 build 並確認沒有型別或打包錯誤。
- [ ] 依 `tag-searcher-checklist.md` 完成 Tag Searcher 最終驗收。

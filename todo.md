# TODO

## 功能模組整理

- [ ] 重整 `todo.md` 架構，改以功能模組分類
  - [ ] 定義各功能模組的分類方式
  - [ ] 將現有任務移入對應模組
  - [ ] 保留既有任務狀態與決策脈絡

- [ ] 將 Tag Searcher 從 Video Analyze 的影片 tag 篩選功能中拆分
  - [ ] 保留原本的影片 tag 篩選功能
  - [ ] 將 `TagSearcher` 改為獨立的 X/Twitter 搜尋入口
  - [x] 建立 `docs/03-tag-searcher/tag-searcher-migration-checklist.md`
  - [ ] 完成 `docs/03-tag-searcher/tag-searcher-migration-checklist.md` 的全部項目
  - [ ] 依 migration checklist 驗證新舊功能

## others

- 調整 video.json 的新格式
  - [ ] 轉換 video.json
    - ref: https://claude.ai/chat/34f302af-77b4-4839-b648-c7a0adad08f7
  - [ ] 轉換完之後透過 codex 重新修改前端

## Category 欄位清理

目標：依照設計書，將 `category` 從資料結構中移除，改由 `tags` 統一管理分類資訊。

- [x] 清理 Excel -> JSON 轉換流程中產生 `category` 的邏輯
  > 將 category 當作 tag 的初始值，放到tags list裡
- [ ] 確認轉換後的 `videos.json` 不再輸出 `category`
- [ ] 將原本 `category` 的分類值合併或轉換到 `tags`
- [ ] 清理 `src/types/video.ts` 裡的 `category?: string`
- [ ] 檢查並移除前端所有使用 `video.category` 的地方
- [ ] 更新 `useVideos` 的搜尋與 tag 建立邏輯，避免依賴 `category`
- [ ] 重新執行資料轉換與前端 build，確認沒有型別錯誤

## Members 欄位清理

目標：依照設計書，將會員影片欄位統一為 `isMembersOnly`，移除舊欄位 `isMembers`。

- [x] 清理 Excel -> JSON 轉換流程中產生 `isMembers` 的邏輯
- [ ] 將轉換流程改成輸出 `isMembersOnly`
- [ ] 確認轉換後的 `videos.json` 不再輸出 `isMembers`
- [ ] 將既有 `videos.json` 的 `isMembers` 資料遷移為 `isMembersOnly`
- [ ] 清理 `src/types/video.ts` 裡的 `isMembers?: boolean`
- [ ] 將 `src/types/video.ts` 的 `isMembersOnly?: boolean` 改成必要欄位 `isMembersOnly: boolean`
- [ ] 檢查並移除前端所有使用 `video.isMembers` 的地方
- [ ] 更新 `useVideos`、`TopPage`、`VideoTable` 等會員影片判斷邏輯，只依賴 `isMembersOnly`
- [ ] 重新執行資料轉換與前端 build，確認沒有型別錯誤

## Playlist 欄位清理

目標：依照設計書，將 `playlist` 統一為 `string[]`，支援同一影片存在於多個 playlist 的情況。

- [x] 清理 Excel -> JSON 轉換流程中產生 `playlist: string` 的邏輯
- [ ] 將轉換流程改成固定輸出 `playlist: string[]`
- [ ] 確認轉換後的 `videos.json` 每筆資料都使用陣列格式
- [ ] 將既有 `videos.json` 的 `playlist: string` 遷移為 `playlist: string[]`
- [ ] 清理 `src/types/video.ts` 裡的 `playlist: string | string[]`
- [ ] 將 `src/types/video.ts` 的型別改成 `playlist: string[]`
- [ ] 檢查並簡化前端處理 `playlist` 的相容邏輯，例如 `toList`
- [ ] 更新 `useVideos`、`VideoTable`、`VideoAnalytics` 等使用 playlist 的地方，只依賴 `string[]`
- [ ] 重新執行資料轉換與前端 build，確認沒有型別錯誤

## Status 欄位清理

目標：依照設計書，移除 `status` 欄位。此欄位目前只有 `ongoing` / `completed`，但卒業済み資料集不需要再用它表示狀態。

- [x] 清理 Excel -> JSON 轉換流程中產生 `status` 的邏輯
- [ ] 確認轉換後的 `videos.json` 不再輸出 `status`
- [ ] 將既有 `videos.json` 的 `status` 欄位移除
- [ ] 清理 `src/types/video.ts` 裡的 `status?: string`
- [ ] 檢查前端是否有使用 `video.status`
- [ ] 移除或改寫所有依賴 `status` 的顯示、篩選、統計邏輯
- [ ] 重新執行資料轉換與前端 build，確認沒有型別錯誤

## isDeleted 欄位補齊

> 目標：依照設計書，未來轉換後的每筆影片資料都需要有 `isDeleted` 欄位；如果沒有刪檔資訊，預設為 `false`。
> 
> - [ ] 更新 Excel -> JSON 轉換流程，固定輸出 `isDeleted`
> - [ ] 如果來源資料沒有刪檔資訊，將 `isDeleted` 預設為 `false`
> - [ ] 補上人工標記刪檔影片的資料來源或欄位規則
> - [ ] 確認轉換後的 `videos.json` 每筆資料都有 `isDeleted`
> - [ ] 將既有 `videos.json` 補上 `isDeleted: false`
> - [ ] 將 `src/types/video.ts` 的 `isDeleted?: boolean` 改成必> 要欄位 `isDeleted: boolean`
> - [ ] 檢查 `useVideos` 等前端邏輯是否需要依照 `isDeleted` 顯示標籤或篩選
> - [ ] 重新執行資料轉換與前端 build，確認沒有型別錯誤

isDeleted 廢除，改以 `visibility` 代替
(visibility: 'public' | 'unlisted' | 'unavailable')

## 左側章節選單

目標：在畫面左側加入章節選單，讓使用者可以快速跳到各個 block。

- [ ] 確認每個主要 block 都有穩定的 `id`，例如 `hero`、`videos`、`analytics`、`tag-searcher`、`fanart-preview`、`links`
- [ ] 新增章節選單資料結構，例如 `{ id: 'videos', label: 'Video Block' }`
- [ ] 建立 `SectionNav` 或類似元件
- [ ] 在桌面版將章節選單固定於左側，使用 `position: sticky`
- [ ] 點擊章節項目時使用 anchor 跳轉到對應 block，例如 `href="#videos"`
- [ ] 加上 `scroll-margin-top`，避免跳轉後標題貼齊視窗上緣
- [ ] 設計目前章節的 active 狀態，之後可用 Intersection Observer 判斷
- [ ] 手機版改成上方橫向選單或收合選單，避免佔用畫面寬度
- [ ] 確認鍵盤操作與可讀性，例如 link focus 樣式
- [ ] 跑 build 並檢查桌面與手機版 layout

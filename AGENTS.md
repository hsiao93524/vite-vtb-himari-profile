# AGENTS.md

## 暫時限制紀錄：Staged 內容待確認（已停用）

本章節只保留有 Staged 內容時需要使用的 agent.md 文本，不再作為有效工作規則。

```text
## 暫時限制：Staged 內容待確認（啟用中）

- 目前 Git index 內已有一批 staged 內容等待使用者確認。
- 只要使用者要求修改本專案的任何檔案，開始修改前都必須先提醒：「目前 staged 內容尚待確認。」
- 在使用者明確表示「已完成確認」或同等意思之前：
  - 不得 commit、unstage、restore 或改寫目前 staged 內容。
  - 不得把其他檔案加入 staged 內容。
  - 可以依使用者要求修改 working tree，但修改前仍需先提醒 staged 內容尚待確認。
- 純讀取、調查、說明或執行不會改變檔案與 Git index 的唯讀操作，不需要重複提醒。
- 使用者明確表示已完成確認後，將本章節改成「已停用」紀錄。
```

## Top Page / Top Profile 工作守則

Codex 處理 Top page 或 Top/Profile 區塊時，先依照以下規則工作：

- Top/Profile 的主要實作位置是 `src/components/TopPage/index.tsx`，相關樣式通常在 `src/App.css` 的 `.top-profile*` 區塊。
- 修改前先檢查 `docs/01-top-visual/top-visual-block-design.md`、`docs/01-top-visual/top-visual-data-design.md`、`docs/01-top-visual/top-visual-checklist.md`。
- Profile 文字、外部連結、出道日、畢業日使用 `src/data/profile.json`；不要重新 hardcode 到 component。
- 桌面版維持主視覺與 profile 內容的雙欄構圖；手機版可垂直排列，但主視覺、名稱、profile 文案與 stats 都要可讀。
- 若移動或替換 Top/Profile 資產，同步檢查 React import、Markdown docs、根目錄 preview HTML。

## 基本回覆規則

- 一律用繁體中文回答。
- 回答保持精簡；若涉及架構、資料流、部署流程或跨檔案設計，需說明取捨與影響範圍。
- 寫程式或修改檔案前，先用簡短段落說明計畫。
- 修改程式後必須跑驗證；若無法跑測試或專案沒有測試指令，需明確說明原因與已改跑的替代驗證。
- 不要回復或覆蓋使用者既有變更，除非使用者明確要求。

## 專案概況

- 本專案是 React、TypeScript、Vite、自訂 CSS 的 VTuber fan-made profile/archive site。
- 這是非官方 fan project；文字、素材與外部連結需避免暗示官方授權、官方營運或隸屬關係。
- 主要資料來源是 `src/data/videos.json`。
- 影片資料型別定義在 `src/types/video.ts`。
- 資料讀取、正規化、搜尋與篩選邏輯集中在 `src/hooks/useVideos.ts`。
- 縮圖放在 `public/thumbnails/{videoId}.jpg`，前端路徑需考慮 Vite `base` 與 `import.meta.env.BASE_URL`。

## 常用指令

- `npm run dev`：啟動本機開發伺服器。
- `npm run build`：執行 TypeScript build 與 Vite build。
- `npm run lint`：執行 ESLint。
- `npm run preview`：預覽 build 後的成果。
- `npm run deploy`：先 build，再以 `gh-pages -d dist` 發布；不要在未經要求時主動部署。

## 開發流程

- 功能或修正完成後，至少執行 `npm run build`。
- 若變更包含 lint 風險，例如 hook、component、型別或 import 調整，也執行 `npm run lint`。
- 若是純文件變更，可不跑 build，但最終回覆需說明「僅文件變更，未執行程式驗證」。
- 若啟動 dev server 或使用瀏覽器檢查 UI，需回報實際 URL 與檢查範圍。

## 程式規範

- 優先沿用現有 React function component、hook 與 CSS class 寫法。
- 型別要從 `src/types/video.ts` 擴充，不要在元件內重複定義資料模型。
- 篩選、搜尋、資料正規化邏輯優先放在 `useVideos.ts`，避免散落在各 UI component。
- UI component 盡量只接收整理好的 props，避免直接依賴 raw JSON 結構。
- 不要新增大型狀態管理、router、UI framework 或資料 fetching library，除非需求明確需要。
- 避免留下開發用 `console.log`；若需要暫時除錯，完成前移除或說明保留理由。

## 資料規範

- `src/data/videos.json` 是目前 app 直接 import 的資料來源；修改 schema 時要同步更新 `Video` 型別與 `useVideos` 的正規化邏輯。
- `playlist` 目前處於 `string | string[]` 過渡期；新邏輯應優先支援 `string[]`，並保留相容處理直到資料完成遷移。
- `isMembers` / `isMembersOnly`、`isDeleted` / 未來 `visibility` 等欄位若要遷移，需同時檢查資料、型別、篩選、顯示與統計邏輯。
- 新增縮圖時，檔名需使用 YouTube `videoId`，格式為 `public/thumbnails/{videoId}.jpg`。
- 不要把私密 token、YouTube API key、個人憑證或未公開資料放入 repo。

## 文件與編碼

- 文件預設使用 UTF-8。若看到中文或日文變成亂碼，先確認讀檔編碼，不要直接判定內容損壞。
- 更新 `docs/` 或 `todo.md` 時，保留原本的任務結構與決策脈絡。
- 資料流、schema 遷移或部署規則有變更時，同步更新 README 或 `docs/` 相關文件。

## 前端體驗規範

- 這個站點是資料瀏覽型 archive/profile site；優先確保搜尋、篩選、表格、圖廊與統計資訊清楚可用。
- 響應式版面要維持可讀性；修改 CSS 後需檢查桌面與窄螢幕寬度。
- 外部影片連結使用 `target="_blank"` 時需搭配 `rel="noreferrer"`。
- 圖片需避免破圖；縮圖路徑修改後要確認 GitHub Pages base path 仍可運作。

## Git 與變更範圍

- 變更應保持小而聚焦；不要順手重構不相關檔案。
- 若工作區已有使用者未提交變更，需保留並繞開；不得使用 destructive git 指令。
- 不要主動提交 commit、push 或 deploy，除非使用者明確要求。

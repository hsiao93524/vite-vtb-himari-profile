# ref 資料夾目錄與檔案說明

本資料夾是一組「結萌ひまり影片資料整理」的參考原型，涵蓋 YouTube 撈取、Excel 產生、Excel 轉 JSON、縮圖下載、JSON 檢查頁、React 介面草稿與統計圖表設計。

> 注意：部分檔案在目前環境中顯示為 mojibake 亂碼，但從檔名、函式、常數與 HTML 結構可判讀其功能。若後續要沿用，建議先統一確認原始編碼與文字內容。

## 目錄

```text
ref/
├─ chart_design.html
├─ himari_archive_react_preview.html
├─ videos_check.html
└─ python/
   ├─ check.py
   ├─ download_thumbnails.py
   ├─ fetch_durations.py
   ├─ fetch_himari.py
   ├─ fetch_himari_modified_streaming_time.py
   └─ himari_archive.py
```

## 根目錄 HTML 參考檔

| 檔案 | 類型 | 功能 / 內容 |
| --- | --- | --- |
| `chart_design.html` | 靜態 HTML / CSS / JavaScript | 影片統計圖表設計稿。內建 `DATA` 範例資料，支援分類統計與合作對象統計，並可切換橫條圖、圓餅圖、泡泡圖。主要用於前端視覺與互動原型參考。 |
| `himari_archive_react_preview.html` | 靜態 HTML / CSS / JavaScript | 類 React 風格的影片封存頁面預覽稿。包含頁首統計、搜尋列、篩選按鈕、表單入口、播放清單折疊區塊與 YouTube 縮圖。資料為內嵌範例 `data`。 |
| `videos_check.html` | 產生出的檢查報表 HTML | `videos.json` 的資料檢查結果頁。含統計卡、分類篩選、警告篩選、文字搜尋與完整影片表格。應是由 `python/check.py` 產生，內含約 279 筆影片資料。 |

## python 腳本

| 檔案 | 主要輸入 | 主要輸出 | 功能 / 內容 |
| --- | --- | --- | --- |
| `python/fetch_himari.py` | YouTube Data API、指定 channel ID | `test.xlsx` | 從結萌ひまり YouTube channel 撈取所有播放清單，再逐一取得播放清單影片，輸出成 Excel。每個播放清單成為一個 sheet，欄位包含日期、標題、URL，並套用粉色系 Excel 樣式。 |
| `python/fetch_himari_modified_streaming_time.py` | YouTube Data API、指定 channel ID | `卒業アルバム_修正版.xlsx` | `fetch_himari.py` 的修正版。改用 `videos().list()` 取得 `liveStreamingDetails.actualStartTime` / `scheduledStartTime`，用較接近實際直播開始時間的日期填入 Excel。額外輸出 `date_source` 欄位，標示日期來源。 |
| `python/fetch_durations.py` | `卒業アルバム.xlsx`、YouTube Data API key | `videos.json` | 將 Excel 播放清單資料轉成前端可用 JSON，並透過 YouTube Data API 補上影片時長 `duration`。同時建立 `id`、`date`、`title`、`url`、`videoId`、`thumbnailUrl`、`playlist`、`category`、`status`、`isMembers`、`tags`、`collab` 等欄位。 |
| `python/check.py` | `videos.json` | `videos_check.html` | 驗證 `videos.json` 欄位完整度，檢查 `date`、`videoId`、`duration`、`title`、`url` 等欄位是否缺失，並產生可視化 HTML 檢查頁。 |
| `python/download_thumbnails.py` | `卒業アルバム.xlsx` | `thumbnails/` | 讀取 Excel 各 sheet 的 YouTube URL，解析 video ID 後下載縮圖。會依 sheet 建資料夾，依序嘗試 `maxresdefault`、`hqdefault`、`mqdefault`，檔名含日期、標題與 video ID。 |
| `python/himari_archive.py` | 無外部資料，程式內建版型 | `/home/claude/himari_archive.xlsx` | 建立一份 Excel 封存表範本。包含首頁、頻道資訊、統計區、播放清單導覽、表單連結、版本紀錄，以及數個範例播放清單 sheet。主要是 Excel 樣式 / 結構原型。 |

## 主要資料流程

```text
YouTube channel
  ↓
fetch_himari.py 或 fetch_himari_modified_streaming_time.py
  ↓
卒業アルバム.xlsx / 卒業アルバム_修正版.xlsx
  ↓
fetch_durations.py
  ↓
videos.json
  ↓
check.py
  ↓
videos_check.html
```

輔助流程：

```text
卒業アルバム.xlsx
  ↓
download_thumbnails.py
  ↓
thumbnails/{playlist}/{date title videoId}.jpg
```

前端 / 視覺參考：

```text
videos.json / 統計資料
  ↓
chart_design.html
himari_archive_react_preview.html
```

## 重要欄位與資料模型

`fetch_durations.py` 產生的 `videos.json` 單筆資料大致包含：

```json
{
  "id": "playlist-slug-001",
  "date": "2026-04-27",
  "title": "影片標題",
  "url": "https://youtu.be/...",
  "videoId": "YouTube影片ID",
  "thumbnailUrl": "https://img.youtube.com/vi/.../mqdefault.jpg",
  "playlist": "播放清單名稱",
  "category": "分類",
  "status": "ongoing 或 completed",
  "isMembers": false,
  "duration": 3600,
  "tags": [],
  "collab": []
}
```

## 風險與整理建議

- `fetch_himari.py` 與 `fetch_himari_modified_streaming_time.py` 內有硬編碼 YouTube API key，建議移到環境變數或本機 `.env`，並檢查該 key 是否需要停用 / 輪替。
- 多個檔案文字顯示有 mojibake，建議先確認原始編碼，再統一轉為 UTF-8。
- `fetch_durations.py` 的 `API_KEY` 是 placeholder，但 `fetch_himari*.py` 是實 key；兩者設定方式不一致，建議統一。
- `himari_archive.py` 的輸出路徑是 `/home/claude/himari_archive.xlsx`，在 Windows 專案環境中可能不可用，建議改為相對路徑或可設定輸出路徑。
- `videos_check.html` 是產物檔，檔案很大。若可重現，建議只保留產生器 `check.py` 與資料來源，必要時再重新產生。
- 若這些參考檔會整合進 Vite 專案，建議把 `videos.json` 作為單一資料源，前端圖表與列表都改由同一份資料動態產生。

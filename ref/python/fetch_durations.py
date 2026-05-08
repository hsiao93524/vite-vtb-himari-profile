"""
結萌ひまり 配信アーカイブ
Excel → JSON 変換 + YouTube API で duration 取得スクリプト

使い方:
  pip install pandas openpyxl requests
  1. 下の API_KEY に自分のキーを貼る
  2. python fetch_durations.py
"""

import json
import re
import time
from datetime import datetime
from pathlib import Path

import pandas as pd
import requests

# ── ここを編集してください ────────────────────────────────────────────────────
API_KEY   = "YOUR_API_KEY_HERE"        # YouTube Data API v3 キー
INPUT     = "卒業アルバム.xlsx"         # Excelファイルのパス
OUTPUT    = "videos.json"              # 出力JSONのパス
# ─────────────────────────────────────────────────────────────────────────────

# ── playlist → category マッピング ──────────────────────────────────────────
CATEGORY_MAP = {
    "GUILTY GEAR": "格ゲー",
    "GGST": "格ゲー",
    "スト6": "格ゲー",
    "ドラクエ": "RPG",
    "ELDEN RING": "RPG",
    "エルデン": "RPG",
    "biohazard": "ホラー",
    "BIOHAZARD": "ホラー",
    "バイオ": "ホラー",
    "シャドバ": "カードゲーム",
    "Minecraft": "マイクラ",
    "マイクラ": "マイクラ",
    "ReAcT": "コラボ",
    "雑談": "雑談",
    "記念": "記念配信",
    "メン限": "メン限",
    "メンバーシップ": "メン限",
    "ショート": "ショート",
    "短編": "その他",
    "VLOG": "その他",
    "公式切り抜き": "その他",
    "ARC Raiders": "その他",
    "雀魂": "その他",
    "Dead by Daylight": "その他",
}

# 除外するシート
SKIP_SHEETS = {"workspace", "🏠 トップ", "VALORANT"}


def get_category(playlist: str) -> str:
    for keyword, category in CATEGORY_MAP.items():
        if keyword in playlist:
            return category
    return "その他"


def get_status(playlist: str) -> str:
    if "完結" in playlist:
        return "completed"
    if "進行中" in playlist:
        return "ongoing"
    return "ongoing"


def is_members(playlist: str, title: str) -> bool:
    return "メン限" in playlist or "メンバーシップ" in playlist or "メン限" in title


def extract_video_id(url: str) -> str | None:
    if not isinstance(url, str):
        return None
    patterns = [
        r"youtu\.be/([A-Za-z0-9_\-]{11})",
        r"youtube\.com/watch\?v=([A-Za-z0-9_\-]{11})",
        r"youtube\.com/shorts/([A-Za-z0-9_\-]{11})",
    ]
    for p in patterns:
        m = re.search(p, url)
        if m:
            return m.group(1)
    return None


def parse_date(raw) -> str | None:
    if pd.isna(raw):
        return None
    s = str(int(raw)) if isinstance(raw, float) else str(raw).strip()
    if len(s) == 6:
        try:
            return datetime.strptime("20" + s, "%Y%m%d").strftime("%Y-%m-%d")
        except ValueError:
            pass
    return None


def make_slug(playlist: str, index: int) -> str:
    slug = re.sub(r"[^\w\-]", "-", playlist)[:20].strip("-")
    return f"{slug}-{index:03d}"


# ── YouTube API ───────────────────────────────────────────────────────────────
def fetch_durations(video_ids: list[str], api_key: str) -> dict[str, int]:
    """videoId → 秒数 の辞書を返す（50件ずつバッチ処理）"""
    result = {}
    for i in range(0, len(video_ids), 50):
        batch = video_ids[i : i + 50]
        params = {
            "part": "contentDetails",
            "id": ",".join(batch),
            "key": api_key,
        }
        resp = requests.get(
            "https://www.googleapis.com/youtube/v3/videos", params=params, timeout=10
        )
        if resp.status_code != 200:
            print(f"  [API Error] {resp.status_code}: {resp.text[:200]}")
            continue
        for item in resp.json().get("items", []):
            vid = item["id"]
            iso = item["contentDetails"]["duration"]  # e.g. PT1H23M45S
            m = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso)
            if m:
                h, mn, s = (int(x or 0) for x in m.groups())
                result[vid] = h * 3600 + mn * 60 + s
        print(f"  取得済み: {len(result)} 件 ({i + len(batch)}/{len(video_ids)})")
        time.sleep(0.1)
    return result


# ── メイン ────────────────────────────────────────────────────────────────────
def main():
    if API_KEY == "YOUR_API_KEY_HERE":
        print("❌ API_KEY を設定してください（スクリプト上部）")
        return

    xlsx_path = Path(INPUT)
    if not xlsx_path.exists():
        print(f"❌ ファイルが見つかりません: {xlsx_path}")
        return

    print(f"📂 読み込み中: {xlsx_path}")
    all_sheets = pd.read_excel(xlsx_path, sheet_name=None, header=None)


    videos = []
    for sheet_name, df in all_sheets.items():
        if sheet_name in SKIP_SHEETS:
            continue

        # ヘッダー行を探す（「配信日 (YYMMDD)」がある行）
        header_row = None
        for idx, row in df.iterrows():
            if any("配信日" in str(cell) for cell in row if pd.notna(cell)):
                header_row = idx
                break
        if header_row is None:
            continue

        # header_row の次の行からデータ取得
        data_rows = df.iloc[header_row + 1 :].reset_index(drop=True)

        count = 0
        for _, row in data_rows.iterrows():
            date_raw = row.iloc[0] if len(row) > 0 else None
            title = str(row.iloc[1]).strip() if len(row) > 1 and pd.notna(row.iloc[1]) else None
            url = str(row.iloc[2]).strip() if len(row) > 2 and pd.notna(row.iloc[2]) else None

            # 無効行スキップ
            if not title or not url:
                continue
            if "トップへ戻る" in title or title == "nan":
                continue

            video_id = extract_video_id(url)
            date_str = parse_date(date_raw)
            members = is_members(sheet_name, title)

            count += 1
            videos.append(
                {
                    "id": make_slug(sheet_name, count),
                    "date": date_str,
                    "title": title,
                    "url": url,
                    "videoId": video_id,
                    "thumbnailUrl": (
                        f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg"
                        if video_id
                        else None
                    ),
                    "playlist": sheet_name,
                    "category": get_category(sheet_name),
                    "status": get_status(sheet_name),
                    "isMembers": members,
                    "duration": None,  # API で後から埋める
                    "tags": [],
                    "collab": [],
                }
            )

    print(f"✅ 読み込み完了: {len(videos)} 件")

    # YouTube API で duration 取得
    valid_ids = [v["videoId"] for v in videos if v["videoId"]]
    unique_ids = list(dict.fromkeys(valid_ids))  # 重複除去・順序保持
    print(f"🎬 YouTube API で duration 取得中... ({len(unique_ids)} 件)")
    duration_map = fetch_durations(unique_ids, API_KEY)

    # duration を埋める
    filled = sum(
        1
        for v in videos
        if v["videoId"] and duration_map.get(v["videoId"]) is not None
    )
    for v in videos:
        if v["videoId"]:
            v["duration"] = duration_map.get(v["videoId"])

    print(f"✅ duration 取得完了: {filled}/{len(videos)} 件")

    # 出力
    output_path = Path(OUTPUT)
    output_path.write_text(
        json.dumps(videos, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"💾 保存完了: {output_path}  ({len(videos)} 件)")

    # サマリー
    by_category = {}
    for v in videos:
        by_category.setdefault(v["category"], 0)
        by_category[v["category"]] += 1
    print("\n📊 カテゴリ別件数:")
    for cat, cnt in sorted(by_category.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {cnt} 件")


if __name__ == "__main__":
    main()

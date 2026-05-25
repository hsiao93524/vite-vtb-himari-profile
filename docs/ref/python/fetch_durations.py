"""
結萌ひまり 配信アーカイブ
Excel → JSON 変換 + YouTube API で duration / visibility 取得スクリプト

【今回の変更点】
  - category    削除・値を tags の初期値として移行
  - status      削除
  - isMembers   → isMembersOnly に改名（boolean 必須）
  - isDeleted   削除・visibility に統合
  - playlist    → string[]（複数 playlist 対応・重複マージ）
  - visibility  追加: 'public' | 'unlisted' | 'unavailable'
                  unavailable = 削除済み or 非公開（API で取得不能）
  - duration    YouTube API で自動取得

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

# ── 設定 ─────────────────────────────────────────────────────────────────────
API_KEY   = "YOUR_API_KEY_HERE"        # YouTube Data API v3 キー
INPUT     = "卒業アルバム.xlsx"         # Excelファイルのパス
OUTPUT    = "videos.json"              # 出力JSONのパス
# ─────────────────────────────────────────────────────────────────────────────

# ── category → tags 変換マップ ───────────────────────────────────────────────
# Excel シート名から自動推定した category を tags の初期値として使う
# キーワードが一致した最初のものを採用（順序重要）
CATEGORY_TAG_MAP: list[tuple[str, str]] = [
    ("GUILTY GEAR", "格ゲー"),
    ("GGST",        "格ゲー"),
    ("スト6",       "格ゲー"),
    ("ドラクエ",    "RPG"),
    ("ELDEN RING",  "RPG"),
    ("エルデン",    "RPG"),
    ("biohazard",   "ホラー"),
    ("BIOHAZARD",   "ホラー"),
    ("バイオ",      "ホラー"),
    ("シャドバ",    "カードゲーム"),
    ("Minecraft",   "マイクラ"),
    ("マイクラ",    "マイクラ"),
    ("ReAcT",       "コラボ"),
    ("コラボ",      "コラボ"),
    ("雑談",        "雑談"),
    ("記念",        "記念配信"),
    ("メン限",      "メン限"),
    ("メンバーシップ", "メン限"),
    ("ショート",    "ショート"),
    ("短編",        "その他"),
    ("VLOG",        "その他"),
    ("公式切り抜き",    "その他"),
    ("ARC Raiders", "その他"),
    ("雀魂",        "その他"),
    ("Dead by Daylight",     "その他"),
    ("Vlog",        "その他"),
]
# 除外するシート
SKIP_SHEETS = {"workspace", "🏠 トップ", "VALORANT"}


# merge category to tags and init tags by guessing contents
def playlist_to_initial_tags(playlist: str) -> list[str]:
    """シート名からカテゴリタグを推定して返す"""
    for keyword, tag in CATEGORY_TAG_MAP:
        if keyword in playlist:
            return [tag]
    return ["その他"]


# ── ユーティリティ ────────────────────────────────────────────────────────────
def is_members_only(playlist: str, title: str) -> bool:
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
def fetch_video_info(video_ids: list[str], api_key: str) -> dict[str, dict]:
    """
    videoId → { duration: int, visibility: str } を返す

    visibility の判定:
      - API レスポンスに含まれる → 'public' or 'unlisted'
        (status.privacyStatus が 'public' / 'unlisted' / 'private')
        ※ private は本来 API キーだけでは取得できないが、
           取得できた場合は 'unlisted' として扱う
      - API レスポンスに含まれない（items に存在しない）→ 'unavailable'
        （削除済み or 非公開でアクセス不能）
    """
    result: dict[str, dict] = {}

    for i in range(0, len(video_ids), 50):
        batch = video_ids[i : i + 50]
        params = {
            "part": "contentDetails,status",
            "id":   ",".join(batch),
            "key":  api_key,
        }
        resp = requests.get(
            "https://www.googleapis.com/youtube/v3/videos",
            params=params,
            timeout=10,
        )
        if resp.status_code != 200:
            print(f"  [API Error] {resp.status_code}: {resp.text[:200]}")
            continue

        for item in resp.json().get("items", []):
            vid = item["id"]

            # duration
            iso = item["contentDetails"]["duration"]  # e.g. PT1H23M45S
            m = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso)
            dur = 0
            if m:
                h, mn, s = (int(x or 0) for x in m.groups())
                dur = h * 3600 + mn * 60 + s

            # visibility
            privacy = item.get("status", {}).get("privacyStatus", "")
            if privacy == "public":
                vis = "public"
            else:
                # unlisted / private（取得できた = 最低限アクセス可能）
                vis = "unlisted"

            result[vid] = {"duration": dur, "visibility": vis}

        print(
            f"  取得済み: {len(result)} 件 ({i + len(batch)}/{len(video_ids)})"
        )
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

    videos: list[dict] = []

    for sheet_name, df in all_sheets.items():
        if sheet_name in SKIP_SHEETS:
            continue

        # ヘッダー行を探す
        header_row = None
        for idx, row in df.iterrows():
            if any("配信日" in str(cell) for cell in row if pd.notna(cell)):
                header_row = idx
                break
        if header_row is None:
            continue

        # header_row の次の行からデータ取得
        data_rows = df.iloc[header_row + 1 :].reset_index(drop=True)
        initial_tags = playlist_to_initial_tags(sheet_name)

        count = 0
        for _, row in data_rows.iterrows():
            date_raw = row.iloc[0] if len(row) > 0 else None
            title    = str(row.iloc[1]).strip() if len(row) > 1 and pd.notna(row.iloc[1]) else None
            url      = str(row.iloc[2]).strip() if len(row) > 2 and pd.notna(row.iloc[2]) else None

            # 無効行スキップ
            if not title or not url:
                continue
            if "トップへ戻る" in title or title == "nan":
                continue

            video_id = extract_video_id(url)
            date_str = parse_date(date_raw)
            members = is_members_only(sheet_name, title)

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
                    "playlist": [sheet_name],          # string[]
                    "visibility": "public",              # API 取得後に上書き
                    "isMembersOnly": members,
                    "duration": None,                  # API 取得後に上書き
                    "tags": list(initial_tags),    # category 由来の初期値
                    "collab": [],
                }
            )

    print(f"✅ 読み込み完了: {len(videos)} 件（マージ前）")

    # ── 同一 videoId の playlist をマージ ────────────────────────────────────
    merged: dict[str, dict] = {}
    no_id_list: list[dict] = []

    for v in videos:
        vid = v["videoId"]
        if vid is None:
            no_id_list.append(v)
            continue
        if vid in merged:
            for pl in v["playlist"]:
                if pl not in merged[vid]["playlist"]:
                    merged[vid]["playlist"].append(pl)
            # tags も追記（重複除去）
            for tag in v["tags"]:
                if tag not in merged[vid]["tags"]:
                    merged[vid]["tags"].append(tag)
        else:
            merged[vid] = v

    videos = list(merged.values()) + no_id_list
    print(f"✅ 重複マージ後: {len(videos)} 件")

    # ── YouTube API で duration / visibility 取得 ─────────────────────────────
    valid_ids = [v["videoId"] for v in videos if v["videoId"]]
    print(f"🎬 YouTube API で情報取得中... ({len(valid_ids)} 件)")
    info_map = fetch_video_info(valid_ids, API_KEY)

    filled_dur = 0
    unavailable = 0
    for v in videos:
        vid = v["videoId"]
        if vid:
            if vid in info_map:
                v["duration"]   = info_map[vid]["duration"]
                v["visibility"] = info_map[vid]["visibility"]
                filled_dur += 1
            else:
                # API に存在しない = 削除済み or 非公開
                v["duration"]   = None
                v["visibility"] = "unavailable"
                unavailable += 1

    print(f"✅ duration 取得完了  : {filled_dur} 件")
    print(f"⚠️  unavailable       : {unavailable} 件（削除済み or 非公開）")

    # ── 出力 ─────────────────────────────────────────────────────────────────
    output_path = Path(OUTPUT)
    output_path.write_text(
        json.dumps(videos, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"\n💾 保存完了: {output_path}  ({len(videos)} 件)")

    # ── サマリー ─────────────────────────────────────────────────────────────
    vis_count: dict[str, int] = {}
    for v in videos:
        k = v["visibility"]
        vis_count[k] = vis_count.get(k, 0) + 1

    members_cnt  = sum(1 for v in videos if v["isMembersOnly"])
    multi_pl_cnt = sum(1 for v in videos if len(v["playlist"]) > 1)

    print("\n📊 サマリー:")
    print(f"  総件数          : {len(videos)}")
    for vis, cnt in sorted(vis_count.items()):
        print(f"  visibility={vis:<12}: {cnt}")
    print(f"  isMembersOnly   : {members_cnt}")
    print(f"  複数playlist    : {multi_pl_cnt}")
    print(f"  duration null   : {sum(1 for v in videos if v['duration'] is None)}")
    print("\n出力欄位:")
    print("  id / date / title / url / videoId / thumbnailUrl")
    print("  playlist(string[]) / isMembersOnly / visibility / duration / tags / collab")
    print("削除欄位: category / status / isMembers / isDeleted")


if __name__ == "__main__":
    main()

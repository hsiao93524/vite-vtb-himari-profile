"""
結萌ひまり 配信アーカイブ
videos.json マイグレーションスクリプト

【変換内容】
  1. category  → tags に移行（tags が空なら category の値を初期値として追加）、欄位削除
  2. status    → 欄位削除
  3. isMembers → isMembersOnly に改名
  4. isDeleted → visibility に変換
                  isDeleted=false → "public"
                  isDeleted=true  → "unavailable"
                 （欄位がない場合も "public" として補完）
  5. playlist  → string[] に変換（string の場合は [string] に包む）

使い方:
  python migrate_videos.py
  python migrate_videos.py --input videos.json --output videos.json
  python migrate_videos.py --input videos.json --output videos_migrated.json --dry-run
"""

import json
import argparse
from pathlib import Path
from copy import deepcopy

# ── category → tag 変換マップ ─────────────────────────────────────────────────
# 旧 category の値をそのまま tags に入れる（値が一致するものをマッピング）
# videos.json に存在する category 値をすべて列挙
KNOWN_CATEGORIES = {
    "格ゲー", "RPG", "ホラー", "カードゲーム", "マイクラ",
    "コラボ", "雑談", "記念配信", "メン限", "ショート", "その他",
}

# ── マイグレーション本体 ───────────────────────────────────────────────────────

def migrate_one(v: dict) -> dict:
    """1件の video レコードをマイグレーションして返す（元データは変更しない）"""
    r = deepcopy(v)

    # ── 1. category → tags ───────────────────────────────────────────────────
    old_category = r.pop("category", None)
    if old_category:
        tags = r.get("tags", [])
        if isinstance(tags, list):
            if old_category not in tags:
                tags.insert(0, old_category)   # 先頭に追加
            r["tags"] = tags
        else:
            r["tags"] = [old_category]

    # ── 2. status 削除 ───────────────────────────────────────────────────────
    r.pop("status", None)

    # ── 3. isMembers → isMembersOnly ────────────────────────────────────────
    if "isMembers" in r:
        old_val = r.pop("isMembers")
        # isMembersOnly がすでにある場合は上書きしない
        if "isMembersOnly" not in r:
            r["isMembersOnly"] = bool(old_val)
    elif "isMembersOnly" not in r:
        # 両方ない場合はデフォルト false
        r["isMembersOnly"] = False

    # ── 4. isDeleted → visibility ────────────────────────────────────────────
    if "isDeleted" in r:
        is_deleted = r.pop("isDeleted")
        if "visibility" not in r:
            r["visibility"] = "unavailable" if is_deleted else "public"
    elif "visibility" not in r:
        r["visibility"] = "public"

    # ── 5. playlist: string → string[] ──────────────────────────────────────
    playlist = r.get("playlist")
    if isinstance(playlist, str):
        r["playlist"] = [playlist]
    elif playlist is None:
        r["playlist"] = []

    # ── 欄位の並び順を整理（読みやすさのため） ──────────────────────────────
    ordered_keys = [
        "id", "date", "title", "url", "videoId", "thumbnailUrl",
        "playlist", "isMembersOnly", "visibility",
        "duration", "tags", "collab",
    ]
    ordered = {}
    for k in ordered_keys:
        if k in r:
            ordered[k] = r[k]
    # 上記以外の未知フィールドも残す（将来の拡張に備えて）
    for k, val in r.items():
        if k not in ordered:
            ordered[k] = val

    return ordered


def migrate(videos: list[dict]) -> tuple[list[dict], dict]:
    """全件マイグレーション。変換後リストと統計情報を返す"""
    result = []
    stats = {
        "total": len(videos),
        "category_migrated": 0,
        "status_removed": 0,
        "isMembers_renamed": 0,
        "isDeleted_converted": 0,
        "isDeleted_true": 0,
        "playlist_wrapped": 0,
        "unknown_fields": set(),
    }

    known_fields = {
        "id", "date", "title", "url", "videoId", "thumbnailUrl",
        "playlist", "isMembersOnly", "isMembers", "isDeleted", "visibility",
        "category", "status", "duration", "tags", "collab", "note",
    }

    for v in videos:
        # 統計
        if v.get("category"):
            stats["category_migrated"] += 1
        if "status" in v:
            stats["status_removed"] += 1
        if "isMembers" in v:
            stats["isMembers_renamed"] += 1
        if "isDeleted" in v:
            stats["isDeleted_converted"] += 1
            if v["isDeleted"]:
                stats["isDeleted_true"] += 1
        if isinstance(v.get("playlist"), str):
            stats["playlist_wrapped"] += 1

        # 未知フィールドの検出
        for k in v:
            if k not in known_fields:
                stats["unknown_fields"].add(k)

        result.append(migrate_one(v))

    stats["unknown_fields"] = sorted(stats["unknown_fields"])
    return result, stats


# ── メイン ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="videos.json マイグレーション")
    parser.add_argument("--input",   default="videos.json",          help="入力ファイル")
    parser.add_argument("--output",  default="videos.json",          help="出力ファイル（デフォルトは上書き）")
    parser.add_argument("--dry-run", action="store_true",            help="変換結果を表示するだけで保存しない")
    args = parser.parse_args()

    input_path  = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        print(f"❌ ファイルが見つかりません: {input_path}")
        return

    print(f"📂 読み込み中: {input_path}")
    videos = json.loads(input_path.read_text(encoding="utf-8"))
    print(f"   {len(videos)} 件読み込み完了")

    # マイグレーション実行
    migrated, stats = migrate(videos)

    # ── サマリー表示 ─────────────────────────────────────────────────────────
    print("\n📊 変換サマリー:")
    print(f"  総件数                    : {stats['total']}")
    print(f"  category → tags 移行      : {stats['category_migrated']} 件")
    print(f"  status 削除               : {stats['status_removed']} 件")
    print(f"  isMembers → isMembersOnly : {stats['isMembers_renamed']} 件")
    print(f"  isDeleted → visibility    : {stats['isDeleted_converted']} 件")
    print(f"    うち isDeleted=true      : {stats['isDeleted_true']} 件 → visibility='unavailable'")
    print(f"  playlist string→[]        : {stats['playlist_wrapped']} 件")

    if stats["unknown_fields"]:
        print(f"\n⚠️  未知フィールドを検出: {stats['unknown_fields']}")
        print("   → 変換後もそのまま保持しています。意図的なフィールドか確認してください。")

    # ── 変換後サンプル（先頭3件）────────────────────────────────────────────
    print("\n🔍 変換後サンプル（先頭3件）:")
    for v in migrated[:3]:
        print(f"  [{v.get('id')}]")
        print(f"    playlist     : {v.get('playlist')}")
        print(f"    isMembersOnly: {v.get('isMembersOnly')}")
        print(f"    visibility   : {v.get('visibility')}")
        print(f"    tags         : {v.get('tags')}")
        print(f"    has category : {'category' in v}")
        print(f"    has status   : {'status' in v}")
        print(f"    has isMembers: {'isMembers' in v}")
        print(f"    has isDeleted: {'isDeleted' in v}")

    # ── 保存 ─────────────────────────────────────────────────────────────────
    if args.dry_run:
        print(f"\n⏭️  --dry-run モード: {output_path} への保存をスキップしました")
        return

    output_path.write_text(
        json.dumps(migrated, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"\n💾 保存完了: {output_path}  ({len(migrated)} 件)")
    print("\n✅ 出力欄位: id / date / title / url / videoId / thumbnailUrl")
    print("             playlist(string[]) / isMembersOnly / visibility / duration / tags / collab")
    print("🗑️  削除欄位: category / status / isMembers / isDeleted")


if __name__ == "__main__":
    main()

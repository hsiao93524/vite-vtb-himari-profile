"""
結萌ひまり 配信アーカイブ
videos.json チェッカー → videos_check.html 生成

使い方:
  python check.py
  python check.py --input videos.json --output videos_check.html
"""

import json
import sys
from pathlib import Path

INPUT  = "videos.json"
OUTPUT = "videos_check.html"

def fmt_duration(sec):
    if sec is None:
        return None
    sec = int(sec)
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"

def check_video(v):
    warnings = []
    if not v.get("date"):
        warnings.append("date が null")
    if not v.get("videoId"):
        warnings.append("videoId が取れていない")
    if v.get("duration") is None:
        warnings.append("duration が null")
    if not v.get("title"):
        warnings.append("title が空")
    if not v.get("url"):
        warnings.append("url が空")
    return warnings

def main():
    path = Path(INPUT)
    if not path.exists():
        print(f"❌ {INPUT} が見つかりません")
        sys.exit(1)

    videos = json.loads(path.read_text(encoding="utf-8"))
    print(f"✅ {len(videos)} 件読み込み完了")

    # 統計
    total = len(videos)
    no_duration = sum(1 for v in videos if v.get("duration") is None)
    no_video_id = sum(1 for v in videos if not v.get("videoId"))
    no_date     = sum(1 for v in videos if not v.get("date"))
    no_tags     = sum(1 for v in videos if not v.get("tags"))
    no_collab   = sum(1 for v in videos if not v.get("collab"))
    has_warning = sum(1 for v in videos if check_video(v))

    categories = {}
    for v in videos:
        cat = v.get("category", "不明")
        categories[cat] = categories.get(cat, 0) + 1

    # テーブル行生成
    rows_html = ""
    for i, v in enumerate(videos):
        warnings = check_video(v)
        row_class = "row-warn" if warnings else "row-ok"
        warn_html = "".join(f'<span class="badge-warn">⚠ {w}</span>' for w in warnings)

        tags_html   = ", ".join(v.get("tags", [])) or '<span class="empty">—</span>'
        collab_html = ", ".join(v.get("collab", [])) or '<span class="empty">—</span>'
        dur_fmt     = fmt_duration(v.get("duration")) or '<span class="null">null</span>'
        date_val    = v.get("date") or '<span class="null">null</span>'
        vid_id      = v.get("videoId") or '<span class="null">null</span>'

        thumb = ""
        if v.get("videoId"):
            thumb = f'<img class="thumb" src="{v["thumbnailUrl"]}" loading="lazy" alt="">'

        title_link = f'<a href="{v["url"]}" target="_blank">{v["title"]}</a>' if v.get("url") else v.get("title", "")

        rows_html += f"""
        <tr class="{row_class}" data-category="{v.get('category','')}" data-warn="{'1' if warnings else '0'}">
          <td class="col-num">{i+1}</td>
          <td class="col-thumb">{thumb}</td>
          <td class="col-title">
            {title_link}
            <div class="warn-list">{warn_html}</div>
          </td>
          <td class="col-date">{date_val}</td>
          <td class="col-cat"><span class="badge-cat cat-{v.get('category','その他')}">{v.get('category','')}</span></td>
          <td class="col-playlist" title="{v.get('playlist','')}">{v.get('playlist','')[:20]}{"…" if len(v.get('playlist',''))>20 else ""}</td>
          <td class="col-dur">{dur_fmt}</td>
          <td class="col-vid">{vid_id}</td>
          <td class="col-members">{"✅" if v.get("isMembers") else "—"}</td>
          <td class="col-tags">{tags_html}</td>
          <td class="col-collab">{collab_html}</td>
        </tr>"""

    # カテゴリ別バッジ
    cat_filter_html = '<button class="filter-btn active" onclick="filterCat(this, \'\')" >すべて</button>'
    for cat, cnt in sorted(categories.items(), key=lambda x: -x[1]):
        cat_filter_html += f'<button class="filter-btn cat-btn-{cat}" onclick="filterCat(this, \'{cat}\')">{cat} <span class="cnt">{cnt}</span></button>'

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>videos.json チェッカー — 結萌ひまり</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=JetBrains+Mono:wght@400;600&display=swap');

  :root {{
    --bg: #0f0f13;
    --surface: #1a1a22;
    --surface2: #22222e;
    --border: #2e2e3e;
    --text: #e8e8f0;
    --text-dim: #7a7a9a;
    --accent: #c084fc;
    --accent2: #f0abfc;
    --ok: #4ade80;
    --warn: #fb923c;
    --null: #f87171;
    --mono: 'JetBrains Mono', monospace;
    --sans: 'Noto Sans JP', sans-serif;
  }}

  * {{ box-sizing: border-box; margin: 0; padding: 0; }}

  body {{
    background: var(--bg);
    color: var(--text);
    font-family: var(--sans);
    font-size: 13px;
    line-height: 1.5;
  }}

  /* ヘッダー */
  .header {{
    padding: 28px 32px 20px;
    border-bottom: 1px solid var(--border);
    background: linear-gradient(135deg, #1a0a2e 0%, #0f0f13 60%);
  }}
  .header h1 {{
    font-size: 20px;
    font-weight: 700;
    color: var(--accent2);
    letter-spacing: 0.05em;
    margin-bottom: 4px;
  }}
  .header p {{ color: var(--text-dim); font-size: 12px; }}

  /* 統計カード */
  .stats {{
    display: flex;
    gap: 12px;
    padding: 20px 32px;
    flex-wrap: wrap;
    border-bottom: 1px solid var(--border);
  }}
  .stat-card {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 12px 18px;
    min-width: 110px;
    text-align: center;
  }}
  .stat-card .val {{
    font-size: 26px;
    font-weight: 700;
    font-family: var(--mono);
    line-height: 1.2;
  }}
  .stat-card .label {{ color: var(--text-dim); font-size: 11px; margin-top: 2px; }}
  .val-ok    {{ color: var(--ok); }}
  .val-warn  {{ color: var(--warn); }}
  .val-null  {{ color: var(--null); }}
  .val-dim   {{ color: var(--text-dim); }}

  /* フィルター */
  .filters {{
    padding: 16px 32px;
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    align-items: center;
    border-bottom: 1px solid var(--border);
  }}
  .filter-label {{ color: var(--text-dim); font-size: 11px; margin-right: 4px; }}
  .filter-btn {{
    background: var(--surface2);
    border: 1px solid var(--border);
    color: var(--text-dim);
    border-radius: 20px;
    padding: 4px 12px;
    font-size: 12px;
    cursor: pointer;
    font-family: var(--sans);
    transition: all 0.15s;
  }}
  .filter-btn:hover {{ border-color: var(--accent); color: var(--text); }}
  .filter-btn.active {{ background: var(--accent); border-color: var(--accent); color: #0f0f13; font-weight: 700; }}
  .filter-btn .cnt {{ opacity: 0.7; }}
  .warn-toggle {{
    margin-left: auto;
    background: var(--surface2);
    border: 1px solid var(--warn);
    color: var(--warn);
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 12px;
    cursor: pointer;
    font-family: var(--sans);
    transition: all 0.15s;
  }}
  .warn-toggle.active {{ background: var(--warn); color: #0f0f13; font-weight: 700; }}

  /* テーブル */
  .table-wrap {{
    overflow-x: auto;
    padding: 0 32px 32px;
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 16px;
  }}
  th {{
    background: var(--surface2);
    color: var(--text-dim);
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 10px 12px;
    text-align: left;
    border-bottom: 2px solid var(--border);
    white-space: nowrap;
    position: sticky;
    top: 0;
    z-index: 1;
  }}
  td {{
    padding: 8px 12px;
    border-bottom: 1px solid var(--border);
    vertical-align: middle;
  }}
  tr:hover td {{ background: var(--surface2); }}
  .row-warn td {{ border-left: 3px solid var(--warn); }}
  .row-ok   td {{ border-left: 3px solid transparent; }}

  .col-num   {{ color: var(--text-dim); font-family: var(--mono); width: 40px; }}
  .col-thumb {{ width: 80px; }}
  .col-title {{ max-width: 320px; }}
  .col-title a {{ color: var(--accent2); text-decoration: none; font-size: 12px; }}
  .col-title a:hover {{ text-decoration: underline; }}
  .col-date  {{ font-family: var(--mono); font-size: 12px; white-space: nowrap; }}
  .col-dur   {{ font-family: var(--mono); font-size: 12px; white-space: nowrap; }}
  .col-vid   {{ font-family: var(--mono); font-size: 11px; color: var(--text-dim); }}
  .col-playlist {{ max-width: 160px; font-size: 11px; color: var(--text-dim); }}
  .col-members {{ text-align: center; }}

  .thumb {{
    width: 72px;
    height: 40px;
    object-fit: cover;
    border-radius: 4px;
    border: 1px solid var(--border);
    display: block;
  }}

  .warn-list {{ margin-top: 4px; display: flex; flex-wrap: wrap; gap: 4px; }}
  .badge-warn {{
    background: #431407;
    border: 1px solid var(--warn);
    color: var(--warn);
    border-radius: 4px;
    padding: 1px 6px;
    font-size: 10px;
    white-space: nowrap;
  }}

  .badge-cat {{
    display: inline-block;
    border-radius: 4px;
    padding: 2px 8px;
    font-size: 11px;
    font-weight: 600;
    white-space: nowrap;
  }}
  .cat-格ゲー        {{ background: #1e1b4b; color: #a5b4fc; border: 1px solid #4338ca; }}
  .cat-RPG           {{ background: #14290e; color: #86efac; border: 1px solid #16a34a; }}
  .cat-ホラー        {{ background: #2d0a0a; color: #fca5a5; border: 1px solid #dc2626; }}
  .cat-カードゲーム  {{ background: #1c1207; color: #fcd34d; border: 1px solid #d97706; }}
  .cat-マイクラ      {{ background: #0a1f0a; color: #6ee7b7; border: 1px solid #059669; }}
  .cat-コラボ        {{ background: #1a0a2e; color: #d8b4fe; border: 1px solid #9333ea; }}
  .cat-雑談          {{ background: #111827; color: #9ca3af; border: 1px solid #4b5563; }}
  .cat-記念配信      {{ background: #1f1007; color: #fdba74; border: 1px solid #ea580c; }}
  .cat-メン限        {{ background: #0f1f2e; color: #7dd3fc; border: 1px solid #0284c7; }}
  .cat-ショート      {{ background: #1f1020; color: #f0abfc; border: 1px solid #c026d3; }}
  .cat-その他        {{ background: #1a1a1a; color: #9ca3af; border: 1px solid #374151; }}

  .null  {{ color: var(--null); font-family: var(--mono); }}
  .empty {{ color: var(--text-dim); }}

  .hidden {{ display: none !important; }}

  /* 検索 */
  .search-wrap {{ padding: 0 32px 0; display: flex; gap: 12px; align-items: center; }}
  .search-input {{
    background: var(--surface);
    border: 1px solid var(--border);
    color: var(--text);
    border-radius: 8px;
    padding: 8px 14px;
    font-size: 13px;
    font-family: var(--sans);
    width: 320px;
    outline: none;
    transition: border-color 0.15s;
  }}
  .search-input:focus {{ border-color: var(--accent); }}
  .search-input::placeholder {{ color: var(--text-dim); }}
  .result-count {{ color: var(--text-dim); font-size: 12px; }}
</style>
</head>
<body>

<div class="header">
  <h1>🏵 videos.json チェッカー — 結萌ひまり</h1>
  <p>生成日時: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
</div>

<div class="stats">
  <div class="stat-card">
    <div class="val val-ok">{total}</div>
    <div class="label">総件数</div>
  </div>
  <div class="stat-card">
    <div class="val val-warn">{has_warning}</div>
    <div class="label">⚠ 問題あり</div>
  </div>
  <div class="stat-card">
    <div class="val val-null">{no_duration}</div>
    <div class="label">duration null</div>
  </div>
  <div class="stat-card">
    <div class="val val-null">{no_video_id}</div>
    <div class="label">videoId なし</div>
  </div>
  <div class="stat-card">
    <div class="val val-null">{no_date}</div>
    <div class="label">date null</div>
  </div>
  <div class="stat-card">
    <div class="val val-dim">{no_tags}</div>
    <div class="label">tags 未入力</div>
  </div>
  <div class="stat-card">
    <div class="val val-dim">{no_collab}</div>
    <div class="label">collab 未入力</div>
  </div>
</div>

<div class="search-wrap" style="padding: 16px 32px 0;">
  <input class="search-input" type="text" placeholder="タイトル・IDで検索..." oninput="filterSearch(this.value)">
  <span class="result-count" id="result-count">{total} 件表示中</span>
</div>

<div class="filters">
  <span class="filter-label">カテゴリ</span>
  {cat_filter_html}
  <button class="warn-toggle" id="warn-toggle" onclick="toggleWarnOnly()">⚠ 問題のみ表示</button>
</div>

<div class="table-wrap">
  <table id="main-table">
    <thead>
      <tr>
        <th>#</th>
        <th>サムネ</th>
        <th>タイトル</th>
        <th>日付</th>
        <th>カテゴリ</th>
        <th>Playlist</th>
        <th>Duration</th>
        <th>Video ID</th>
        <th>メン限</th>
        <th>Tags</th>
        <th>Collab</th>
      </tr>
    </thead>
    <tbody id="table-body">
      {rows_html}
    </tbody>
  </table>
</div>

<script>
  let currentCat = '';
  let warnOnly = false;
  let searchQuery = '';

  function applyFilters() {{
    const rows = document.querySelectorAll('#table-body tr');
    let visible = 0;
    rows.forEach(row => {{
      const cat = row.dataset.category;
      const warn = row.dataset.warn === '1';
      const text = row.textContent.toLowerCase();
      const catMatch = !currentCat || cat === currentCat;
      const warnMatch = !warnOnly || warn;
      const searchMatch = !searchQuery || text.includes(searchQuery.toLowerCase());
      if (catMatch && warnMatch && searchMatch) {{
        row.classList.remove('hidden');
        visible++;
      }} else {{
        row.classList.add('hidden');
      }}
    }});
    document.getElementById('result-count').textContent = visible + ' 件表示中';
  }}

  function filterCat(btn, cat) {{
    currentCat = cat;
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    applyFilters();
  }}

  function toggleWarnOnly() {{
    warnOnly = !warnOnly;
    document.getElementById('warn-toggle').classList.toggle('active', warnOnly);
    applyFilters();
  }}

  function filterSearch(val) {{
    searchQuery = val;
    applyFilters();
  }}
</script>
</body>
</html>"""

    out = Path(OUTPUT)
    out.write_text(html, encoding="utf-8")
    print(f"💾 出力完了: {out}")
    print(f"   ⚠ 問題あり: {has_warning} 件 / duration null: {no_duration} 件 / videoId なし: {no_video_id} 件")

if __name__ == "__main__":
    main()

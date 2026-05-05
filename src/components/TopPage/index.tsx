import heroImage from '../../assets/hero.png'
import type { Video } from '../../types/video'

type TopPageProps = {
  videos: Video[]
}

function formatHours(seconds: number) {
  return Math.round(seconds / 3600)
}

export default function TopPage({ videos }: TopPageProps) {
  const membersCount = videos.filter(
    (video) => video.isMembers || video.isMembersOnly,
  ).length
  const totalDuration = videos.reduce(
    (total, video) => total + (video.duration ?? 0),
    0,
  )

  return (
    <section className="hero-section" id="hero">
      <div className="hero-visual">
        <img alt="結萌ひまり archive visual" src={heroImage} />
      </div>
      <div className="hero-content">
        <p className="eyebrow">Vtuber's Archive</p>
        <h1 className="hero-title">
          <span>結萌ひまり</span>
        </h1>
        <p className="hero-copy">
          配信一覧、タグ、統計、関連リンクを一か所にまとめるための React
          アーカイブです。
        </p>
        <div className="hero-actions">
          <a href="https://x.com/RAG_Himari" rel="noreferrer" target="_blank">
            X
          </a>
          <a
            href="https://www.youtube.com/@raghimari"
            rel="noreferrer"
            target="_blank"
          >
            YouTube
          </a>
        </div>
        <p className="last-updated">Last updated: 2026-05-05</p>
      </div>
      <dl className="stats-grid">
        <div>
          <dt>Videos</dt>
          <dd>{videos.length}</dd>
        </div>
        <div>
          <dt>Members</dt>
          <dd>{membersCount}</dd>
        </div>
        <div>
          <dt>Hours</dt>
          <dd>{formatHours(totalDuration)}</dd>
        </div>
      </dl>
    </section>
  )
}

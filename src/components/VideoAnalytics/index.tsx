import PublicationBadge from '../PublicationBadge'
import type { Video } from '../../types/video'

type VideoAnalyticsProps = {
  videos: Video[]
  showInProgress?: boolean
  publicationLabel?: string | null
}

function getPlaylistLabel(playlist: string | string[]) {
  return Array.isArray(playlist) ? playlist[0] : playlist
}

export default function VideoAnalytics({
  publicationLabel,
  videos,
  showInProgress = false,
}: VideoAnalyticsProps) {
  const byPlaylist = Array.from(
    videos.reduce((map, video) => {
      const key = getPlaylistLabel(video.playlist) || 'Unknown'
      map.set(key, (map.get(key) ?? 0) + 1)
      return map
    }, new Map<string, number>()),
  )
    .sort((a, b) => b[1] - a[1])
    .slice(0, 8)

  const maxCount = Math.max(...byPlaylist.map(([, count]) => count), 1)

  return (
    <section className="section-block" id="analytics">
      <div className="section-heading">
        <p className="eyebrow">Video Analyze</p>
        <h2>
          Playlist Distribution
          {publicationLabel && <PublicationBadge>{publicationLabel}</PublicationBadge>}
          {showInProgress && <PublicationBadge>In progress</PublicationBadge>}
        </h2>
      </div>
      <div className="bar-chart" aria-label="Playlist video counts">
        {byPlaylist.map(([playlist, count]) => (
          <div className="bar-row" key={playlist}>
            <span>{playlist}</span>
            <div>
              <i style={{ width: `${(count / maxCount) * 100}%` }} />
            </div>
            <strong>{count}</strong>
          </div>
        ))}
      </div>
    </section>
  )
}

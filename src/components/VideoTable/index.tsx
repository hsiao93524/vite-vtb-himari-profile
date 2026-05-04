import type { Video } from '../../types/video'

type VideoTableProps = {
  videos: Video[]
}

function getPlaylistLabel(playlist: string | string[]) {
  return Array.isArray(playlist) ? playlist.join(' / ') : playlist
}

function formatDuration(seconds: number | null) {
  if (!seconds) {
    return '-'
  }

  const hours = Math.floor(seconds / 3600)
  const minutes = Math.floor((seconds % 3600) / 60)
  return hours > 0 ? `${hours}h ${minutes}m` : `${minutes}m`
}

export default function VideoTable({ videos }: VideoTableProps) {
  return (
    <div className="table-wrap">
      <table className="video-table">
        <thead>
          <tr>
            <th>Date</th>
            <th>Title</th>
            <th>Playlist</th>
            <th>Duration</th>
            <th>Type</th>
          </tr>
        </thead>
        <tbody>
          {videos.map((video) => (
            <tr key={video.id}>
              <td>{video.date}</td>
              <td>
                <a href={video.url} rel="noreferrer" target="_blank">
                  {video.title}
                </a>
              </td>
              <td>{getPlaylistLabel(video.playlist)}</td>
              <td>{formatDuration(video.duration)}</td>
              <td>
                {video.isMembers || video.isMembersOnly ? 'Members' : 'Public'}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

import type { Video } from '../../types/video'

type VideoGalleryProps = {
  videos: Video[]
}

export default function VideoGallery({ videos }: VideoGalleryProps) {
  return (
    <div className="gallery-wrap">
      <div className="gallery-grid">
        {videos.map((video) => (
          <a
            className="video-card"
            href={video.url}
            key={video.id}
            rel="noreferrer"
            target="_blank"
          >
            <img alt="" src={video.thumbnailUrl} />
            <div>
              <p>{video.date}</p>
              <h3>{video.title}</h3>
            </div>
          </a>
        ))}
      </div>
    </div>
  )
}

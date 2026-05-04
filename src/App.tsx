import { useEffect, useState } from 'react'
import './App.css'
import FanartPreview from './components/FanartPreview'
import RelatedLinks from './components/RelatedLinks'
import TagSearcher from './components/TagSearcher'
import TopPage from './components/TopPage'
import VideoAnalytics from './components/VideoAnalytics'
import VideoGallery from './components/VideoGallery'
import VideoTable from './components/VideoTable'
import useVideos from './hooks/useVideos'
import type { ViewMode } from './types/video'

export default function App() {
  const {
    allPlaylists,
    allTags,
    allVideos,
    clearFilters,
    filteredVideos,
    search,
    selectedPlaylists,
    selectedTags,
    setSearch,
    togglePlaylist,
    toggleTag,
  } = useVideos()
  const [viewMode, setViewMode] = useState<ViewMode>('table')

  useEffect(() => {
    console.log(filteredVideos)
  }, [filteredVideos])

  return (
    <main>
      <TopPage videos={allVideos} />

      <section className="section-block" id="videos">
        <div className="section-heading">
          <p className="eyebrow">Video Block</p>
          <h2>配信一覧</h2>
        </div>

        <div className="toolbar">
          <input
            aria-label="Search videos"
            onChange={(event) => setSearch(event.target.value)}
            placeholder="タイトル、playlist、tag で検索"
            type="search"
            value={search}
          />
          <div className="segmented-control" aria-label="View mode">
            <button
              className={viewMode === 'table' ? 'active' : ''}
              onClick={() => setViewMode('table')}
              type="button"
            >
              Table
            </button>
            <button
              className={viewMode === 'gallery' ? 'active' : ''}
              onClick={() => setViewMode('gallery')}
              type="button"
            >
              Gallery
            </button>
          </div>
          <button className="clear-button" onClick={clearFilters} type="button">
            Clear
          </button>
        </div>

        <div className="filter-row" aria-label="Playlist filters">
          {allPlaylists.slice(0, 14).map((playlist) => (
            <button
              className={
                selectedPlaylists.includes(playlist) ? 'tag-pill active' : 'tag-pill'
              }
              key={playlist}
              onClick={() => togglePlaylist(playlist)}
              type="button"
            >
              {playlist}
            </button>
          ))}
        </div>

        <p className="result-count">
          Showing {filteredVideos.length} / {allVideos.length} videos
        </p>

        {viewMode === 'table' ? (
          <VideoTable videos={filteredVideos} />
        ) : (
          <VideoGallery videos={filteredVideos} />
        )}
      </section>

      <VideoAnalytics videos={allVideos} />
      <TagSearcher
        onToggleTag={toggleTag}
        selectedTags={selectedTags}
        tags={allTags}
      />
      <FanartPreview />
      <RelatedLinks />
    </main>
  )
}

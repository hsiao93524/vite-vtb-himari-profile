import { useEffect, useState } from 'react'
import './App.css'
import FanartPreview from './components/FanartPreview'
import RelatedLinks from './components/RelatedLinks'
import TagSearcher from './components/TagSearcher'
import TopPage from './components/TopPage'
import VideoAnalytics from './components/VideoAnalytics'
import VideoGallery from './components/VideoGallery'
import VideoTable from './components/VideoTable'
import PublicationBadge from './components/PublicationBadge'
import {
  getSectionVisibilityLabel,
  isSectionInProgress,
  isSectionVisible,
} from './config/publication'
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
      {isSectionVisible('hero') && (
        <TopPage
          publicationLabel={getSectionVisibilityLabel('hero')}
          videos={allVideos}
        />
      )}

      {isSectionVisible('videos') && (
        <section className="section-block" id="videos">
          <div className="section-heading">
            <p className="eyebrow">Video Block</p>
            <h2>
              配信一覧
              {getSectionVisibilityLabel('videos') && <PublicationBadge>{getSectionVisibilityLabel('videos')}</PublicationBadge>}
              {isSectionInProgress('videos') && <PublicationBadge>In progress</PublicationBadge>}
            </h2>
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
                  selectedPlaylists.includes(playlist)
                    ? 'tag-pill active'
                    : 'tag-pill'
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
      )}

      {isSectionVisible('analytics') && (
        <VideoAnalytics
          publicationLabel={getSectionVisibilityLabel('analytics')}
          showInProgress={isSectionInProgress('analytics')}
          videos={allVideos}
        />
      )}
      {isSectionVisible('tagSearcher') && (
        <TagSearcher
          onToggleTag={toggleTag}
          publicationLabel={getSectionVisibilityLabel('tagSearcher')}
          selectedTags={selectedTags}
          showInProgress={isSectionInProgress('tagSearcher')}
          tags={allTags}
        />
      )}
      {isSectionVisible('fanartPreview') && (
        <FanartPreview
          publicationLabel={getSectionVisibilityLabel('fanartPreview')}
          showInProgress={isSectionInProgress('fanartPreview')}
        />
      )}
      {isSectionVisible('links') && (
        <RelatedLinks publicationLabel={getSectionVisibilityLabel('links')} />
      )}
    </main>
  )
}

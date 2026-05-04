import { useMemo, useState } from 'react'
import rawData from '../data/videos.json'
import type { Video } from '../types/video'

const data = rawData as Video[]

function toList(value: string | string[] | undefined) {
  if (!value) {
    return []
  }

  return Array.isArray(value) ? value : [value]
}

function buildSearchText(video: Video) {
  return [
    video.title,
    video.date,
    video.videoId,
    ...toList(video.playlist),
    video.category,
    ...video.tags,
    ...video.collab,
  ]
    .filter(Boolean)
    .join(' ')
    .toLowerCase()
}

function getVideoTags(video: Video) {
  return Array.from(
    new Set([
      ...video.tags,
      ...video.collab,
      video.category,
      video.isMembers || video.isMembersOnly ? 'Members Only' : undefined,
      video.isDeleted ? 'Deleted' : undefined,
    ].filter(Boolean) as string[]),
  )
}

export default function useVideos() {
  const [search, setSearch] = useState('')
  const [selectedTags, setSelectedTags] = useState<string[]>([])
  const [selectedPlaylists, setSelectedPlaylists] = useState<string[]>([])

  const allTags = useMemo(() => {
    return Array.from(new Set(data.flatMap(getVideoTags))).sort((a, b) =>
      a.localeCompare(b),
    )
  }, [])

  const allPlaylists = useMemo(() => {
    return Array.from(new Set(data.flatMap((video) => toList(video.playlist)))).sort(
      (a, b) => a.localeCompare(b),
    )
  }, [])

  const filteredVideos = useMemo(() => {
    const query = search.trim().toLowerCase()

    return data
      .filter((video) => !query || buildSearchText(video).includes(query))
      .filter((video) => {
        if (selectedTags.length === 0) {
          return true
        }

        const videoTags = getVideoTags(video)
        return selectedTags.every((tag) => videoTags.includes(tag))
      })
      .filter((video) => {
        if (selectedPlaylists.length === 0) {
          return true
        }

        const playlists = toList(video.playlist)
        return selectedPlaylists.some((playlist) => playlists.includes(playlist))
      })
      .sort((a, b) => b.date.localeCompare(a.date))
  }, [search, selectedPlaylists, selectedTags])

  const toggleTag = (tag: string) => {
    setSelectedTags((current) =>
      current.includes(tag)
        ? current.filter((item) => item !== tag)
        : [...current, tag],
    )
  }

  const togglePlaylist = (playlist: string) => {
    setSelectedPlaylists((current) =>
      current.includes(playlist)
        ? current.filter((item) => item !== playlist)
        : [...current, playlist],
    )
  }

  const clearFilters = () => {
    setSearch('')
    setSelectedTags([])
    setSelectedPlaylists([])
  }

  return {
    videos: data,
    allVideos: data,
    filteredVideos,
    search,
    setSearch,
    selectedTags,
    setSelectedTags,
    selectedPlaylists,
    setSelectedPlaylists,
    allTags,
    allPlaylists,
    toggleTag,
    togglePlaylist,
    clearFilters,
  }
}

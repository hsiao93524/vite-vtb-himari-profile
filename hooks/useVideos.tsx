// hooks/useVideos.js
import { useState, useMemo } from "react"
import data from "../data/videos.json"

export default function useVideos() {
  const [search, setSearch] = useState("")
  const [selectedTags, setSelectedTags] = useState([])

  const filteredVideos = useMemo(() => {
    return data
      .filter(v => v.title.toLowerCase().includes(search.toLowerCase()))
      .filter(v =>
        selectedTags.length === 0 ||
        selectedTags.every(tag => v.tags.includes(tag))
      )
      .sort((a, b) => b.date.localeCompare(a.date))
  }, [search, selectedTags])

  return {
    videos: data,
    filteredVideos,
    search,
    setSearch,
    selectedTags,
    setSelectedTags,
  }
}
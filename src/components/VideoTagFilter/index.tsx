type VideoTagFilterProps = {
  tags: string[]
  selectedTags: string[]
  onToggleTag: (tag: string) => void
}

export default function VideoTagFilter({
  tags,
  selectedTags,
  onToggleTag,
}: VideoTagFilterProps) {
  if (tags.length === 0) {
    return null
  }

  return (
    <div className="tag-list" aria-label="Video tag filters">
      {tags.slice(0, 36).map((tag) => {
        const isSelected = selectedTags.includes(tag)

        return (
          <button
            className={isSelected ? 'tag-pill active' : 'tag-pill'}
            key={tag}
            onClick={() => onToggleTag(tag)}
            type="button"
          >
            {tag}
          </button>
        )
      })}
    </div>
  )
}

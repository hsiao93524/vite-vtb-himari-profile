type TagSearcherProps = {
  tags: string[]
  selectedTags: string[]
  onToggleTag: (tag: string) => void
}

export default function TagSearcher({
  tags,
  selectedTags,
  onToggleTag,
}: TagSearcherProps) {
  return (
    <section className="section-block" id="tag-searcher">
      <div className="section-heading">
        <p className="eyebrow">Tag Block</p>
        <h2>タグ検索</h2>
      </div>
      <div className="tag-list">
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
    </section>
  )
}

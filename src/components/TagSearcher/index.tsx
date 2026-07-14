import tagSearcherData from '../../data/tag-searcher.json'
import type {
  TagSearchCategory,
  TagSearchData,
  TagSearchEntry,
} from '../../types/tag-searcher'
import PublicationBadge from '../PublicationBadge'

type TagSearcherProps = {
  showInProgress?: boolean
  publicationLabel?: string | null
}

const data = tagSearcherData as TagSearchData

function buildXSearchUrl(query: string) {
  return `https://x.com/search?q=${encodeURIComponent(query)}&src=typed_query`
}

function hasVisibleTag(tag: TagSearchEntry) {
  return tag.label.trim().length > 0 && tag.query.trim().length > 0
}

function hasVisibleCategory(category: TagSearchCategory) {
  return category.label.trim().length > 0 && category.tags.length > 0
}

function getVisibleCategories(categories: TagSearchCategory[]) {
  return categories
    .map((category) => ({
      ...category,
      tags: category.tags.filter(hasVisibleTag),
    }))
    .filter(hasVisibleCategory)
}

export default function TagSearcher({
  publicationLabel,
  showInProgress = false,
}: TagSearcherProps) {
  const visibleCategories = getVisibleCategories(data.categories)

  if (visibleCategories.length === 0) {
    return null
  }

  return (
    <section className="section-block tag-searcher-section" id="tag-searcher">
      <div className="section-heading">
        <p className="eyebrow">Tag Block</p>
        <h2>
          タグ検索
          {publicationLabel && <PublicationBadge>{publicationLabel}</PublicationBadge>}
          {showInProgress && <PublicationBadge>In progress</PublicationBadge>}
        </h2>
      </div>

      <div className="tag-searcher-categories">
        {visibleCategories.map((category) => (
          <section className="tag-searcher-category" key={category.id}>
            <div className="tag-searcher-category-heading">
              <h3>{category.label}</h3>
              {category.description && (
                <p className="tag-searcher-category-description">
                  {category.description}
                </p>
              )}
            </div>

            <div className="tag-searcher-tags">
              {category.tags.map((tag) => (
                <div className="tag-searcher-entry" key={tag.id}>
                  <a
                    className="tag-searcher-link"
                    href={buildXSearchUrl(tag.query)}
                    rel="noreferrer"
                    target="_blank"
                  >
                    {tag.label}
                  </a>
                  {tag.description && (
                    <p className="tag-searcher-tag-description">
                      {tag.description}
                    </p>
                  )}
                </div>
              ))}
            </div>
          </section>
        ))}
      </div>
    </section>
  )
}

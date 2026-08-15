import PublicationBadge from '../PublicationBadge'

const links = [
  {
    href: 'https://x.com/RAG_Himari',
    label: 'X',
  },
  {
    href: 'https://www.youtube.com/@raghimari',
    label: 'YouTube',
  },
]

type RelatedLinksProps = {
  showInProgress?: boolean
  publicationLabel?: string | null
}

export default function RelatedLinks({
  publicationLabel,
  showInProgress = false,
}: RelatedLinksProps) {
  // 260815: reserved for future Recreated Pages description.
  const recreatedPagesDescription = ''

  return (
    <section className="section-block" id="links">
      {/* 260815: section heading uses shared label and description. */}
      <div className="section-heading">
        <h2>
          {/* 260815: reserved for label. */}
          Recreated Pages
          {publicationLabel && <PublicationBadge>{publicationLabel}</PublicationBadge>}
          {showInProgress && <PublicationBadge>In progress</PublicationBadge>}
        </h2>
        {recreatedPagesDescription && (
          <p className="section-description">{recreatedPagesDescription}</p>
        )}
      </div>
      <div className="link-list">
        {links.map((link) => (
          <a href={link.href} key={link.href} rel="noreferrer" target="_blank">
            {link.label}
          </a>
        ))}
      </div>
    </section>
  )
}

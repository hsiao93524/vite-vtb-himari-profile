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
  publicationLabel?: string | null
}

export default function RelatedLinks({ publicationLabel }: RelatedLinksProps) {
  return (
    <section className="section-block" id="links">
      <div className="section-heading">
        <p className="eyebrow">Related Links</p>
        <h2>
          関連リンク集
          {publicationLabel && <PublicationBadge>{publicationLabel}</PublicationBadge>}
        </h2>
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

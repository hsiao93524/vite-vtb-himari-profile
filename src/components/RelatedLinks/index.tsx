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

export default function RelatedLinks() {
  return (
    <section className="section-block" id="links">
      <div className="section-heading">
        <p className="eyebrow">Related Links</p>
        <h2>関連リンク集</h2>
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

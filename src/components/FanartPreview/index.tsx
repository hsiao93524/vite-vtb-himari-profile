import PublicationBadge from '../PublicationBadge'

type FanartPreviewProps = {
  showInProgress?: boolean
  publicationLabel?: string | null
}

export default function FanartPreview({
  publicationLabel,
  showInProgress = false,
}: FanartPreviewProps) {
  // 260815: reserved for future Fanarts description.
  const fanartsDescription = ''

  return (
    <section className="section-block" id="fanart-preview">
      {/* 260815: section heading uses shared label and description. */}
      <div className="section-heading">
        <h2>
          {/* 260815: reserved for label. */}
          Fanart Preview
          {publicationLabel && <PublicationBadge>{publicationLabel}</PublicationBadge>}
          {showInProgress && <PublicationBadge>In progress</PublicationBadge>}
        </h2>
        {fanartsDescription && (
          <p className="section-description">{fanartsDescription}</p>
        )}
      </div>
      <p className="muted">
        Twitter API 方針が決まったら、ここに fanart ギャラリーを接続します。
      </p>
    </section>
  )
}

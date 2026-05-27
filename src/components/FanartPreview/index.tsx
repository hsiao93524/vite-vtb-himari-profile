import PublicationBadge from '../PublicationBadge'

type FanartPreviewProps = {
  showInProgress?: boolean
}

export default function FanartPreview({
  showInProgress = false,
}: FanartPreviewProps) {
  return (
    <section className="section-block" id="fanart-preview">
      <div className="section-heading">
        <p className="eyebrow">Fanarts</p>
        <h2>
          Fanart Preview
          {showInProgress && <PublicationBadge>In progress</PublicationBadge>}
        </h2>
      </div>
      <p className="muted">
        Twitter API 方針が決まったら、ここに fanart ギャラリーを接続します。
      </p>
    </section>
  )
}

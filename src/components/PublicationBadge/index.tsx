import type { ReactNode } from 'react'

type PublicationBadgeProps = {
  children: ReactNode
}

export default function PublicationBadge({ children }: PublicationBadgeProps) {
  return <span className="publication-badge">[{children}]</span>
}

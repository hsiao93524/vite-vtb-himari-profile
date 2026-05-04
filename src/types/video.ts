export type Video = {
  id: string
  date: string
  title: string
  url: string
  videoId: string
  thumbnailUrl: string
  playlist: string | string[]
  category?: string
  status?: string
  isMembers?: boolean
  isMembersOnly?: boolean
  isDeleted?: boolean
  duration: number | null
  tags: string[]
  collab: string[]
  note?: string
}

export type ViewMode = 'table' | 'gallery'

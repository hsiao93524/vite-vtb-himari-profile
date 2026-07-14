export type TagSearchEntry = {
  id: string
  label: string
  query: string
  description?: string
}

export type TagSearchCategory = {
  id: string
  label: string
  description?: string
  tags: TagSearchEntry[]
}

export type TagSearchData = {
  categories: TagSearchCategory[]
}

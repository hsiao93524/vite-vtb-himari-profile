export type PublicationAudience = 'public' | 'hr' | 'development'
export type SectionStatus = 'public' | 'wip-visible' | 'hidden'
export type SectionVisibilityLabel = 'public' | 'limit' | 'hidden'

export const sectionIds = [
  'hero',
  'videos',
  'analytics',
  'tagSearcher',
  'fanartPreview',
  'links',
] as const

export type SectionId = (typeof sectionIds)[number]

const sectionStatus: Record<SectionId, SectionStatus> = {
  hero: 'public',
  videos: 'public',
  analytics: 'wip-visible',
  tagSearcher: 'wip-visible',
  fanartPreview: 'wip-visible',
  links: 'public',
}

function getPublicationAudience(): PublicationAudience {
  const previewAudience = new URLSearchParams(window.location.search).get('view')

  if (
    import.meta.env.DEV &&
    (previewAudience === 'public' || previewAudience === 'hr')
  ) {
    return previewAudience
  }

  if (import.meta.env.DEV) {
    return 'development'
  }

  return import.meta.env.MODE === 'hr' ? 'hr' : 'public'
}

export const publicationAudience = getPublicationAudience()

export function isSectionVisible(sectionId: SectionId) {
  const status = sectionStatus[sectionId]

  if (publicationAudience === 'development') {
    return true
  }

  if (status === 'hidden') {
    return false
  }

  return status === 'public' || publicationAudience === 'hr'
}

export function isSectionInProgress(sectionId: SectionId) {
  return (
    publicationAudience === 'hr' && sectionStatus[sectionId] === 'wip-visible'
  )
}

export function getSectionVisibilityLabel(
  sectionId: SectionId,
): SectionVisibilityLabel | null {
  if (publicationAudience !== 'development') {
    return null
  }

  const status = sectionStatus[sectionId]

  return status === 'wip-visible' ? 'limit' : status
}

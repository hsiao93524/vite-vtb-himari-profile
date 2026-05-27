export type PublicationAudience = 'public' | 'hr'
export type SectionStatus = 'public' | 'wip-visible' | 'hidden'

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
  return import.meta.env.MODE === 'hr' ? 'hr' : 'public'
}

export const publicationAudience = getPublicationAudience()

export function isSectionVisible(sectionId: SectionId) {
  const status = sectionStatus[sectionId]

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

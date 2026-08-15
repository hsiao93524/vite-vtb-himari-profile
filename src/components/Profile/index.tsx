import { useMemo } from 'react'
import heroImage from '../../assets/profile/hero.png'
import expression01 from '../../assets/profile/expressions/expression-01.jpg'
import expression02 from '../../assets/profile/expressions/expression-02.jpg'
import expression03 from '../../assets/profile/expressions/expression-03.jpg'
import expression04 from '../../assets/profile/expressions/expression-04.jpg'
import expression05 from '../../assets/profile/expressions/expression-05.jpg'
import expression06 from '../../assets/profile/expressions/expression-06.jpg'
import expression07 from '../../assets/profile/expressions/expression-07.jpg'
import expression08 from '../../assets/profile/expressions/expression-08.jpg'
import expression09 from '../../assets/profile/expressions/expression-09.jpg'
import expression10 from '../../assets/profile/expressions/expression-10.jpg'
import expression11 from '../../assets/profile/expressions/expression-11.jpg'
import expression12 from '../../assets/profile/expressions/expression-12.jpg'
import expression13 from '../../assets/profile/expressions/expression-13.jpg'
import expression14 from '../../assets/profile/expressions/expression-14.jpg'
import expression15 from '../../assets/profile/expressions/expression-15.jpg'
import PublicationBadge from '../PublicationBadge'
import type { Video } from '../../types/video'
import blockDescriptions from '../../data/block-descriptions.json'
import profile from '../../data/profile.json'
import site from '../../data/site.json'

type ProfileProps = {
  videos: Video[]
  publicationLabel?: string | null
}

function formatHours(seconds: number) {
  return Math.round(seconds / 3600)
}

const expressionImages = [
  expression01,
  expression02,
  expression03,
  expression04,
  expression05,
  expression06,
  expression07,
  expression08,
  expression09,
  expression10,
  expression11,
  expression12,
  expression13,
  expression14,
  expression15,
]

function pickRandomExpressions(images: string[], count = 3) {
  return [...images].sort(() => Math.random() - 0.5).slice(0, count)
}

function getVisibleText(value?: string) {
  return value?.trim() ?? ''
}

function getVisibleProfileLinks(links: typeof profile.links) {
  return links.filter(
    (link) =>
      getVisibleText(link.href) &&
      (getVisibleText(link.label) || getVisibleText(link.shortLabel)),
  )
}

export default function Profile({ publicationLabel, videos }: ProfileProps) {
  const selectedExpressions = useMemo(
    () => pickRandomExpressions(expressionImages, 3),
    [],
  )
  const membersCount = videos.filter(
    (video) => video.isMembers || video.isMembersOnly,
  ).length
  const totalDuration = videos.reduce(
    (total, video) => total + (video.duration ?? 0),
    0,
  )

  const stats = [
    { label: 'VIDEOS', value: videos.length },
    { label: 'MEMBERS', value: membersCount },
    { label: 'HOURS', value: formatHours(totalDuration) },
  ]
  const profileDescription = getVisibleText(profile.description)
  const visibleProfileLinks = getVisibleProfileLinks(profile.links)
  const lastUpdated = getVisibleText(site.lastUpdated)
  const profileBlockLabel = getVisibleText(blockDescriptions.profile.label)
  const profileSectionLabel = profileBlockLabel || `${profile.name} Profile`

  return (
    <section
      aria-label={profileSectionLabel}
      className="profile"
      id="hero"
    >
      <div className="profile-character">
        <img alt={`${profile.name} 全身視覺`} src={heroImage} />
      </div>

      <div className="profile-content">
        <h1 className="profile-name">
          <span className="profile-name-text">
            <span>{profile.name}</span>
          </span>
          <span className="profile-name-trails" aria-hidden="true">
            <span className="profile-name-trail profile-name-trail-primary" />
            <span className="profile-name-trail profile-name-trail-secondary" />
            <span className="profile-name-trail profile-name-trail-tertiary" />
          </span>
        </h1>
        {publicationLabel && (
          <p className="profile-publication">
            <PublicationBadge>{publicationLabel}</PublicationBadge>
          </p>
        )}
        {profileDescription && (
          <p className="profile-copy">
            {profileDescription}
          </p>
        )}
        <p className="profile-graduation">
          Active: {profile.debutDate}~{profile.graduationDate}
        </p>
        <div className="profile-middle">
          {visibleProfileLinks.length > 0 && (
            <nav className="profile-links" aria-label="Official Profile links">
              {visibleProfileLinks.map((link) => (
                <a
                  className={`profile-link profile-link-${link.kind}`}
                  href={link.href}
                  key={link.href}
                  rel="noreferrer"
                  target="_blank"
                >
                  <span className="visually-hidden">{link.label}</span>
                  {link.shortLabel || link.label}
                </a>
              ))}
            </nav>
          )}

          <div className="profile-expressions" aria-label="表情差分預覽">
            {selectedExpressions.map((src, index) => (
              <div className="profile-expression" key={src}>
                <img alt={`${profile.name} 表情差分 ${index + 1}`} src={src} />
              </div>
            ))}
          </div>
        </div>

        <dl className="profile-stats" aria-label="統計資訊">
          {stats.map((item) => (
            <div className="profile-stat" key={item.label}>
              <dt>{item.label}</dt>
              <dd>{item.value.toLocaleString('en-US')}</dd>
            </div>
          ))}
        </dl>
      </div>

      {lastUpdated && (
        <p className="profile-updated">Last updated: {lastUpdated}</p>
      )}
    </section>
  )
}

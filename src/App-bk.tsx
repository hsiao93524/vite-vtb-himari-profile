import './App.css'
import useVideos from './hooks/useVideos'

function App() {
  const { filteredVideos } = useVideos()

  console.log(filteredVideos)

  return (
    <main>
      <section id="hero" />
      <section id="videos" />
      <section id="analytics" />
      <section id="links" />
    </main>
  )
}

export default App

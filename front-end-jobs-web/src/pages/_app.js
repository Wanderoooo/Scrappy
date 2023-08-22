import '@/styles/globals.css'
import Navbar from '../components/Navbar'


export default function App({ Component, pageProps }) {
  return (
    <div className="main">
      <Navbar className="comps"/>
      <Component {...pageProps} className="comps"/>
    </div>
  )
}

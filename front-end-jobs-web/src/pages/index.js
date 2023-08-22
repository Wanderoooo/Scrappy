import Head from 'next/head'
import Image from 'next/image'
import { Inter, Roboto_Flex } from 'next/font/google'
import styles from '@/styles/Home.module.css'
import Wave from 'react-wavify'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  
return (
  <div className='index'>
    <h1 className='title'>Front End Jobs Data</h1>
    <p className='p'>Land a position informed with job location, skill expectations, and level of commitment</p>
    <Wave fill="url(#gradient)" options={{
          height: 0.1,
          amplitude: 60,
          speed: 0.2,
          points: 3
        }} className='wave'>
  <defs>
    <linearGradient id="gradient" gradientTransform="rotate(90)">
      <stop offset="10%"  stopColor="#d4af37" />
      <stop offset="90%" stopColor="#f00" />
    </linearGradient>
  </defs>
</Wave>
  </div>
)
  
}

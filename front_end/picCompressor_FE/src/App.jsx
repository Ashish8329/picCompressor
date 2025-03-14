import { useState } from 'react'
import './App.css'
import Navbar from './components/Navbar'
import Button from './components/Button'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <Navbar />
    </>
  )
}

export default App

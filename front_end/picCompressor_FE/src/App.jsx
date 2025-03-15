import { useState } from 'react'
import './App.css'
import Navbar from './components/Navbar'
import Dashboard from './pages/Dashboard'
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'
import FileUpload from './pages/FileUpload'
import CheckStatus from './pages/CheckStatus'


function App() {

  return (
    <>
      <Navbar />

      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/Upload" element={<FileUpload />} />
        <Route path="/Status" element={<CheckStatus />} />
      </Routes>

    </>
  )
}

export default App

import React from 'react'
import icon from "../assets/icon2.svg"
import './Navbar.css'


const Navbar = () => {
  return (
    <nav className="navbar">
      <div>
        <img src={icon} alt="icon" className="icon" />
      </div>
      <h1 className="navbar-title">icCompressor</h1>

    </nav>
  )
}

export default Navbar

import React from 'react'
import { Routes, Route, useNavigate, Link, Outlet } from "react-router-dom";
import './button.css'

const Button1 = ({ buttonName, path = '' }) => {

  const navigate = useNavigate();

  return (
    <button className="button-33" onClick={() => navigate(path)} role="button">
      
      {buttonName}

    </button>
  )
}

export default Button1

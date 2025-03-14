import React from 'react'
import './Dashboard.css'
import Button from '../components/Button1.jsx'

const Dashboard = () => {
  return (
    <div className='dashboard'>
        <div className="container-1">
        <Button ButtonName="Upload File"/>
        <label htmlFor="btn">upload a file for compression.</label>
        </div>
        <div className="container-1">
        <Button ButtonName="Check Status"/>
        <label htmlFor="btn">check the status of image compression.</label>

        </div>
    </div>
  )
}

export default Dashboard

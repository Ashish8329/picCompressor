import React from "react";
import { Routes, Route, useNavigate, Link, Outlet } from "react-router-dom";
import "./Dashboard.css";
import Button from "../components/Button1.jsx";


const Dashboard = () => {
  const navigate = useNavigate();

  return (
    <div className="dashboard">

      <div className="container-1">

        <Button buttonName="Upload File" path='/upload' />
        <label>Upload a file for compression.</label>

      </div>


      <div className="container-1">

        <Button buttonName="Check Status" path='/Status'/>

        <label>Check the status of image compression.</label>

      </div>

       
    </div>
  );
};

export default Dashboard;

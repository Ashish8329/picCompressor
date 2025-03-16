import React, { useState } from "react";
import { Routes, Route, useNavigate, Link, Outlet } from "react-router-dom";

import "./styles/Container.css";
import Button from "./Button";  // Ensure Button component exists

const Container = () => {
  const [file, setFile] = useState(null);
  const [name, setName] = useState("");
  const [data, setData] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate();



  const url = 'http://127.0.0.1:8000/product/'


  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleNameChange = (event) => {
    setName(event.target.value);
  };



  const handleSubmit = async (event) => {
    console.log('working')
    event.preventDefault();
    setLoading(true);

    if (!file || !name) {
      alert("Please select a file and enter a product name.");
      setLoading(false);
      return;
    }

    const formData = new FormData();
    formData.append("csv_file", file);
    formData.append("name", name);

    try {
      const response = await fetch("http://127.0.0.1:8000/product/", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        // Convert response status and text into an error and throw it
        const errorText = await response.text();
        throw new Error(`HTTP Error: ${response.status} - ${errorText}`);
        setLoading(false);
      }

      const data = await response.json();
      setData(data)
      setLoading(false);

      // ✅ Clear form after successful upload
      setFile(null);
      setName("");

    } catch (error) {
      // TODO error handling 
      setError(error)
      alert(`File upload failed! ${error}`);
      setLoading(false);
    }
  };



  return (
    <>
    <div className="switch">
      <div className="switch_box">
        <button className="cta" onClick={() => navigate('/status')}>
          <span> Check Status </span>
          <svg width="15px" height="10px" viewBox="0 0 13 10">
            <path d="M1,5 L11,5"></path>
            <polyline points="8 1 12 5 8 9"></polyline>
          </svg>
        </button>
      </div>
      </div>
      <div className="container_box">
        <div className="container_box2">

          <form onSubmit={handleSubmit} className="upload-form">

            <div className="input">
              <label>Name:</label>
              <input type="text" value={name} onChange={handleNameChange} required />
            </div>

            <div className="input">
              <label>CSV File:</label>
              <input type="file" accept=".csv" onChange={handleFileChange} required />
            </div>

            <button type="submit" disabled={loading}>
              {loading ? "Uploading..." : "Upload"}
            </button>

          </form>

          {data ? (
            <div className="response">
              <h3>Request ID :  {data.req_id}</h3>
            </div>
          ) : (
            ''
          )}


        </div>

      </div>
    </>
  );
};

export default Container;

import React, { useState } from "react";
import "./styles/Container.css";
import Button from "./Button";  // Ensure Button component exists

const Container = () => {
  const [file, setFile] = useState(null);
  const [name, setName] = useState("");

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

    if (!file || !name) {
      alert("Please select a file and enter a product name.");
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
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      console.log("API Response:", data);
      alert("File uploaded successfully!");
    } catch (error) {
      console.error("API Error:", error);
      alert("File upload failed!");
    }
  };



  return (
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

          <button type="submit">Upload</button>

        </form>

      </div>
    </div>
  );
};

export default Container;

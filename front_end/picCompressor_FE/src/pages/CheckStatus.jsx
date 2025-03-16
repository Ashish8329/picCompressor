import React, { useState } from 'react';
import "./styles/CheckStatus.css";

const CheckStatus = () => {
  const url = `http://127.0.0.1:8000/product/?req_id=`
  const [req_id, setRequestID] = useState('');


  const handleRequestChange = (event) => {
    setRequestID(event.target.value)
  }

  const handleSubmit = async (event) => {
    console.log('woring')
    event.preventDefault();
    console.log(req_id)

    try {
      const response = await fetch(`http://127.0.0.1:8000/product/?req_id=${req_id}`);

      // Ensure response is successfully received
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      // Parse JSON response
      const res = await response.json();

      // Log the entire response data
      console.log("Full Response Data:", res);
      // Check if the response is an array
      if (Array.isArray(res)) {
        alert(res.map(item => JSON.stringify(item)).join("\n"));  // Display each item in a new line
      } else {
        alert(JSON.stringify(res, null, 2));  // Pretty-print JSON object
      }
      // console.log("Response Object:", response);
    } catch (error) {
      console.error("API Error:", error);
    }


  }

  return (


    <div className="container_box">
      <div className="container_box2">

        <form onSubmit={handleSubmit} className="upload-form">

          <div className="input">
            <label>Request id:</label>
            <input type="text" value={req_id} onChange={handleRequestChange} required />
          </div>


          <button type="submit">Check Status</button>

        </form>

      </div>
    </div>
  )
}

export default CheckStatus

import React, { useState } from 'react';
import "./styles/CheckStatus.css";
import { fetchProductStatus } from "../utils/get";

const CheckStatus = () => {
  const [req_id, setRequestID] = useState('');
  const [data, setData] = useState({});

  const handleRequestChange = (event) => {
    setRequestID(event.target.value)
  }

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const res = await fetchProductStatus(req_id);
      setData(res)

    } catch (error) {

      alert("Failed to fetch data. Please try again.");

    }

  };

  return (


    <div className="container_box">
      <div className="container_box2">

        <form onSubmit={handleSubmit} className="upload-form">

          <div className="input">
            <label>Request id:</label>
            <input type="text" value={req_id} onChange={handleRequestChange} required />
          </div>


          <button type="submit">Check Status</button>
          {data && data.status && (
            <div className={data.status === "pending" ? "error_response" : "success_response"}>
              <h3>status {data.status}</h3>
            </div>
          )}


        </form>
        

      </div>
    </div>
  )
}

export default CheckStatus

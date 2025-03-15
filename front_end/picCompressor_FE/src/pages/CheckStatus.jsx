import React from 'react'
import "./styles/CheckStatus.css";

const CheckStatus = () => {
  return (
    <div className="container_box">
      <div className="container_box2">
        <div className="smcontainer">
          <label htmlFor="btn">Request ID</label>
          <input type="text" id="btn" />
        </div>

        <div className="btn">

          <button>check status</button>
        </div>
      </div>
    </div>
  )
}

export default CheckStatus

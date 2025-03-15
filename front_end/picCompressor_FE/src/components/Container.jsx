import React from "react";
import "./styles/Container.css";
import Button from "./Button";  // Ensure Button component exists

const Container = () => {
  return (
    <div className="container_box">
      <div className="container_box2">
        <div className="smcontainer">
          <label htmlFor="btn">Upload CSV file</label>
          <input type="file" id="btn" />
        </div>

        <div className="buttons">
          <button className="btn">
            <span aria-hidden="true"></span>
            <p data-start="Good luck!" data-text="Start!" data-title="Upload Csv"></p>
          </button>
        </div>
      </div>
    </div>
  );
};

export default Container;

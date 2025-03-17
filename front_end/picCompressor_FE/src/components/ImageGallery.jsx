import React from "react";
import "./styles/ImageGallery.css"; // Import CSS for styling

function ImageGallery({ imagePaths }) {
  return (
    <div className="gallery-container">
      {imagePaths.map((image, index) => (
        <div key={index} className="gallery-item">
          <img src={`http://127.0.0.1:8000/media/${image}`} alt={`Image ${index + 1}`} className="gallery-image" />
          
        </div>
      ))}
    </div>
  );
}

export default ImageGallery;

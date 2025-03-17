import React from "react";
import "./styles/ImageGallery.css"; // Import CSS for styling

function ImageGallery({ data }) {
  console.log("images");

  const originalImages = data.original_images_urls || [];
  const compressedImages = data.output_image_urls || [];
  const imgSizeBefore = data.img_size_before || [];
  const imgSizeAfter = data.img_size_after || [];

  return (
    <div className="gallery-container">
      {originalImages.map((original, index) => {
        const compressed = compressedImages[index] || "";
        const sizeBefore = imgSizeBefore[index] || "N/A";
        const sizeAfter = imgSizeAfter[index] || "N/A";

        return (
          <div className="image-pair-container" key={index}>
            {/* Original Image Container */}
            <div className="image-container">
              <p>Original Image</p>
              <img src={original} alt={`Original ${index + 1}`} className="gallery-image" />
              <div className="info-box">
                <p>Size Before: {sizeBefore} KB</p>
              </div>
            </div>

            {/* Compressed Image Container */}
            <div className="image-container">
              <p>Compressed Image</p>
              <img src={compressed} alt={`Compressed ${index + 1}`} className="gallery-image" />
              <div className="info-box">
                <p>Size After: {sizeAfter} KB</p>
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
}

export default ImageGallery;

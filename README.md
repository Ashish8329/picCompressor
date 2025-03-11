# Image Processing System :camera_flash:

Welcome to the Image Processing System repository! This project is designed to efficiently process image data from CSV files, ensuring validation, asynchronous processing, and storage of compressed images. The system provides APIs for uploading, tracking processing status, and webhook integration for automated responses(upcomming).

---

## Key Features :star2:

- **CSV-Based Image Processing**:
  - Accepts CSV files containing product names and image URLs.
  - Supports multiple input images per product.
  
- **Data Validation**:
  - Ensures correct CSV format before processing.
  
- **Asynchronous Image Compression**:
  - Reduces image quality by 50% to optimize storage and performance.
  
- **Database Storage**:
  - Stores original and processed image URLs along with product details.
  
- **RESTful APIs**:
  - Upload API to submit CSV and receive a unique request ID.
  - Status API to track image processing progress.
  
- **Webhook Integration**:
  - Option to trigger a webhook after processing completion.
  
---

## Tech Stack :computer:

- **Backend**: Python (Django/Django REST Framework) 
- **Database**: PostgreSQL, 
- **Asynchronous Processing**: Celery with Redis (for Python)
- **Image Processing**: Pillow (Python)  
 

---

## Getting Started

Follow these steps to set up the Image Processing System:

### 1. Clone the Repository
Clone this repository to your local machine:
```sh
 git clone https://github.com/Ashish8329/picCompressor.git
```

### 2. Set Up a Virtual Environment (Python)
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
 

### 3. Navigate to the Project Directory
```sh
cd picCompressor
```

### 4. Set Up the Database
- Configure the database settings in `.env` file.
```
DB_NAME = your_db_name
DB_USER = your_db_user
DB_PASSWORD = your_db_password
DB_HOST = localhost
DB_PORT = 5432

```
- Run migrations (for Django):
```sh
python manage.py migrate
```

### 5. Create a Superuser (Django Admin)
```sh
python manage.py createsuperuser
```

### 6. Run Celery Workers in different terminals (Python) 
```sh
celery -A picCompressor worker --loglevel=info
```
For flower :
```sh
celery -A picCompressor flower
```

### 7. Start the Development Server
For Django:
```sh
python manage.py runserver
```
For Node.js:
 
Now visit `http://127.0.0.1:8000/admin/` to manage image processing.

---

## API Endpoints :rocket:

### Upload API
**POST** `/api/product`
- Accepts a CSV file and returns a unique request ID.

### Status API
**GET** `/api/status/{request_id}`
- Retrieves processing status for the given request ID.

---
## Documentation 📖

For detailed Project documentation, visit:  
[📄 Project Documentation](https://docs.google.com/document/d/1yd4U50l6zCW0i6BOulP43dmtyoIvBontwxSf-lRqrwM/edit?usp=sharing)


For Api documentation, visit:  
[📄 API Documentation ](https://docs.google.com/document/d/1k_H6J-OVBThmURbQPekJ-dbDYT3LrrptYUtWCtiw11g/edit?usp=sharing)

For Postman collection, visit:  
[📩 Postman Collection](https://drive.google.com/drive/folders/10KfjKN0jSNWS7Y7QqpqbtHk4pyTBnhqg?usp=drive_link)

## Contribution Guidelines
We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a feature branch (e.g., `feat/image-compression`).
3. Commit with clear messages (e.g., `feat: Add async image processing`).
4. Push changes and create a pull request.

---
## Contact 📬

For any queries or collaborations, feel free to reach out:

📧 Email: [ashishauti123@gmail.com](mailto:ashishauti123@gmail.com)  
🔗 LinkedIn: [Ashish](https://www.linkedin.com/in/ashish-auti-069346254)

## Explore the System :sparkles:
:point_right: **Congratulations** :tada:! Your Image Processing System is now ready to use. :confetti_ball:

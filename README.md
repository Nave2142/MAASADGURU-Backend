# Maasadguru Backend API

A professional Flask-based backend for the Maasadguru Social Service project.

## Features
- **API Health Check**: Quick verification of system status.
- **Inquiry Management**: Secure storage for contact form submissions.
- **Admin Authentication**: Secure JWT-based login for admin dashboard access.
- **Dynamic Gallery**: Full management of social service photos with upload and delete capabilities.
- **PDF Generation**: Automated generation of project overview documents.
- **API Documentation**: Integrated Swagger UI for interactive endpoint testing.
- **CORS Support**: Pre-configured for seamless integration with the React frontend.
- **Environment Driven**: Easily configurable via `.env`.

## Tech Stack
- **Framework**: Flask
- **Database**: SQLite (SQLAlchemy)
- **Authentication**: PyJWT
- **API Documentation**: Flasgger (Swagger UI)
- **PDF Engine**: ReportLab
- **Config**: Python-Dotenv

## Getting Started

### 1. Setup Virtual Environment
```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 2. Install Dependencies
```powershell
pip install -r requirement.txt
```

### 3. Run the Server
```powershell
python main.py
```

The server will start at `http://localhost:5000`.

## API Documentation
Once the server is running, you can access the interactive API documentation (Swagger) at:
`http://localhost:5000/apidocs`

## API Endpoints

### `GET /`
Health check endpoint.

### `POST /api/admin/login`
Admin authentication to receive JWT token.

### `POST /api/inquiry`
Submit a new inquiry.

### `GET /api/gallery`
Retrieve all gallery photos.

### `POST /api/gallery/upload` (Auth Required)
Upload a new photo to the gallery.

### `DELETE /api/gallery/<id>` (Auth Required)
Remove a photo from the gallery.

### `POST /api/generate-pdf`
Generates a Maasadguru Project PDF.
**Payload (Optional):**
```json
{
  "content": "Additional custom details for the PDF..."
}
```
**Response:** Binary PDF file.


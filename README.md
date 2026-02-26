# Maasadguru Backend API

A professional Flask-based backend for the Maasadguru Social Service project.

## Features
- **API Health Check**: Quick verification of system status.
- **Inquiry Management**: Secure storage for contact form submissions.
- **PDF Generation**: Automated generation of project overview documents.
- **CORS Support**: Pre-configured for seamless integration with the React frontend.
- **Environment Driven**: Easily configurable via `.env`.

## Tech Stack
- **Framework**: Flask
- **Database**: SQLite (SQLAlchemy)
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

## API Endpoints

### `GET /`
Health check endpoint.

### `POST /api/inquiry`
Submit a new inquiry.
**Payload:**
```json
{
  "full_name": "John Doe",
  "email": "john@example.com",
  "mobile": "1234567890",
  "subject": "Volunteer Registration",
  "message": "I would like to help."
}
```

### `POST /api/generate-pdf`
Generates a Maasadguru Project PDF.
**Payload (Optional):**
```json
{
  "content": "Additional custom details for the PDF..."
}
```
**Response:** Binary PDF file.

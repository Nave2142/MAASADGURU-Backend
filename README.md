# Maasadguru Backend API

A professional Flask-based backend for the Maasadguru Social Service project.

## Features
- **API Health Check**: Quick verification of system status.
- **Inquiry Management**: Secure storage for contact form submissions.
- **Admin Authentication**: Secure JWT-based login for admin dashboard access.
- **Dynamic Gallery**: Full management of social service photos with upload and delete capabilities.
- **Database Migration**: Easy schema updates via a dedicated migration script.
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

### 4. Create Admin User
To access protected endpoints and the admin dashboard, you need to create an admin account:
```powershell
python create_admin.py <your_username> <your_password>
```
Example: `python create_admin.py admin admin123`

### 5. Database Migration
If you've updated the source code and need to update your database schema (e.g., adding new columns), run:
```powershell
python migrate_db.py
```
This script ensures your database stays in sync with the latest application features without losing existing data.


## Detailed Features

### 1. 📩 Inquiry Management (Contact Form)
The backend provides a robust system to capture and store inquiries from the website's "Contact Us" page.
- **Validation**: Ensures all fields like Name, Email, Mobile, Subject, and Message are provided.
- **Persistent Storage**: All inquiries are saved in the SQLite database with a timestamp.
- **Endpoint**: `POST /api/inquiry`

### 2. 🔐 Admin Authentication (JWT)
Secure access to administrative features such as the gallery manager.
- **Security**: Uses `PyJWT` for stateless authentication and `werkzeug` for secure password hashing.
- **Session**: Tokens are valid for 24 hours.
- **Endpoint**: `POST /api/admin/login`

### 3. 🖼️ Dynamic Gallery Management
Empowers admins to manage the visual content of the social service projects directly from the dashboard.
- **Image Upload**: Supports `png`, `jpg`, `jpeg`, and `gif`. Automatically handles unique filename generation to prevent overwriting.
- **File Serving**: Images are served via the `/api/static/uploads/` path.
- **Fallback**: If no images are uploaded, the API provides high-quality default placeholders to ensure the UI always looks great.
- **Endpoints**: `GET /api/gallery`, `POST /api/gallery/upload`, `DELETE /api/gallery/<id>`

### 4. 📄 Automated PDF Generation
A specialized engine to generate professional project overview documents for donors or stakeholders.
- **Branded Design**: Includes the Maasadguru logo details, registration number, and official formatting.
- **Customizable**: Allows passing specific project content via the API to be included in the PDF dynamically.
- **Real-time**: Generates and serves the binary PDF file instantly upon request.
- **Endpoint**: `POST /api/generate-pdf`

### 5. 🛠️ Interactive API Docs (Swagger)
Built-in documentation for developers and frontend integrators.
- **Live Testing**: Test every API endpoint directly from the browser without needing Postman.
- **Schema Info**: Detailed information on required payloads and response formats.
- **URL**: `http://localhost:5000/apidocs`

### 6. 🔄 Database Migration Utility
A dedicated script to manage schema evolutions as the project grows.
- **Automated Updates**: Safely adds missing columns (like the `type` field in the gallery) to existing tables.
- **Safety First**: Checks for existing columns before attempting modifications to prevent SQL errors.
- **Ease of Use**: Can be run anytime via `python migrate_db.py`.

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


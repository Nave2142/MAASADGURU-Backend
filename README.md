# Maasadguru Backend API

A professional Flask-based backend for the Maasadguru Social Service project.

## 🌟 Key Features
- **Production Ready**: Integrated with **Waitress** for high-performance Windows hosting.
- **Modular Architecture**: Built with **Flask Blueprints** for organized code and easy scaling.
- **Configuration Management**: Separate `development` and `production` settings via `config.py`.
- **Advanced Error Handling**: Global JSON-based error handlers for all common HTTP statuses (404, 500, etc.).
- **Admin Dashboard Auth**: Secure **JWT-based** authentication with encrypted password storage.
- **Dynamic Content Manager**: Full API support for uploading and managing social service **Photos & Videos**.
- **Automated PDF Engine**: Instant generation of branded project overview documents for NGOs.
- **Database Migrations**: Custom utility script to update schemas safely without data loss.
- **API Documentation**: Interactive **Swagger UI** for live endpoint testing and integration.

## 🛠️ Tech Stack
- **Framework**: Flask
- **WSGI Server**: Waitress (Production)
- **Database**: SQLite (SQLAlchemy)
- **Authentication**: PyJWT
- **API Documentation**: Flasgger (OpenAPI/Swagger)
- **PDF Engine**: ReportLab
- **Security**: Werkzeug Hashing
- **Environment**: Python-Dotenv

## 🚀 Getting Started

### 1. Setup Environment
```powershell
# Create & Activate Virtual Environment
python -m venv venv
.\venv\Scripts\activate

# Install Dependencies
pip install -r requirement.txt
```

### 2. Configuration (`.env`)
Create or update your `.env` file with these keys:
```env
FLASK_ENV=development # Change to 'production' for live hosting
PORT=5000
DATABASE_URL=sqlite:///maasadguru.db
SECRET_KEY=your-secure-key
JWT_SECRET_KEY=your-jwt-key
```

### 3. Initialize Database & Admin
```powershell
# Create tables
python -c "from main import create_app; from extensions import db; app=create_app(); app.app_context().push(); db.create_all()"

# Create your admin account
python create_admin.py <username> <password>
```

### 4. Run the Server
```powershell
python main.py
```
- **Development**: Starts with Debug mode and Auto-reload enabled.
- **Production**: Starts the industrial-grade **Waitress server** automatically.

---

## 📂 Project Structure
- `main.py`: App Factory & Central Registry.
- `config.py`: Dev/Production settings management.
- `models.py`: Database schemas (Inquiry, Photo, User).
- `contact.py`: Inquiry & Contact Form Blueprint.
- `gallery.py`: Photo/Video Management Blueprint.
- `donate.py`: PDF Generation & Donation Blueprint.
- `auth.py`: JWT Login & Security Blueprint.
- `migrate_db.py`: Database schema update utility.

---

## 🛠️ Developer Tools

### 📖 Interactive API Docs (Swagger)
Access the live documentation to test every endpoint directly from your browser:
🔗 **`http://localhost:5000/apidocs/`**

### 🔄 Database Migration
If you update `models.py` and need to sync the existing database:
```powershell
python migrate_db.py
```

---

## 🛣️ API Endpoints Summary

### Public Endpoints
- `GET /`: API Health & Status.
- `POST /api/inquiry`: Submit website contact forms.
- `GET /api/gallery`: Fetch all social service activities.
- `POST /api/generate-pdf`: Generate branded project documents.

### Admin Endpoints (Secured)
- `POST /api/admin/login`: Get JWT Access Token.
- `POST /api/gallery/upload`: Securely upload photos/videos.
- `DELETE /api/gallery/<id>`: Remove gallery content.

## 🛡️ Security Note
In production mode, the application enables stricter error handling and utilizes Waitress for secure request processing. Always use a strong `SECRET_KEY` in your `.env` for live deployments.

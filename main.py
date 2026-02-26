import os
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime
from dotenv import load_dotenv
from flasgger import Swagger
from extensions import db
from contact import contact_bp
from gallery import gallery_bp
from donate import donate_bp
from auth import auth_bp

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Enable CORS
    CORS(app)

    # Database Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///maasadguru.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'maasadguru-secret-key-123')

    # Initialize Extensions
    db.init_app(app)
    
    # Initialize Swagger
    swagger = Swagger(app, template={
        "info": {
            "title": "Maasadguru Social Service API",
            "description": "API documentation for the Maasadguru Backend System",
            "version": "1.0.0",
            "contact": {
                "email": "maasadguru@gmail.com"
            }
        }
    })

    # Register Blueprints
    app.register_blueprint(contact_bp)
    app.register_blueprint(gallery_bp)
    app.register_blueprint(donate_bp)
    app.register_blueprint(auth_bp)

    # Static file serving for uploads
    @app.route('/api/static/uploads/<path:filename>')
    def uploaded_file(filename):
        return send_from_directory(os.path.join(app.root_path, 'static', 'uploads'), filename)

    # Health Check Route
    @app.route('/', methods=['GET'])
    def health_check():
        """
        Health check endpoint
        ---
        responses:
          200:
            description: Returns the status of the API
            schema:
              properties:
                status:
                  type: string
                  example: online
                message:
                  type: string
                  example: Maasadguru Backend API is running
                timestamp:
                  type: string
                  example: 2024-02-26T12:00:00Z
        """
        return jsonify({
            "status": "online",
            "message": "Maasadguru Backend API is running",
            "timestamp": datetime.utcnow().isoformat()
        })

    # Initialize Database Tables
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

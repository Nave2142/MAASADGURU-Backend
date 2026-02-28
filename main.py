import os
import logging
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime
from dotenv import load_dotenv
from flasgger import Swagger
from extensions import db
from config import config_by_name # Use consistent config system
from contact import contact_bp
from gallery import gallery_bp
from donate import donate_bp
from auth import auth_bp

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def create_app(config_name=None):
    """Application Factory Pattern."""
    app = Flask(__name__)
    
    # Environment selection (default to development for now)
    config_name = config_name or os.getenv('FLASK_ENV', 'development').lower()
    app.config.from_object(config_by_name[config_name])

    # Enhanced CORS for production if needed (can be more restrictive)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Extensions setup
    db.init_app(app)
    
    # Swagger Documentation
    swagger = Swagger(app, template={
        "info": {
            "title": "Maasadguru Social Service API",
            "description": "API documentation for the Maasadguru Backend System",
            "version": "1.0.0",
            "contact": { "email": "maasadguru@gmail.com" }
        }
    })

    # Central Blueprints Registration
    app.register_blueprint(contact_bp)
    app.register_blueprint(gallery_bp)
    app.register_blueprint(donate_bp)
    app.register_blueprint(auth_bp)

    # Static file serving for uploads
    @app.route('/api/static/uploads/<path:filename>')
    def uploaded_file(filename):
        return send_from_directory(os.path.join(app.root_path, 'static', 'uploads'), filename)

    # Global Error Handlers
    @app.errorhandler(404)
    def handle_404(e):
        return jsonify({"status": "error", "message": "Resource not found"}), 404

    @app.errorhandler(500)
    def handle_500(e):
        logger.error(f"Server error: {str(e)}")
        return jsonify({"status": "error", "message": "Internal server error. Please try again later."}), 500

    @app.errorhandler(400)
    def handle_400(e):
        return jsonify({"status": "error", "message": str(e.description)}), 400

    # API Base Route / Health Check
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
    env = os.getenv('FLASK_ENV', 'development').lower()

    if env == 'production':
        from waitress import serve
        logger.info(f"🚀 Starting Production Server (Waitress) on port {port}...")
        serve(app, host='0.0.0.0', port=port)
    else:
        logger.info(f"🛠️ Starting Development Server (Debug) on port {port}...")
        app.run(host='0.0.0.0', port=port, debug=True)

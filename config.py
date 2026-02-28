import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-maasadguru-secret-key-change-it')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///maasadguru.db')
    
    # JWT Settings (for future auth expansion)
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', SECRET_KEY)
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
    
    # Swagger
    SWAGGER = {
        'title': 'Maasadguru Social Service API',
        'uiversion': 3
    }

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    FLASK_ENV = 'development'

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    FLASK_ENV = 'production'
    # In production, we should ideally use a more robust DB like PostgreSQL
    # If using SQLite, the path should be absolute to avoid surprises
    
    # Security: Enable these in real production behind SSL
    # SESSION_COOKIE_SECURE = True
    # REMEMBER_COOKIE_SECURE = True

config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}

# Variable to pick based on FLASK_ENV
active_config = config_by_name.get(os.getenv('FLASK_ENV', 'development'), DevelopmentConfig)

from flask import Blueprint, request, jsonify
from models import User
from extensions import db
import jwt
import datetime
import os

auth_bp = Blueprint('auth', __name__)

SECRET_KEY = os.getenv('SECRET_KEY', 'maasadguru-secret-key-123')

@auth_bp.route('/api/admin/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, SECRET_KEY, algorithm="HS256")
        
        return jsonify({
            "status": "success",
            "token": token,
            "username": user.username
        })
    
    return jsonify({"status": "error", "message": "Invalid username or password"}), 401

@auth_bp.route('/api/admin/setup', methods=['POST'])
def setup_admin():
    # Only allow if no users exist
    if User.query.first():
        return jsonify({"status": "error", "message": "Admin already exists"}), 400
    
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"status": "success", "message": "Admin user created"})

import os
from flask import Blueprint, jsonify, request, current_app
from models import Photo
from extensions import db
from werkzeug.utils import secure_filename
from datetime import datetime

gallery_bp = Blueprint('gallery', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@gallery_bp.route('/api/gallery', methods=['GET'])
def get_gallery():
    """
    Returns gallery items for the frontend
    ---
    responses:
      200:
        description: List of images and their details
        schema:
          properties:
            status:
              type: string
            data:
              type: array
              items:
                properties:
                  url:
                    type: string
                  title:
                    type: string
                  desc:
                    type: string
            count:
              type: integer
    """
    photos = Photo.query.order_by(Photo.created_at.desc()).all()
    images = [p.to_dict() for p in photos]
    
    # If no photos in DB, return some defaults for now (or empty list)
    if not images:
        images = [
            {
                "url": "https://plus.unsplash.com/premium_photo-1682092585257-58d1c813d9b4?q=80&w=1170&auto=format&fit=crop",
                "title": "Educational Reform",
                "desc": "Empowering rural students through digital literacy."
            },
            {
                "url": "https://images.unsplash.com/photo-1652858672796-960164bd632b?q=80&w=1170&auto=format&fit=crop",
                "title": "Environmental Impact",
                "desc": "Sustaining local ecosystems through community action."
            }
        ]
        
    return jsonify({
        "status": "success",
        "data": images,
        "count": len(images)
    })

@gallery_bp.route('/api/gallery/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"status": "error", "message": "No file part"}), 400
    
    file = request.files['file']
    title = request.form.get('title', '')
    desc = request.form.get('desc', '')

    if file.filename == '':
        return jsonify({"status": "error", "message": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # Create unique filename
        filename = f"{datetime.now().timestamp()}_{filename}"
        
        # Ensure upload folder exists
        upload_folder = os.path.join(current_app.root_path, 'static', 'uploads')
        os.makedirs(upload_folder, exist_ok=True)
        
        filepath = os.path.join(upload_folder, filename)
        file.save(filepath)
        
        # In a real app, you'd save the relative URL
        url = f"/api/static/uploads/{filename}"
        
        new_photo = Photo(url=url, title=title, desc=desc)
        db.session.add(new_photo)
        db.session.commit()
        
        return jsonify({
            "status": "success",
            "message": "Image uploaded successfully",
            "data": new_photo.to_dict()
        })
    
    return jsonify({"status": "error", "message": "Invalid file type"}), 400

@gallery_bp.route('/api/gallery/<int:photo_id>', methods=['DELETE'])
def delete_photo(photo_id):
    photo = Photo.query.get_or_404(photo_id)
    
    # Optional: Delete file from disk
    # filename = photo.url.split('/')[-1]
    # filepath = os.path.join(current_app.root_path, 'static', 'uploads', filename)
    # if os.path.exists(filepath):
    #     os.remove(filepath)
    
    db.session.delete(photo)
    db.session.commit()
    return jsonify({"status": "success", "message": "Photo deleted"})

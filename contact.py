from flask import Blueprint, request, jsonify
from models import Inquiry
from extensions import db

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/api/inquiry', methods=['POST'])
def handle_inquiry():
    """
    Submit a new inquiry
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          properties:
            full_name:
              type: string
            email:
              type: string
            mobile:
              type: string
            subject:
              type: string
            message:
              type: string
    responses:
      201:
        description: Inquiry received successfully
      400:
        description: Missing required field
      500:
        description: Server error
    """
    try:
        data = request.json
        
        # Validation
        required_fields = ['full_name', 'email', 'mobile', 'subject', 'message']
        for field in required_fields:
            if not data.get(field):
                return jsonify({"error": f"Missing required field: {field}"}), 400

        # Save to database
        new_inquiry = Inquiry(
            full_name=data['full_name'],
            email=data['email'],
            mobile=data['mobile'],
            subject=data['subject'],
            message=data['message']
        )
        db.session.add(new_inquiry)
        db.session.commit()

        return jsonify({
            "status": "success",
            "message": "Inquiry received successfully. We will contact you soon.",
            "inquiry_id": new_inquiry.id
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

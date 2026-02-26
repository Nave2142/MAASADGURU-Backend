from main import create_app
from extensions import db
from models import User
import sys

def create_admin(username, password):
    app = create_app()
    with app.app_context():
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            print(f"User {username} already exists.")
            return
        
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        print(f"Admin user '{username}' created successfully!")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python create_admin.py <username> <password>")
    else:
        create_admin(sys.argv[1], sys.argv[2])

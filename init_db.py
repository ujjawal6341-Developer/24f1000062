from app import app
from models import db, Admin


with app.app_context():

    # Create all tables
    db.create_all()

    print("Database tables created successfully.")

    # Check if admin already exists
    existing_admin = Admin.query.filter_by(username="admin").first()

    if not existing_admin:

        admin = Admin(
            username="admin",
            password="admin123"
        )

        db.session.add(admin)
        db.session.commit()

        print("Default Admin created successfully.")

    else:
        print("Admin already exists.")
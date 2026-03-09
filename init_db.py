from app import app
from models import db, Admin


with app.app_context():

    db.create_all()

    if not Admin.query.first():

        admin = Admin(

            username="admin",

            password="admin"

        )

        db.session.add(admin)

        db.session.commit()

        print("Admin created")
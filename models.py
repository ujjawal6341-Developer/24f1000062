from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


# ===============================
# Admin Model
# ===============================
class Admin(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), unique=True, nullable=False)

    password = db.Column(db.String(100), nullable=False)


# ===============================
# Student Model
# ===============================
class Student(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(100), nullable=False)

    course = db.Column(db.String(100))

    resume = db.Column(db.String(200))

    status = db.Column(db.String(50), default="Active")


# ===============================
# Company Model
# ===============================
class Company(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    company_name = db.Column(db.String(150), nullable=False)

    hr_contact = db.Column(db.String(100))

    website = db.Column(db.String(200))

    email = db.Column(db.String(120), unique=True)

    password = db.Column(db.String(100))

    approval_status = db.Column(db.String(50), default="Pending")


# ===============================
# Placement Drive Model
# ===============================
class Drive(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))

    job_title = db.Column(db.String(150), nullable=False)

    job_description = db.Column(db.Text)

    eligibility = db.Column(db.String(200))

    deadline = db.Column(db.Date)

    status = db.Column(db.String(50), default="Pending")


# ===============================
# Application Model
# ===============================
class Application(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

    drive_id = db.Column(db.Integer, db.ForeignKey('drive.id'))

    application_date = db.Column(db.DateTime, default=datetime.utcnow)

    status = db.Column(db.String(50), default="Applied")
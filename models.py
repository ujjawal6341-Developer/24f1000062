from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    email = db.Column(db.String(100), unique=True)

    password = db.Column(db.String(100))

    course = db.Column(db.String(100))


class Company(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    email = db.Column(db.String(100), unique=True)

    password = db.Column(db.String(100))


class Drive(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    company_id = db.Column(db.Integer)

    company_name = db.Column(db.String(100))

    role = db.Column(db.String(100))

    package = db.Column(db.String(50))

    location = db.Column(db.String(100))


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    drive_id = db.Column(db.Integer, db.ForeignKey('drive.id'))

    status = db.Column(db.String(50), default="Applied")
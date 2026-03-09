from flask import Blueprint, render_template, request, redirect, session
from models import db, Student, Drive, Application

# Create Blueprint
student_bp = Blueprint("student", __name__)


# ===============================
# Student Register
# ===============================
@student_bp.route("/student/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        course = request.form["course"]

        # Check if email already exists
        existing_student = Student.query.filter_by(email=email).first()

        if existing_student:
            return "Email already registered. Please login."

        new_student = Student(
            name=name,
            email=email,
            password=password,
            course=course
        )

        db.session.add(new_student)
        db.session.commit()

        return redirect("/login")

    return render_template("student/register.html")


# ===============================
# Student Dashboard
# ===============================
@student_bp.route("/student/dashboard")
def dashboard():

    if not session.get("student_id"):
        return redirect("/login")

    return render_template("student/dashboard.html")


# ===============================
# Student Profile
# ===============================
@student_bp.route("/student/profile")
def profile():

    if not session.get("student_id"):
        return redirect("/login")

    student_id = session.get("student_id")
    student_data = Student.query.get(student_id)

    return render_template("student/profile.html", student=student_data)


# ===============================
# View Drives
# ===============================
@student_bp.route("/student/drives")
def drives():

    if not session.get("student_id"):
        return redirect("/login")

    drives = Drive.query.all()

    return render_template("student/drives.html", drives=drives)


# ===============================
# Apply to Drive
# ===============================
@student_bp.route("/apply/<int:drive_id>")
def apply(drive_id):

    if not session.get("student_id"):
        return redirect("/login")

    student_id = session.get("student_id")

    # Check if already applied
    existing_application = Application.query.filter_by(
        student_id=student_id,
        drive_id=drive_id
    ).first()

    if existing_application:
        return "You have already applied for this drive."

    application = Application(
        student_id=student_id,
        drive_id=drive_id
    )

    db.session.add(application)
    db.session.commit()

    return redirect("/student/applications")


# ===============================
# View Applications
# ===============================
@student_bp.route("/student/applications")
def applications():

    if not session.get("student_id"):
        return redirect("/login")

    student_id = session.get("student_id")

    apps = Application.query.filter_by(student_id=student_id).all()

    return render_template("student/applications.html", apps=apps)
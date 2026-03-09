from flask import Blueprint, render_template, request, redirect, session
from models import Student, Company

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():

    # If already logged in, redirect to dashboard
    if session.get("student_id"):
        return redirect("/student/dashboard")

    if session.get("company_id"):
        return redirect("/company/dashboard")

    if session.get("admin"):
        return redirect("/admin/dashboard")

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]
        role = request.form["role"]

        # Student Login
        if role == "student":

            student = Student.query.filter_by(email=email, password=password).first()

            if student:
                session["student_id"] = student.id
                return redirect("/student/dashboard")

        # Company Login
        elif role == "company":

            company = Company.query.filter_by(email=email, password=password).first()

            if company:
                session["company_id"] = company.id
                return redirect("/company/dashboard")

        # Admin Login
        elif role == "admin":

            if email == "admin@gmail.com" and password == "admin":
                session["admin"] = True
                return redirect("/admin/dashboard")

    return render_template("login.html")


@auth.route("/logout")
def logout():

    session.clear()
    return redirect("/")
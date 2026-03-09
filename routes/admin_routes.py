from flask import Blueprint, render_template, request, redirect, session
from models import Student, Company, Drive, Application

admin = Blueprint("admin", __name__)


# Admin Login
@admin.route("/admin", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":
        password = request.form["password"]

        if password == "1234":
            session["admin"] = True
            return redirect("/admin/dashboard")

    return render_template("admin/admin_login.html")


# Admin Dashboard
@admin.route("/admin/dashboard")
def dashboard():

    if not session.get("admin"):
        return redirect("/admin")

    return render_template("admin/dashboard.html")


# View Students
@admin.route("/admin/students")
def students():

    if not session.get("admin"):
        return redirect("/admin")

    students = Student.query.all()
    return render_template("admin/students.html", students=students)


# View Companies
@admin.route("/admin/companies")
def companies():

    if not session.get("admin"):
        return redirect("/admin")

    companies = Company.query.all()
    return render_template("admin/companies.html", companies=companies)


# View Drives
@admin.route("/admin/drives")
def drives():

    if not session.get("admin"):
        return redirect("/admin")

    drives = Drive.query.all()
    return render_template("admin/drives.html", drives=drives)


# View Applications
@admin.route("/admin/applications")
def applications():

    if not session.get("admin"):
        return redirect("/admin")

    apps = Application.query.all()
    return render_template("admin/applications.html", apps=apps)


# Admin Logout
@admin.route("/admin/logout")
def admin_logout():

    session.pop("admin", None)
    return redirect("/")
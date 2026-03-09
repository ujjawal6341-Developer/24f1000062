from flask import Blueprint, render_template, request, redirect, session
from models import Student, Company, Drive, Application, Admin

admin = Blueprint("admin", __name__)


# ==============================
# Admin Login
# ==============================

@admin.route("/admin", methods=["GET", "POST"])
def admin_login():

    if session.get("admin_id"):
        return redirect("/admin/dashboard")

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        admin_user = Admin.query.filter_by(username=username, password=password).first()

        if admin_user:
            session["admin_id"] = admin_user.id
            return redirect("/admin/dashboard")

    return render_template("admin/admin_login.html")


# ==============================
# Admin Dashboard
# ==============================

@admin.route("/admin/dashboard")
def dashboard():

    if not session.get("admin_id"):
        return redirect("/admin")

    total_students = Student.query.count()
    total_companies = Company.query.count()
    total_drives = Drive.query.count()
    total_applications = Application.query.count()

    return render_template(
        "admin/dashboard.html",
        students=total_students,
        companies=total_companies,
        drives=total_drives,
        applications=total_applications
    )


# ==============================
# View Students
# ==============================

@admin.route("/admin/students")
def students():

    if not session.get("admin_id"):
        return redirect("/admin")

    students = Student.query.all()
    return render_template("admin/students.html", students=students)


# ==============================
# View Companies
# ==============================

@admin.route("/admin/companies")
def companies():

    if not session.get("admin_id"):
        return redirect("/admin")

    companies = Company.query.all()
    return render_template("admin/companies.html", companies=companies)


# ==============================
# View Drives
# ==============================

@admin.route("/admin/drives")
def drives():

    if not session.get("admin_id"):
        return redirect("/admin")

    drives = Drive.query.all()
    return render_template("admin/drives.html", drives=drives)


# ==============================
# View Applications
# ==============================

@admin.route("/admin/applications")
def applications():

    if not session.get("admin_id"):
        return redirect("/admin")

    apps = Application.query.all()
    return render_template("admin/applications.html", apps=apps)


# ==============================
# Approve Company
# ==============================
@admin.route("/admin/company/approve/<int:id>")
def approve_company(id):

    if not session.get("admin_id"):
        return redirect("/admin")

    company = Company.query.get(id)
    company.approval_status = "Approved"

    db.session.commit()

    return redirect("/admin/companies")


# ==============================
# Reject Company
# ==============================
@admin.route("/admin/company/reject/<int:id>")
def reject_company(id):

    if not session.get("admin_id"):
        return redirect("/admin")

    company = Company.query.get(id)
    company.approval_status = "Rejected"

    db.session.commit()

    return redirect("/admin/companies")


# ==============================
# Approve Drive
# ==============================
@admin.route("/admin/drive/approve/<int:id>")
def approve_drive(id):

    if not session.get("admin_id"):
        return redirect("/admin")

    drive = Drive.query.get(id)
    drive.status = "Approved"

    db.session.commit()

    return redirect("/admin/drives")


# ==============================
# Reject Drive
# ==============================
@admin.route("/admin/drive/reject/<int:id>")
def reject_drive(id):

    if not session.get("admin_id"):
        return redirect("/admin")

    drive = Drive.query.get(id)
    drive.status = "Rejected"

    db.session.commit()

    return redirect("/admin/drives")


# ==============================
# Admin Logout
# ==============================

@admin.route("/admin/logout")
def admin_logout():

    session.pop("admin_id", None)
    return redirect("/")
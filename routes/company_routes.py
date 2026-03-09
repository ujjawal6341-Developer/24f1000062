from flask import Blueprint, render_template, request, redirect, session
from models import db, Company, Drive, Application

company_bp = Blueprint("company", __name__)


# ==============================
# Company Registration
# ==============================

@company_bp.route("/company/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        company_name = request.form["company_name"]
        email = request.form["email"]
        website = request.form["website"]
        password = request.form["password"]

        # Check if email already exists
        existing_company = Company.query.filter_by(email=email).first()

        if existing_company:
            return "Company with this email already exists. Please login."

        new_company = Company(
            company_name=company_name,
            email=email,
            website=website,
            password=password
        )

        db.session.add(new_company)
        db.session.commit()

        return redirect("/login")

    return render_template("company/register.html", error="Email already exists")

# ==============================
# Company Shortlist Students
# ==============================

@company_bp.route("/company/shortlist/<int:id>")
def shortlist(id):

    if not session.get("company_id"):
        return redirect("/login")

    app = Application.query.get(id)

    app.status = "Shortlisted"

    db.session.commit()

    return redirect("/company/applications")

# ==============================
# Company Dashboard
# ==============================

@company_bp.route("/company/dashboard")
def dashboard():

    if not session.get("company_id"):
        return redirect("/login")

    company = Company.query.get(session["company_id"])

    if company.approval_status != "Approved":
        return "Waiting for admin approval."

    return render_template("company/dashboard.html")


# ==============================
# View Company Drives
# ==============================

@company_bp.route("/company/drives")
def drives():

    if not session.get("company_id"):
        return redirect("/login")

    company_id = session["company_id"]

    drives = Drive.query.filter_by(company_id=company_id).all()

    return render_template("company/drives.html", drives=drives)


# ==============================
# Create New Drive
# ==============================

@company_bp.route("/company/create_drive", methods=["GET", "POST"])
def create_drive():

    if not session.get("company_id"):
        return redirect("/login")

    if request.method == "POST":

        job_title = request.form["job_title"]
        job_description = request.form["job_description"]
        eligibility = request.form["eligibility"]

        company_id = session["company_id"]

        drive = Drive(
            company_id=company_id,
            job_title=job_title,
            job_description=job_description,
            eligibility=eligibility
        )

        db.session.add(drive)
        db.session.commit()

        return redirect("/company/drives")

    return render_template("company/create_drive.html")


# ==============================
# View Applications
# ==============================

@company_bp.route("/company/applications")
def applications():

    if not session.get("company_id"):
        return redirect("/login")

    company_id = session["company_id"]

    drives = Drive.query.filter_by(company_id=company_id).all()

    drive_ids = [d.id for d in drives]

    apps = Application.query.filter(Application.drive_id.in_(drive_ids)).all()

    return render_template("company/applications.html", apps=apps)
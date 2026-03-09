from flask import Blueprint, render_template, request, redirect, session
from models import db, Company, Drive, Application

from flask import Blueprint

company_bp = Blueprint("company", __name__)


# Company Registration
@company_bp.route("/company/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        company_name = request.form["company_name"]
        email = request.form["email"]
        website = request.form["website"]
        password = request.form["password"]

        new_company = Company(
            company_name=company_name,
            email=email,
            website=website,
            password=password
        )

        db.session.add(new_company)
        db.session.commit()

        return redirect("/login")

    return render_template("company/register.html")


# Company Dashboard
@company_bp.route("/company/dashboard")
def dashboard():

    if not session.get("company_id"):
        return redirect("/login")

    return render_template("company/dashboard.html")


# View Company Drives
@company_bp.route("/company/drives")
def drives():

    if not session.get("company_id"):
        return redirect("/login")

    company_id = session.get("company_id")

    drives = Drive.query.filter_by(company_id=company_id).all()

    return render_template("company/drives.html", drives=drives)


# Create New Drive
@company_bp.route("/company/create_drive", methods=["POST"])
def create_drive():

    if not session.get("company_id"):
        return redirect("/login")

    role = request.form["role"]
    eligibility = request.form["eligibility"]

    company_id = session.get("company_id")

    drive = Drive(
        company_id=company_id,
        role=role,
        eligibility=eligibility
    )

    db.session.add(drive)
    db.session.commit()

    return redirect("/company/drives")


# View Applications for Company's Drives
@company_bp.route("/company/applications")
def applications():

    if not session.get("company_id"):
        return redirect("/login")

    company_id = session.get("company_id")

    drives = Drive.query.filter_by(company_id=company_id).all()

    drive_ids = [d.id for d in drives]

    apps = Application.query.filter(Application.drive_id.in_(drive_ids)).all()

    return render_template("company/applications.html", apps=apps)
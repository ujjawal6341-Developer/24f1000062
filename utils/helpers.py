import os

from functools import wraps

from flask import session, redirect, url_for, flash

from werkzeug.utils import secure_filename

from models import Application


# LOGIN REQUIRED

def login_required(role):

    def decorator(f):

        @wraps(f)

        def wrapper(*args, **kwargs):

            if role not in session:

                flash("Please login first")

                return redirect(url_for("auth.login"))

            return f(*args, **kwargs)

        return wrapper

    return decorator


# SAVE RESUME FILE

def save_resume(file, upload_folder):

    if file:

        filename = secure_filename(file.filename)

        path = os.path.join(upload_folder, filename)

        file.save(path)

        return filename

    return None


# CHECK DUPLICATE APPLICATION

def already_applied(student_id, drive_id):

    app = Application.query.filter_by(

        student_id=student_id,

        drive_id=drive_id

    ).first()

    if app:

        return True

    return False


# ADMIN CHECK

def admin_required(f):

    @wraps(f)

    def wrapper(*args, **kwargs):

        if "admin" not in session:

            flash("Admin login required")

            return redirect(url_for("auth.login"))

        return f(*args, **kwargs)

    return wrapper


# COMPANY CHECK

def company_required(f):

    @wraps(f)

    def wrapper(*args, **kwargs):

        if "company" not in session:

            flash("Company login required")

            return redirect(url_for("auth.login"))

        return f(*args, **kwargs)

    return wrapper


# STUDENT CHECK

def student_required(f):

    @wraps(f)

    def wrapper(*args, **kwargs):

        if "student" not in session:

            flash("Student login required")

            return redirect(url_for("auth.login"))

        return f(*args, **kwargs)

    return wrapper
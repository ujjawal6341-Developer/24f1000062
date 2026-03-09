from flask import Flask, render_template
from models import db, Drive
import os

# ==============================
# Create Flask App
# ==============================

app = Flask(__name__)

# Secret key for sessions
app.config["SECRET_KEY"] = "secretkey"

# ==============================
# Upload Folder Configuration
# ==============================

UPLOAD_FOLDER = "static/resumes"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# ==============================
# Database Configuration
# ==============================

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///placement.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize database
db.init_app(app)

# ==============================
# Import Blueprints
# ==============================

from routes.auth_routes import auth
from routes.student_routes import student_bp
from routes.company_routes import company_bp
from routes.admin_routes import admin

# ==============================
# Register Blueprints
# ==============================

app.register_blueprint(auth)
app.register_blueprint(student_bp)
app.register_blueprint(company_bp)
app.register_blueprint(admin)

# ==============================
# Home Routes
# ==============================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# ==============================
# Public Jobs Page
# ==============================

@app.route("/jobs")
def jobs():

    drives = Drive.query.all()

    return render_template("jobs.html", drives=drives)


# ==============================
# Run Application
# ==============================

if __name__ == "__main__":
    app.run(debug=True)
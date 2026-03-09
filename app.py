from flask import Flask, render_template
from models import db
from models import db, Drive
from models import *

# Import Blueprints
from routes.auth_routes import auth
from routes.student_routes import student_bp
from routes.company_routes import company_bp
from routes.admin_routes import admin


# ==============================
# Create Flask App
# ==============================

app = Flask(__name__)

# Secret key for sessions
app.config["SECRET_KEY"] = "secretkey"


# ==============================
# Database Configuration
# ==============================

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///placement.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize database
db.init_app(app)

# ==============================
# Register Blueprints
# ==============================

app.register_blueprint(auth)
app.register_blueprint(student_bp)
app.register_blueprint(company_bp)
app.register_blueprint(admin)


# ==============================
# Home Route
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

@app.route("/jobs")
def jobs():

    drives = Drive.query.all()

    return render_template("jobs.html", drives=drives)

# ==============================
# Run Application
# ==============================

if __name__ == "__main__":

    with app.app_context():
        db.create_all()  # Create tables if they do not exist

    app.run(debug=True)
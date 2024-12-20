from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from practizr.db import get_db
from practizr.auth import login_required


views_bp = Blueprint("views", __name__)


@views_bp.route("/")
def index():
    return render_template("views/index.html")


@views_bp.route("/dashboard")
@login_required
def dashboard():
    db = get_db()
    area_rows = db.execute("SELECT * FROM area").fetchall()
    areas = [row['area_name'] for row in area_rows]
    return render_template("views/dashboard.html", areas=areas)

# def templates():
#     return render_template("views/templates.html")


# @views_bp.route("/items", methods=["GET", "POST"])
# def items():
#     return render_template("views/items.html")


# @views_bp.route("/addrow", methods=["POST"])
# def addrow():
#     if request.method == "POST":
#         db = get_db()

#     return redirect("/")
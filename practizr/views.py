from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from practizr.db import get_db


views_bp = Blueprint("views", __name__)


@views_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return render_template("views/index.html")
    db = get_db()
    areas = ["Technique", "Music Theory", "Repertoire", "Transcription", "Ear Training", "Improvisation"]
    return render_template("views/index.html", areas=areas)


# @views_bp.route("/templates", methods=["GET", "POST"])
# def templates():
#     return render_template("views/templates.html")


# @views_bp.route("/items", methods=["GET", "POST"])
# def items():
#     return render_template("views/items.html")


@views_bp.route("/addrow", methods=["POST"])
def addrow():
    if request.method == "POST":
        db = get_db()

    return redirect("/")
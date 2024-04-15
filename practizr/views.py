from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from practizr.db import get_db


views_bp = Blueprint("views", __name__)


@views_bp.route("/", methods=["GET", "POST"])
def index():
    db = get_db()
    if request.method == "POST":
        return render_template("views/index.html")
    return render_template("views/index.html")


@views_bp.route("/templates", methods=["GET", "POST"])
def templates():
    return render_template("views/templates.html")


@views_bp.route("/items", methods=["GET", "POST"])
def items():
    return render_template("views/items.html")


@views_bp.route("/addrow", methods=["GET", "POST"])
def addrow():
    if request.method == "POST":
        return render_template("views/index.html")

    else:
        return render_template("views/index.html")

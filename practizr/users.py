from functools import wraps

from flask import Blueprint, request, flash

from practizr.db import get_db


users_bp = Blueprint("users", __name__)


@users_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db

        if not username:
            flash("Username required.")
        if not password:
            flash("Password required.")
        
        
from functools import wraps

from flask import Blueprint, redirect, render_template, request, flash, url_for

from practizr.db import get_db

from practizr.functions import is_empty

from werkzeug.security import check_password_hash, generate_password_hash


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        db = get_db
        message = is_empty(username=username, password=password)

        if message is None:
            try:
                db.execute(
                    "INSTERT INTO user (username, password_hash) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                message = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))
            
        flash(message)

    return render_template("auth/register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        message = None

        
        

            

        

        
        
        
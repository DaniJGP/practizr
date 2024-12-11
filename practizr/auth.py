from functools import wraps

from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    flash,
    url_for,
    session,
    g,
)

from practizr.db import get_db

from practizr.functions import is_empty

from werkzeug.security import check_password_hash, generate_password_hash


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        db = get_db()
        message = is_empty(username=username, password=password)

        if message is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password_hash) VALUES (?, ?)",
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
        message = is_empty(username=username, password=password)

        if message is None:
            row = db.execute("SELECT * FROM user WHERE username = ?", (username,)).fetchone()
            if row is None:
                message = "User does not exist."
            else:
                if check_password_hash(row["password_hash"], password):
                    session["user_id"] = row["id"]
                    session["username"] = row["username"]
                    return redirect(url_for("views.dashboard"), 302)
                else:
                    message = "Wrong password."

        flash(message)

    return render_template("auth/login.html")


@auth_bp.route("/logout", methods=["GET","POST"])
def logout():
    session.clear()
    return redirect(url_for("views.index"))


@auth_bp.before_app_request
def load_login_to_g():
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
    else:
        g.user = (
            get_db().execute("SELECT * FROM user WHERE id = ?", (user_id,)).fetchone()
        )


def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        
        return view(**kwargs)
    
    return wrapped_view


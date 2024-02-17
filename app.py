from flask import Flask, flash, render_template

app = Flask(__name__)
app.secret_key = b'I.zCPA"m,8TAkoy(}Cfc'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/addrow", methods=["POST"])
def addrow():
    flash("You added the row")
    return render_template("index.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
from flask import Flask, redirect, render_template, request
from cs50 import SQL

app = Flask(__name__)
# TODO Read more about this secret key stuff
app.secret_key = b'I.zCPA"m,8TAkoy(}Cfc'


practice_table = []

db = SQL("sqlite:///tmp/test.db")

@app.route("/")
def index():
    area_list = []
    for row in db.execute("SELECT DISTINCT area FROM items"):
        area_list.append(row['area'])
    
    return render_template("index.html", area_list=area_list)


@app.route("/addrow", methods=['GET','POST'])
def addrow():
    if request.method == 'POST':
        practice_table.append(request.form)
        return render_template("index.html", practice_table=practice_table)
    else:
        return redirect("/")


if __name__ == '__main__':
    app.debug = True
    app.run()
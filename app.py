from flask import Flask, redirect, render_template, request

app = Flask(__name__)
# TODO Read more about this secret key stuff
app.secret_key = b'I.zCPA"m,8TAkoy(}Cfc'

area_list = ["Technique", "Music Theory", "Repertoire", "Transcription", "Ear Training", "Improvisation"]
practice_table = []

@app.route("/")
def index():
    return render_template("index.html", area_list=area_list)


@app.route("/addrow", methods=['GET','POST'])
def addrow():
    if request.method == 'POST':
        practice_table.append(request.form)
        return render_template("index.html", area_list=area_list, practice_table=practice_table)
    else:
        return redirect("/")


if __name__ == '__main__':
    app.debug = True
    app.run()
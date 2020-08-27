from flask import Flask, render_template, url_for, request, redirect
from bin.music.diatonic import Chords, get_all_notes

app = Flask(__name__)

@app.route('/')
def hello_world():
    # info = Chords("C").get_diatonic_chords()
    return render_template("index.html")

@app.route('/diatonic', methods=['GET', 'POST'])
def diatonic_home():
    notes = get_all_notes()
    if request.method == "POST":
        key = request.form["comp_select"]
        x = redirect(url_for("major_chords",key=key))
    else:
        x = render_template("diatonic.html", notes=notes)

    return x

@app.route('/<key>-major-chords',methods=['GET', 'POST'])
def major_chords(key):
    # key = request.form.get("comp_select")
    chords = Chords(key).get_all_triads()
    return render_template("triads.html", key = key, **chords)

@app.route('/basic-music-theory')
def basic_theory():
    # info = Chords("C").get_diatonic_chords()
    return render_template("basic-music-theory.html")

@app.route('/advanced-ideas')
def advanced_ideas():
    # info = Chords("C").get_diatonic_chords()
    return render_template("advanced-ideas.html")

@app.route('/about-us')
def about_us():
    # info = Chords("C").get_diatonic_chords()
    return render_template("about-us.html")


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)
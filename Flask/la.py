from flask import Flask

app = Flask(__name__)


@app.route("/judul_routing")
def judul_routing():
    return "Ini Halaman Judul Routing"


@app.route("/nama_anda")
def nama_anda():
    return "Ini Halaman Naufal Arkan Zhafran"


@app.route("/nama_teman1")
def nama_teman1():
    return "Ini Halaman King Fajar"


@app.route("/nama_teman2")
def nama_teman2():
    return "Ini Halaman King Rehan"


@app.route("/nama_teman3")
def nama_teman3():
    return "Ini Halaman King Hazeem"


if __name__ == "__main_":
    app.run(debug=True)

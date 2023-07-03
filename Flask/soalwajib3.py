from flask import Flask

app = Flask(__name__)

@app.route("/")
def judul_routing():
    return "Hallo Nama Saya Naufal Arkan Zhafran"


@app.route("/about")
def nama_anda():
    return "Saya Dari Kelas 1IA10"


@app.route("/tujuan")
def nama_teman1():
    return "Tujuan Saya Masuk Informatika Adalah Untuk Menjadi Seorang Web Developer"


if __name__ == "__main__":
    app.run(debug=True)
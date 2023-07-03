from flask import Flask, jsonify, request

app = Flask(__name__)
stores = [
    {
        "name": "Perpustakaan",
        "items": [
            {
                "name": "Jurnal Implementasi Array 3 Dimensi",
                "pembuat": "Adrian Nova",
                "terbit": "3 Januari 2020",
                "price": 50000,
            }
        ],
    },
    {
        "name": "Toko Komik",
        "items": [
            {
                "name": "Violet Evergarden",
                "pembuat": "Kana Akatsuki",
                "terbit": "25 Desember 2015",
                "price": 64000,
            }
        ],
    },
]


# GET Nama Toko
@app.route("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store["name"])
    return jsonify({"message": "Store Not Found"})


# GET Item Toko
@app.route("/store/<string:name>/item")
def get_store_items(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store["items"])
    return jsonify({"message": "Store Not Found"})


# POST Membuat Toko
@app.route("/store", methods=["POST"])
def create_store():
    req_data = request.get_json()
    new_store = {"name": req_data["name"], "items": []}
    stores.append(new_store)
    return jsonify(new_store)


# POST Membuat Item Toko
@app.route("/store/<string:name>/item", methods=["POST"])
def create_store_item(name):
    for store in stores:
        if store["name"] == name:
            req_data = request.get_json()
            new_item = {
                "nama barang": req_data["nama barang"],
                "pembuat": req_data["pembuat"],
                "tanggal rilis": req_data["tanggal rilis"],
                "price": req_data["price"],
            }
            store["items"].append(new_item)
            return jsonify(new_item)


@app.route("/")
def home():
    return "hey"


app.run(port=8000)

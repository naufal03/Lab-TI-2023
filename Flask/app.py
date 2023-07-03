from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
  a = 'Hello Nama Saya Naufal Arkan Zhafran'
  b = 'Saya Mahasiswa Gunadarma'
  return a+b

@app.route('/about')
def about():
  return 'Salam Kenal, Ini adalah page "about"'

if __name__ == '__main__':
  app.run(debug=True)
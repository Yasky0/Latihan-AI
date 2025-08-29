from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Halo ini API sekolah"

@app.route('/siswa/<name>')
def siswa(name):
    return f"Halo {name}, selamat datang di sistem sekolah!"

if __name__ == '__main__':
    app.run(debug=True)
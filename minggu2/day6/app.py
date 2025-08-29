from flask import Flask, jsonify

app = Flask(__name__)

daftarGuru = ['Pak Budi', 'Bu Sandy', 'Pak Anis']
daftarSiswa = {
    'ucup': {'nama':'ucup', 'kelas':'XIIA'},
    'agus': {'nama':'agus', 'kelas':'XIIB'},
    'dudung': {'nama':'dudung', 'kelas':'XIIC'}
}

@app.route('/guru')
def guru():
    return jsonify(daftarGuru)

@app.route('/siswa/<nama>')
def siswa(nama):
    nama = nama.lower()
    if nama in daftarSiswa:
        return jsonify(daftarSiswa[nama])
    else:
        return jsonify({'error': "Siswa tidak ditemukan"})

if __name__ == '__main__':
    app.run(debug=True)
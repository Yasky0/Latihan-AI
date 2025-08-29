import os
import sqlite3
from flask import Flask,jsonify,request

nama = {}
kelas = {}

app = Flask(__name__)
path = 'minggu2/day7/sekolah.db'

def init_db():
    """Inisialisasi database"""
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS sekolah(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT,
        kelas VARCHAR (4)
    )
    """)
        
    cur.execute("SELECT COUNT(*) FROM sekolah")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO sekolah(nama, kelas) VALUES(?, ?)", ("Yasky","XIIA"))
        cur.execute("INSERT INTO sekolah(nama, kelas) VALUES(?, ?)", ("Einstein","XIIB"))
        cur.execute("INSERT INTO sekolah(nama, kelas) VALUES(?, ?)", ("Robert","XIIC"))
        conn.commit()

    cur.close()
    conn.close()
    
# Flask API
@app.route('/semua_siswa', methods=["GET"])
def home():
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM sekolah")
    siswa = cur.fetchall()
    cur.close()
    conn.close()
    
    hasil = [
        {"id": row[0], "nama": row[1], "kelas": row[2]}
        for row in siswa
    ]
    
    return jsonify(hasil)

# Akses data siswa dengan ID
@app.route('/semua_siswa/id=<int:id>', methods=["GET"])
def siswa(id):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM sekolah WHERE id=?", (id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    
    if row:
        hasil = {"id": row[0], "nama": row[1], "kelas": row[2]}
        return jsonify(hasil)
    else:
        return jsonify({"error": "Siswa tidak ditemukan"}), 404

# Menambahkan data siswa
@app.route('/tambah_siswa', methods=['POST'])
def tambah_siswa():
    data = request.json
    nama = data.get("nama")
    kelas = data.get("kelas")
    
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute("INSERT INTO sekolah(nama, kelas) VALUES(?, ?)", (nama, kelas))
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({"message": f"data {nama} berhasil ditambahkan ke dalam data base"})

# Delete data siswa
@app.route('/hapus_siswa/id=<int:id>', methods=["GET", "DELETE"])
def delete_siswa(id):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute("DELETE FROM sekolah WHERE id=?", (id,))
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({"message": f"data dengan ID {id} berhasil dihapus dari database"})
    
if __name__ == "__main__":
    # hanya init DB kalau bukan child reloader
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        init_db()
    app.run(debug=True)
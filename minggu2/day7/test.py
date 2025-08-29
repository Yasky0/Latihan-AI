import requests

url = "http://127.0.0.1:5000/hapus_siswa/id=4"
d = requests.delete(url)
print(d.json())
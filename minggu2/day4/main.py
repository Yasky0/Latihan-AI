import requests

username = input("Masukan username GitHub: ")
url = requests.get(f'https://api.github.com/users/{username}')
data = url.json()
print(f"Nama: {data['login']} \nJumlah Repository Publik: {data['public_repos']} \nLokasi: {data['location']}")
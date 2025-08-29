import csv

with open("minggu2/day2/jadwal.csv", "r") as file:
    jadwal = csv.DictReader(file)
    jadwal_dict = {row["hari"]: row["mapel"] for row in jadwal}
    hari = input("Hari apa? ").capitalize()
    print(f"Jadwal untuk hari {hari} adalah {jadwal_dict.get(hari)}")
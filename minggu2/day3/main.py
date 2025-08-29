import csv

with open("minggu2/day3/jadwal.csv", "r") as csvjadwal:
    dict_jadwal = csv.DictReader(csvjadwal)
    jadwal = {key["hari"].capitalize(): [key["mapel"].capitalize(), key["guru"].capitalize()] for key in dict_jadwal}
    while True:
        try:
            user_hari = input(f"{'='*35}\nMasukan hari: ").capitalize()
            if user_hari == "Minggu":
                print("Tidak ada jadwal pada hari Minggu")
                continue
            print(f"{'='*35}\nJadwal pelajaran untuk hari {user_hari}:\n{jadwal[user_hari][0]} - {jadwal[user_hari][1]}")
            isdone = input("Apakah ingin melanjutkan (y/n)? ")
            if isdone == "n":
                break
        except:
            print(f"Tidak hari bernama {user_hari}")
            isdone = input("Apakah ingin melanjutkan (y/n)? ")
            if isdone == "n":
                break
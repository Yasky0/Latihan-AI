class hero:
    # Class variabel
    jumlah_hero = 0
    
    def __init__(self, nama, health, power, armor,):
        self.nama = nama
        self.health = health
        self.power = power
        self.armor = armor
        hero.jumlah_hero += 1
        print(f"Berhasil menambahkan hero baru bernama : {nama}")
    
    def siapa(self):
        print(f"Hero1 adalah {self.nama}")
    
    def healthUp(self, up):
        self.health += up
    
    def diserang(self, power):
        return self.health - power

hero1 = hero('Tank', 300, 3, 7)
hero2 = hero('Marksman', 100, 30, 3)
hero3 = hero('Fighter', 200, 12, 5)
hero3.healthUp(50)
print(hero3.health)
print(hero1.diserang(hero2.power))

hero1.siapa()
hero2.siapa()
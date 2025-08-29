class hero:
    
    def __init__(self, name, health, power, armor,):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
    
    def healthUp(self, up):
        self.health += up
    
    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}")
        lawan.diserang(self, self.power)

    def diserang(self, lawan, attackPower):
        print(f'{self.name} diserang {lawan.name}')
        damage = attackPower/self.armor
        print(f"Damage yang diterima {self.name}: {damage}")
        self.health -= damage
        print(f"health yang tersisa {self.name} adalah {self.health}")

tank = hero('Tank', 300, 5, 10)
marksman = hero('Marksman', 100, 30, 2.5)
fighter = hero('Fighter', 200, 10, 5)

print(tank.health)
while True:
    fighter.serang(tank)
    print('\n')
    tank.serang(fighter)
    if tank.health or fighter.health <= 0:
        break
print(tank.health)
print(fighter.health)

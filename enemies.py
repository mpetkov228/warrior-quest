class Enemy:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage
        self.isAlive = True

    
    def attack(self, target):
        target.health -= self.damage


class Ghoul(Enemy):
    def __init__(self):
        super().__init__(40, 5)
        self.name = "Ghoul"

    
    def speak(self):
        print("Ghoul: Me eat brains...")


class Troll(Enemy):
    def __init__(self):
        super().__init__(55, 10)
        self.name = "Troll"


    def speak(self):
        print("Troll: Ye'd make a fine dinner...")


class Crocolisk(Enemy):
    def __init__(self):
        super().__init__(45, 8)
        self.name = "Crocolisk"
    

    def speak(self):
        print("Crocolisk: Raaawr...")


class Raptor(Enemy):
    def __init__(self):
        super().__init__(60, 12)
        self.name = "Raptor"

    
    def speak(self):
        print("Raptor: Raaawr...")


class Undead(Enemy):
    def __init__(self):
        super().__init__(65, 15)
        self.name = "Undead"


    def speak(self):
        print("Undead: Intruder.. Die!")


class DarkSorcerer(Enemy):
    def __init__(self):
        super().__init__(80, 20)
        self.name = "Dark Sorcerer"
    

    def speak(self):
        print("Dark Sorcerer: You will not disturb the master...")
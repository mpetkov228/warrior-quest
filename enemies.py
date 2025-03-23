class Enemy:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    
    def attack(self, target):
        target.health -= self.damage


class Ghoul(Enemy):
    def __init__(self):
        super().__init__(40, 5)

    
    def speak(self):
        print("Ghoul: Me eat brains...")


class Troll(Enemy):
    def __init__(self):
        super().__init__(55, 10)


    def speak(self):
        print("Troll: Ye'd make a fine dinner...")


class Crocolisk(Enemy):
    def __init__(self):
        super().__init__(45, 8)
    

    def speak(self):
        print("Crocolisk: Raaawr...")


class Raptor(Enemy):
    def __init__(self):
        super().__init__(60, 12)
    
    def speak(self):
        print("Raptor: Raaawr...")


class Undead(Enemy):
    def __init__(self):
        super().__init__(65, 15)


    def speak(self):
        print("Undead: Intruder.. Die!")


class DarkSorcerer(Enemy):
    def __init__(self):
        super().__init__(80, 20)
    

    def speak(self):
        print("Dark Sorcerer: You will not disturb the master...")
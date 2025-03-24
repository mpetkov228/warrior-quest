class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.isAlive = True

    
    def attack(self, target):
        target.take_damage(self.damage)
        print(f"\n{self.name} attacks {target.name}")


    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.isAlive = False



class Ghoul(Enemy):
    def __init__(self):
        super().__init__("Ghoul", 40, 5)

    
    def speak(self):
        print("Ghoul: Me eat brains...")


class Troll(Enemy):
    def __init__(self):
        super().__init__("Troll", 55, 10)


    def speak(self):
        print("Troll: Ye'd make a fine dinner...")


class Crocolisk(Enemy):
    def __init__(self):
        super().__init__("Crocolisk", 45, 8)
    

    def speak(self):
        print("Crocolisk: Raaawr...")


class Raptor(Enemy):
    def __init__(self):
        super().__init__("Raptor", 60, 12)

    
    def speak(self):
        print("Raptor: Raaawr...")


class Undead(Enemy):
    def __init__(self):
        super().__init__("Undead", 65, 15)


    def speak(self):
        print("Undead: Intruder.. Die!")


class DarkSorcerer(Enemy):
    def __init__(self):
        super().__init__("Dark Sorcerer", 80, 20)
    

    def speak(self):
        print("Dark Sorcerer: You will not disturb the master...")
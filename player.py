class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 20
        self.isAlive = True

    
    def attack(self, target):
        print(f"{target.name}: {target.health} hp")
        print(f"You attack {target.name} dealing {self.damage} damage")
        target.health -= self.damage
        print(f"{target.name} has {target.health} hp remaining")


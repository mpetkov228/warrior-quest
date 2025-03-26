class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 20
        self.gold_amount = 20
        self.is_alive = True
        self.inventory = {
            "health potion": 2,
            "wooden sword": 1,
            "cloth armor": 1
        }

    
    def attack(self, target):
        print(f"\nYou attack {target.name} dealing {self.damage} damage")
        target.take_damage(self.damage)
        if target.health < 0:
            print(f"{target.name} has 0 hp")
        else:
            print(f"{target.name} has {target.health} hp remaining")

    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False


    def buy_item(self, item):
        item_type, price = item
        self.gold_amount -= price
        if item_type in self.inventory:
            self.inventory[item_type] += 1
        else:
            self.inventory[item_type] = 1



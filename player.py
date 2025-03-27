class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 20
        self.armor = 5
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
        armor_reduction = 0
        if self.armor > 0:
            armor_reduction = damage * (self.armor / 100)

        self.health -= int(damage - armor_reduction)
        if self.health <= 0:
            self.is_alive = False


    def buy_item(self, item):
        item_type, price = item
        self.gold_amount -= price
        if item_type in self.inventory:
            self.inventory[item_type] += 1
        else:
            self.inventory[item_type] = 1

    
    def drink_potion(self):
        if self.inventory["health potion"] <= 0:
            print("No potions in inventory")
            return
        if self.health == 100:
            print("You are already at full health")
            return
        
        self.health += 40
        if self.health > 100:
            self.health = 100



    def change_armor(self):
        if "chain-mail armor" in self.inventory:
            self.armor = 30
        elif "leather armor" in self.inventory:
            self.armor = 15
            
    
    def change_weapon(self):
        if "steel sword" in self.inventory:
            self.damage = 50
        elif "bronze sword" in self.inventory:
            self.damage = 35
import random
from player import Player
from enemies import Ghoul, Raptor, Crocolisk, Troll, Undead, DarkSorcerer
from utils import dash_separator


player = Player("Bob")

locations = {
    "town": {
        "name": "Dunhaven",
        "description": "A bustling town centre.",
        "directions": {
            "north": "outskirts",
            "shop": "shop"
        }
    },
    "shop": {
        "name": "Adventurer Supplies",
        "description": "One stop shop for your adventuring needs",
        "directions": {
            "vendor": "shop",
            "back": "town"
        }
    },
    "outskirts": {
        "name": "Outskirts of Dunhaven",
        "description": "Outskirts of town.",
        "directions": {
            "north": "woods",
            "south": "town"
        }
    },
    "woods": {
        "name": "The Whispering Woods",
        "description": "The Whispering Woods - a scary place!",
        "directions": {
            "west": "marsh",
            "south": "outskirts"
        }
    },
    "marsh": {
        "name": "The Hollow Marsh",
        "description": "The Hollow Marsh, home to the fearsome Bogwyrm.",
        "directions": {
            "north": "ruins",
            "east": "woods"
        }
    },
    "ruins": {
        "name": "Ruins of Eldoria",
        "description": "Ruins of Eldoria, Malagar's fortress",
        "directions": {
            "south": "marsh"
        }
    }
}


encounters = {
    "woods": ["ghoul", None, "troll", None],
    "marsh": ["raptor", None, None, "crocolisk"],
    "ruins": ["undead", None, "dark sorcerer", None]
}


def create_enemy(kind):
    match kind:
        case "ghoul":
            return Ghoul()
        case "troll":
            return Troll()
        case "crocolisk":
            return Crocolisk()
        case "raptor":
            return Raptor()
        case "undead":
            return Undead()
        case "dark sorcerer":
            return DarkSorcerer()


def combat(enemy):
    print(dash_separator)
    enemy.speak()
    print(f"{enemy.name} engages you in combat!")

    while True:
        choice = input("What is your next move? ")
        if choice == "attack":
            player.attack(enemy)

        if not enemy.is_alive:
            print(f"Victory! {enemy.name} is defeated!")
            break
        
        enemy.attack(player)
        print(f"You have {player.health} hp remaining")

        if not player.is_alive:
            print(f"You were killed by {enemy.name}!")
            print("Game Over!")
            exit()


def trigger_encounter(location):
    if location not in encounters:
        return

    possible_encounters = encounters[location]
    choice = random.choice(possible_encounters)
    if not choice:
        return
    
    enemy = create_enemy(choice)
    combat(enemy)


def load_shop():
    shop_inventory = {
        "health potion": 5,
        "bronze sword": 20,
        "steel sword": 50,
        "leather armor": 25,
        "chain-mail armor": 60,
        "wooden buckler": 15,
        "medium shield": 45
    }

    print(dash_separator)

    items = list(shop_inventory.items())
    i = 1
    for item, price in items:
        print(f"{i}. {item} - {price}g")
        i += 1

    while True:
        choice = input("Shopkeeper: What do you want to buy? (enter the item number or 'leave')\n")

        if choice == "leave":
            print("Shopkeeper: See you again soon!")
            break

        try:
            index = int(choice) - 1
            if index in range(len(items)):
                item_type, price = items[index]
                if price <= player.gold_amount:
                    player.buy_item((item_type, price))
                    print(f"You buy {item_type}.")
                else:
                    print("Not enough gold!")
        except:
            print()
        print(player.inventory)



def move(new_location):
    print("You move to " + locations[new_location]["name"] + ".")
    trigger_encounter(new_location)
    return new_location, locations[new_location]["directions"]
    

def main():
    current_location = "town"
    directions = locations[current_location]["directions"]

    while True:
        print("--------------")
        print(f"You are in {locations[current_location]["name"]}")
        print("Where would you like to go from here?")
        for key, value in directions.items():
            print(f"{key} - {locations[value]["name"]}")

        direction = input().lower()

        if direction == "quit":
            break

        if direction in directions:
            current_location, directions = move(directions[direction])
            if current_location == "shop":
                load_shop()
        else:
            print("Please enter a valid direction or 'quit'")
            continue


main()
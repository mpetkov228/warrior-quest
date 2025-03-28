import random
from player import Player
from enemies import Ghoul, Raptor, Crocolisk, Troll, Undead, DarkSorcerer
from bosses import Malagar
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
            "dark tower": "dark tower",
            "south": "marsh"
        }
    },
    "dark tower": {
        "name": "The Dark Tower",
        "description": "Lord Malagar's lair",
        "directions": {
            "back": "ruins"
        }
    }
}


encounters = {
    "woods": ["ghoul", None, "troll", None],
    "marsh": ["raptor", None, None, "crocolisk"],
    "ruins": ["undead", None, "dark sorcerer", None],
    "dark tower": ["malagar"]
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
        case "malagar":
            return Malagar()


def random_gold():
    return random.randint(5, 10)


def fight_mob(enemy):
    while True:
        print("1. Attack")
        print("2. Drink potion")
        print("3. Flee")
        choice = input("What is your next move? (enter number) ")
        if choice == "1":
            player.attack(enemy)
        elif choice == "2":
            player.drink_potion()
        elif choice == "3":
            print("You flee and manage to escape.")
            return
        else:
            continue

        if not enemy.is_alive:
            gold = random_gold()
            player.gold_amount += gold
            print(f"Victory! {enemy.name} is defeated! You loot {gold} gold.")
            return
        
        enemy.attack(player)
        print(f"You have {player.health} hp remaining")

        if not player.is_alive:
            print(f"You were killed by {enemy.name}!")
            print("Game Over!")
            exit()


def fight_boss(enemy):
    fight_mob(enemy)
    print(dash_separator)
    print("Congratulations! You have bested " + enemy.name + " and saved Dunhaven and its people!")
    print("Thank you for playing!")
    exit()


def combat(enemy):
    print(dash_separator)
    enemy.speak()
    print(f"{enemy.name} engages you in combat!")

    if enemy.name != "Lord Malagar":
        fight_mob(enemy)
    else:
        fight_boss(enemy)


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

    while True:
        i = 1
        for item, price in items:
            print(f"{i}. {item} - {price}g")
            i += 1
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
                    player.change_armor()
                    player.change_weapon()
                    print(f"You buy {item_type}.")
                else:
                    print("Not enough gold!")
        except:
            print()


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
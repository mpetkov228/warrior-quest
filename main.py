import random
from player import Player
from enemies import Ghoul, Raptor, Crocolisk, Troll, Undead, DarkSorcerer

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
    print(f"{enemy.name} engages you in combat!")

    while enemy.isAlive or player.isAlive:
        choice = input("What is your next move?")
        if choice == "attack":
            player.attack(enemy)
        
        enemy.attack(player)


def trigger_encounter(location):
    if location not in encounters:
        return

    possible_encounters = encounters[location]
    choice = random.choice(possible_encounters)
    if not choice:
        return
    
    enemy = create_enemy(choice)
    enemy.speak()
    combat(enemy)


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
        else:
            print("Please enter a valid direction or 'quit'")
            continue


main()
from player import Player

player = Player("Bob")

locations = {
    "town": {
        "name": "Dunhaven",
        "description": "A bustling town centre.",
        "directions": {
            "north": "outskirts"
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


def main():
    current_location = "town"
    directions = locations[current_location]["directions"]

    while True:
        print()
        print(f"You are in {locations[current_location]["name"]}")
        print("Where would you like to go from here?")
        for key, value in directions.items():
            print(f"{key} - {locations[value]["name"]}")
        direction = input()
        if direction == "quit":
            break
        if direction in directions:
            current_location = directions[direction]
            directions = locations[current_location]["directions"]
            print(f"You move to {locations[current_location]["name"]}")
        else:
            print("Please type in a valid direction or 'quit'")
            continue


main()
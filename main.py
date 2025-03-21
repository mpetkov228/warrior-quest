from player import Player

player = Player("Bob")

locations = {
    "town": {
        "description": "A bustling town centre.",
        "directions": {
            "north": "outskirts"
        }
    },
    "outskirts": {
        "description": "Outskirts of town.",
        "directions": {
            "north": "woods",
            "south": "town"
        }
    },
    "woods": {
        "description": "The Whispering Woods - a scary place!",
        "directions": {
            "west": "marsh",
            "south": "outskirts"
        }
    },
    "marsh": {
        "description": "The Hollow Marsh, home to the fearsome Bogwyrm.",
        "directions": {
            "north": "ruins",
            "east": "woods"
        }
    },
    "ruins": {
        "description": "Ruins of Eldoria, Malagar's fortress",
        "directions": {
            "south": "marsh"
        }
    }
}


def main():

    current_location = "town"

    



main()
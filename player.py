class Player:
    def __init__(self, name, current_location="town"):
        self.name = name
        self.health = 100
        self.current_location = current_location

    
    def move(self, location):
        self.current_location = location

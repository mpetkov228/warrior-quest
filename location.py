class Location:
    def __init__(self, name, directions):
        self.name = name
        self.directions = directions

    
    def __str__(self):
        result = f"You are in {self.name}...\n"
        return result + "\n".join(self.directions)
            
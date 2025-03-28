from enemies import Enemy


# class Bogwyrm(Enemy):
#     def __init__(self):
#         super().__init__("Bogwyrm", 200, 30)
#         self.armor = 50

    
class Malagar(Enemy):
    def __init__(self):
        super().__init__("Lord Malagar", 300, 40)
        self.armor = 60


    def speak(self):
        print("I have watched you struggle against my followers.")
        print("Quite pitiful... Come, weakling! Face your doom!")
from src.objects import unit

class Pig(unit.Unit):
    def __init__(self, x, y, width, height, end):
        super().__init__(x, y, width, height, end)
        self.health = 11
        print(self.health)
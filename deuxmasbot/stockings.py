import random

class Gift:
    def generate_gift():
        return Gift(is_good=True, name="Awesome Gift", sprite='images/test-sprite.png', points=50)

    def __init__(self, is_good, name, sprite, points=0):
        self.is_good = is_good
        self.name = name
        self.points = points
        self.sprite = sprite

            

class Stocking:
    def __init__(self):
        self.gift = Gift.generate_gift()

class StockingCollection:
    pass

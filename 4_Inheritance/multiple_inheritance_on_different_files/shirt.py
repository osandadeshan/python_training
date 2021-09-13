from item import Item
from garment import Garment

# Child class
class Shirt(Item, Garment):
    def __init__(self, id, section, type, name, colour):
        Item.__init__(self, id)
        Garment.__init__(self, section, type)
        self.name = name
        self.colour = colour

    def print_shirt(self):
        print("{} {} on sale".format(self.colour, self.name))
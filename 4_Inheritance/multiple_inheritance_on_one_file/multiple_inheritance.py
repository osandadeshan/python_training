# Parent class1
class Item:
    def __init__(self, id):
        self.id = id

    def print_id(self):
        print("The item id is: {}".format(self.id))


# Parent class2
class Garment:
    def __init__(self, section, type):
        self.section = section
        self.type = type

    def print_garment(self):
        print("The garment is in section {} and type of {}".format(self.section, self.type))


# Child class
class Shirt(Item, Garment):
    def __init__(self, id, section, type, name, colour):
        Item.__init__(self, id)
        Garment.__init__(self, section, type)
        self.name = name
        self.colour = colour

    def print_shirt(self):
        print("{} {} on sale".format(self.colour, self.name))


shirt1 = Shirt("200222", "Tops", "Mens", "TShirt", "Red")
shirt1.print_shirt()
shirt1.print_garment()
shirt1.print_id()
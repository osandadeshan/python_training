# Parent class2
class Garment:
    def __init__(self, section, type):
        self.section = section
        self.type = type

    def print_garment(self):
        print("The garment is in section {} and type of {}".format(self.section, self.type))
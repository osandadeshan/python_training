# Parent class1
class Item:
    def __init__(self, id):
        self.id = id

    def print_id(self):
        print("The item id is: {}".format(self.id))
class Shape:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print("Shape is a {}".format(self.name))

# circle = Shape("Circle")
# circle.get_name()

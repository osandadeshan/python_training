class Shape:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print("Shape is a {}".format(self.name))


class Circle(Shape):
    pass


circle1 = Circle("Circle")
circle1.get_name()    
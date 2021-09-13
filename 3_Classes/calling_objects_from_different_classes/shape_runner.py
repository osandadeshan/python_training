from shape import Shape


class ShapeRunner:

    def run():
        circle = Shape("Circle")
        circle.get_name()

        rectangle = Shape("Rectangle")
        rectangle.get_name()


shape_runner = ShapeRunner
shape_runner.run()


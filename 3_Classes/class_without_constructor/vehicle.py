class Vehicle:                                      # constructor overloading

    def __init__(self):                             # constructor without any arguments
        print("I am the constructor")               # Note: self is not an argument


    def __init__(self, type):                       # constructor with one argument
        self.type = type


    def model(name):
        print("Vehicle model is: {}".format(name))


    def sound(self):
        print("Burmmmmmmmm {}".format(self.type))

car = Vehicle                                       # we dont pass any values here because the constructor 'init'
car.model("Toyota")                                 # does not accept any arguments

bike = Vehicle
bike.model("Bajaj")

vehicle1 = Vehicle("Light")
vehicle1.sound()

class Person:
    a = 100

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def hello(self):
        print("My name is {} {}".format(self.first_name, self.last_name))


person1 = Person("Harshan", "W")
person1.hello()

person2 = Person("Osanda", "N")
person2.hello()

variable1 = Person("", "").a
print(variable1)

variable1 = person1.a
print(variable1)
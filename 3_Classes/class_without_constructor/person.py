class Person:
    a = 100

    def __init__(self, first_name, last_name):                      # self is not a keyword
        self.first_name = first_name                                # self is an instance of the class
        self.last_name = last_name                                  # using self we can call class members. Eg self.first_name

    def hello(self):
        print("My name is {} {}".format(self.first_name, self.last_name))


person1 = Person("Harshan", "W")                    # we pass the values here because the constructor 'init' accepts 2 arguments
person1.hello()                                     # which are first_name & last_name

person2 = Person("Osanda", "N")
person2.hello()

variable1 = Person("", "").a
print(variable1)

variable1 = person1.a
print(variable1)
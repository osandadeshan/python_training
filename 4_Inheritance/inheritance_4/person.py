class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def print_full_name(self):
        print("Full name is {} {}".format(self.first_name, self.last_name))
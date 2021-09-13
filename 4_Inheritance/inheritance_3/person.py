class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def print_full_name(self):
        print("Full name is {} {}".format(self.first_name, self.last_name))


class Student(Person):
    def __init__(self, first_name, last_name, graduation_year):
        super().__init__(first_name, last_name)                 # we're sending the student's firstname & last name to the Person Class
        self.graduation_year = graduation_year


    def welcome(self):
        print("Welcome {} {} to the class of {}".format(self.first_name, self.last_name, self.graduation_year))


student1 = Student("Tom", "Cruise", 2020)
student1.welcome()
student1.print_full_name()
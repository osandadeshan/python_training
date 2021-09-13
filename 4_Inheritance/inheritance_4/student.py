from person import Person

class Student(Person):
    def __init__(self, first_name, last_name, graduation_year):
        super().__init__(first_name, last_name)                 # we're sending the student's firstname & last name to the Person Class
        self.graduation_year = graduation_year


    def welcome(self):
        print("Welcome {} {} to the class of {}".format(self.first_name, self.last_name, self.graduation_year))
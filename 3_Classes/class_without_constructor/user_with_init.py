class UserWithInit:
    def __init__(self, email):
        self.email = email


    def say_first_name(self, first_name):
        print("{} My first name is: {}".format(self.email, first_name))


    def say_last_name(self, last_name):
        print("{} My last name is: {}".format(self.email, last_name))


user1 = UserWithInit("testuser@gmail.com")
user1.say_first_name("HappyPuppy")
user1.say_last_name("UglyPuppy")

        
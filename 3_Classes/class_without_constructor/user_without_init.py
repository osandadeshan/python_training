class UserWithoutInit:

    def say_first_name(email, first_name):
        print("{} My first name is: {}".format(email, first_name))


    def say_last_name(email, last_name):
        print("{} My last name is: {}".format(email, last_name))


person1 = UserWithoutInit
person1.say_first_name("test@gmail.com", "HappyPuppy")
person1.say_last_name("test@gmail.com", "NicePuppy")

        
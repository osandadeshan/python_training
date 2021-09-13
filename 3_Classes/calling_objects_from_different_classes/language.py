class Language:
    def __init__(class_self, name):
        class_self.name = name


    def info(class_self):
        print("Language is: {}".format(class_self.name))


lan = Language("Python")
lan.info()
class ForLoop:
    fruits = ["Apple", "Orange", "Pears", "Grapes"]

    # for fruit in fruits:
    #     print("Fruit is: {}".format(fruit))


    for index,fruit in enumerate(fruits):
        print(fruit)
        print(fruit, index)

    print("Fruit in 2nd place is : {}".format(fruits[1]))

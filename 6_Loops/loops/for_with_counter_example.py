class ForWithCounter:
    mylist = ["Apple", 1, "Pears", 3.444]

    counter = 0
    for item in mylist:
        print(counter, item)
        counter += 1

    print(mylist[2])
    print(len(mylist))
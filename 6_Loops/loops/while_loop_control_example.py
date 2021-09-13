class WhileLoopControl:
    temp = 28

    while temp < 40:
        print("Temperature is: {}".format(temp))
        temp += 1

        if (temp == 32):
            print("{} is too hot".format(temp))
            break
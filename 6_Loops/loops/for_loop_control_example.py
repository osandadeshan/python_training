class ForLoopControl:
    for temp in range(28, 41):

        if (temp == 32):
            print("Temperature {} is too hot".format(temp))
            continue                                                # Exits the repetition

        print("Temperature is: {}".format(temp))


        # can use 'pass' instead of 'continue'
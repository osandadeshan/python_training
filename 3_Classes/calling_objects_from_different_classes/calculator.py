def addition():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))          # casting a string to integer
    print(a + b)


def subtraction():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a - b)


def multiplication():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a * b)


def division():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)


def calc():
    math_function = input("Enter mathematical function: ")
    if math_function == '+':
        addition()
    elif math_function == '-':
        subtraction()
    elif math_function == '*':
        multiplication()
    elif math_function == '/':
        division()
    else:
        print("Invalid math function. Please reenter")


calc()
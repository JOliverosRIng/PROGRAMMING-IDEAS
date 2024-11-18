# define the funtions needed: add, sub, mul, div
def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))
    print("------------------------------------------->")


def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))
    print("------------------------------------------->")


def mul(a, b):
    answer = a * b
    print(str(a) + " x " + str(b) + " = " + str(answer))
    print("------------------------------------------->")


def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))
    print("------------------------------------------->")

while True:
    # print the menu to the user
    print("BASIC CALCULATOR")
    print("A. Addition")
    print("B. Substraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Select the operation: ")

    if choice == "a" or choice == "A":
        print("A. ADDITION")
        a = float(input("First number: "))
        print("+")
        b = float(input("Second number: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("B. SUBSTRACTION")
        a = float(input("First number: "))
        print("-")
        b = float(input("Second number: "))
        sub(a, b)
    elif choice == "b" or choice == "B":
        print("B. SUBSTRACTION")
        a = float(input("First number: "))
        print("-")
        b = float(input("Second number: "))
        sub(a, b)
    elif choice == "C" or choice == "c":
        print("C. MULTIPLICATION")
        a = float(input("First number: "))
        print("x")
        b = float(input("Second number: "))
        mul(a, b)
    elif choice == "d" or choice == "D":
        print("D. DIVISION")
        a = float(input("First number: "))
        print("/")
        b = float(input("Second number: "))
        div(a, b)

    elif choice == "E" or choice == "e":
        print("GOOD BYE")
        quit()

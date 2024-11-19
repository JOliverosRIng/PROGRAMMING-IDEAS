# Define the functions for basic operations
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed!")
        return a  # Retorna el valor previo
    else:
        return a / b


def calculatorLogic():
    # Initialize the starting value
    a = None  # None means there is not an initial value

    # Loop to keep the calculator running
    while True:
        print("\nBASIC CALCULATOR")
        print("A. Addition")
        print("B. Subtraction")
        print("C. Multiplication")
        print("D. Division")
        print("N. New Operation")
        print("E. Exit")

        # Get the user's choice
        choice = input("Select the operation: ").lower()

        if choice in ["a", "b", "c", "d", "n"]:
        #Restart the calculator operations
            if choice == "n":
                calculatorLogic()
            # Use the previous result or ask for the first number
            if a is None:
                a = float(input("Enter the first number: "))
            # Ask for the second number
            b = float(input("Enter the next number: "))

            # Perform the chosen operation
            if choice == "a":
                print(f"{a} + {b}")
                a = add(a, b)
                print(f"Result: {a}")
            elif choice == "b":
                print(f"{a} - {b}")
                a = sub(a, b)
                print(f"Result: {a}")
            elif choice == "c":
                print(f"{a} x {b}")
                a = mul(a, b)
                print(f"Result: {a}")
            elif choice == "d":
                print(f"{a} / {b}")
                a = div(a, b)
                print(f"Result: {a:.5f}")
        elif choice == "e":
            print("Goodbye!")
            break  # Exit the loop
        else:
            print("Invalid choice! Please select a valid operation.")


# Main
calculatorLogic()

# 4-operation calculator

# Function definition
def calculator():
    print("*** 4-function calculator ***")
    print()

    # Receive data from your user
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    # Choose a mathematical operation
    process = input("Select action (+, -, *, /): ")

    # Mathematical operations section
    if process == "+":
        conclusion = number1 + number2

    elif process == "-":
        conclusion = number1 - number2

    elif process == "*":
        conclusion = number1 * number2

    elif process == "/":
        if number2 != 0:
            conclusion = number1 / number2
        else:
            print("Error: A number cannot be divided by zero (0)!")
            return
    else:
        print("You have chosen an invalid mathematical operation!")
        return

    # Print the output
    print(f"Conclusion: {conclusion}")


# Call function
calculator()

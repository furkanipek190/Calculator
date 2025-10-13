# 🧮 Simple 4-Operation Calculator

A simple **Python calculator** that performs the four basic arithmetic operations: addition, subtraction, multiplication, and division.

---

## 🎯 Purpose

This project is designed to help beginners understand the fundamentals of **algorithms**, **pseudocode**, and **Python programming**.  
It also demonstrates the workflow from **problem definition → pseudocode → Python code → testing**.

---

## 🧠 Problem Definition

The user enters two numbers and selects a mathematical operation (`+`, `-`, `*`, `/`).  
The program performs the chosen operation and prints the result.

---

## 🔣 Pseudocode

1) Start

2) Display "4-function calculator"

3) Get first number → a

4) Get second number → b

5) Ask user to choose an operation (+, -, *, /)

6) If operation = '+', then result = a + b

7) If operation = '-', then result = a - b

8) If operation = '*', then result = a * b

9) If operation = '/', then result = a / b (if b ≠ 0)

10) Display the result

11) End



## Python Code

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



## 💻 Example Output
*** 4-function calculator ***

Enter the first number: 78
Enter the second number: 18
Select action (+, -, *, /): *
Conclusion: 1404.0


## 🗂️ Project Structure
Calculator/
│
├── calculator.py
├── README.md


## ⚙️ How to Run

Run the following command in your terminal:
python calculator.py

## ✨ Developer

Furkan İPEK
📍 Türkiye
💬 Created as part of a beginner-level learning project.
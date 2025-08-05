# Simple Calculator Program

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose an operation: + for addition, - for subtraction, * for multiplication, / for division")
operation = input("Enter your operation: ")

# Perform the selected operation
if operation == "+":
    result = num1 + num2
    print("Result:", result)
elif operation == "-":
    result = num1 - num2
    print("Result:", result)
elif operation == "*":
    result = num1 * num2
    print("Result:", result)
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose +, -, *, or /.")

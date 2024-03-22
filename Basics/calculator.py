# Description: A simple calculator program that can perform addition, subtraction, multiplication, and division.
#
# Usage: python calculator.py
# Output: 
# Enter first number: 10
# Enter second number: 20
# Enter operation (+, -, *, /): +
# 10 + 20 = 30
#
# Enter first number: 10
# Enter second number: 20
# Enter operation (+, -, *, /): -
# 10 - 20 = -10
#
# Enter first number: 10
# Enter second number: 20
# Enter operation (+, -, *, /): *
# 10 * 20 = 200
#
# Enter first number: 10
# Enter second number: 20
# Enter operation (+, -, *, /): /

# 10 / 20 = 0.5

# Program to create a simple calculator
# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")
    
    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
            
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            
        # Check if the user wants another calculation
        # Break the while loop if answer is no
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    else:
        print("Invalid Input")
        




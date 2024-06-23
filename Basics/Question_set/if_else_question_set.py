#   1. Write a Python script that takes a user's input of a number and prints "Positive" if it's greater than zero, 
# "Negative" if it's less than zero, and "Zero" if it's equal to zero.

n = int(input("Enter a no.  "))
if n == 0:
    print("Zero")
elif n > 0:
    print("Positive")
else:
    print("Negative")

#   2. Create a Python function that takes two numbers as input and returns the larger number using if-else statements.

a = int(input())
b = int(input())

if a > b:
    print(a)
else:
    print(b)

#   3. Write a Python script that takes a user's input of an age and prints "Child" if the age is less than 18, and "Adult" if it's 18 or older.

age = int(input("Enter your age: "))

if age < 18:
    print("Child")
else:
    print("Adult")
    
#   4. Create a Python function that takes a year as input and prints "Leap year" if it's divisible by 4, otherwise prints "Not a leap year" using if-else statements.

year = int(input("Enter a year: "))
if year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
    
#   5. Write a Python script that takes a user's input of a temperature in 
# Celsius and prints "Freezing" if it's below 0°C, "Normal" if it's between 0°C and 25°C, and "Hot" if it's above 25°C.

temp = float(input("Enter the temperature in Celsius: "))

if temp < 0:
    print("Freezing")
elif temp >= 0 and temp <= 25:
    print("Normal")
else:
    print("Hot")

#   6. Create a Python function that takes three numbers as input and returns the smallest number using if-else statements.

a = int(input("Enter the number "))
b = int(input("Enter the number "))
c = int(input("Enter the number "))

if a < b and a < c:
    print(a)
elif b < c:
    print(b)
else:
    print(c)

#   7. Write a Python script that takes a user's input of a string and prints "Long" if the
# length of the string is greater than 10 characters, otherwise prints "Short".

input_1 = input("Enter your string ")

if len(input_1) > 10:
    print("Long")
else:
    print("Short")

#   8. Create a Python function that takes a grade (A, B, C, D, F) as input and prints "Pass" 
# if the grade is A, B, or C, otherwise prints "Fail".

grade = input("Enter your grade ")

if grade == "A" or "B" or  "C" or "D" or "a" or "b" or "c" or "d":
    print("Pass")
elif grade == "F" or "f":
    print("Fail")
else:
    print("Invalid grade")
    
#   9. Write a Python script that takes a user's input of two numbers and prints "Even" if both numbers are even,
# "Odd" if both numbers are odd, and "Mixed" otherwise.

num1 = int(input("Enter a number "))
num2 = int(input("Enter a number "))
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Even")
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Odd")
else:
    print("Mixed")

'''
Suppose that you are an invigilator in an exam.
A calculator is not allowed for the exam. You discover somehow that students are planning to cheat in exams,
using a calculator program in Python language. Somehow, you get your hands on the calculator program.
Now you want to alter a few results in the calculator with your own provided results to catch the 
students trying to cheat using the calculator program.

The user will provide the following inputs:

    Operator
    The two numbers between which the operator is applied

All the results will be correct, except for these few:

    45 * 3 = 555
    56+9 = 77
    56/6 = 4

'''
print("=================================================================================")
print("============\t Welcome to the Calculator world \t============")
print("=================================================================================")

print()

print('Enter the operator you want to perform: ')
print(""" + for addition, 
        - for subtraction 
      * for multiplication 
    / for division """)

op = input()

num1 = int(input("Enter your first no. "))
num2 = int(input("Enter your second no. "))

if op == "+":
    if num1 == 56 and num2 == 9:
        print("77")
    else:
        print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    if num1 == 45 and num2 == 3:
        print("555")
    else:
        print(num1 * num2)
elif op == "/":
    if num1 == 56 and num2 == 6:
        print("4")
    else:
        print(num1 / num2)
else:
    print("enter valid inputs")



'''
You have to follow certain instructions, which are as follows:

    You have to take an integer type variable, and the input of the variable will define the length of the triangle.
    You have to declare another Boolean variable.
    When the value of Boolean is 1 i.e. True, the pattern will be printed as shown above.
    But if the value of Boolean is 0 or false, then the triangle will be printed upside down.
'''

# Get user input for the number
num = int(input("Enter your number: "))

# Get user input for the boolean value and convert it to a boolean
boolean_input = input("Enter your type (True or False): ").strip().lower()
is_increasing = boolean_input == 'true'

# Print the pattern based on the boolean value
if is_increasing:
    for i in range(num):
        print("*" * (i + 1))
else:
    for i in range(num):
        print("*" * (num - i))

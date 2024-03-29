# This script is all about the functions of python 

# Functions are the reusable piece of code which helps in modularizing the code.
# Functions are defined using def keyword in python.
# Syntax of function definition:
# def function_name(parameters):
#     """docstring"""
#     statement(s)
#

# Example of function definition
def greet(name):
    """This function greets to the person passed in as parameter"""
    print("Hello, " + name + ". Good morning!")

# Function call
greet('Paul')

# Output: Hello, Paul. Good morning!

# In the above example, greet() is a function which takes a parameter name.

# We can pass the parameter to the function using the function call greet('Paul').
# Here, 'Paul' is the argument passed to the function.

# Functions can return a value to the caller using the return statement.
# A return statement with no arguments is the same as return None.

def sum(a,b):
    return a+b

#function call 
print(sum(1,3))


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



# Output: 4

# The return statement returns with a value from a function. return statement can not be used outside the function.

# If a function doesn't have a return statement, it returns None.

# Example of return statement
def absolute_value(num):
    """This function returns the absolute value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num
    
# Output: 2
print(absolute_value(2))

# Output: 4
print(absolute_value(-4))

# Output: 0
print(absolute_value(0))

# In the above example, absolute_value() function returns the absolute value of the entered number.

# All functions in Python have a return value, either explicit or implicit. If no return statement appears in a function, Python returns None.

# Scope and Lifetime of variables
# Scope of a variable is the portion of a program where the variable is recognized.
# Parameters and variables defined inside a function are not visible from outside the function. Hence, they have a local scope.

# Lifetime of a variable is the period throughout which the variable exits in the memory.
# The lifetime of variables inside a function is as long as the function executes.

# They are destroyed once we return from the function. Hence, a function does not remember the value of a variable from its previous calls.

# Here is an example to illustrate the scope of a variable inside a function.

def my_func():
    x = 10
    print("Value inside function:",x)
    
x = 20
my_func()
print("Value outside function:",x)

# Output: Value inside function: 10
# Output: Value outside function: 20

# In this program, we can see that the value of x is 20 initially. Even though the function my_func() changed the value of x to 10, it did not affect the value outside the function.

    
    
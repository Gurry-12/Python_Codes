#======================================

# Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. Decorators allow us to wrap another
# function in order to extend the behavior of the wrapped function, without permanently modifying it.


# example 
# Decorators can be thought of as functions which 
# modify the functionality of another function. They help to make our code shorter and more "Pythonic".

# To understand decorators, we must first know:
# 1. Functions are objects in Python.
# 2. Functions can be passed as arguments to other functions.
# 3. Functions can return another function.

# Decorators can be nested, i.e., a function can be decorated multiple times with different (or same) decorators.

# A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.

# Decorators can be used to check for permissions, modify or track the arguments passed to a function, logging the calls to a specific function, etc.


# example 1
def decorator_function(original_function):
    def wrapper_function():
        print(f'Wrapper executed this before {original_function.__name__}')
        return original_function()
    return wrapper_function

def display():
    print('display function ran')

decorated_display = decorator_function(display)
decorated_display()

# example 2

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'Wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)
    return wrapper_function

def display():
    print('display function ran')

@decorator_function
def display_info(name, age):
    print(f'display_info ran with arguments {name} and {age}')

display_info('John', 25)

# example 3

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")
    
say_whee = my_decorator(say_whee)
say_whee()

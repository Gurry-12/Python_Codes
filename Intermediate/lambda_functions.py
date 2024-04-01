# Lambda functions in Python are small, anonymous functions that are defined using the lambda keyword. They can take any number of arguments, but can only have one expression. The syntax for a lambda function is lambda arguments: expression.

# Here's an example of a lambda function that adds two numbers:


add = lambda x, y: x + y
add(2, 3) 

# returns 5
# Lambda functions are especially useful when used with built-in functions like filter(), map(), and reduce(). Here's an example of using a lambda function with filter() to filter out the odd numbers from a list:


numbers = [1, 2, 3, 4, 5]
filtered = filter(lambda x: x % 2 == 0, numbers)
list(filtered)  

# returns [2, 4]
# In the example above, the filter() function takes a lambda function as its first argument and a list of numbers as its second argument. The lambda function takes each number in the list and returns True if the number is even (i.e., if the number modulo 2 is 0) and False otherwise. The filter() function then uses this lambda function to filter out the odd numbers from the list, resulting in a new list that contains only the even numbers.

# In the example you provided, the addition and square functions can be defined as lambda functions like this:

addition = lambda x, y: x + y
square = lambda x: x ** 2

# These lambda functions can then be used just like regular functions. For example:

addition(2, 3)  # returns 5
square(2)  # returns 4

# Lambda functions can also be used to create nested functions, which can be useful in some cases. Here's an example of a lambda function that creates a nested function that increments a number by a specified amount:



make_incrementor = lambda n: lambda x: x + n

increment_by_2 = make_incrementor(2)
increment_by_2(42)  # returns 44

increment_by_6 = make_incrementor(6)
increment_by_6(42) 

# returns 48

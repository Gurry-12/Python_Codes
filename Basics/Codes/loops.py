
# Loops are used to iterate over a sequence (list, tuple, string) or other iterable objects.
# There are two types of loops in Python, for and while.

# For Loop
# The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects.
# Iterating over a sequence is called traversal.

# Syntax:
# for val in sequence:
#     Body of for

# Here, val is the variable that takes the value of the item inside the sequence on each iteration.

# Example:
# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
    sum = sum + val

print("The sum is", sum)

# Output: The sum is 48

# The range() function

# We can generate a sequence of numbers using range() function. range(10) will generate numbers from 0 to 9 (10 numbers).

# We can also define the start, stop and step size as range(start, stop, step size). step size defaults to 1 if not provided.

# This function does not store all the values in memory, it would be inefficient. So it remembers the start, stop, step size and generates the next number on the go.

# To force this function to output all the items, we can use the function list().

# The following example will clarify this.

# Example:
# Program to iterate through a list using indexing

genre = ['pop', 'rock', 'jazz']

# iterate over the list using index
for i in range(len(genre)):
    print("I like", genre[i])

# Output:
# I like pop
# I like rock
# I like jazz

# While Loop
# The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.

# We generally use this loop when we don't know the number of times to iterate beforehand.

# Syntax:
# while test_expression:
#     Body of while

# In while loop, test expression is checked first. The body of the loop is entered only if the test_expression evaluates to True. After one iteration, the test expression is checked again. This process continues until the test_expression evaluates to False.

# In Python, the body of the while loop is determined through indentation.

# The body starts with indentation and the first unindent line marks the end.

# Python interprets any non-zero value as True. None and 0 are interpreted as False.

# Example:
# Program to add natural numbers up to n

# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))
n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1    # update counter

# print the sum
print("The sum is", sum)

# Output: The sum is 55

# While loop with else
# Same as that of for loop, we can have an optional else block with while loop as well.

# The else part is executed if the condition in the while loop evaluates to False.

# The while loop can be terminated with a break statement.

# In such cases, the else part is ignored.

# Hence, a while loop's else part runs if no break occurs and the condition is false.

# Example:

# Example to illustrate

# while loop with else
counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")
    
# Output:
# Inside loop
# Inside loop
# Inside loop
# Inside else

# Single statement while block

# Similar to if block, if the while block consists of a single statement, we can declare the entire block in a single line.

# Example:
# Program to print the numbers from 1 to 5

# counter = 1
# while counter <= 5: print(counter); counter += 1

# Output:
# 1
# 2
# 3
# 4
# 5



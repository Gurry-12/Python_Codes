# This script is all about break and continue statement of control statement in python.

# Break statement is used to break the loop and come out of the loop.
# Continue statement is used to skip the current iteration and move to the next iteration.

# Example of break statement
for i in range(1, 11):
    if i == 5:
        break
    print(i)
    
# Output: 1 2 3 4

# Example of continue statement
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
    
# Output: 1 2 3 4 6 7 8 9 10

# In the above example, when i = 5, break statement is executed and loop is terminated.

# In the second example, when i = 5, continue statement is executed and loop is continued to next iteration.

# That's all about break and continue statement in python.

# Happy Learning!

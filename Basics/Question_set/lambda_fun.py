"""
this is the python file in which i will solve the problem related to the lambda function and its other uses """

# write a python function in which sort a list and print it 

# list_1 = [2, 6,4 ,3 ,6,543,56,2,5,5]

# list_1.sort(key = None)
# print(list_1)



# 2. Use a lambda function to filter out all even numbers from a given list.

list_1 = [ x  for x in range(1,int(input("Enter your count how many values you wanna add in list: "))+1)]

print(list_1)


print(list(filter(lambda i :  i%2 == 0,list_1)))


# 3. Write a lambda function to compute the square of a given number.

# 4. Create a lambda function that takes two arguments and returns their product.
# 5. Write a lambda function to find the maximum of two numbers.
# 6. Implement a lambda function to reverse a string.
# 7. Use a lambda function to calculate the factorial of a number.
# 8. Write a lambda function to merge two dictionaries.
# 9. Create a lambda function to check if a given string is a palindrome.
# 10. Write a lambda function to convert a list of integers into a list of their squares.
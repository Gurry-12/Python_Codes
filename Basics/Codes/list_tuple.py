# this is about list and tuple

# List and Tuple are two of the most commonly used data structures in Python. They are used to store collections of items, and can be used to store different types of data, such as integers, strings, and even other lists or tuples.

# List:
# A list is a mutable, ordered collection of items. This means that you can change the items in a list after it has been created, and that the items in a list are stored in a specific order. Lists are created using square brackets [] and can contain any number of items, separated by commas. For example:

# numbers = [1, 2, 3, 4, 5]
# names = ['Alice', 'Bob', 'Charlie']
# mixed = [1, 'Alice', 3.14, True]

# You can access individual items in a list using their index, which is an integer that represents the position of the item in the list. Indexing in Python is zero-based, which means that the first item in a list has an index of 0, the second item has an index of 1, and so on. For example:

# numbers = [1, 2, 3, 4, 5]
# print(numbers[0])  # prints 1
# print(numbers[1])  # prints 2
# print(numbers[2])  # prints 3

# You can also change the value of an item in a list by assigning a new value to its index. For example:

# numbers = [1, 2, 3, 4, 5]
# numbers[0] = 42

# print(numbers)  # prints [42, 2, 3, 4, 5]

# You can add new items to a list using the append() method, which adds the item to the end of the list. For example:

# numbers = [1, 2, 3, 4, 5]

# numbers.append(6)
# print(numbers)  # prints [1, 2, 3, 4, 5, 6]

# You can also remove items from a list using the remove() method, which removes the first occurrence of the specified item from the list. For example:

# numbers = [1, 2, 3, 4, 5]

# numbers.remove(3)
# print(numbers)  # prints [1, 2, 4, 5]

# Tuple:
# A tuple is an immutable, ordered collection of items. This means that you cannot change the items in a tuple after it has been created, and that the items in a tuple are stored in a specific order. Tuples are created using parentheses () and can contain any number of items, separated by commas. For example:

# numbers = (1, 2, 3, 4, 5)
# names = ('Alice', 'Bob', 'Charlie')
# mixed = (1, 'Alice', 3.14, True)

# You can access individual items in a tuple using their index, just like with lists. For example:

# numbers = (1, 2, 3, 4, 5)
# print(numbers[0])  # prints 1
# print(numbers[1])  # prints 2

# However, because tuples are immutable, you cannot change the value of an item in a tuple after it has been created. For example, the following code will raise an error:

# numbers = (1, 2, 3, 4, 5)
# numbers[0] = 42  # raises an error

# You can add new items to a tuple by creating a new tuple that contains the new items along with the existing items. For example:

# numbers = (1, 2, 3, 4, 5)
# numbers = numbers + (6,)
# print(numbers)  # prints (1, 2, 3, 4, 5, 6)

# You can also remove items from a tuple by creating a new tuple that contains only the items you want to keep. For example:

# numbers = (1, 2, 3, 4, 5)
# numbers = numbers[:2] + numbers[3:]
# print(numbers)  # prints (1, 2, 4, 5)

# In general, lists are more commonly used than tuples in Python, because lists are more flexible and can be modified after they are created. However, tuples are useful when you want to create a collection of items that should not be changed, or when you want to use a collection of items as a key in a dictionary.

# In summary, lists and tuples are two of the most commonly used data structures in Python. Lists are mutable, ordered collections of items, while tuples are immutable, ordered collections of items. Lists are more commonly used than tuples, but tuples are useful when you want to create a collection of items that should not be changed.

# Write a program to store seven fruits in a list entered by user.

# li = []

# for i in range(7):
#     fruit = input(f"Enter your {i+1} Fruit Name : ")
#     li.append(fruit)
    
# print("List  of fruits is : ",li)


# Write a program to accept marks of 6 students and display them in a sorted manner.
li_1 = []
li_2 = ["Hindi", "English", "Maths"]

for i in range(2):
    marks = []
    for j in range(3):
        mark = int(input(f"Enter your {li_2[j]} Marks : "))
        marks.append(mark)
    li_1.append(marks)

print(li_2)
for i in li_1:
    print(i)
    

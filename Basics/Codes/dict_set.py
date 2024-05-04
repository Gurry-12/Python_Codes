# This file is about dictionary and sets

# Dictionary:

# A dictionary is an unordered, mutable collection of key-value pairs. This means that you can use a dictionary to store a collection of items, where each item is associated with a unique key. Dictionaries are created using curly braces {} and can contain any number of key-value pairs, separated by commas. For example:

# Create a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Access a value using a key
print(my_dict['name'])  # Output: John

# Add a new key-value pair
my_dict['email'] = '' # Add a new key-value pair
print(my_dict)  # Output: {'name': 'John', 'age': 25, 'city': 'New York', 'email': ''}
# You can also use the get() method to access a value using a key. If the key does not exist, the get() method will return None instead of raising an error. For example:

# Access a value using a key
print(my_dict.get('name'))  # Output: John

# Access a value using a key that does not exist
print(my_dict.get('country'))  # Output: None
# You can also use the get() method to provide a default value if the key does not exist. For example:

# Access a value using a key that does not exist
print(my_dict.get('country', 'USA'))  # Output: USA
# You can use the keys() method to get a list of all the keys in a dictionary. For example:

# Get a list of all the keys
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city', 'email'])
# You can use the values() method to get a list of all the values in a dictionary. For example:

# Get a list of all the values
print(my_dict.values())  # Output: dict_values(['John', 25, 'New York', ''])
# You can use the items() method to get a list of all the key-value pairs in a dictionary. For example:

# Get a list of all the key-value pairs
print(my_dict.items())  # Output: dict_items([('name', 'John'), ('age', 25), ('city', 'New York'), ('email', '')])
# You can use the pop() method to remove a key-value pair from a dictionary. For example:

# Remove a key-value pair
my_dict.pop('email')
print(my_dict)  # Output: {'name': 'John', 'age': 25, 'city': 'New York'}
# You can use the popitem() method to remove the last key-value pair from a dictionary. For example:

# Remove the last key-value pair
my_dict.popitem()
print(my_dict)  # Output: {'name': 'John', 'age': 25}
# You can use the clear() method to remove all the key-value pairs from a dictionary. For example:

# Remove all key-value pairs
my_dict.clear()
print(my_dict)  # Output: {}
# You can use the del keyword to delete a dictionary. For example:

# Delete a dictionary
del my_dict
# You can use the update() method to update a dictionary with the key-value pairs from another dictionary. For example:

# Create two dictionaries
dict1 = {'name': 'John', 'age': 25}
dict2 = {'city': 'New York', 'email': ''}

# Update dict1 with the key-value pairs from dict2

dict1.update(dict2)
print(dict1)  # Output: {'name': 'John', 'age': 25, 'city': 'New York', 'email': ''}
# You can use the copy() method to create a shallow copy of a dictionary. For example:

# Create a shallow copy of a dictionary
dict_copy = dict1.copy()
print(dict_copy)  # Output: {'name': 'John', 'age': 25, 'city': 'New York', 'email': ''}
# You can use the fromkeys() method to create a new dictionary with the specified keys and values. For example:

# Create a new dictionary with the specified keys and values
my_dict = dict.fromkeys(['name', 'age', 'city'], '')
print(my_dict)  # Output: {'name': '', 'age': '', 'city': ''}
# You can use the setdefault() method to get the value of a key in a dictionary. If the key does not exist, the setdefault() method will create a new key with the specified value. For example:

# Get the value of a key
print(my_dict.setdefault('name'))  # Output: ''
# Get the value of a key that does not exist
print(my_dict.setdefault('country'))  # Output: None
# Create a new key with the specified value
print(my_dict)  # Output: {'name': '', 'age': '', 'city': '', 'country': None}
# You can use the setdefault() method to provide a default value if the key does not exist. For example:

# Get the value of a key that does not exist
print(my_dict.setdefault('country', 'USA'))  # Output: USA
# Create a new key with the specified value

# Sets:

# A set is an unordered, mutable collection of unique elements. This means that you can use a set to store a collection of items, where each item is unique. Sets are created using curly braces {} and can contain any number of elements, separated by commas. For example:

# Create a set
my_set = {1, 2, 3, 4, 5}

# Add an element to a set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
# You can use the remove() method to remove an element from a set. For example:

# Remove an element from a set
my_set.remove(6)
print(my_set)  # Output: {1, 2, 3, 4, 5}
# You can use the discard() method to remove an element from a set. If the element does not exist, the discard() method will not raise an error. For example:

# Remove an element from a set
my_set.discard(6)
print(my_set)  # Output: {1, 2, 3, 4, 5}
# You can use the pop() method to remove and return an arbitrary element from a set. For example:

# Remove and return an arbitrary element from a set
element = my_set.pop()
print(element)  # Output: 1
print(my_set)  # Output: {2, 3, 4, 5}
# You can use the clear() method to remove all the elements from a set. For example:

# Remove all elements from a set
my_set.clear()
print(my_set)  # Output: set()
# You can use the del keyword to delete a set. For example:

# Delete a set
del my_set
# You can use the union() method to create a new set that contains all the elements from two sets. For example:

# Create two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Create a new set that contains all the elements from set1 and set2
new_set = set1.union(set2)
print(new_set)  # Output: {1, 2, 3, 4, 5}
# You can use the intersection() method to create a new set that contains only the elements that are common to two sets. For example:

# Create a new set that contains only the elements that are common to set1 and set2
new_set = set1.intersection(set2)
print(new_set)  # Output: {3}
# You can use the difference() method to create a new set that contains only the elements that are unique to one set. For example:

# Create a new set that contains only the elements that are unique to set1
new_set = set1.difference(set2)
print(new_set)  # Output: {1, 2}
# You can use the symmetric_difference() method to create a new set that contains only the elements that are unique to one set or the other, but not both. For example:

# Create a new set that contains only the elements that are unique to set1 or set2, but not both
new_set = set1.symmetric_difference(set2)
print(new_set)  # Output: {1, 2, 4, 5}
# You can use the isdisjoint() method to check if two sets have no elements in common. For example:

# Check if set1 and set2 have no elements in common
result = set1.isdisjoint(set2)
print(result)  # Output: False
# You can use the issubset() method to check if one set is a subset of another set. For example:

# Check if set1 is a subset of set2
result = set1.issubset(set2)
print(result)  # Output: False
# You can use the issuperset() method to check if one set is a superset of another set. For example:


# Check if set1 is a superset of set2
result = set1.issuperset(set2)
print(result)  # Output: False
# You can use the copy() method to create a shallow copy of a set. For example:

# Create a shallow copy of a set
set_copy = set1.copy()
print(set_copy)  # Output: {1, 2, 3}
# You can use the fromkeys() method to create a new set with the specified elements. For example:

# Create a new set with the specified elements
my_set = set.fromkeys([1, 2, 3, 4, 5])
print(my_set)  # Output: {1, 2, 3, 4, 5}
# You can use the intersection_update() method to update a set with the elements that are common to two sets. For example:

# Update set1 with the elements that are common to set1 and set2
set1.intersection_update(set2)
print(set1)  # Output: {3}






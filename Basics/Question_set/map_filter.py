#=====================================================

# map() function

# map() function returns a map object(which is an iterator) 
# of the results after applying the given function to each item of a given iterable (list, tuple etc.)

# 1. write a program to print the all values multiply with 2 of given list 

list_1 = [  x for x in range(1,10) ]

#print(list_1)

list_2 = list(map(lambda x : x * 2 , list_1))

print(list_2)


# 2. write a program to print the all values of given list in upper case

list_3 = ['apple', 'banana', 'cherry', 'date']

list_4 = list(map(lambda x : x.upper() , list_3))

print(list_4)

# 3. write a program to print the all values of given list in lower case

list_5 = ['APPLE', 'BANANA', 'CHERRY', 'DATE']

list_6 = list(map(lambda x : x.lower() , list_5))

print(list_6)

# 4. write a program to print the all values of given list in title case

list_7 = ['APPLE', 'BANANA', 'CHERRY', 'DATE']
list_8 = list(map(lambda x : x.title() , list_7))
print(list_8)


#=======================================================

# filter() function

# filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.

# 1. write a program to print the all values of given list which are greater than 5

list_9 = [  x for x in range(1,10) ]

l1 = list(filter(lambda x : x > 5 , list_9))

print(l1)

# 2. write a program to print the all values of given list which are less than 5

list_10 = [  x for x in range(1,10) ]

l2 = list(filter(lambda x : x < 5 , list_10))

print(l2)

# 3. write a program to print the all values of given list which are even
list_11 = [  x for x in range(1,10) ]

l3 = list(filter(lambda x : x % 2 is 0 , list_11))

print(l3)


#=======================================

# reduce() function

# reduce() function is defined in functools module. It does not return a new list as map() and filter() does.
# It returns a single value.

# 1. write a program to print the sum of all values of given list

from functools import reduce
list_12 = [  x for x in range(1,10) ]

l1 = int(reduce(lambda x,y : x+y , list_9))

print(l1)

# 2. write a program to print the product of all values of given list   
from functools import reduce
list_12 = [  x for x in range(1,10) ]

l1 = int(reduce(lambda x,y : x*y , list_9))

print(l1)
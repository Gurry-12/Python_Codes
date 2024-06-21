'''
l = [9 , 7 ,5 , 4 ,7 ,2,6 ,3, 1 ]
print(l)
l.sort()
print(l)

l1 = ['d','c', 'a']

print(l1)
l1.sort()
print(l1)

#  1. Write a Python program that creates a list of numbers and prints the sum of all the elements.
l1 = []

for i in range(int(input())):
    l1.append(int(input()))
print(sum(l1))

#  2. Create a Python program that takes a list of numbers as input and prints the largest and smallest elements.

l2 = []

for i in range(int(input())):
    l2.append(int(input()))

print(max(l2))
print(min(l2))

'''
#  3. Write a Python program that takes a list of strings as input and prints the longest and shortest strings.
'''
l3 = []

n = int(input("How many string you wanna enter? "))

for i in range(n):
    l3.append(input())
    
print(max(l3, key = len))
print(min(l3, key = len))

'''
#  4. Create a Python program that reverses a given list.
'''
l4 = []

n = int(input("How many elements you wanna input in the list? "))

for i in range(n):
    a = input()
    if a.isnumeric():
        l4.append(int(a))
    else:
        l4.append(a)

print(l4)
l4.reverse()
print(l4)
'''
#  5. Write a Python program that removes duplicates from a list.
'''
l5 = []

n = int(input("How many elements you wanna input in the list? "))
for i in range(n):
    a = input()
    if a.isnumeric():
        l5.append(int(a))
    else:
        l5.append(a)
        
print(l5)
l5 = list(set(l5))
print(l5)
'''
#  6. Create a Python program that finds the common elements between two lists.
'''
l6_1 = []
l6_2 = []

n = int(input("How many elements you wanna input in the list 1 ? "))

for i in range(n):
    a = input()
    if a.isnumeric():
        l6_1.append(int(a))
    else:
        l6_1.append(a)
        
n1 = int(input("How many elements you wanna input in the list 2 ? "))
for i in range(n1):
    a = input()
    if a.isnumeric():
        l6_2.append(int(a))
    else:
        l6_2.append(a)
        
print(l6_1)
print(l6_2)
print(set(l6_1) & set(l6_2))
print(set(l6_1) | set(l6_2))

'''
#  7. Write a Python program that finds the frequency of each element in a list.
'''
l7 = []

n = int(input("How many elements you wanna input in the list? "))

for i in range(n):
    a = input()
    if a.isnumeric():
        l7.append(int(a))
    else:
        l7.append(a)
        
print(l7)
for i in set(l7):
    print(i, l7.count(i))
    
'''
#  8. Create a Python program that sorts a list of numbers in ascending and descending order.
'''
l8 = []

n = int(input("How many elements you wanna input in the list? "))

for i in range(n):
    a = input()
    if a.isnumeric():
        l8.append(int(a))
    else:
        l8.append(a)
        
print(l8)
l8.sort()
print(l8)
l8.reverse()
print(l8)

'''
#  9. Write a Python program that finds the second largest element in a list.

l9 = []

n = int(input("How many elements you wanna input in the list? "))

for i in range(n):
    a = input()
    if a.isnumeric():
        l9.append(int(a))
    else:
        l9.append(a)

print(l9)
l9 = list(set(l9))
l9.sort()
print(l9[-2])
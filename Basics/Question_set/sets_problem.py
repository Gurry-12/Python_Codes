
# 1. write a program to perform set 

# 1. Write a Python program to create a set.
'''
s = {1,3,4,6}
print(s)

s1 = set()

for i in range(int(input())):
    s1.add(i)
print(s1)

'''

# 2. Write a Python program to iterate over sets.
'''
s1 = set()
for i in range(int(input())):
    s1.add(int(input()))
print(s1)

'''

# 3. Write a Python program to perform intersection and union 

s1 = set()
s2 = set()

n = int(input())

for i in range(n):
    s1.add(int(input()))

for i in range(n):
    s2.add(int(input()))
    
print(s1.intersection(s2))
print(s1.union(s2))


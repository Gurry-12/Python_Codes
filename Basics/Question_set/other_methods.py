#=======================================================================

# 1. Write a Python program to get the Python version you are using.

import sys
print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)

# 2. Write a Python program to display the current date and time.

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

# 3. Write a Python program to display the current date and time.

import time
print()
print(time.ctime())
print()

# 4. Write a Python program to get the current time in Python.

import datetime
print()
print(datetime.datetime.now().time())
print()

# 5. Write a Python program to calculate number of days between two dates.

from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)

# 6. Write a Python program to get the volume of a sphere with radius 6.

import math
r = 6

V = 4.0/3.0*math.pi* r**3
print('The volume of the sphere is: ',V)

# 7. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

def difference(n):

    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2

print(difference(22))
print(difference(14))

# 8. Write a Python program to test whether a number is within 100 of 1000 or 2000.

def near_thousand(n):

    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(2200))

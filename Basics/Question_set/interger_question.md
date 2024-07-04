# Data Type Question Set 


###### 1. Write a Python program that takes two numbers as input and prints their sum, difference, product, and quotient.

```python
num1 = int ( input ( " Enter your First Number : " ) )
num2 = int ( input ( " Enter your Second Number : " ) )

sum = num1 + num2 

difference  = num1 - num2 

product = num1 * num2

quotient = num1 / num2

print ( " The Sum of the two numbers is : " , sum )
print ( " The Difference of the two numbers is : " , difference )
print ( " The Product of the two numbers is : " , product )
print ( " The Quotient of the two numbers is : " , quotient )
```


###### 2. Create a Python program that calculates the square of a given number using exponentiation.

```python

num = int ( input ( " Enter a number : " ) )

square = num ** 2

print ( " The Square of the number is : " , square )
```


###### 3. Write a Python program that calculates the average of three numbers entered by the user.

```python 

num1 = int ( input ( " Enter your First Number : " ) )
num2 = int ( input ( " Enter your Second Number : " ) )
num3 = int ( input ( " Enter your Third Number : " ) )

average = ( num1 + num2 + num3 ) / 3

print ( " The Average of the three numbers is : " , average )
```

###### 4. Create a Python program that checks if a given number is even or odd and prints the result.

```python

num = int ( input ( " Enter a number : " ) )

if num % 2 == 0 :
    print ( " The number is Even " )
else :
    print ( " The number is Odd " )
```

    
###### 5. Write a Python program that calculates the area of a circle given its radius using the math module for the value of π.
import math 

```python

radius = int ( input ( " Enter the radius of the circle : " ) )

area = math.pi * ( radius ** 2 ) 

print ( " The Area of the circle is : " , area )
```

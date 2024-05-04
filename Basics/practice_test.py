# 1. Write a Python program that declares two variables, `x` and `y`, and swaps their values without using a third variable.

x = int ( input ( "Enter your First Number : "))
y = int ( input ( "Enter your Second Number : "))

print ( " Before Swapping the Numbers are : " )
print ( "x = " , x )
print ( "y = " , y )

x = x + y 
y = x - y 
x = x - y 

print ( " After Swapping the Numbers are : " )
print ( "x = " , x )
print ( "y = " , y )
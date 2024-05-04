# Practice Test 
This is a new Markdown file.

###### 1. Write a Python program that declares two variables, `x` and `y`, and swaps their values without using a third variable.

```python

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
```

###### 2. Create a Python program that calculates the area of a rectangle using variables for length and width entered by the user.

```python

print ( " \t\t Welcome in the World of Rectangle \t\t " )
print ( " \t\t ================================= \t\t " )
print ( )
length = int ( input ( " Enter the Length of the Rectangle : "))
width = int ( input ( " Enter the Width of the Rectangle : "))

area = length * width 

print ( " Area of the Rectangle is : " , area , "unit per square " )
```

###### 3. Write a Python program that converts temperature from Celsius to Fahrenheit using variables.

```python 

print ( " \t\t Welcome in the World of Temperature Conversion \t\t " )
print ( " \t\t ============================================= \t\t " )

celsius = float ( input ( " Enter the Temperature in Celsius : " ) )

fahrenheit = ( celsius * 9/5 ) + 32

print ( " The Temperature in Celsius is : " , celsius , " ° C " )
print ( " The Temperature in Fahrenheit is : " , fahrenheit , " ° F " )
```

###### 4. Create a Python program that takes the radius of a circle as input and calculates its circumference using variables.

```python 

print ( " \t\t Welcome in the World of Circle \t\t " )
print ( " \t\t ============================== \t\t " )

radius = float ( input ( " Enter the Radius of the Circle : " ) )

circumference = 2 * 3.14 * radius

print ( " The Circumference of the Circle is : " , circumference , "unit " )
```

###### 5. Write a Python program that calculates the volume of a cylinder using variables for radius and height entered by the user.

```python

print ( " \t\t Welcome in the World of Cylinder \t\t " )
print ( " \t\t =============================== \t\t " )

radius = float ( input ( " Enter the Radius of the Cylinder : " ) )
height = float ( input ( " Enter the Height of the Cylinder : " ) )

volume = 3.14 * radius * radius * height

print ( " The Volume of the Cylinder is : " , volume , "unit per cube " )
```

###### 6. Write a Python program that calculates the simple interest using principal amount, rate, and time entered by the user using variables.

```python

print ( " \t\t Welcome in the World of Simple Interest \t\t " )
print ( " \t\t ====================================== \t\t " )

principal = float ( input ( " Enter the Principal Amount : " ) )
rate = float ( input ( " Enter the Rate of Interest : " ) )
time = float ( input ( " Enter the Time Period : " ) )

simple_interest = ( principal * rate * time ) / 100

print ( " The Simple Interest is : " , simple_interest , "unit " )
```

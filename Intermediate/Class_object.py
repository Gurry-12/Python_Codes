# Class and object 

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        
# Create an object of the Student class
student1 = Student("Alice", 20)

# Call the display method of the student1 object
student1.display()

# In the above example, we define a class named Student with two attributes: name and age. We define a constructor (__init__) method that initializes the name and age attributes. We define a display method that prints the name and age of the student. We create an object of the Student class named student1 with the name "Alice" and age 20. We call the display method of the student1 object to print the name and age of the student.

# You can also define class methods and static methods in a class. For example:

class Math:
    @classmethod
    def add(cls, a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b
    
# Call the add class method of the Math class

result = Math.add(10, 20)
print(result)

# Call the multiply static method of the Math class

result = Math.multiply(10, 20)
print(result)

# this file is about basics of class and object in python

# In the above example, we define a class named Math with two methods: add and multiply. The add method is a class method that
# takes two arguments a and b and returns their sum. The multiply method is a static method that takes two arguments a and b
# and returns their product. We call the add class method of the Math class with arguments 10 and 20 and store the result in the
# variable result. We print the result. We call the multiply static method of the Math class with arguments 10 and 20 and store

# the result in the variable result. We print the result.

# You can also define properties in a class using the @
# property decorator. For example:

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        
# Create an object of the Person class
person = Person("Alice")

# Get the name property of the person object
print(person.name)

# Set the name property of the person object

person.name = "Bob"

# Get the name property of the person object

print(person.name)

# In the above example, we define a class named Person with a private attribute _name. We define a constructor (__init__) method that initializes the _name attribute. We define a property named name using the @property decorator that returns the value of the _name attribute. We define a setter method for the name property using the @name.setter decorator that sets the value of the _name attribute. We create an object of the Person class named person with the name "Alice". We get the name property of the person object using the dot notation and print it. We set the name property of the person object to "Bob" using the dot notation. We get the name property of the person object using the dot notation and print it.

# You can also define class properties using the @classmethod decorator. For example:

class Circle:
    
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

    @property
    def area(self):
        return 3.14 * self.radius * self.radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

# Create an object of the Circle class
circle = Circle(5)

# Get the diameter property of the circle object
print(circle.diameter)

# Get the area property of the circle object
print(circle.area)

# Create an object of the Circle class using the from_diameter class method
circle = Circle.from_diameter(10)

# Get the diameter property of the circle object
print(circle.diameter)

# Get the area property of the circle object
print(circle.area)

# In the above example, we define a class named Circle with an attribute radius. We define a constructor (__init__) method that initializes the radius attribute. We define two properties named diameter and area using the @property decorator that return the diameter and area of the circle, respectively. We define a class method named from_diameter using the @classmethod decorator that creates a Circle object from the diameter of the circle. We create an object of the Circle class named circle with a radius of 5. We get the diameter and area properties of the circle object using the dot notation and print them. We create an object of the Circle class named circle using the from_diameter class method with a diameter of 10. We get the diameter and area properties of the circle object using the dot notation and print them.

# You can also define class properties using the @staticmethod decorator. For example:


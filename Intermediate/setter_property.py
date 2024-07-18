# Sure! Here are five questions focused on using setters and properties in Python:

# ### Setters and Properties Problems

# 1. **Create a class `Person` with a private attribute `_age`.
# Implement a property `age` with a getter and setter to access and modify the `_age` attribute. 
# Ensure the setter checks that the age is a positive integer.

#class
class Person:
    
    #constructor 
    def __init__(self, age):
        self._age = age
        
    #getter 
    @property
    def age(self):
        return self._age
    
    #setter
    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            print("Age must be a positive integer.")
        
person = Person(25)
print(person.age) #25
person.age = 30
print(person.age) #30
person.age = -5 #Age must be a positive integer.
print(person.age) #30

# 2. **Define a class `Rectangle` with private attributes `_width` and `_height`.
# Implement properties `width` and `height` with getters and setters to access and modify these attributes.
# Ensure the setters check that the width and height are positive values.

#class
class Rectangle:
    
    #constructor
    def __init__(self, width, height):
        self._width = width
        self._height = height
        
    #getter
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    #setter 
    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            print("Width must be a positive value.")
            
    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            print("Height must be a positive value.")

rectangle = Rectangle(10, 20)
print(rectangle.width) #10
print(rectangle.height) #20
rectangle.width = 15
rectangle.height = 25
print(rectangle.width) #15
print(rectangle.height) #25
rectangle.width = -5 #Width must be a positive value.
rectangle.height = -10 #Height must be a positive value.
print(rectangle.width) #15
print(rectangle.height) #25

# 3. **Create a class `Student` with a private attribute `_grade`. Implement a property `grade` with a getter and setter to access and modify the `_grade` attribute. Ensure the setter checks that the grade is within the range 0 to 100.**

#class
class Student:
    
    #constructor
    def __init__(self, grade):
        self._grade = grade
        
    #getter
    @property
    def grade(self):
        return self._grade
    
    #setter
    @grade.setter
    def grade(self, value):
        if value in range(0, 101):
            self._grade = value
        else:
            print("Grade must be between 0 and 100.")
            
student = Student(85)
print(student.grade) #85
student.grade = 90
print(student.grade) #90
student.grade = 105 #Grade must be between 0 and 100.
print(student.grade) #90




# Sure! Here is a set of 15 questions focused on practical applications of classes and objects in Python:

# ### Practical Application Questions

# 1. **Define a Python class named `Book` with attributes `title`, 
# `author`, and `year_published`. Include a method to display the book's information.**
'''
#Class
class Book:
    
    #constructor 
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published
        
    #method to display the book's information
    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")
        
#creating an object of the class
book1 = Book("Python Programming", "John Doe", 2020)
book1.display()

'''

# 2. **Create a class named `Circle` that has an attribute `radius`. 
# Include methods to calculate the area and circumference of the circle.**

'''
#Class 
class Circle:
    
    #constructor 
    def __init__(self, radius):
        self.radius = radius
    
    #method to calculate the area of the circle
    def calculate_area(self):
        return 3.14 * self.radius * self.radius
    
    #method to calculate the circumference of the circle
    def parameter_circles(self):
        return 2 * 3.14 * self.radius
    

#creating an object of the class'

circle1 = Circle(5)
print(f"Area of the circle: {circle1.calculate_area()}")
print(f"Circumference of the circle: {circle1.parameter_circles()}")

'''   

# 3. **Write a class named `Student` with attributes `name` and `grades` (a list).
# Include methods to add a grade and calculate the average grade.**
''''
#class
class Student:
        
        #constructor
        def __init__(self, name, grades):
            self.name = name
            self.grades = grades
        
        #method to add a grade
        def add_grade(self, grade):
            self.grades.append(grade)
        
        #method to calculate the average grade
        def average_grade(self):
            return sum(self.grades) / len(self.grades)
        
#creating an object of the class
student1 = Student("Alice", [90, 85, 88])
student1.add_grade(92)
print(f"Average grade for {student1.name}: {student1.average_grade()}")

'''

# 4. **Design a class named `BankAccount` with attributes `account_number` and `balance`.
# Include methods to deposit and withdraw money, and to check the balance.**
'''
#class
class BankAccount:
    
    #constructor 
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    #method to deposit money
    def deposit_money(self, money):
        self.balance += money
        
    #method to withdraw money
    def withdraw_money(self, money):
        self.balance -= money
        
    #method to check the balance
    def check_balance(self):
        return self.balance
    
#creating an object of the class
account1 = BankAccount("123456", 100)
account1.deposit_money(50)
account1.withdraw_money(20)
print(f"Current balance: {account1.check_balance()}")

'''

# 5. **Create a class `Car` with attributes `make`, `model`, and `year`.
# Include a method to display the car's information and a method to start the car.**
'''
#class 
class Car:
    
    #constructor 
    def __init__(self, make, model, year):
        self.make = make 
        self.model = model 
        self.year = year

    #method to display the info's
    def display(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
    
    #method to start the car
    def start(self):
        print("Car started!")
    
#creating an object of the class
car1 = Car("Toyota", "Corolla", 2020)
car1.display()
car1.start()

    
'''
# 6. **Write a class `Employee` with attributes `name`, `position`, and `salary`.
# Include a method to give a raise to the employee by a certain percentage.**
'''
#class
class Employee:
        
        #constructor
        def __init__(self, name, position, salary):
            self.name = name
            self.position = position
            self.salary = salary
            
        #method to give a raise
        def give_raise(self, percentage):
            self.salary += self.salary * (percentage / 100)
            print(f"Total salary now : {self.salary}")
            
#create an object 
employee1 = Employee("Ram","BA",45000)
employee1.give_raise(20)
'''

# 7. **Define a class `Rectangle` with attributes `width` and `height`. 
# Include methods to calculate the area and perimeter of the rectangle.
'''
#class
class Rectangle:
    
    #constructor 
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    #method to calculate area 
    def area_of_rectangle(self):
        return self.width * self.height 
    
    #method to calculate perimeter 
    def perimeter_of_rectangle(self):
        return 2 * ( self.width + self.height )
    

#create an object 

rect1 = Rectangle(3,5)
print(rect1.area_of_rectangle())
print(rect1.perimeter_of_rectangle())

'''
# 8. **Create a class `Dog` with attributes `name` and `age`. 
# Include methods to display the dog's details and to increment the dog's age by one year.
'''
#class
class Dog:
    
    #constructor 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #method to display the dog details
    def dog_detail(self):
        print(f"Dog's name : {self.name}")
        print(f"Dog's age : {self.age} years")

    #method to increment the age
    def age_increase(self):
        self.age += 1
        
#create an object 
husky = Dog("Siberian Husky", 4 )
husky.dog_detail()
husky.age_increase()
husky.dog_detail()
'''

        
# 9. **Design a class `Library` that can store a list of `Book` objects (from question 1).
# Include methods to add a book, remove a book, and display all books in the library.

'''
#class
class Book:
    
    #constructor 
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published
        
    #method to display the book's information
    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")
class Library:
        
        #constructor 
        def __init__(self):
            self.books = []
            
        #method to add a book
        def add_book(self, book):
            self.books.append(book)
            
        #method to remove a book
        def remove_book(self, book):
            self.books.remove(book)
            
        #method to display all books
        def display_books(self):
            for book in self.books:
                book.display()
                print()

#creating an object of the class
library = Library()
book1 = Book("Python Programming", "John Doe", 2020)
book2 = Book("Data Structures", "Alice Smith", 2019)
library.add_book(book1)
library.add_book(book2)
library.display_books()
'''

# 10. **Write a class `Temperature` with a single attribute `celsius`.
# Include methods to convert the temperature to Fahrenheit and Kelvin.
'''
#class
class Temperature:
    
    #constructor
    def __init__(self, celsius):
        self.celsius = celsius
        
    #method to convert in Fahrenheit
    def C_to_F(self):
        return (self.celsius * 9/5 ) + 32
    
    #method to convert in Kelvin 
    def C_to_K(self):
        return (self.celsius + 273.15)

#creating an object 
temp = Temperature(56)

print(f"The Temperature in Celsius is : {temp.celsius}")    
print(f"The Temperature in Fahrenheit is : {temp.C_to_F()}")    
print(f"The Temperature in Kelvin is : {temp.C_to_K()}")    

'''
# 11. **Create a class `Person` with attributes `name` and `birthdate`.
# Include methods to calculate the person's age and to display their information.
'''
#class 
import datetime
class Person:
    
    #constructor
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
        
    #calculate the age
    def calculate_age(self):
        today = datetime.datetime.now()
        year = today.year
        birth_year = self.birthdate.year
        return year - birth_year
    
    #display the information
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Birthdate: {self.birthdate}")
        print(f"Age: {self.calculate_age()} years")
        
#creating an object of the class
person1 = Person("Alice", datetime.datetime(1990, 5, 15))
person1.display_info()

'''

# 12. **Define a class `Movie` with attributes `title`, `director`, and `duration`.
# Include methods to display the movie's details and to check if the movie is longer than a given duration.

'''
#class
class Movie:
    
    #constructor
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        
    #display the movie's details
    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Director: {self.director}")
        print(f"Duration: {self.duration} minutes")
        
    #check if the movie is longer than a given duration
    def check_duration(self, given_duration):
        return self.duration > given_duration
    
#creating an object of the class
movie1 = Movie("Inception", "Christopher Nolan", 148)
movie1.display_details()
print(f"Is the movie longer than 2 hours? {movie1.check_duration(120)}")

'''
# 13. **Write a class `ShoppingCart` that can store a list of items. 
# Include methods to add an item, remove an item, and calculate the total price of the items.
'''
#class
class Item:
    
    #constructor
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    #method to display details 
    def display(self):
        print(f"Item : {self.name}, Price : {self.price}")
class ShoppingCart:
    
    #constructor
    def __init__(self,):
        self.items = []
        
    #method to add item
    def add_item(self, item):
        self.items.append(item)
        
    #method to remove item
    def remove_item(self, item):
        self.items.remove(item)
        
    #method to display the item
    def display_item(self):
        for item in self.items:
            item.display()
            print()
            
    #method to calculate total price 
    def total_price(self):
        self.total_price = 0
        for item in self.items:
            self.total_price += item.price
        return self.total_price
            
#create an object 
item1 = Item("Chips", 20)
item2 = Item("Soft Drink", 100)

cart = ShoppingCart()
cart.add_item(item1)
cart.add_item(item2)

cart.display_item()
print(f"Total price is : {cart.total_price()}")
'''

# 14. **Design a class `Point` with attributes `x` and `y`. 
# Include methods to calculate the distance from the point to the origin (0, 0) and to another point.

#class 
class Point:
    
    #constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    #method to calculate distance from the point to the origin
    def distance_to_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    #method to calculate distance to another point
    def distance_to_point(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
    
#creating objects of the class
point1 = Point(3, 4)
point2 = Point(6, 8)

print(f"Distance from point1 to origin: {point1.distance_to_origin()}")
print(f"Distance from point1 to point2: {point1.distance_to_point(point2)}")



# 15. **Create a class `Course` with attributes `course_name` and `students` (a list of `Student` objects from question 3).
# Include methods to add a student, remove a student, and calculate the average grade of all students in the course.**
'''
#class
class Student:
        
        #constructor
        def __init__(self, name, grades):
            self.name = name
            self.grades = grades
        
        #method to add a grade
        def add_grade(self, grade):
            self.grades.append(grade)
        
        #method to calculate the average grade
        def average_grade(self):
            return sum(self.grades) / len(self.grades)
    
class Course:
    
    #constructor 
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []
        
    #method to add a student
    def add_student(self, student):
        self.students.append(student)

    #method to remove a student
    def remove_student(self, student):
        self.students.remove(student)

            
    #method to calculate the average grade of all students
    def average_grade(self):
        total = 0
        for student in self.students:
            total += student.average_grade()
        return total / len(self.students)
    
#creating an object of the class
course = Course("Python Programming")
student1 = Student("Alice", [90, 85, 88])
student2 = Student("Bob", [80, 75, 78])
course.add_student(student1)
course.add_student(student2)
print(f"Average grade of all students in the course: {course.average_grade()}")
'''
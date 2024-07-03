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



# 4. **Design a class named `BankAccount` with attributes `account_number` and `balance`.
# Include methods to deposit and withdraw money, and to check the balance.**

# 5. **Create a class `Car` with attributes `make`, `model`, and `year`. Include a method to display the car's information and a method to start the car.**

# 6. **Write a class `Employee` with attributes `name`, `position`, and `salary`. Include a method to give a raise to the employee by a certain percentage.**

# 7. **Define a class `Rectangle` with attributes `width` and `height`. Include methods to calculate the area and perimeter of the rectangle.**

# 8. **Create a class `Dog` with attributes `name` and `age`. Include methods to display the dog's details and to increment the dog's age by one year.**

# 9. **Design a class `Library` that can store a list of `Book` objects (from question 1). Include methods to add a book, remove a book, and display all books in the library.**

# 10. **Write a class `Temperature` with a single attribute `celsius`. Include methods to convert the temperature to Fahrenheit and Kelvin.**

# 11. **Create a class `Person` with attributes `name` and `birthdate`. Include methods to calculate the person's age and to display their information.**

# 12. **Define a class `Movie` with attributes `title`, `director`, and `duration`. Include methods to display the movie's details and to check if the movie is longer than a given duration.**

# 13. **Write a class `ShoppingCart` that can store a list of items. Include methods to add an item, remove an item, and calculate the total price of the items.**

# 14. **Design a class `Point` with attributes `x` and `y`. Include methods to calculate the distance from the point to the origin (0, 0) and to another point.**

# 15. **Create a class `Course` with attributes `course_name` and `students` (a list of `Student` objects from question 3). Include methods to add a student, remove a student, and calculate the average grade of all students in the course.**

# Would you like any specific examples or explanations for these questions?
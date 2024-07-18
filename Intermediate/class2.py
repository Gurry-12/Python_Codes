# Certainly! Here are some questions that focus on the practical application of static methods and class methods in Python:

# 1. **Define a Python class named `MathOperations` 
# that includes a static method to calculate the square of a number.

#class 
class MathOperations:
    
    @staticmethod
    def square(value):
        return value ** 2
    
# Test the static method
print(MathOperations.square(5))  # Output: 25

# 2. **Create a class `TemperatureConverter` with static methods
# to convert temperatures between Celsius, Fahrenheit, and Kelvin.

#class
class Temperature:
    
    @staticmethod
    def celsius_to_Fahrenheit(value):
        return ( value * 9/5) + 32

    @staticmethod
    def Fahrenheit_to_celsius(value):
        return ( value - 32) * 5/9
    
    @staticmethod
    def celsius_to_kelvin(value):
        return value + 273.15
    
    @staticmethod
    def kelvin_to_celsius(value):
        return value - 273.15
    
    @staticmethod
    def Fahrenheit_to_kelvin(value):
        return ( value - 32) * 5/9 + 273.15
    
    @staticmethod
    def kelvin_to_Fahrenheit(value):
        return ( value - 273.15) * 9/5 + 32
    
# Test the static methods
print(Temperature.celsius_to_Fahrenheit(0))  # Output: 32.0
print(Temperature.Fahrenheit_to_celsius(32))  # Output: 0.0
print(Temperature.celsius_to_kelvin(0))  # Output: 273.15
print(Temperature.kelvin_to_celsius(273.15))  # Output: 0.0
print(Temperature.Fahrenheit_to_kelvin(32))  # Output: 273.15
print(Temperature.kelvin_to_Fahrenheit(273.15))  # Output: 32.0


# 3. **Write a class `Utilities` with a static method that checks if a string is a palindrome.

#class
class Utilities:
    
    @staticmethod
    def check_palindrome(str):
        return str == str[::-1]
    
# Test the static method
print(Utilities.check_palindrome("radar"))

# 4. **Define a class `Date` with a class method `today` that returns the current date.

#class
from datetime import date

class Date:
        
        @classmethod
        def today(cls):
            return date.today()
        
# Test the class method
print(Date.today())  # Output: current date

# 5. **Create a class `Employee` with a class attribute `employee_count`. 
# Include a class method to increment this count every time a new employee is created.

#class
class Employee:
    
    employee_count = 0
    
    #constructor
    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1
    
    @classmethod
    def get_employee_count(cls):
        return cls.employee_count
    
# Test the class method
emp1 = Employee("Alice")
emp2 = Employee("Bob")
print(Employee.get_employee_count())  # Output: 2


# 6. **Write a class `Logger` with a class attribute `log_file`. 
# Include a static method to log messages to this file.**
#class
class Logger:
        
        log_file = "log.txt"
        
        @staticmethod
        def log_message(message):
            with open(Logger.log_file, "a") as file:
                file.write(message + "\n")
                
# Test the static method
Logger.log_message("An error occurred")  # Logs the message to the file


# 7. **Define a class `Vehicle` with a class method `from_string`
# that takes a string in the format "make,model,year" and returns a new instance of the class.

#class
class Vehicle:
        
        def __init__(self, make, model, year):
            self.make = make
            self.model = model
            self.year = year
            
        @classmethod
        def from_string(cls, string):
            make, model, year = string.split(",")
            return cls(make, model, year)
        
# Test the class method
car = Vehicle.from_string("Toyota,Corolla,2020")
print(car.make)  # Output: Toyota
print(car.model)  # Output: Corolla
print(car.year)  # Output: 2020


# 8. Create a class `Bank` with a static method to validate if a given account number follows the bank's account number format.

#class 
class Bank:
    
    #constructor
    def __init__(self, account_number):
        self.account_number = account_number
    
    #method to validate account no.
    @staticmethod
    def validate_account_number(account_number):
        if len(account_number) == 10 and account_number.isnumeric():
            return True
        return False
    
# Test the class method
account_1 = Bank(7654328932)
account_2 = Bank(1234567890)

print(Bank.validate_account_number(str(account_1.account_number)))  # Output: True
print(Bank.validate_account_number(str(account_2.account_number)))  # Output: True


# 9. **Write a class `Configuration` with a class attribute `settings` (a dictionary). 
# Include a class method to update these settings.

#class
class Configuration:
    
    settings = {"color" : "light", "resolution" : "high"}
    
    @classmethod
    def update_settings(cls, key, value):
        if key in cls.settings:
            cls.settings[key] = value  
                
# Test the class method
Configuration.update_settings("color", "dark")
    

# 10. **Define a class `Calculator` with a static method to add two numbers and a
# class method to store and retrieve the last calculated result.

#class 
class Calculator:
    
    last_value = 0
    
    @staticmethod
    def add(a, b):
        Calculator.last_value = a + b
        return a + b
    
    @classmethod
    def get_last_value(cls):
        return cls.last_value
    
# Test the static method
print(Calculator.add(3, 4))  # Output: 7
    
    
# 11. **Create a class `Planet` with a class attribute `planet_count`. 
#  Include a class method to keep track of the number of planets created.

#class
class Planet:
        
        planet_count = 0
        
        #constructor
        def __init__(self, name):
            self.name = name
            Planet.planet_count += 1
        
        @classmethod
        def get_planet_count(cls):
            return cls.planet_count
        
# Test the class method
planet1 = Planet("Earth")
planet2 = Planet("Mars")
print(Planet.get_planet_count())  # Output: 2


# 12. **Write a class `FileManager` with static methods to read from and write to a file.

#class
class FileManager:
        
        @staticmethod
        def read_file(file_name):
            with open(file_name, "r") as file:
                return file.read()
        
        @staticmethod
        def write_file(file_name, data):
            with open(file_name, "w") as file:
                file.write(data)
        
# Test the static methods
FileManager.write_file("data.txt", "Hello, World!")
print(FileManager.read_file("data.txt"))  # Output: Hello, World!



# 13. **Define a class `Student` with a class attribute `school_name`. 
# Include a class method to change the school name for all students.

#class
class Student:
    
    school_name = "ABC School"
    
    #constructor
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name
        
# Test the class method
student1 = Student("Alice")
student2 = Student("Bob")
Student.change_school_name("XYZ School")
print(student1.school_name)  # Output: XYZ School
print(student2.school_name)  # Output: XYZ School

# 14. **Create a class `Shape` with a static method to calculate the area of a rectangle 
# and a class method to set a default color for all shapes.

#class
class Shape:
    
    default_color = "red"
    
    @staticmethod
    def calculate_area_rectangle(length, width):
        return length * width
    
    @classmethod
    def set_default_color(cls, color):
        cls.default_color = color
        
# Test the static method
print(Shape.calculate_area_rectangle(5, 3))  # Output: 15


# 15. **Write a class `Conversion` with static methods for various unit 
# conversions (e.g., kilometers to miles, pounds to kilograms).

#class
class Conversion:
    
    @staticmethod
    def km_to_miles(km):
        return km * 0.621371
    
    @staticmethod
    def miles_to_km(miles):
        return miles / 0.621371
    
    @staticmethod
    def pounds_to_kg(pounds):
        return pounds * 0.453592
    
    @staticmethod
    def kg_to_pounds(kg):
        return kg / 0.453592
    
# Test the static methods
print(Conversion.km_to_miles(10))  # Output: 6.21371
print(Conversion.miles_to_km(6.21371))  # Output: 10.0
print(Conversion.pounds_to_kg(10))  # Output: 4.53592
print(Conversion.kg_to_pounds(4.53592))  # Output: 10.0



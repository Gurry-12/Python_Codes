# ### Inheritance Problems

# 1. Create a base class `Animal` with a method `speak`. 
# Then create two subclasses `Dog` and `Cat` that override the `speak` method to print "Bark" and "Meow" respectively.

#base class
class Animal:
    
    #method to speak
    def speak(self):
        print("Animal speaks")

#sub class 1 
class Dog(Animal):
    
    #override the method
    def speak(self):
        print("Bark")

#sub class 2
class Cat(Animal):
    
    #override the method
    def speak(self):
        print("Meow")
        

#creating objects
dog = Dog()
cat = Cat()

#calling the method
dog.speak()
cat.speak()

# 2. Write a class `Vehicle` with attributes `make` and `model`.
# Create a subclass `Car` that adds the attribute `number_of_doors` and a method `display_info` to show all attributes.

#base class
class Vehicle:
    
    #constructor 
    def __init__(self, make, model):
        self.make = make 
        self.model = model

#sub class 
class Car(Vehicle):
    
    #constructor
    def __init__(self, make, model, number_of_doors):
        super().__init__(make,model)
        self.number_of_doors = number_of_doors
        
    #method to display all the attribute 
    def display_att(self):
        print(f"Made by : {self.make}")
        print(f"Model : {self.model}")
        print(f"No. of Doors : {self.number_of_doors}")
        
        
#creating object
car = Car("Toyota", "Corolla", 4)
car.display_att()

# 3. Define a class `Person` with attributes `name` and `age`.
# Create a subclass `Student` that adds the attribute `student_id` and a method `study`.

#class
class Person:
    
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

#sub class
class Student(Person):
    
    #constructor 
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        
    #method to study
    def study(self):
        print(f"{self.name} is studying")
        
#creating an object 
student = Student("John", 20, 1234)
student.study()


# 4. Create a class `Shape` with a method `area` that raises `NotImplementedError`.
#  Implement two subclasses `Circle` and `Rectangle` that override the `area` method to return the area of the shape.

#base class
class Shape:
    
    #method to calculate area
    def area(self):
        raise NotImplementedError("Subclass must implement this method")

#sub class 1
class Circle(Shape):
    
    #override the method
    def area(self):
        print("Area of Circle")

#sub class 2 
class Rectangle(Shape):
    
    #override the method
    def area(self):
        print("Area of Rectangle")

#creating an object 
circle = Circle()
rectangle = Rectangle()
circle.area()

# 5. Write a class `Employee` with attributes `name` and `salary`.
# Create a subclass `Manager` that adds the attribute `department` and a method to display all attributes.

#base class 
class Employee:
    
    #constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

#sub class
class Manager(Employee):
    
    #constructor 
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    #method to display attributes
    def display(self):
        print(f"Name : {self.name}")
        print(f"Salary : {self.salary}")
        print(f"Department : {self.department}")
        
#create an object
emp = Manager("Mohan" , 34000, "HR")
emp.display()
# 6. Define a class `Account` with attributes `account_number` and `balance`.
# Create a subclass `SavingsAccount` that adds the attribute `interest_rate` and a method to calculate interest.

#base class
class Account:
    
    #constructor
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

#base class
class SavingsAccount(Account):
    
    #constructor
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    
    #method to calculate interest
    def calculate_interest(self):
        print("Interest calculated")
        self.value = self.balance * (self.interest_rate / 100)
        print(f"Interest : {self.value}")
        print(f"Total balance : {self.balance + self.value}")
        
#create an object
account = SavingsAccount(1234567, 100, 10)
account.calculate_interest()

# 7. Create a class `Device` with attributes `brand` and `model`.
# Create a subclass `Phone` that adds the attribute `phone_number` and a method to make a call.

#base class
class Device:
    
    #constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

#sub class 
class Phone(Device):
    
    #constructor
    def __init__(self, brand, model, phone_number):
        super().__init__(brand, model)
        self.phone_number = phone_number
    
    #method to make a call
    def call(self):
        print(f"Calling {self.phone_number}")

#create an object
phone = Phone("Samsung", "Galaxy", 1234567890)
phone.call()

        


# 8. Write a class `LibraryItem` with attributes `title` and `author`.
# Create a subclass `Book` that adds the attribute `isbn` and a method to display all attributes.

#base class
class LibraryItem:
    
    #constructor
    def __init__(self, title, author):
        self.title = title
        self.author = author

#sub class
class Book(LibraryItem):
    
    #constructor
    def __init__(self, title, author, isbn):
        super().__init__(title, author)
        self.isbn = isbn
        
    #method to display all attributes
    def display(self):
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"ISBN : {self.isbn}")
        
#create an object
book = Book("Python", "Guido", 123456789)
book.display()


# 9. Define a class `Appliance` with attributes `brand` and `power`.
# Create a subclass `WashingMachine` that adds the attribute `load_capacity` and a method to display all attributes.

#base class
class Appliance:
    
    #constructor
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power

#sub class
class WashingMachine(Appliance):
    
    #constructor
    def __init__(self, brand, power, load_capacity):
        super().__init__(brand, power)
        self.load_capacity = load_capacity
        
    #method to display all attributes
    def display(self):
        print(f"Brand : {self.brand}")
        print(f"Power : {self.power}")
        print(f"Load Capacity : {self.load_capacity}")

# 10. Create a base class `Account` with methods `deposit` and `withdraw`.
# Implement two subclasses `CheckingAccount` and `SavingsAccount` that override these methods to include specific fees or interest calculations.

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance")


class CheckingAccount(Account):
    def __init__(self, owner, balance=0, fee=1):
        super().__init__(owner, balance)
        self.fee = fee

    def deposit(self, amount):
        super().deposit(amount)
        # No additional action needed for deposit

    def withdraw(self, amount):
        total_withdraw = amount + self.fee
        if amount > 0 and total_withdraw <= self.balance:
            self.balance -= total_withdraw
            print(f"Withdrew {amount} with fee {self.fee}. New balance is {self.balance}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance minus fee")


class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.01):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        super().deposit(amount)
        # Apply interest rate to the balance after deposit
        self.balance += self.balance * self.interest_rate
        print(f"Applied interest. New balance is {self.balance}")

    def withdraw(self, amount):
        super().withdraw(amount)
        # No additional fee for withdraw in savings account


# Example usage
checking = CheckingAccount("John Doe", 100)
checking.deposit(50)
checking.withdraw(30)

savings = SavingsAccount("Jane Doe", 200)
savings.deposit(100)
savings.withdraw(50)




# 11. Write a class `Building` with attributes `address` and `floors`.
# Create a subclass `OfficeBuilding` that adds the attribute `number_of_offices` and a method to display all attributes.

#base class 
class Building:
    
    #constructor
    def __init__(self, address, floors):
        self.address = address
        self.floors = floors

#sub class
class OfficeBuilding(Building):
    
    #constructor
    def __init__(self, address, floors, number_of_offices):
        super().__init__(address, floors)
        self.number_of_offices = number_of_offices
        
    #method to display all attributes
    def display(self):
        print(f"Address : {self.address}")
        print(f"Floors : {self.floors}")
        print(f"Number of Offices : {self.number_of_offices}")
        
#create an object
building = OfficeBuilding("123 Main St", 4, 10)
building.display()


# 12. Define a class `Instrument` with a method `play`.
# Create two subclasses `Piano` and `Guitar` that override the `play` method to print specific sounds for each instrument.

#base class
class Instrument:
    
    #method to play
    def play(self):
        print("Playing")

#sub class 1
class Piano(Instrument):
    
    #override
    def play(self):
        print("Piano sound")

#sub class 2 
class Guitar(Instrument):
    
    #override
    def play(self):
        print("Guitar sound")
        
#creating objects
piano = Piano()
guitar = Guitar()

#calling the method
piano.play()
guitar.play()


# 13. Create a class `Product` with attributes `name` and `price`.
# Create a subclass `Electronics` that adds the attribute `warranty` and a method to display all attributes.

#base class 
class Product:
        
        #constructor
        def __init__(self, name, price):
            self.name = name
            self.price = price

#sub class 
class Electronics(Product):
    
    #constructor
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty
        
    #method to display all attributes
    def display(self):
        print(f"Name : {self.name}")
        print(f"Price : {self.price}")
        print(f"Warranty : {self.warranty}")
        
#create an object
product = Electronics("Laptop", 500, 1)
product.display()


# 14. Write a class `Vehicle` with attributes `make` and `model`.
# Create a subclass `Truck` that adds the attribute `payload_capacity` and a method to display all attributes.

#base class 
class Vehicle:
        
    #constructor
    def __init__(self, make, model):
        self.make = make
        self.model = model

#subclass
class Truck(Vehicle):
        
    #constructor
    def __init__(self, make, model, payload_capacity):
        super().__init__(make, model)
        self.payload_capacity = payload_capacity
        
    #method to display all attributes
    def display(self):
        print(f"Make : {self.make}")
        print(f"Model : {self.model}")
        print(f"Payload Capacity : {self.payload_capacity}")
            
#create an object
truck = Truck("Toyota", "Tacoma", 1000)
truck.display()


# 15. Define a class `Member` with attributes `name` and `membership_number`.
# Create a subclass `PremiumMember` that adds the attribute `membership_level` and a method to display all attributes.

#base class
class Member:
        
    #constructor
    def __init__(self, name, membership_number):
        self.name = name
        self.membership_number = membership_number

#sub class
class PremiumMember(Member):
    
    #constructor
    def __init__(self, name, membership_number, membership_level):
        super().__init__(name, membership_number)
        self.membership_level = membership_level
        
    #method to display all attributes
    def display(self):
        print(f"Name : {self.name}")
        print(f"Membership Number : {self.membership_number}")
        print(f"Membership Level : {self.membership_level}")
                
#create an object
member = PremiumMember("John", 1234, "Gold")
member.display()


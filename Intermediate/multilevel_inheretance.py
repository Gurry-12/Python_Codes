# ### Multilevel Inheritance Problems

# 1. Create a base class `Animal` with a method `eat`.
# Create a subclass `Mammal` that inherits from `Animal` and adds a method `walk`.
# Create a subclass `Dog` that inherits from `Mammal` and adds a method `bark`. Test the methods in the `Dog` class.

#base class 
class Animal:
    
    def eat(self):
        print("Animal is eating")

#sub class1
class Mammal(Animal):
    
    def walk(self):
        print("Animal is walking")
        

#sub class2
class Dog(Mammal):
    
    def bark(self):
        print("Dog is barking")
        

dog = Dog()
dog.eat()   
dog.walk()
dog.bark()


# 2. Define a class `Device` with an attribute `brand` and a method `power_on`.
# Create a subclass `Computer` that inherits from `Device` and adds an attribute `processor`.
# Create a subclass `Laptop` that inherits from `Computer` and adds an attribute `battery_life`.
# Write a method to display all attributes in the `Laptop` class.

#base class 
class Device:
    
    #constructor
    def __init__(self, brand):
        self.brand = brand
        
    #method to power on
    def power_on(self):
        print("Device is power on")

#sub class 1
class Computer(Device):
    
    #constructor
    def __init__(self, brand, processor):
        super().__init__(brand)
        self.processor = processor
        

#sub class 2 
class Laptop(Computer):
    
    #constructor
    def __init__(self, brand, processor, battery_life):
        super().__init__(brand, processor)
        self.battery_life = battery_life
        
    #method to display all attributes
    def display(self):
        print(f"Brand: {self.brand}, Processor: {self.processor}, Battery Life: {self.battery_life}")
        

laptop = Laptop("Dell", "i5", "5 hours")
laptop.display()




# 3. Write a base class `Person` with attributes `name` and `age`.
# Create a subclass `Employee` that inherits from `Person` and adds an attribute `employee_id`.
# Create a subclass `Manager` that inherits from `Employee` and adds an attribute `department`.
# Implement methods to display the information at each level.

#base class
class Person:
    
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

#sub class
class Employee(Person):
    
    #constructor
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

#sub class 1 
class Manager(Employee):
    
    #constructor
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        self.department = department
        
    #method to display information
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, Department: {self.department}")
        

manager = Manager("John", 30, 101, "IT")
manager.display()

# 4. Create a base class `Shape` with a method `draw`.
# Create a subclass `Polygon` that inherits from `Shape` and adds a method `calculate_perimeter`.
# Create a subclass `Triangle` that inherits from `Polygon` and adds a method `calculate_area`.
# Test the methods in the `Triangle` class.

#base class 
class Shape:
    
    def draw(self):
        print("Shape is drawing")

#sub class 
class Polygon(Shape):
        
        def calculate_perimeter(self):
            print("Calculating perimeter")

#sub class 1
class Triangle(Polygon):
        
        def calculate_area(self):
            print("Calculating area")
            
triangle = Triangle()
triangle.draw()
triangle.calculate_perimeter()
triangle.calculate_area()



# 5. Define a class `Vehicle` with an attribute `make` and a method `drive`.
# Create a subclass `Car` that inherits from `Vehicle` and adds an attribute `number_of_doors`.
# Create a subclass `ElectricCar` that inherits from `Car` and adds an attribute `battery_capacity`.
# Write a method to display all attributes in the `ElectricCar` class.

#base class
class Vehicle:
    
    #constructor
    def __init__(self, make):
        self.make = make
        
    #method to drive
    def drive(self):
        print("Vehicle is driving")

#sub class 1 
class Car(Vehicle):
        
        #constructor
        def __init__(self, make, number_of_doors):
            super().__init__(make)
            self.number_of_doors = number_of_doors
    

#sub class 2
class ElectricCar(Car):
    
    #constructor
    def __init__(self, make, number_of_doors, battery_capacity):
        super().__init__(make, number_of_doors)
        self.battery_capacity = battery_capacity
        
    #method to display all attributes
    def display(self):
        print(f"Make: {self.make}, Number of Doors: {self.number_of_doors}, Battery Capacity: {self.battery_capacity}")
        

electric_car = ElectricCar("Tesla", 4, "100 kWh")
electric_car.display()


# 6. Write a class `Appliance` with an attribute `brand` and a method `turn_on`.
# Create a subclass `KitchenAppliance` that inherits from `Appliance` and adds an attribute `use`.
# Create a subclass `Microwave` that inherits from `KitchenAppliance` and adds an attribute `power`.
# Implement methods to display the attributes at each level.

#base class 
class Appliance:
    
    #constructor
    def __init__(self, brand):
        self.brand = brand
        
    #method to turn on
    def turn_on(self):
        print("Appliance is turning on")

#sub class 1
class KitchenAppliance(Appliance):
        
        #constructor
        def __init__(self, brand, use):
            super().__init__(brand)
            self.use = use


#sub class 2
class Microwave(KitchenAppliance):
        
        #constructor
        def __init__(self, brand, use, power):
            super().__init__(brand, use)
            self.power = power
            
        #method to display attributes
        def display(self):
            print(f"Brand: {self.brand}, Use: {self.use}, Power: {self.power}")
            
microwave = Microwave("Samsung", "Heating", "1000 W")
microwave.display()



# 7. Create a base class `Plant` with an attribute `species` and a method `grow`.
# Create a subclass `FloweringPlant` that inherits from `Plant` and adds an attribute `flower_color`.
# Create a subclass `Rose` that inherits from `FloweringPlant` and adds an attribute `thorns`.
# Write a method to display all attributes in the `Rose` class.

#base class 
class Plant:
    
    #constructor
    def __init__(self, species):
        self.species = species
        
    #method to grow
    def grow(self):
        print("Plant is growing")

#sub class
class FloweringPlant(Plant):
        
        #constructor
        def __init__(self, species, flower_color):
            super().__init__(species)
            self.flower_color = flower_color

#sub class
class Rose(FloweringPlant):
            
            #constructor
            def __init__(self, species, flower_color, thorns):
                super().__init__(species, flower_color)
                self.thorns = thorns
                
            #method to display attributes
            def display(self):
                print(f"Species: {self.species}, Flower Color: {self.flower_color}, Thorns: {self.thorns}")
                
rose = Rose("Rose", "Red", "Yes")
rose.display()


# 8. Define a class `Building` with an attribute `address` and a method `describe`.
# Create a subclass `ResidentialBuilding` that inherits from `Building` and adds an attribute `num_units`.
# Create a subclass `Apartment` that inherits from `ResidentialBuilding` and adds an attribute `floor_number`.
# Test the methods in the `Apartment` class.

#base class 
class Building:
    
    #constructor
    def __init__(self, address):
        self.address = address
        
    #method to describe
    def describe(self):
        print("Building is described")

#sub class 
class ResidentBuilding(Building):
        
        #constructor
        def __init__(self, address, num_units):
            super().__init__(address)
            self.num_units = num_units
            

#sub class
class Apartment(ResidentBuilding):
            
            #constructor
            def __init__(self, address, num_units, floor_number):
                super().__init__(address, num_units)
                self.floor_number = floor_number
        
apartment = Apartment("123 Main St", 10, 2)
apartment.describe()


# 9. Write a class `Media` with an attribute `title` and a method `play`.
# Create a subclass `Audio` that inherits from `Media` and adds an attribute `duration`.
# Create a subclass `Song` that inherits from `Audio` and adds an attribute `artist`.
# Write a method to display all attributes in the `Song` class.

#base class 
class Media:
    
    #constructor
    def __init__(self, title):
        self.title = title
        
    #method to play
    def play(self):
        print("Media is playing")

#sub class 
class Audio(Media):
        
        #constructor
        def __init__(self, title, duration):
            super().__init__(title)
            self.duration = duration

#sub class 
class Song(Audio):
                
    #constructor
    def __init__(self, title, duration, artist):
        super().__init__(title, duration)
        self.artist = artist
        
    #method to display attributes
    def display(self):
        print(f"Title: {self.title}, Duration: {self.duration}, Artist: {self.artist}")


# 10. Create a base class `User` with attributes `username` and `email`.
# Create a subclass `Member` that inherits from `User` and adds an attribute `member_id`.
# Create a subclass `Admin` that inherits from `Member` and adds an attribute `admin_level`.
# Implement methods to display the information at each level.

#base class 
class User:
    
    #constructor
    def __init__(self, username, email):
        self.username = username
        self.email = email

#sub class 1
class Member(User):
        
        #constructor
        def __init__(self, username, email, member_id):
            super().__init__(username, email)
            self.member_id = member_id

#sub class 2
class Admin(Member):
    
    #constructor
    def __init__(self, username, email, member_id, admin_level):
        super().__init__(username, email, member_id)
        self.admin_level = admin_level
        
    #method to display information
    def display(self):
        print(f"Username: {self.username}, Email: {self.email}, Member ID: {self.member_id}, Admin Level: {self.admin_level}")
        

admin = Admin("John", "xyz@abc.com", 3, 4)
admin.display()

# 11. Define a class `Game` with an attribute `name` and a method `start`.
# Create a subclass `BoardGame` that inherits from `Game` and adds an attribute `board_size`.
# Create a subclass `Chess` that inherits from `BoardGame` and adds an attribute `number_of_pieces`.
# Write a method to display all attributes in the `Chess` class.

#base class 
class Game:
        
        #constructor
        def __init__(self, name):
            self.name = name
            
        #method to start
        def start(self):
            print("Game is starting")

#sub class
class BoardGame(Game):
        
    #constructor
    def __init__(self, name, board_size):
        super().__init__(name)
        self.board_size = board_size

#sub class 2
class Chess(BoardGame):
                
    #constructor
    def __init__(self, name, board_size, number_of_pieces):
        super().__init__(name, board_size)
        self.number_of_pieces = number_of_pieces
        
    #method to display attributes
    def display(self):
        print(f"Name: {self.name}, Board Size: {self.board_size}, Number of Pieces: {self.number_of_pieces}")
        
chess = Chess("Chess", "8x8", 32)
chess.display()


# 12. Write a class `Instrument` with an attribute `type` and a method `play`.
# Create a subclass `StringInstrument` that inherits from `Instrument` and adds an attribute `number_of_strings`.
# Create a subclass `Guitar` that inherits from `StringInstrument` and adds an attribute `brand`.
# Test the methods in the `Guitar` class.

#base class
class Instrument:
    
    #constructor
    def __init__(self, type):
        self.type = type
        
    #method to play
    def play(self):
        print("Instrument is playing")

#sub class 
class StringInstrument(Instrument):
    
    #constructor
    def __init__(self, type, number_of_strings):
        super().__init__(type)
        self.number_of_strings = number_of_strings

#sub class 
class Guitar(StringInstrument):
        
    #constructor
    def __init__(self, type, number_of_strings, brand):
        super().__init__(type, number_of_strings)
        self.brand = brand
        
guitar = Guitar("Acoustic", 6, "Fender")
guitar.play()


# 13. Create a base class `Document` with an attribute `title` and a method `read`.
# Create a subclass `TextDocument` that inherits from `Document` and adds an attribute `word_count`.
# Create a subclass `Report` that inherits from `TextDocument` and adds an attribute `summary`.
# Implement methods to display the attributes at each level.

#Base class
class Document:
    
    #constructor
    def __init__(self, title):
        self.title = title
        
    #method to read
    def read(self):
        print("Document is reading")

#sub class
class TextDocument(Document):
        
        #constructor
        def __init__(self, title, word_count):
            super().__init__(title)
            self.word_count = word_count

#sub class
class Report(TextDocument):
                
    #constructor
    def __init__(self, title, word_count, summary):
        super().__init__(title, word_count)
        self.summary = summary
        
    #method to display attributes
    def display(self):
        print(f"Title: {self.title}, Word Count: {self.word_count}, Summary: {self.summary}")
        
report = Report("Report", 1000, "Summary of the report")
report.display()


# 14. Define a class `Appliance` with an attribute `power_rating` and a method `turn_on`.
# Create a subclass `CookingAppliance` that inherits from `Appliance` and adds an attribute `max_temperature`.
# Create a subclass `Oven` that inherits from `CookingAppliance` and adds an attribute `volume`.
# Write a method to display all attributes in the `Oven` class.

#Base class
class Appliance:
        
    #constructor
    def __init__(self, power_rating):
        self.power_rating = power_rating

    #method to turn on
    def turn_on(self):
        print("Appliance is turning on")

#sub class
class CookingAppliance(Appliance):
        
    #constructor
    def __init__(self, power_rating, max_temperature):
        super().__init__(power_rating)
        self.max_temperature = max_temperature

#sub class
class Oven(CookingAppliance):
                
    #constructor
    def __init__(self, power_rating, max_temperature, volume):
        super().__init__(power_rating, max_temperature)
        self.volume = volume
        
    #method to display attributes
    def display(self):
        print(f"Power Rating: {self.power_rating}, Max Temperature: {self.max_temperature}, Volume: {self.volume}")
        
oven = Oven("1000 W", "500 F", "5 cu ft")
oven.display()

# 15. Write a class `Software` with an attribute `version` and a method `install`.
# Create a subclass `Application` that inherits from `Software` and adds an attribute `license_key`.
# Create a subclass `GameApp` that inherits from `Application` and adds an attribute `genre`.
# Test the methods in the `GameApp` class.

#Base class
class Software:
        
    #constructor
    def __init__(self, version):
        self.version = version
        
    #method to install
    def install(self):
        print("Software is installing")

# sub class
class Application(Software):
    
    #constructor
    def __init__(self, version, license_key):
        super().__init__(version)
        self.license_key = license_key

#sub class
class GameApp(Application):
                    
    #constructor
    def __init__(self, version, license_key, genre):
        super().__init__(version, license_key)
        self.genre = genre 
        
game_app = GameApp("1.0", "1234", "Action")
game_app.install() 


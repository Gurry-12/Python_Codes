# Certainly! Here are some questions focused on polymorphism in Python:

# ### Polymorphism Problems

# 1. **Create a base class `Animal` with a method `speak`. 
# Create subclasses `Dog`, `Cat`, and `Cow` that each implement the `speak`
# method to return "Bark", "Meow", and "Moo" respectively. Write a function 
# that takes an `Animal` object and calls its `speak` method.

#class 
class Animal:
    
    def speak(self):
        return "I am an animal"
    
#subclass
class Dog(Animal):
    
    def speak(self):
        return "Bark"
    
#subclass
class Cat(Animal):
    
    def speak(self):
        return "Meow"
    
#subclass
class Cow(Animal):
    
    def speak(self):
        return "Moo"
    
def animal_speak(animal):
    return animal.speak()

dog = Dog()
cat = Cat()
cow = Cow()

print(animal_speak(dog)) #Bark
print(animal_speak(cat)) #Meow
print(animal_speak(cow)) #Moo

# 2. **Define a base class `Shape` with a method `area`.
# Create subclasses `Rectangle` and `Circle` that each implement the `area` 
# method to calculate the area of the respective shapes. Write a function that
# takes a `Shape` object and prints its area.

#class
class Shape:
    
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return 0
    
#subclass
class Rectangle(Shape):
        
        def __init__(self, length, breadth):
            self.length = length
            self.breadth = breadth
            
        def area(self):
            return self.length * self.breadth
        
#subclass
class Circle(Shape):
        
        def __init__(self, radius):
            self.radius = radius
            
        def area(self):
            return 3.14 * self.radius * self.radius
        
def shape_area(shape):
    return shape.area()

rectangle = Rectangle(10, 20)
circle = Circle(5)

list_1 = [rectangle, circle]

for i in list_1:
    print(shape_area(i))

# 3. **Write a base class `Employee` with a method `get_salary`.
# Create subclasses `HourlyEmployee` and `SalariedEmployee`
# that each implement the `get_salary` method to calculate and return the salary based
# on hours worked and annual salary respectively. Write a function that takes an `Employee` object and prints its salary.

#class
class Employee:
    
    def get_salary(self):
        return 0
    
#subclass
class HourlyEmployee(Employee):
    
    def __init__(self, hourly_worked , hourly_rate):
        self.hourly_worked = hourly_worked
        self.hourly_rate = hourly_rate
    
    def get_salary(self):
        return self.hourly_rate * self.hourly_worked
    
#subclass
class SalariedEmployee(Employee):
        
        def __init__(self, annual_salary):
            self.annual_salary = annual_salary
            
        def get_salary(self):
            return self.annual_salary / 12
        
def employee_salary(employee):
    return employee.get_salary()

hourly_employee = HourlyEmployee(160, 20)
salaried_employee = SalariedEmployee(50000)

list_2 = [hourly_employee, salaried_employee]

for i in list_2:
    print(employee_salary(i))
    

# 4. **Create a base class `Media` with a method `play`.
# Create subclasses `Song` and `Movie` that each implement the `play`
# method to display "Playing song" and "Playing movie" respectively. 
# Write a function that takes a `Media` object and calls its `play` method.

#class
class Media:
        
    def play(self):
        return "Playing media"
    
#subclass
class Song(Media):
        
        def play(self):
            return "Playing song"
        
#subclass
class Movie(Media):

        def play(self):
            return "Playing movie"
        
def media_play(media):
    return media.play()

song = Song()
movie = Movie()

print(media_play(song))
print(media_play(movie))


# 5. **Define a base class `Vehicle` with a method `start_engine`.
# Create subclasses `Car` and `Motorcycle` that each implement the `start_engine` 
# method to display "Car engine started" and "Motorcycle engine started" respectively. 
# Write a function that takes a `Vehicle` object and calls its `start_engine` method.

#class
class Vehicle:
        
        def start_engine(self):
            return "Vehicle engine started"
        
#subclass
class Car(Vehicle):

        def start_engine(self):
            return "Car engine started"

#subclass
class Motorcycle(Vehicle):
    
            def start_engine(self):
                return "Motorcycle engine started"
            
def vehicle_start_engine(vehicle):
    return vehicle.start_engine()

car = Car()
motorcycle = Motorcycle()

print(vehicle_start_engine(car))
print(vehicle_start_engine(motorcycle))

    

# 6. **Create a base class `Fruit` with a method `nutrition`.
# Create subclasses `Apple` and `Banana` that each implement the `nutrition`
# method to display "Apple is rich in Vitamin A" and "Banana is rich in Vitamin B" respectively.
# Write a function that takes a `Fruit` object and calls its `nutrition` method.

#class
class Fruit:
        
        def nutrition(self):
            return "Fruit is rich in vitamins"
        
#subclass
class Apple(Fruit):
        
        def nutrition(self):
            return "Apple is rich in Vitamin A"
        
#subclass
class Banana(Fruit):
    
            def nutrition(self):
                return "Banana is rich in Vitamin B"
            
def fruit_nutrition(fruit):
    return fruit.nutrition()

apple = Apple()
banana = Banana()

print(fruit_nutrition(apple))
print(fruit_nutrition(banana))
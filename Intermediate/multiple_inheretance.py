# ### Multiple Inheritance Problems

# 1. Create two base classes `Flyable` and `Swimmable` each with a method `move`.
# Implement a subclass `Duck` that inherits from both `Flyable` and `Swimmable` and 
# overrides the `move` method to print both flying and swimming actions.

#base class 1
class Flyable:
    
    def move(self):
        return "I can fly"

#base class 2
class Swimmable:
    
    def move(self):
        return "I can swim"

# sub class 
class Duck(Flyable, Swimmable):
    
    def move(self):
        return f"{Flyable.move(self)} and {Swimmable.move(self)}"
    

duck = Duck()
print(duck.move()) #I can fly and I can swim



# 2. Define two classes `Teacher` and `Engineer` each with an attribute `name` and a method `work`.
# Create a subclass `TeacherEngineer` that inherits from both classes and overrides the `work` 
# method to include both teaching and engineering activities.

#base class 1 
class Teacher:
    
    #constructor 
    def __init__(self,name):
        self.name = name
        
    #method 
    def work(self):
        return "I am a teacher"
    
#base class 2
class Engineer:
        
        #constructor
        def __init__(self,name):
            self.name = name
            
        #method
        def work(self):
            return "I am an engineer"
        
#subclass
class TeacherEngineer(Teacher, Engineer):
    
    def work(self):
        return f"{Teacher.work(self)} and {Engineer.work(self)}"
    
teacher_engineer = TeacherEngineer("John")
print(teacher_engineer.work()) #I am a teacher and I am an engineer


# 3. Create two classes `Person` and `Athlete` each with an attribute `name` and a method `introduce`.
# Implement a subclass `AthleticPerson` that inherits from both and overrides the `introduce`
# method to include information from both base classes.

#base class 1
class Person:
        
        #constructor
        def __init__(self,name):
            self.name = name
            
        #method
        def introduce(self):
            return "I am a person"
        
#base class 2
class Athlete:
        
        #constructor
        def __init__(self,name):
            self.name = name
            
        #method
        def introduce(self):
            return "I am an athlete"
        
#subclass
class AthleticPerson(Person, Athlete):

    def introduce(self):
        return f"{Person.introduce(self)} and {Athlete.introduce(self)}"

athletic_person = AthleticPerson("John")
print(athletic_person.introduce()) #I am a person and I am an athlete


# 4. Write two classes `MusicPlayer` and `VideoPlayer` each with methods `play` and `stop`. 
# Create a subclass `MediaPlayer` that inherits from both and overrides the `play` and `stop` methods to handle both music and video.


#base class 1
class MusicPlayer:

    def play(self):
        return "Playing music"
    
    def stop(self):
        return "Stopped playing music"
    
#base class 2
class VideoPlayer:
    
        def play(self):
            return "Playing video"
        
        def stop(self):
            return "Stopped playing video"
        
#subclass
class MediaPlayer(MusicPlayer, VideoPlayer):
    
    def play(self):
        return f"{MusicPlayer.play(self)} and {VideoPlayer.play(self)}"
    
    def stop(self):
        return f"{MusicPlayer.stop(self)} and {VideoPlayer.stop(self)}"

media_player = MediaPlayer()
print(media_player.play()) #Playing music and Playing video
print(media_player.stop()) #Stopped playing music and Stopped playing video


# 5. Define two classes `ElectricVehicle` and `GasVehicle` each with an attribute `fuel_type` and a method `refuel`.
# Implement a subclass `HybridVehicle` that inherits from both and provides its own `refuel` method.

#base class 1
class ElectricVehicle:
    
    def refuel(self):
        return "Refueling electric vehicle"
    
#base class 2
class GasVehicle:
    
    def refuel(self):
        return "Refueling gas vehicle"
    
#subclass

class HybridVehicle(ElectricVehicle, GasVehicle):
        
        def refuel(self):
            return "Refueling hybrid vehicle"
        
hybrid_vehicle = HybridVehicle()
print(hybrid_vehicle.refuel()) #Refueling hybrid vehicle

    

# 6. Create two classes `Readable` and `Writable` each with a method `access`.
# Create a subclass `File` that inherits from both and overrides the `access` method to handle both reading and writing.

#base class 1
class Readable:
        
        def access(self):
            return "Reading file"
        
#base class 2
class Writable:

        def access(self):
            return "Writing file"
        
#subclass
class File(Readable, Writable):
        
        def access(self):
            return f"{Readable.access(self)} and {Writable.access(self)}"
        
file = File()
print(file.access()) #Reading file and Writing file


# 7. Write two classes `Artist` and `Writer` each with a method `create_art` and `write_book` respectively.
# Implement a subclass `CreativePerson` that inherits from both and adds a method `create` to call both `create_art` and `write_book`.


#base class 1
class Artist:
            
            def create_art(self):
                return "Creating art"
            
#base class 2
class Writer:


            def write_book(self):
                return "Writing book"
            
#subclass
class CreativePerson(Artist, Writer):

    def create(self):
        return f"{Artist.create_art(self)} and {Writer.write_book(self)}"
    
    
creative_person = CreativePerson()
print(creative_person.create()) #Creating art and Writing book


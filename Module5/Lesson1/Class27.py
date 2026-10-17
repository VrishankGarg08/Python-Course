# Topic : Object oriented programming
# Object Oriented Programming is a way of writting code build entirely around classes and objects. In it you    organize your program around things called objects instead of just a list of instructions..
# EVERY OBJECT HAS PROPERTY(s)
# CLASS = BLUEPRINT : IS BLUEPRINT OR A TEMPLATE THAT DISCRIBES WHAT SOMETHING CAN LOOK LIKE AND WHAT IT CAN DO BUT IT ISN'T THE THING ITSELF.
# OBJECT : A REAL THING BUILD FROM CLASS ( BLUEPRINT ). ALSO KNOWN AS INSTANCE
# EXAMPLE:
class Chips : 
    pass
Chips1 = Chips()
# Attribute : A PIECE OF DATA THAT BELONGS TO IT'S CLASS OR IT'S OBJECT
# 2 TYPES OF ATTRIBUTES ARE :
# 1 . INSTANCE ATTRIBUTE : BELONGS TO 1 SECIFIC OBJECT... EACH OBJECT CAN HAVE DIFFERENT VALUES.
# 2 . CLASS ATTRIBUTE : SHARED BY ALL OBJECT OF THE CLASS .. SAME VALUE FOR EVERYTHING/ EVERYONE
# EXAMPLE :
class Dog :
    sound = "Bark"
    def __init__(self,name,species):
        self.name = name
        self.species = species
Dog1 = Dog("Buddy","Labrador")
Dog2 = Dog("Candy","Pug")
print("My First Dog's Name is :", Dog1.sound)
# INIT METHOD : Special Function in a class that runs as soon as a new object is created from it.
# SELF : Refers To Exact Object a method is currently working with connecting it to it's own attribute.

# ACTIVITY :
# 1 .Write a program to create a class with the name Student and perform the following tasks -
#  1. Declare a variable grade 
#  2. Print a sentence inside the class
#  3. Create an object of class student and see the output

class student:
	Sport = "Cricket"
	print("I PLay",Sport)
A = student()
# 2 .Write a program to create a class Vehicle and perform the following tasks -
# 1. Create an __init__ method with arguments - max_speed and mileage
# 2. Create an object of class Vehicle and pass the maximum speed and mileage of the car
# 3. Print the values of max_speed and mileage by using the object

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
modelX = Vehicle(240, 18)
print("Model Max Speed:",modelX.max_speed)
print("Model Mileage:", modelX.mileage)

# 3 .Write a program to create a class Parrot and perform the following tasks - 1. Create a class variable species 2. Create a __init__ method that has instance variables - name and age 3. Create instances of class Parrot, passing arguments as well 4. Print Class variable by accessing it 5. Print Instance variables as well
class Parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
Coco = Parrot("Coco", 10)
Blue = Parrot("Blue", 15)
print("Coco is a {}".format(Coco.species))
print("Woo is also a {}".format(Blue.species))
print("{} is {} years old".format(Coco.name, Coco.age))
print("{} is {} years old".format(Blue.name, Blue.age))
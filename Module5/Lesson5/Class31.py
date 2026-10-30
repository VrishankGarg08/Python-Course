# Abstraction and Polymorphism
# Abstraction : Hiding The Complicate Details And Showing The Necessary Details Only..
# Example :
class Coffee_Machine:
    def Make_Coffee(self):
        self._Boil_Water()
        self._Grind_Beans()
        self._Brew()
    def _Boil_Water(self):
        print("Process Started : Boiling Water")
    def _Grind_Beans(self):
        print("Process Working : Grinding Coffee Beans")
    def _Brew(self):
        print("Process Finished : Brewed The Coffe With Fresh Beans")
Coffee = input("What Type Of Coffee You Would Like :")
print(f"Making {Coffee} Coffee")
Capuchino_Machine = Coffee_Machine()
Capuchino_Machine.Make_Coffee()
print("Proccess Completed ! Thank You Please Visit Again.")
# Abstract Class : Template That Can't Be Used Directly. It Defines what Methods A Child Class Must Have But Wouldn't Tell How.
# Example :
from abc import ABC,abstractmethod
class Shape(ABC) :
    @abstractmethod
    def Area(self):
        pass
    def Describe(self):
        print(f"Area is =  {self.Area()}sq.m")
class Helicopter_Shot(Shape):
    def __init__(self,Height,Width):
        self.Height = Height
        self.Width = Width
    def Area(self):
        return self.Height * self.Width
Bed_Room = Helicopter_Shot(15,20)
Bed_Room.Describe()

# Polymorphism : Same Method Behaving Differentaly
# Polymorphism Through Method Overriding : 
# Example :
class Animal :
    def Sound(self):
        print("Some Animals Sound")
class Dog(Animal):
    def Sound(self):
        print("Bark")
A = Animal().Sound()
D = Dog().Sound()
# Polymorphism without inheritance a simple interface :A Shared Interface
# In Python, objects don't need a common parent class to be used interchangeably. If they simply have the same method name, they work. This is called duck typing:
# "If it walks like a duck and quacks like a duck, it's a duck."
class Dog:
    def speak(self):
        print("Woof!")
class Robot:
    def speak(self):
        print("Beep boop!")

class Radio:
    def speak(self):
        print("Now playing music ... ")
def make_it_speak(thing):
    thing. speak()
make_it_speak(Dog())
make_it_speak(Robot())
make_it_speak(Radio())
# What's happening: Dog, Robot, and Radio have no relationship to each other. No shared parent.
#But they all provide a speak() method (a shared "interface"), so the function works with all of
# them.
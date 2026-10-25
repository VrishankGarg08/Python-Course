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

# Polymorphism : 
# Polymorphism Through Method Overriding 
# Polymorphism without inheritance a simple interface
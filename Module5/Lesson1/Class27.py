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
# INIT METHOD 
#SELF KEY WORD 
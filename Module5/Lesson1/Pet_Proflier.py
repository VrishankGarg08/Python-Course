class Pet :
    print("Hi! I am a Pet Profiler.")
Pet_Object = Pet()
class PetProfiler :
    Category = Pet
    def __init__(self,name,animal_type,age,tasty_food) :
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.tasty_food = tasty_food
Pet1 = PetProfiler("Candy","Cat",7,"Chocolate Fish Treat")
Pet2 = PetProfiler("Buddy","Dog",7,"Oreo Bisuit")
print("Candy is a {}".format(Pet1.Category))
print("Buddy is a {}".format(Pet2.Category))
print("DETAILS FOR 1ST PET")
print("{} is {} & is {} years old..".format(Pet1.name,Pet1.animal_type,Pet1.age))
print("{} likes eating {}".format(Pet1.name,Pet1.tasty_food))
print("DETAILS FOR 2ND PET")
print("{} is {} & is {} years old..".format(Pet2.name,Pet2.animal_type,Pet2.age))
print("{} likes eating {}".format(Pet2.name,Pet2.tasty_food))
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
Pet1 = PetProfiler("Candy",)
Pet2 =
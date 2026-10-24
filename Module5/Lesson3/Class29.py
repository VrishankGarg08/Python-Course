# # Topic : Inheritance ,
# # Inheritance : Means one class can pass down it's feature to another class without retyping anything at all.The class receiving the feature is called the CHILD CLASS and the class giving the feature is called PARENT CLASS.
# # EXAMPLE :
# class CHARACTER :
#     def Walk(self):
#         print("WALKING..")
# class ROBOT(CHARACTER):
#     def DETECT(self):
#         print("ENEMY DETECTED!! PLEASE ALLOW TO FIRE")
#         print("FIRINGG...........")
#         print("ENEMY KILLED !!! MASTERY ACHIVED..")
# Habibot = ROBOT()
# Habibot.Walk()
# Habibot.DETECT()
# # EXAMPLE 2 :
# class CHARACTER :
#     def __init__(self,name,health):
#         self.name = name
#         self.health = health
# class Dog_Man(CHARACTER) :
#     pass
# Saver = Dog_Man("Saver",1000)
# print("Name :",Saver.name)
# print("Health :",Saver.health)

# SUPER KEYWORD : is a shortcut that reached the PARENT classes Features without you having to type the name of the PARENT class inside your PYTHON CODE.
# Example :
class CHARACTER :
    def __init__(self,name,health):
        self.name = name
        self.health = health
class Wimpy_Kid(CHARACTER) :
    def __init__(self,name,health,power):
        super().__init__(name,health)
        self.power = power
Wimpy = Wimpy_Kid("Wimpy",100,"Ability to make anyone LAUGH..")
print(Wimpy.name,Wimpy.health,Wimpy.power)
# OVERRIDING A METHOD : Method Overriding happens when a child class writes its own version of method that already exsist in the parent class
#EXAMPLES:
class Animal :
    def Sound(self):
        print("Some Animals Sound")
class Dog(Animal):
    def Sound(self):
        print("Bark")
A = Animal().Sound()
D = Dog().Sound()

#ISSUBCLASS: Built-in Function that checks whether 1 class is child of another class .
# Example :
print(issubclass(Dog,Animal))
print(issubclass(Wimpy_Kid,CHARACTER))
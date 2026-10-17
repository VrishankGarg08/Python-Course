# # Topic : Method
# # Method : It is a function that belongs to an object or an class.It Decribes Something an object can do
# # Example :
# class Dog :
#     def Bark(self):
#         print("Woof!..")
# My_Dog = Dog().Bark()
# # Constructor & Destructor
# # Constructor : Is a phase in which an object is created
# # Destructor : Is a phase in which an object is deleted
# # Example :
# class Dog :
#     def __init__(self,Name): # CONSTRUCTOR
#         self.Name = Name     
#         print("Woof!..")
#     def __del__(self): # DESTRUCTOR     
#         print("Woof!.. IS GONEEEEE")
# D = Dog("UNO")
# del D
# Enumerate: It will loop over a list and gives a items and index
# Example :
Fruits = ["Mango","Orange","Guava","Lichee","Strawberry"]
for index,Fruit in enumerate(Fruits):
    print(index,Fruit)
# ACIVITY :
# Write a program to create a class IOString which consists of a constructor that gives a default value to variable Str1. Next up create a method that gets a string as input from the user. Create another method that will print the string in the upper case. Next up create an object and call methods to get everything implemented.
class IOString():
    def __init__(self):
        self.Str1 = ""
    def get_String(self):
        self.Str1 = input("Enter Some Words: ")
    def print_String(self):
        print("Your Words In Capital Are :", self.Str1.upper())
Str1 = IOString()
Str1.get_String()
Str1.print_String()

# ACIVITY :
# Write a program to create a class with the named employee and create a constructor and destructor. Then, write a function to create an object for that class and delete the object. Make sure you call the function to get everything implemented!
class Employee:
    def __init__(self):
        print("Employee Created")
    def __del__(self):
        print("Destructor Created ")
def Create_obj():
    print("Making Object.")
    Obj = Employee()
    print("Function end.")
    return Obj
print("Calling Create_obj() function...")
Obj = Create_obj()
print("Program End...")
# ACTIVITY :
# Write a Program to create a class that will find the numbers in the tuple that add  up to the sum  and return the position  of elements.The Value of sum can be taken as input from user.Tuple - (10,20,30,40,50,60,70).

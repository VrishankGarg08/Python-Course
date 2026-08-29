# Topic : Functions
# Positional Arguments : It means that whena  parameter is passed it matches the order of the parameter
# Example 1 :
# def details (name1 , age1) :
#     print("Hi! My Name is ", name1 ,". My Age is", age1 ,".")
# details ("Vrishank " , 12)

# DocString is like a sticky note which is attached with the function. Explaining what it does with Example 2 :

# def add (a,b) : 
#     """Adds 2 numbers and returns their sum as result """
#     return a + b
# print(add.__doc__)
# print(add(234567 , 876543 ))

# When A FUNTION Calls itself to solve a smaller version of the same problem it is called recursion

# Example 
def factorial (n):
    if n == 1 : 
        return 1
    else :
        return n * factorial (n - 1)
print(factorial(7))

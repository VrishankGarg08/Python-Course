# TOPIC : TUPLE
# TUPLE IS A datastructure in which elements are kept together. ONCE TUPLE is created it can't be changed.      (NEVER EVER)..
# Example 1 :
# A = (1,3,5,7,9,11,)
# print(len(A))
# print (A[::-1])                                                                                                  
# Activity 1 :
#  Write a program to perform the following operations:
#  1. Create a tuple with different datatypes
#  2. Create another tuple of integers 
#  3. Create a new tuple by adding 9 to the previous tuple
#  4. Count the occurrences of an element in the tuple
#  5. Perform slicing on the tuple
A = (7,"Vrishank",)
V = (45,7,18,)
V = V+(9,)
T = (7, "Is","Number","Jursey","Your","Hi")
print(len(T))
print(T[::-1])
print(A)
print(V)
# Activity 2 :
#Write a program to check whether the given tuple - (1,2,3,3,2,1,) is a palindrome or not. If it's a palindrome, then it is the same after being reversed.
A = (1,2,3,3,2,1,)
if A == A[::-1] :
    print(f"The Tulip Set: {A} IS A PALINDROME. ")
else:
    print(f"The Tulip Set: {A} IS A NOT A PALINDROME. ")
# Activity 3:
# Create a tuple named weather with these elements - (1, 0, 0, 0, 1, 1, 0). If the element is 1 then the value of rainy increases by 1 otherwise the value of sunny increases by 1. On the basis of the value of rainy and sunny, predict the weather.
Weather = (1, 0, 0, 0, 1, 1, 0,)
Rainy = 0
Sunny = 0
try :
    for i in Weather :
        if i == 1:
            Rainy += 1
        elif i == 0 :
            Sunny += 1
    print(Weather)
    print("Rain Prediction :", Rainy)
    print("Clear Weather Prediction :", Sunny)
    print("Please Consider Above For Through Out The Weak")
except ValueError :
    print("PLEASE USE THE BINARY NUMBERS 1 AND 0 ONLY WITH COMMA(,) AFTER EVERY NUMBER EVEN AT LAST")
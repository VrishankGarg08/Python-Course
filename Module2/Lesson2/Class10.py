#Topic: Loops
#Types of Loops:
#For Loop: It's used to Iterate(Move or Repeat) over a sequence such as string with the help of for loop we can  Iterate over each item that is present in a squence and exectue the same set of oprations again and again.
#Example 1:
# N="HELLO WORLD"
# for I in N:
#     print(I)
#Example 2:
# for I in range(67):
#     print(I)
#ACTIVITY 1
#Write a program to calculate the sum of whole numbers.

# Num = int(input("Enter a Number : "))
# Sum = 0 
# for i in range(Num):
#     Sum = Sum + i
#     print(Sum)
#ACTIVITY 2
#Write a program to reverse the string entered by the user.
# Str=input("Enter any Name :")
# Ans=""
# for i in Str:
#     Ans=i + Ans
# print("Reversed String",Ans)
#ACTIVITY 3
#Write a program to print the numbers in reverse order beginning from the number entered by the user.
Num = int(input("Enter a Number : "))
for i in range(Num,0,-1):
    print(i)
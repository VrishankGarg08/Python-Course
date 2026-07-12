# Topics to be covered today: 
# 1.Indentation : It tells python that a group of statements belong to a particular block of code, its used for highlighting the block of code. 
# 2.Conditional Statements : They are also called decision making statements. A statement's expression or condition is tested, an depending upon the test condition, if it returns True or False, then other block of code is executed.
#  2.1-If statements : It's a simple statement, it contains a block that will be executed if the condition is True.
#  2.2-If else statements : It evaluates when the given statement is True or False, if a condition is True, then if will be executed otherwise else will be executed. Else cannot be used without If.

# Example for If statement:
# number=7
# if number>0: #True as 7 is bigger than 0 hence it is printing
#     print(number,"is a positive number")

# number=-7
# if number>0: #False as -7 is smaller than 0 so it is not printing anything
#     print(number," is a negative number")


# Example for If-else:

# i=25

# if (i<25): #False
#     print("i is smaller than 25.")
# else:
#     print("i is greater than 25")


# Activity 1:
# write a program to check whether the given number is positive?

# Num=int(input("Enter Your Number : "))
# if (Num>0):
#     print(Num,"Is positive Number.")
# Activity 2: 
# Write to check if a person is buying oranges at 100 rs and later selling it at 120 rs. Find that he has profit or loss?

buy=100
sell=120
if(sell>buy):
    print("Profit")
else :
    print("Loss")

# Activity 3: 
# Write a program to check whether the given number is greater than 15 or smaller than 15.

Num =int(input("Enter A Number :"))
if (Num>15):
    print(Num,"Is Greater than 15")
else:
    print(Num,"Is Smaller than 15")
# Activity 4:
# Write a program to check whether the given number is even or odd?

Num = int(input("Enter A Number :"))
if (Num%2==0):
    print(Num," Is Even")
else: 
    print(Num," Is Odd")
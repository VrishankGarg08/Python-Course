import random
import math
Lucky_Number = random.randint(1,10)
print("Your Lucky No. is :", Lucky_Number)
Choice = ["Play Roblox" , "Practise Coding" , "Solve Mind Games" , "Watch Something."]
print("Choices - " , Choice)
random_activity = random.choice(Choice)
print("Random Activity from 4 of them is to ", random_activity)
print("Guess The Secret Number From 1 to 10 ")
Secret = random.randint(1,10)
while True :
    try:
        S_R = input("Enter a number from 1 to 10 ")
        if S_R == Secret :
            print(" Your Guess Is Correct !")
            break
    except ValueError :
        print("Your Number Wasn't Valid .")
        print("Please Insert a number from 1 to 10 only..")

print("=======================================================================================================")
D_No = float(input("Please Enter A Decimal Number : "))
print("Ceiling Value = " , math.ceil(D_No))
print("Floor Value = " , math.floor(D_No))
x = int(10)
y = int(-5)
print("Copy Sign Result =", math.copysign(x,y))
N_N = int(input("Enter A Negative Value(WITH SIGN) : "))
print("Absolute Value Results = ", math.fabs(N_N))
num1 = int(input("Enter Your First Number"))
num2 = int(input("Enter Your Second Number"))
print("GCD is =" , math.gcd(num1,num2))
print("=======================================================================================================")
print("LUCKY Number : ", Lucky_Number)
print("Random Activity : ",random_activity)
print("Secret Number was ", Secret)
#TOPIC : EXEPTION
# EXEPTION is unusual error or condition that interuptes a programs normal flow stopping the rest of the code from  running.
# try is used when when we need to write a risky code and the risk(s) are to be mentioned in except
# except is like a safety net which acts as the barrier for the code and prevents the whole code from breaking.
#EXAMPLE 1:
# try :
#     N = int(input("Enter A Number : "))
#     Result =(10 / N)
#     print("Result :",Result)
# except ValueError :
#     print("Enter A Valid Number ")
# except ZeroDivisionError :
#     print("Number Can't be divided .")
# What is ELSE FINALLY ?
# else block will work when there is no error is the TRY BLOCK .
# finnaly block will RUNS ALWAYS WHETER THERE IS A ERROR OR NOT.
# Example 2 :
# try :
#     N = int(input("Enter A Number : "))
#     Result =(10 / N)
#     print("Result :",Result)
# except ValueError :
#     print("Enter A Valid Number ")
# else :
#     print("Your Number Was Valid.")
# finally :
#   print("==========================================!Thanks For Trying!========================================")
# EXAMPLE 3:
# Valid = False
# while not Valid :
#     try :
#         N = int(input("Enter A Number : "))
#         Valid = True
#     except ValueError :
#         print(" Your Number WAS NOT Valid.")
# ACTIVITY 1 :
# Write a program to understand how the value error exception works?
Valid = False
while not Valid :
    try :
        N = int(input("Enter A Number : "))
        Valid = True
    except ValueError :
        print(" Your Number WAS NOT Valid.")

#ACTICITY 2 :
#Write a program to check how the exceptions and finally statement works?
try :
     N = int(input("Enter A Number : "))
     Result =(10 / N)
     print("Result :",Result)
except ValueError :
     print("Enter A Valid Number ")
else :
     print("Your Number Was Valid.")
finally :
   print("==========================================!Thanks For Trying!========================================")

# ACTIVITY 3:
# Write a program using nested while loop. If the value is divided by two, then it will run an infinite loop of the bye.
#Step 1: Set a flag variable valid to False, and start a while not valid loop.
#Step 2: Inside the loop, start a try block and read a number using int(input( ... )).
#Step 3: Start an inner while loop that keeps running as long as the number is even (n % 2 == 0).
#Step 4: Inside that inner loop, print "bye", then ask for a new number.
#Step 5: Once an odd number is entered, the inner loop ends and valid is set to True, stopping the outer loop.
#Step 6: Add an except ValueError block that prints "Invalid" if the entered text isn't a number, letting the outer
#loop ask again.
Valid = False
while not Valid:
    try:
        N = int(input("Enter a number: "))
        while N % 2 == 0: # % IS = is Divided by 
            print("bye")
            N = int(input("Enter a new number: "))
        valid = True
    except ValueError:
        print("Invalid")
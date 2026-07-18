# Topic : Python Operators-II

# Topics: 
# 1. if-elif-else Statements :

# Example:
# day="Saurday"

# if day=="Monday":
#     print("First Day of the week.")
# elif day=="Tuesday": 
#     print("Second Day of the week.")   
# elif day=="Wednesday":    
#     print("Third Day of the week.")
# elif day=="Thursday":    
#     print("Fourth Day of the week.")
# elif day=="Friday":    
#     print("Fifth Day of the week.")
# elif day=="Saturday":    
#     print("Weekend.")
# elif day=="Sunday":       
#     print("Funday.")
# else:
#     print("Day not recognized.")

# 2. AND Operator : It is used to join two conditions together, both the conditions should be True. It returns True or False based upon the condition fulfillment.
# Example:
# weather="Rainy"
# homework="Yes"
# day="Monday"
# if weather=="Sunny" and homework=="Yes":
#     print("After school: Head to park.")
# 3. OR Operator : It is used to join two or more conditions. If any one condition is True, it returns True.
# Example:

# if weather=="Rainy" or homework=="No":
#     print("After school: Enjoy Offline")

# 4. NOT Operator :It flips the boolean value.

# Example:
# if not (homework=="Yes"):
#     print("Homework not done yet, Finish it before going out.")
# else:
#     print("NOT applied here")


# 5. Combining Logical Operators :

# if (weather=="Rainy") and not (homework=="Yes"):
#     print("Best Plan: Stay in, finish homework first")
# elif (weather=="Sunny") and (homework=="Yes") and not (day=="Saturday"):
#     print("All set for School Day")
# else:
#     print("Enjoy your day")


# Activity:
# A Python program that asks the user three questions. It classifies the day using if-elif-else. It uses AND to check sunny weather and homework done together. It uses OR to check rainy or cloudy weather. It uses NOT to catch homework not done. It combines all three operators to print the best plan for the day.

# STEPS

# Step 1:  Print the welcome message: "=== Smart School Day Planner ===".

# Step 2:  Use input() to ask for the day, weather, and homework status. Store each in a variable.

# Step 3:  Print the plan header using the day variable in an f-string.

# Step 4:  Write if-elif-else to classify the day type (weekend / Monday / Friday / other school day).

# Step 5:  Write an if statement using AND to check sunny weather and homework done together.

# Step 6:  Write an if statement using OR to check rainy or cloudy weather.

# Step 7:  Write an if statement using NOT to catch when homework is not done.

# Step 8:  Write if-elif-else using AND, OR, and NOT combined to print the best plan message.

# Step 9:  Print the closing message: "Plan complete! Have a wonderful day!"

# Step 10:  Run the program with three different combinations of inputs to test all branches.

Weather=input("WHAT'S THE WEATHER ? :".upper())
Day=input("WHAT'S THE DAY? :")
Homework=input("IS YOUR HOMEWOR DONE ? :")

# TOPIC -- FUNCTION
# Function is a block of code containing related statements. that perform 1 specific task. Function's let you break a big program into smaller pieces of organised code which helps us from repeating the same line again and again through out the code.
#Types of Function :
# Built in : They are the functions that already exsist in PYTHON..
# User Defined : They are the functions which are defined by US .
# Arguments are piece of information that we write inside the brackets when we call a function so that , the USER can use the function with different values every sungle time..
def greet ():
    print("Welcome")

def name (name1) :
    print("Intelligent",name1)
name ("Vrishank") 
greet () 

#ACTIVITY :
# A Lemonade Stand Calculator that greets every customer, calculates the total cost and change due using functions with arguments and return statements, and prints a personalized thank you message alongside the final receipt.
# HOW IT WORKS

# Step 1: Define and call greet_customer() to welcome every customer to the stand.
# Step 2: Ask for the price per cup and the number of cups sold.
# Step 3: Define and call calculate_total() to return the total cost using arguments.
# Step 4: Round the total using the built-in round() function and print it.
# Step 5: Define and call calculate_change() to return the change due.
# Step 6: Define and call thank_you_message() to return a personalized closing line.
# Step 7: Print the final lemonade stand receipt with every calculated value.
Name = input("Enter You Name :")
def greet_customer (Name1) :
    print("Welcome",Name1)
greet_customer (Name)

input("Enter The Price of Cup ? :")
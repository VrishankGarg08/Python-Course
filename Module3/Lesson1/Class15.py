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
SERVING = True
customer = 0
total_money = 0
while SERVING :
    Name = input("Enter You Name :")
    def greet_customer (Name1) :
        print("Welcome",Name1)
    greet_customer (Name)
    print("Tea Cup is of 20 Rs.")
    print("Coffee Cup is of 30 Rs.")
    print("Black Coffee Cup is of 40 Rs.")
    print("Cold Coffe Cup is of 50 Rs.")
    print("KitKat Shake Cup is of 60 Rs.")
    print("Oreo Shake Cup is of 70 Rs.")
    print("Brownie Shake Cup is of 80 Rs.")
    print("Chili Guava Mojito Cup is of 90 Rs.")
    item_count = int(input("How many Types Of Cups are you buying ? "))
    item_number = 1
    total_cost = 0
    while item_number <= item_count :
        number = int(input(f"Enter the No. Of Cup You Want ? :"))
        prize = int(input(f"Enter The Price of Cup ? :"))
        total_cost += (prize*number)
        item_number += 1
        if total_cost > 1000 :
            print("Please Reduce The No. Of Cups (Max Amount Of a Particular Cup Can be 1000 Rs. Only.. ) ")
    def calculate_total(total_cost1) :
        return(total_cost1)
    calculate_total (total_cost)
    print("Your Total Cost is", total_cost)
    total_money += total_cost
    customer += 1
    user_paid = int(input("Enter The Cost You are Paying :"))
    change_due = user_paid - total_cost
    def calculate_change(change_due1) :
        return(change_due1)
    calculate_change (change_due)
    print("Amount to Be Returned =",change_due)
    if change_due < 0 :
        print("Amount Still Needed",change_due)
    Thankyou_msg = "== Your Welcome =="
    def thankyou_msg () :
        return(thankyou_msg)
    print(Thankyou_msg)
    print("Total Amount " , total_cost)
    print("=========================================================================================================")
    print("Customer Served :",customer )
    print("Money Earned :", total_money)
    Queue = input("Are There More Customers ?").upper().strip()
    if Queue == "YES" :
        SERVING = True
    else :
        SERVING = False
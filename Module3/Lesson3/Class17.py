# TOPIC : KEYWORDS
# Keyword is a word specially resserved by python. It has a fix meaning which we can't use as a variable..
# Return keyword is used inside a function to send back a result and stop the function from running further...
# Break Keyword is used to immediatly stop a loop even if the loop wasn'y finished..
# Continue Keyword it skips current round of the loop and move to the next one..
# Pass Keyword does nothing.It is used wehn we need to write some code structure but are not ready to write the actual logic..
# EXAMPLE of RETURN :
# a = 7  
# b= 10
# c = 18
# def add ( a, b ) :
#     return a + b 
# print(add( 7 , 10 ))
#EXAMPLE OF BREAK : 
# for i in range(1,10) :
#     if i == 5 :
#         break
#     print(i)
#EXAMPLE OF PASS :
# for i in range(5) :
#     pass
# EXAMPLE OF CONTINUE :
# for i in range(1,15) :
#     if i == 2 :
#         continue
#     print(i)

# # ACTIVITY
# You build a snack vending machine that accepts coins one at a time, rejects invalid ones, stops once enough money is inserted, and calculates any change owed using a function.
# # STEPS :
# Step 1: Define a function calculate_change(paid, price) that subtracts price from paid and returns the result.
# Step 2: Set the snack price and print a greeting showing the price and the accepted coin values.
# Step 3: Start a while True loop that keeps asking for coins, using continue to reject any coin that isn't 1,2,5, 10, or 20.
# Step 4: Add every valid coin to a running total and print how much has been inserted so far.
# Step 5: Use break to stop the loop the moment the total reaches or passes the snack price.
# Step 6: Call calculate_change() with the total inserted and the snack price to work out the change.
# Step 7: Use pass when the change is exactly zero, or print the change amount otherwise, then print a purchase summary.
def calculate_change(paid, price):
    return paid - price
price = 100

print("Welcome to the Snack Vending Machine!")
print("Snack Price:", price)
print("Accepted Coins in our Shop : 1, 2, 5, 10, 20")
total = 0
while total != price :
    coin = int(input("Insert a coin : "))
    if coin not in [1, 2, 5, 10, 20]:
        print("Invalid coin! Please insert 1, 2, 5, 10, or 20 coin only .")
        continue
    total += coin
    print("Money given :", total)

    if total >= price:
        break

change = calculate_change(total, price)
if change == 0:
    pass
else:
    print("Change to be returned:", change)
print("=============================================Purchase Summary==============================================")
print("Snack price:", price)
print("Total paid:", total)
print("Change Given :", change)
print("Thank you for your purchase!")
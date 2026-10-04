# ADVANCE PYTHON FUNTIONS:
# LIST COMPREHENSION : It is a quick 1 line way to build a brand new list based on the values already in an   existing list... 
# EXAMPLE :
A = [n*n for n in range(1,6)]
print("Squares for numbers :",A)
# Dictionary Comprehension : It is a similar to list comprehension but it creates key values pairs using {}....
# EXAMPLE :
B = {f"{n} X {n}":n*n for n in range(1,6)}
print(B)
# MAP FUNCTION : Map Applies a function to every item in an iteratable format and returns the result.
# EXAMPLE :
C = [1,2,3,4]
print(list(map(lambda x : x * 2,C)))
# ZIP FUNCTION : Pairs ups matching items from 2 seprate list.. Gives a single combined result
# EXAMPLE :
N = ["Vrishank Garg","Abhishek Sharma","Rohit Sharma","Virat Kholi","MS Dhoni"]
M = [99,80,90,49,100]
Result = zip(N,M)
print(list(Result))
# Exit : AS THE NAME SAYS IT STOPS THE PROGRAM...........
# EXAMPLE :
Age = int(input("Tell me your age now !!!:( :"))
if Age < 18 :
    print("Your are not an adult..")
    print("ACCESS DENIED")
    exit()
print("WELCOME")
# ACTIVITY 1 :
#A School Store Inventory Checker that filters in-stock items, pairs item names with stock counts into a dictionary, applies a price markup, asks which item you want to buy, and stops the program immediately if that item has already run out.

# Step 1: Create a list of store item names and a list of matching stock counts.

# Step 2: Pair items with stock counts into a dictionary using zip() and dictionary comprehension.

# Step 3: Filter out only the items that are still in stock using list comprehension.

# Step 4: Ask which item the shopper wants to buy.

# Step 5: Stop the checker immediately using exit() if that item has run out.

# Step 6: Apply a markup to every price using map().

# Step 7: Print the final price paid and the updated inventory.

items = ["Pen", "Notebook", "Pencil", "Eraser", "Bag"]
stock = [10, 0, 15, 0, 5]
prices = [10, 50, 5, 8, 500]

inventory = {item: count for item, count in zip(items, stock)}

in_stock = [item for item in items if inventory[item] > 0]

choice = input("Which item do you want to buy? ")

if inventory.get(choice, 0) == 0:
    print("Sorry, this item is out of stock.")
    exit()

updated_prices = list(map(lambda price: price * 1.10, prices))

index = items.index(choice)
final_price = updated_prices[index]

inventory[choice] -= 1

print("Final price paid:", final_price)
print("Updated inventory:", inventory)
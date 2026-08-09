#Topic : Nested Loops
# Nested Loops : Is A Loop placed entirely inside a body of another loop. Inner Loop finishes everyone of its repeats each time the outer loop runs once.
# Nested While Loop : Is a while loop inside a while loop.
#Example :
# i = 1
# while i <= 3:
#     J = 1
#     while J <= 3:
#         print(i * J,end = " ") # end is used for adding a space
#         J = J+1
#     print()
#     i = i + 1

#Nested For Loop : Used for making patterns 
#Example :
# for i in range(1,3) :
#     for j in range(1,3):
#         print(i*j,end = " ")                                      
#     print()                                                        

# for i in range(1,4): # for i=0 i<3 i=i+1
#     print("New value after each cycle",i)

# continue # is keyword that skips the remaining code in the courrent repeat cycle and jumps straight back to loops condition.
for i in range(10) :
    if i == 3 :
        continue 
    elif i == 6 :
        continue
    elif i== 8 :
        continue
    else :
        print(i)


# Activity 1:
# This one activity keeps you working with both nested loop types end to end - a daily ATM session that serves several customers, then a denomination report printed once the day is done.
#Steps
# Step 1: Set up six counter variables (one per note value) plus counters for customers served and
# total dispensed, all starting at 0.
# Step 2: Start an outer while loop that keeps serving customers until the flag variable serving
# becomes False.
# Step 3: Ask for the customer's name and withdrawal amount; if the amount is invalid, print a
# message and continue back to the top of the loop.
# Step 4: Inside that same repeat, run an inner while loop that checks each of the six note values
# one at a time and works out how many of each note to dispense.
# Step 5: Update the matching counter variable for whichever note value was just dispensed, then
# ask if there is a next customer, setting serving to False if not.
# Step 6: Once the outer while loop ends, start an outer for loop stepping through each of the six
# note values to print the daily denomination report.
# Step 7: Inside that same repeat, run an inner for loop that prints one symbol for every note of that
# value dispensed across the whole day.
    # ATM Cash Dispenser

total_100 = total_50 = total_20 = total_10 = total_5 = total_1 = 0
customers_served = 0
total_dispensed = 0

serving = True
while serving:                                # outer while -- one customer per loop
    name = input("Enter customer name: ")
    amount = int(input("Hello {name}! Enter withdrawal amount: "))
    if amount <= 0:
        print("Invalid amount. Please enter a positive number.")
        continue

    print("Dispensing {amount} units for {name}:")
    remaining = amount
    idx = 1
    while idx <= 6:                            # inner while -- breaks amount into notes
        if idx == 1:
            value = 100
        elif idx == 2:
            value = 50
        elif idx == 3:
            value = 20
        elif idx == 4: 
            value = 10
        elif idx == 5:
            value = 5
        else: value = 1
        count = remaining // value
        if count > 0:
            print("{count} x {value}-unit note(s) =",count * value)
            remaining -= count * value
            if value == 100:
                total_100 += count
            elif value == 50: 
                total_50 += count
            elif value == 20: 
                total_20 += count
            elif value == 10: 
                total_10 += count
            elif value == 5:
                total_5 += count
            else: total_1 += count
        idx += 1

    customers_served += 1
    total_dispensed += amount
    print("Transaction complete, {name}!")
    again = input("Next customer? (yes/no): ").strip().lower()
    if again != "yes":
        serving = False

print("=== Daily Denomination Report ===")
for slot in range(1, 7):                      # outer for -- one denomination per loop
    if slot == 1: value, total = 100, total_100
    elif slot == 2: value, total = 50, total_50
    elif slot == 3: value, total = 20, total_20
    elif slot == 4: value, total = 10, total_10
    elif slot == 5: value, total = 5, total_5
    else: value, total = 1, total_1
    if total > 0:
        print("  {value}-unit notes dispensed : {total} ", end="")
        for note in range(total):             # inner for -- one symbol per note
            print("=", end="")
        print()

print("Customers served : {customers_served}")
print("Total dispensed  : {total_dispensed} units")
print("ATM session closed. Goodbye!")
# Nested Conditionals: Means that keeping one or multiple conditional statements inside another conditional statement.

# Example:

choice=int(input("Enter 1 or 2:  "))
type=int(input("Choose 1 for Fast food or 2 for Main Course: "))
if choice==1:
    if type==1:
        print("Fries are only left, in fast food")
    else:
        print("Have cake as dessert")
elif choice==2:
    if type==2:
        print("Eat Naan & Paneer Combo")
    else:
        print("Eat a Thali")
else:
    print("Invalid option")
# ACTIVITY 1:
# A Python program that prints a welcome banner. It asks you to pick a vehicle — Bike or Car. It uses a nested if-else inside each branch to ask for a specific model. It prints the name, top speed or seats, and best use case for the chosen model. It handles invalid input with an else at the outer level. It closes with a goodbye message.

# STEPS

# Step 1: Print the welcome banner: " === Welcome to Ride Builder! === ".

# Step 2: Print the Step 1 menu: "1 - Bike" and "2 - Car". Take input and store in choice.

# Step 3: Write the outer if for choice == 1 (Bike branch).

# Step 4: Inside the Bike branch, print the Step 2 bike menu. Take input and store in bike_type.

# Step 5: Write a nested if-else for bike_type: Scooty details if 1, Mountain Bike details if else.

# Step 6: Write the outer elif for choice == 2 (Car branch).

# Step 7: Inside the Car branch, print the Step 2 car menu. Take input and store in car_type.

# Step 8: Write a nested if-else for car_type: Sedan details if 1, SUV details if else.

# Step 9: Write the outer else to print an invalid choice message.

# Step 10: Print the closing banner: " === Your custom ride is ready! === ".

print(" === Welcome to Ride Builder! === ")
Choose = int(input("Choose 1 for Bike or 2 for Car: "))
if Choose==1 :
    print("Step 2 Choose Your Ride")
Bike_type=input("If you want to ride a Sport Bike press 1 or Mountain_Bike press 2")
if Choose==1:
    if Bike_type==1 :
        print("Bikes Name: Sport Bike")
        print("Highest Speed: 250 Km/h")
        print("Seats Available:2")
        print("Best Use: Highways and Races")
else:
     print("Name: Mountain Bike")
     print("Top Speed:100 km/h")
     print("Seats Available:2")
     print("Best Use: Off-road trails and hills")
if Choose==2:
    print("Step 2 Choose your Car")
Car_type=input("If you want to ride a Sport Car press 1 or BMW press 2")
if Choose==2:
    if Car_type==1 :
        print("Bikes Name: Sport Car")
        print("Highest Speed: 300 Km/h")
        print("Seats Available:4")
        print("Best Use: High-speed performance and Races")
else:
     print("Name: BMW")
     print("Top Speed:100 km/h")
     print("Seats Available:4")
     print("Best Use: Luxury and city driving")
# Topic : SETS & ARRAYS
# Sets : A Collection where every item appears only once..(EVEN AFTER GIVEN TWICE)
# Example :
MySet = {1,2,3,4,5,5,4,3,2,1}
print(MySet)
# Adding One Items To A Set : (.add)
MySet.add(7)
print("After Adding One No.", MySet)
MySet.update([6,7,8,9,10])
print("After Adding More No.", MySet )
# Set Intersection :
x = {1,2,3,4,5,":)",67}
y = {6,7,8,9,10,":)",67}
# Using Symbol
Common1 = x & y
print(Common1)
# Using Method 
Common2 = x.intersection(y)
print(Common2)
# Hence, PROVED BOTH ARE SAME""




# Arrays : Collection of items that are all of 1 Data type .. IT HAS A FIXED ORDER INSIDE THE MEMORY OF COMPUTER. ## We Need To Import It 
import array as arr
a = arr.array('i',[67,24,24,24,24,24,24,24,24,24,24,24,24,24,24]) 
print(a)
# Adding 1 item to ARRAY :
a.append(11)# Adds Item to the end
print(a)
# Insert : Place a new item at a selected position 
a.insert(0,4)
print(a)
# Count
print(a.count(24))
# Reversing 
a.reverse()
print(a)

# Activity 1:
# A Class Fruit Basket Organizer that stores two fruit baskets as sets, finds the fruits shared between both baskets, and tracks fruit counts using an array that gets updated, counted, and reversed.
#Step 1: Create two fruit baskets as sets, each holding some repeated fruit names.

# Step 2: Add a new fruit into the first basket using add().

# Step 3: Find the fruits shared between both baskets using intersection().

# Step 4: Create an array of fruit counts using the array module.

# Step 5: Add new fruit counts into the array using insert() and append().

# Step 6: Count how many times a chosen number appears in the array.

# Step 7: Reverse the order of the fruit counts array and print the final organizer summary.
import array

basket1 = {"Apple", "Banana", "Mango", "Apple"}
basket2 = {"Banana", "Orange", "Mango", "Banana"}

basket1.add("Grapes")

common = basket1.intersection(basket2)

counts = array.array('i', [10, 20, 30, 20, 40])

counts.insert(1, 15)
counts.append(50)

number = 20
total = counts.count(number)

counts.reverse()

print("Basket 1:", basket1)
print("Basket 2:", basket2)
print("Common fruits:", common)
print("Fruit counts:", counts)
print("Count of", number, ":", total)
print("Reversed counts:", counts)
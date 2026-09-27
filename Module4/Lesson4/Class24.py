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
a = arr.array('i',[67,4,4,4,4,1,1,1,2,3,4,5,6,2,5,9,1,12,24,24,24,24]) 
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

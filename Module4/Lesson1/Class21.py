# TOPIC : LIST 
# DATA STRUCTURE : Just a way of organising storing info. so that a computer can use it easily and quickly.....
# LIST : Ordered Collection of items which is enclosed in square brackets.It's Items can be changed added or # removed any times . It can also have many datatypes.
# EXAMPLE :
# Numbers = [1,2,3,4,5,6,7,8,9,10]
# print(Numbers)
# #FINDING LENGTH OF THE LIST :
# print(len(Numbers))
# # ACCESING RANGE WITH SLICING
# print(Numbers[2:5])
# # ITERATING TO A LIST 
# # ITERATING : ACCESING EACH ELEMENT USING FOR LOOP
# for i in Numbers:                       #  Number = range(1,10)
#     print(i)
# ACTIVITY  1 
# Write a program to perform the following operations on a List:
# 1. Create an empty list 
# 2. A list with elements 
# 3. Use * operator 
# 4. Reverse a list...                # [::-1]
# WHAT YOU WILL BUILD
# You build and print an empty list, a list of numbers, a repeated list using the * operator, and a reversed list using
# slicing.

# HOW IT WORKS
# Step 1: Create an empty list called empty_list and print a blank line.
# Step 2: Create a list called numbers holding five integers and print it.
# Step 3: Use the * operator to repeat [1, 2, 3] three times and store it in triples.
# Step 4: Print the triples list.
# Step 5: Create a list called aList holding five numbers.
# Step 6: Reverse aList using slicing with [ :- 1] and store it back into aList.
# Step 7: Print the reversed aList.
print("======================================================================================================")

# ACTIVITY 2
# Write a Python program to count the number of strings where the string length is two or more, and the first and last characters are the same from a given list of strings.

# WHAT YOU WILL BUILD
# You check a list of words to find which ones have the same first and last character, counting and collecting
# every match.

# HOW IT WORKS
# Step 1: Define a function match_words(words) that takes a list of words.
# Step 2: Set a counter ctr to 0 and an empty list Ist to store matching words.
# Step 3: Loop through every word in the words list.
# Step 4: Check whether the word's length is greater than 1 and its first character equals its last character.
# Step 5: If true, add 1 to ctr and append the word to Ist.
# Step 6: Print the list of matching words once the loop finishes.
# Step 7: Return ctr, call match_words() with a sample list, and print the final count.

print("======================================================================================================")

#ACTIVITY 3
# Write a Python program to find the sum and average of the list. The average of the list is defined as the sum of the elements divided by the number of the elements. Also, find the largest and the smallest number in the list.
# Play with Lists

# WHAT YOU WILL BUILD
# You find the sum, average, smallest, and largest values in a list of numbers.

# HOW IT WORKS
# Step 1: Create a list L holding several integers and print it as the original list.
# Step 2: Set a counter, count, to 0 to store the running sum.
# Step 3: Loop through every element in L and add it to count.
# Step 4: Divide count by len(L) to calculate the average, storing it in avg.
# Step 5: Print the total sum and the average.
# Step 6: Sort Lin ascending order using L.sort().
# Step 7: Print L[o] as the smallest element and L[-1] as the largest element.ITY 
print("======================================================================================================")
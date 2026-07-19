#Topics to be covered : 
# 1. Identity Operators : They checks if two variables point to the same object or not. It has is and is not as the operators.
# Two identity operators: 
# is : Returns True if both variables point to the same object in the memory.
# is not : Returns True if both variables point to the different object in the memory.
# Example:
# a=[1,2,3]
# b=[1,2,3]
# c=a
# print(a==b)
# print(a is b)
# print(a is c)
# print(a is not b)

# 2. Membership Operators : These operators check whether a value exists within a sequence (list, string, tuple, set, dictionary) or not.
# Two type of operators:
# in : Returns True if found in the sequence.
# not in: Returns True if not found in the sequence.

# fruits=["apple","banana","mango"]
# print("banana" in fruits)
# print("grape" not in fruits)

# city="Lucknow"

# print("know" not in city)

# student={"Name":"Ravi","Age":12}
# print("Name" in student)
# print("Riya" in student)

# 3. Bitwise Operators : Bitwise operators work on binary representation of integers, manipulating individual bits.
# Type: AND(&), OR(|), NOT(~)

print(5&3) # 5=0101 & 3=0011 = + = 0001
print(5|3) # 
print(~3)  # 

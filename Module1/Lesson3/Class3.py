#Topic 1:
# Data types: Data types are type of values a variable can hold.It is a classification which specifies which type of value a variable has or what operation can be performed on it.
# Integer: They are the data types which hold whole integer values, including positive and negative numbers.
# Float: Float contains a fractional numbers.(Basically Decimal).Like(1.45)
# Boolean: They contain two values (True and False)
# String: They have text value or a sequence of characters. For example: coding. Anything written inside double quotes("") is a String. 

#Topic 2:
# Typecasting: Its a method to convert a variable data type into a specific data type to perform the operation required by the users.
a="41"
b=39

print(int(a)+b)
print("a+b")

# Topic 3: User Input: 
Name = input("Enter Your Name : ")
print("Your Name is : ", Name)

#String Operations: In python , you can perform various operations on string. Some of the commonly used operations are lower(), upper(), join(), split(), find(), replace(), etc.
# Length of the String: The length of the string.(VRISHANK HAR 8 LENGTH OF STRING)
# Indexing: Each character has a index of its own, by which it can be quickly accessible.
# Slicing: Obtaining a substring is known as slicing. To slice a string : str_name[start,end,steps]. Default value of start is 0 , step is 1, if you want to reverse a string use -1 as step.
# Concatenation: Joining two strings into one. 

# Indexing
string="Coding"
print("Position of i in Coding is: ", string[3])

# Concatenation
str1="Hello "
str2="World"

print(str1+str2)

# Slicing: 
Str="string"
print(Str[3:])
print(Str[0:1])
print(Str[-1:])
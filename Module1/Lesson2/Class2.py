import keyword 
print("Hello Everyone.")
# Cocepts to be covered today:
# 1. Variables: A variable is user-defined. It is a quantity that may change within the context of program. There is no specific command to create a variable. Instead, it gives you a space to assign some value or store some value to it. # Example: age=20
# 2. Keywords: A keyword is a word that has some specific meaning reserved by the programming language, for example: int,float,True,False, if, for, elif, else,etc.
# 3. Identifiers: An identifier is a name used to define variables, function , classes , modules, etc. , so it can be an alphabet, a combination of alphabets,underscore and digit. Keywords cannot be used as identifiers and identifiers cannot start with a digit. It is only a name or label without a value. #Example: my_function

# Write a program to create different variables to store various values.
# Write a program for print command.
# Write a program to print all the keywords.: import keyword -> print(keyword.kwlist)

My_Name="Vrishank"
My_School="DWPS, AJMER"
print("My Name: ",My_Name)
print("My School: ",My_School)
print("Keywords: ", keyword.kwlist)
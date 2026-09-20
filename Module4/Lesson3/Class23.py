# Topic : Dictionary
# Dictionary stores data as key-value pairs, in python we write dictionary with curly braces {}, and each pair looks like key:value.
# Example:
# student={
#     "name":"Aman",
#     "age": 12,
#     "course":"Python"
# }
# print(student)
# If we want to access a particular value, the following ways:
# print(student["name"])
## print(student["class"]) #It will throw an error.
# print(student.get("age"))
# print(student.keys())
# print(student.values())
# print(student.items())

# Add or Update an items:

# student["class"]=8
# print(student)
# student["name"]="Vrishu"
# print(student)

# Updating multiple items at a same time:

# student.update({"age":15,"course":"HTML"})
# print(student)

# Remove items from a Dictionary:

# Method 1 : pop(key):-
# student.pop("class")
# print(student)

# Method 2: popitem(): It removes the last item added
# student.popitem()
# print(student)

# Method 3: del: Removes a specific key:

# del student["class"]
# print(student)

# Method 4: clear(): It removes everything and leaves the dictionary empty.

# student.clear()
# print(student)

# Checking the length of the Dictionary:

# print(len(student))

# Iterating through the Dictionary:

# Iterate through the keys:

# for key in student:
#     print(key)
    
# Iterate through the keys and values:

# for key,value in student.items():
#     print(key," : ",value)

# Activity 1 : First, create a dictionary that consists of - id, name, class and subject integration of students. Then, write a program to retrieve unique entries and eliminate the rest.
ID1 = {"ID" : 211152,"NAME" : "VRISHANK","CLASS" : 7,"SUBJECT" : "MATH"}
ID2 = {"ID" : 211153,"NAME" : "KANGANA","CLASS" : 7,"SUBJECT" : "MATH"}
ID3 = {"ID" : 211154,"NAME" : "KRISHNA","CLASS" : 7,"SUBJECT" : "MATH"}
ID4 = {"ID" : 211155,"NAME" : "ABHISHEK","CLASS" : 7,"SUBJECT" : "MATH"}

# Activity 2 : Write a program to check the frequency of a value in a dictionary - {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}.
test_dict = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
print("The original dictionary : ",test_dict)
K = 2
res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1 
print("Frequency of 2 is : ",res)
# Activity 3 :Write a program to return the country code for various countries. Here’s a dictionary of different country codes - {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}.
country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}
print("Country code for India -")
print(country_code.get('India', 'Not Found'))

print("Country code for Austalia -")
print(country_code.get('Austalia', 'Not Found'))

print("Country code for Nepal -")
print(country_code.get('Nepal', 'Not Found'))


print("Country code for Japan -")
print(country_code.get('Japan', 'Not Found'))
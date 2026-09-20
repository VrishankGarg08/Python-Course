# Topic : Dictionary
# Dictionary stores data as key-value pairs, in python we write dictionary with curly braces {}, and each pair looks like key:value.
# Example:
student={
    "name":"Aman",
    "age": 12,
    "course":"Python"
}
print(student)
# If we want to access a particular value, the following ways:
# print(student["name"])
## print(student["class"]) #It will throw an error.
# print(student.get("age"))
# print(student.keys())
# print(student.values())
# print(student.items())

# Add or Update an items:

student["class"]=8
print(student)
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


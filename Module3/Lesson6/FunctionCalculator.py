# --- FUNCTIONS --------------------------------------------

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


# --- MAIN PROGRAM ------------------------------------------

print("=" * 36)
print("      🧮 FUNCTION CALCULATOR")
print("=" * 36)
print("Operations: add | subtract | multiply | divide")
print()

try:
    # Read two numbers from the user
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    # Read the operation from the user
    operation = input("Enter the operation: ").strip().lower()

    # Call the correct function
    if operation == "add":
        result = add(a, b)

    elif operation == "subtract":
        result = subtract(a, b)

    elif operation == "multiply":
        result = multiply(a, b)

    elif operation == "divide":
        try:
            result = divide(a, b)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
            result = None

    else:
        print("Error: Unknown operation.")
        result = None

    # Print result if a valid result was computed
    if result is not None:
        print("Result:", result)

except ValueError:
    print("Error: Please enter valid numbers.")
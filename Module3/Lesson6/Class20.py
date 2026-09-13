# Function Calculator
# Build a calculator that uses a separate function for each operation. The user picks an operation and enters two numbers. Your program handles invalid input and division by zero without crashing.

# What you need to use
# ------------------------------------------------------------------------
# 1.  def and return     →  define 4 functions: add, subtract, multiply, divide
# 2.  try/except         →  catch ZeroDivisionError and ValueError without crashing
# 3.  float(input())     →  to read numbers from the user
# 4.  return values      →  each function must return the correct result
# ------------------------------------------------------------------------

# What you'll be marked on
# ------------------------------------------------------------------------
# 1.  4 functions defined — add, subtract, multiply, divide        →  10 marks
# 2.  Each function returns the correct result for any two numbers →  10 marks
# 3.  ZeroDivisionError caught and prints a clear message          →  10 marks
# 4.  ValueError caught for non-number input                       →   5 marks
# 5.  Program runs without any errors                              →   5 marks
# ========================================================================
# Total  →  40 marks
# ========================================================================

# How to submit 🚀
# Push your completed code to a public GitHub repository and paste the
# repo link in the box below. Make sure your repo is public and your
# code runs correctly before submitting.

print("=======================================================================================================")
Operation = input("Enter Your Operation : ").upper()
try :
    a = int(input(f"Enter Your 1st Number For {Operation} : ")) 
    b = int(input(f"Enter Your 2nd Number For {Operation} : ")) 
except ValueError :
    print("Please Enter A Valid Positive Number")
except ZeroDivisionError :
    print("Please Don't Enter ZERO as Your Number")
if Operation == "ADD":
    def add(c,d) :
        return c + d
    print(add( a + b ))
elif Operation == "SUBTRACT":
    def subtract(c ,d) :
        return c  - d
    print(subtract( a  - b ))
elif Operation == "MULTIPLY" :
    def multiply(c ,d) :
        return c  * d
    print(multiply( a * b ))
elif Operation == "DIVIDE":
    def divide(c ,d) :
        return c  / d
    print(divide( a / b ))
    divide(a , b)
else :
    print("PLEASE ENTER VALID OPERATION FROM ADD, SUBTRACT , MULTIPLY, DIVIDE.")




################################################################################################################
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def proper_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid Input. Please enter a numeric value.")
def operation():
    """Keep asking until the user enters a valid number."""
    valid_ops={"+","-","*","/"}

    while True:
        op=input("Choose an operation (+,-,*,/): ").strip()
        if op in valid_ops:
            return op
        print("Invalid Operation.")
def calculator():
    print("=== Simple Calculator ===")
    op=operation()
    num1=proper_number("Enter the first number: ")
    num2=proper_number("Enter the second number: ")
    try:
        if op=="+":
            result= add(num1,num2)
        elif op=="-":
            result= subtract(num1,num2)
        elif op=="*":
            result= multiply(num1,num2)
        elif op=="/":
            result= divide(num1,num2)
        print(f"\nResult: {num1} {op} {num2} = {result}")
    except ZeroDivisionError:
        print("\n Error: Cannot divide by zero.")

calculator()

#Topic Python Challenges:
#Operator Precedence: The Hierarchy in which 2 Experation bind together by an operator.
#FULL FORM OF PEMDAS :
#P - BRACKETS 
#E - EXPONIATATION
#M - MULTIPLICATION
#D - DIVISION
#A - ADDITION
#S - SUBTRACTION

# print((1+1)**(5-2)/3)

#ACTIVITY 1:

# 1) Store values in `v`, `w`, `x`, `y`, and `z`.

# 2) Calculate the expression (v + w) * x / y and store the result back in `z`.

# 3) Print the value of `z` with a message.

# 4) Store a name in `name` and a number in `age`.

# 5) Check this condition using `or` and `and`:

# - The code checks if `name` is "Alex"

# OR (if `name` is "John" AND `age` is 2 or more).

# - If the condition is true, print the welcome message.

# - Otherwise, print the goodbye message.

V =7
W =18
X =45
Y =10
Z =77
A = 1
Z=(V + W) * X/Y
print(Z)
NAME = "JOHN"
AGE = 12
if NAME =="ALEX" or (NAME =="JOHN" and AGE >=2) :
    print("You're Welcome",NAME)
else :
    print("Have A Nice Day", NAME)

#ACTIVITY 2:

# 1) Ask the user to enter the numerator and store it in `numn`.

# 2) Ask the user to enter the denominator and store it in `numd`.

# 3) Check if `numn` is divisible by `numd`:

# - Find the remainder when `numn` is divided by `numd`.

# - If the remainder is 0, it means perfectly divisible.

# 4) If divisible, print that `numn` is divisible by `numd`.

# 5) Otherwise, print that `numn` is not divisible by `numd`.

NUMN = input("Enter the numerator : ")
NUMD = input("Enter the denominator : ")
if (NUMD / NUMN) == 0 :
    print("Numerator is divisible by denominator")
if (NUMD / NUMN) > 0 :
    print("Numerator is divisible by denominator")
#ACTIVITY 3:

# 1) Store the given values:

# `mean1`(wrong mean), `wrong_number`, `correct_number`, and `total_number`.

# 2) Calculate the total sum using the wrong mean:

# - Multiply `mean1` by `total_number`

# - Store it in `sum`

# - Print the sum.

# 3) Fix the sum to get the correct total:

# - Remove the wrong number (subtract `wrong_number`)

# - Add the correct number (add `correct_number`)

# - Store the corrected total in `num2`

# - Print the corrected sum.

# 4) Find the correct mean:

# - Divide `num2` by `total_number`

# - Store it in `mean2`

# - Print `mean2`.

mean1 = 7
wrong_number = 10
correct_number = 45
total_number = 18
wrong_mean = (mean1 + wrong_number + correct_number + total_number)
Sum = (mean1 * total_number)
print(Sum)

# Activity 4:

# 1) Take three integer inputs from the user and store them in `a`, `b`, and `c`.

# 2) Calculate the average of `a`, `b`, and `c`:
#    - Add them and divide by 3
#    - Store the result in `avg`
#    - Print `avg`

# 3) Compare `avg` with `a`, `b`, and `c` using if–elif:
#    - If `avg` is greater than all three numbers, print that it is higher than `a`, `b`, and `c`.
#    - Else if `avg` is greater than `a` and `b`, print that it is higher than `a` and `b`.
#    - Else if `avg` is greater than `a` and `c`, print that it is higher than `a` and `c`.
#    - Else if `avg` is greater than `b` and `c`, print that it is higher than `b` and `c`.
#    - Else if `avg` is greater than only `a`, print that it is just higher than `a`.
#    - Else if `avg` is greater than only `b`, print that it is just higher than `b`.
#    - Else if `avg` is greater than only `c`, print that it is just higher than `c`.

# 4) If none of the above conditions match, print "invalid input".
a=7
b=18
c=45
avg =((a+b+c)/3)
if a < avg and b < avg and c < avg :
    print("AVERAGE IS HINGER THAN", a , b , c)
elif  a < avg and b < avg :
    print("AVERAGE IS HINGER THAN", a , b)
elif a < avg and c < avg :
    print("AVERAGE IS HINGER THAN", a , c)
elif b < avg and c < avg :
    print("AVERAGE IS HINGER THAN", b , c)
elif a < avg :
    print("AVERAGE IS HINGER THAN", a)
elif b < avg :
    print("AVERAGE IS HINGER THAN", b)
elif c < avg :
    print("AVERAGE IS HINGER THAN", c)
else:
    print("invalid input")
# Student Grade Book
# Build a grade book that stores student names and scores in a dictionary. Your program calculates the class average, finds the top and bottom scorer, and lets the user look up any student's grade.

# What you need to use
# ------------------------------------------------------------------------
# 1.  dictionary      →  store at least 5 student name-score pairs
# 2.  for loop        →  to calculate the class average
# 3.  max() min()     →  to find the top and bottom scorer
# 4.  .get()          →  to look up a student by name
# 5.  input()         →  to let the user search for a student
# ------------------------------------------------------------------------

# What you'll be marked on
# ------------------------------------------------------------------------
# 1.  Dictionary created with at least 5 student name-score pairs  →   5 marks
# 2.  A loop correctly calculates and prints the class average      →  10 marks
# 3.  Highest and lowest scores and students identified             →  10 marks
# 4.  .get() used to look up student — friendly message if missing  →  10 marks
# 5.  Program runs without any errors                               →   5 marks
# ========================================================================
# Total  →  40 marks
# ========================================================================

A = {"Vrishank":99,"Ishaan":89,"Dhoni":100,"Ronaldo":98,"Sachin":95}
print(A)
for i in A :
    Average = (99+89+100+98+95)/(100*5)
print(Average)
B = max(A)
print("Maximum Marks :", B)
C = min(A)
print("Minimum Marks :", C)
try :
    Name = input("Enter the Name of Student you want to visit :")
    D= A.pop[Name]
    print(D)
except TypeError:
    print("Please Check the spelling of the person")
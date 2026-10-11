#  STUDENT GRADE BOOK
#  PART 1: the dictionary
#  YOUR CODE HERE
#  Make a dictionary called grades with five students.
#  Each key is a name and each value is a score.
#  PART 2: class average
#  YOUR CODE HERE
#  Make total = 0. Loop over grades and add each score to total.
#  Divide total by len(grades) and print the class average.
#  PART 3: highest score
#  YOUR CODE HERE
#  Make top_name = "" and top_score = 0.
#  Loop over grades. If a score is higher than top_score,
#  save that name in top_name and that score in top_score.
#  Print the highest scorer and the score.
#  PART 4: look up a student
#  YOUR CODE HERE
#  Ask for a student name with input().
#  Print the score with .get(). Use "Not found" if the name is not in grades.


Grades = {"Vrishank":100, "Ishaan":89, "Dhoni":80, "Ronaldo":98, "Sachin":95}
print(Grades)
Total = 0 
for name in Grades:
    Total = Total + Grades[name]
print(Total)
Average = Total / len(Grades)
top_name = ""
top_score = 0
score = 0
if Grades[name] > top_score :
    top_name = [name]
    top_score = Grades[name]
print("Highest Scorer :", top_name)
print("Highest Score :", top_score)
student_name = input("Enter student name: ")
print(Grades.get(student_name, "Not found"))
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
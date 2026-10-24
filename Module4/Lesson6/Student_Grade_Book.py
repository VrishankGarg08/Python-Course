Grades={"Vrishank":100,"Ishaan":89,"Dhoni":80,"Ronaldo":98,"Sachin":95}
print(Grades)
Total=0
for Name in Grades:
    Total=Total+Grades[Name]
print(Total)
Average=Total/len(Grades)
print("Class Average:",Average)
Top_Name=""
Top_Score=0
for Name in Grades:
    if Grades[Name]>Top_Score:
        Top_Name=Name
        Top_Score=Grades[Name]
print("Highest Scorer:",Top_Name)
print("Highest Score:",Top_Score)
Student_Name=input("Enter student name:")
print(Grades.get(Student_Name,"Not found"))
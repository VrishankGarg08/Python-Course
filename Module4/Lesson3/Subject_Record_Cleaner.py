# PART 1: Create a dictionary of student records
student_data = { "ID1": {"name": "Sara", "class": "V", "subject": "english, math, science"},
    "ID2": {"name": "David", "class": "V", "subject": "english, math, science"},
    "ID3": {"name": "Sara", "class": "V", "subject": "english, math, science"},
    "ID4": {"name": "Surya", "class": "V", "subject": "english, coding, math"}}
print("Original Student Records:")
print(student_data)
print("")
print("Details of ID1:")
print(student_data.get("ID1", "Not Found"))
print("")
print("Details of ID5:")
print(student_data.get("ID5", "Not Found"))
student_data["ID5"] = {"name": "Anaya", "class": "V", "subject": "english, art, science"}
print("")
print("After adding ID5:")
print(student_data)
student_data["ID2"]["subject"] = "english, math, coding"
print("")
print("After updating ID2 subject:")
print(student_data["ID2"])

cleaned_data = {}
seen_records = []
for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject"])
 
    if unique_key not in seen_records:
        seen_records.append(unique_key)
        cleaned_data[student_id] = details
student_data = cleaned_data
print("")
print("After removing duplicate records:")
print(student_data)
removed_student = student_data.pop("ID4", "Student not found")
print("")
print("Removed student:")
print(removed_student)
print("")
print("Total student records left:", len(student_data))
print("")
print("===== FINAL STUDENT SUBJECT RECORDS =====")
 
for student_id, details in student_data.items():
    print(student_id, ":", details)
 
print("==========================================")
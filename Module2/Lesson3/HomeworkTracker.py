
total_homework = 4
original_count = total_homework
print(f"You have {original_count} homework tasks to finish today!")
completed_count = 0
task_num = 1
while task_num <= total_homework:
    if task_num == 1:
        next_task = "Math worksheet"
    elif task_num == 2:
        next_task = "Science reading"
    elif task_num == 3:
        next_task = "English writing"
    else:
        next_task = "Coding practice"
 
    answer = input(f"Have you finished: {next_task}? (YES/NO): ").upper()
    if answer == "YES":
        completed_count += 1
        task_num += 1
        print("Great job! Homework task completed.")
    else:
        print("Okay, finish it and check again!")
    print("Homework tasks remaining:", total_homework - completed_count)
    print("")
print("= ALL HOMEWORK COMPLETE!=")
print("Great work finishing your homework !")
print("-------------------------------------------------------")
test_value = 0
safety_counter = 0
print("A real infinite loop will run forever but I am making it till 50 for now :")
while test_value <= 0 :
        safety_counter += 1
        print(safety_counter)
        if safety_counter == 50 :
             print("Target reached")
             break
print("== HOMEWORK COMPLETION SUMMARY ==")
print("Homework Assigned Today:", original_count)
print("Homework Completed:", completed_count)
print("Homework Remaining:", total_homework - completed_count)

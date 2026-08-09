#TOPIC : WHILE LOOPS
#Types of Loops:
#2nd While Loop: It is a loop that keeps repeating its block of code for as long as the condision stays true without knowing in advance exactly how many times it will run.It stops when the condition is false.
#Syntax for while loop:
# while condition :
#     statement/block of code
#Example:
# I = 1
# while I <= 16 :
#     print(I)
#     I += 1
#Example :
I = 15
N = 1
while N<=10:
    print(I * N)
    N += 1
#ACTIVITY :
#A Task Checklist Countdown that asks about each Task one at a time, uses a while loop to keep checking until the entire list is empty, and prints a final summary of every Task completed today.
#STEPS :
# HOW IT WORKS
# Step 1: Set total_Tasks to 4, store it as original_count, and print how many Tasks are on today's
# list
# Step 2: Set up a completed_count counter starting at 0 and a Task_num counter starting at 1.
# Step 3: Start a while loop that keeps running as long as Task_num is less than or equal to
# total_Tasks.
# Step 4: Inside the loop, work out the current Task's name from Task_num, then ask if it has
# been finished.
# Step 5: If the answer is yes, increase completed_count and Task_num by 1; otherwise, print a
# message and let the loop ask about the same Task again.
# Step 6: Once the while loop ends, print the completion message, then safely demonstrate an
# infinite loop's condition, using a break to stop it after 3 rounds.
# Step 7: Print the final Task checklist summary showing Tasks assigned, completed, and
# remaining.
Total_Task = 4
Origanal_Count = Total_Task
print(Origanal_Count)
Completed_Count= 0
Task_Num = 1
while Task_Num <= Total_Task :
    if Task_Num == 1:
        Task_Name = "Cleaning"
        Task =input("Is Cleaning Finished? ( YES / NO )  :").upper
        if Task=="YES":
            print("Let's Move to next Task.")
            Completed_Count = Completed_Count+1
            Task_Num = Task_Num+1
        else :
            print("Complete the Cleaning of your Place")
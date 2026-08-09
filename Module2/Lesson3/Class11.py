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
# My Chore Checklist Countdown

# PART 1: Set today's total number of chores (no list needed)
total_chores = 4
original_count = total_chores
print(f"You have {original_count} chores to finish today!\n")

# PART 2: Keep a counter for completed chores and the current chore number
completed_count = 0
chore_num = 1

# PART 3: Repeat while there are still chores left to check off
while chore_num <= total_chores:

    # PART 4: Work out the current chore's name from its number
    if chore_num == 1: next_chore = "Make your bed"
    elif chore_num == 2: next_chore = "Feed the pet"
    elif chore_num == 3: next_chore = "Take out the trash"
    else: next_chore = "Wash the dishes"

    answer = input(f"Have you finished: {next_chore}? (yes/no): ")

    # PART 5: Only move on to the next chore once it is marked done
    if answer == "yes":
        completed_count += 1
        chore_num += 1
        print("Great job! Chore completed.")
    else:
        print("Okay, finish it and check again!")

    # PART 6: Print how many chores remain after each check
    print("Chores remaining:", total_chores - completed_count)
    print()

# PART 7: This only prints once every chore is marked done
print("===== ALL CHORES COMPLETE! =====")
print("Great work finishing your entire checklist today!\n")

# PART 8: A safe look at what an infinite loop would look like
print("Now let's safely peek at an infinite loop...")
test_value = 0
safety_counter = 0
while test_value <= 0:
    print("This condition never changes, so this would run forever!")
    safety_counter += 1
    if safety_counter == 3:
        print("(Stopping here on purpose - a real infinite loop never stops on its own!)")
        break

# PART 9: Print the final chore checklist summary
print("\n===== CHORE CHECKLIST SUMMARY =====")
print("Chores Assigned Today:", original_count)
print("Chores Completed:", completed_count)
print("Chores Remaining:", total_chores - completed_count)
print("======================================")
Habit = "Cycling and Coding"
weekly_habits = (1, 0, 1, 1, 0, 1, 1)
print(weekly_habits)
print("Total days tracked:", len(weekly_habits))
print("Day 1 status:", weekly_habits[0])
print("Day 4 status:", weekly_habits[3])
first_three_days = weekly_habits[0:3]
print("First three days:", first_three_days)
weekend_days = weekly_habits[5:7]
print("Weekend days:", weekend_days)

weekly_habits = weekly_habits + (1,)
print("After adding eight day:", weekly_habits)

completed_days = weekly_habits.count(1)
missed_days = weekly_habits.count(0)
 
print("Completed days in which habits are performed:", completed_days)
print("Missed days in which habits are not performed:", missed_days)
done = 0
not_done = 0
for i in range(0, len(weekly_habits)):
    if weekly_habits[i] == 1:
        done += 1
    else:
        not_done += 1
if done > not_done:
    print("Great! habits are progress of building.")
else:
    print("Try to be more consistent with your habits..")
print("")
print("===== WEEKLY HABIT TRACKER =====")
print("Habit to be Perfromed :", Habit)
print("Weekly Record:", weekly_habits)
print("Completed:", done)
print("Missed:", not_done)
print("================================")

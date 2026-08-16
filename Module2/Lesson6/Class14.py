# Number Guessing Game
# Build a game where the computer picks a secret number between 1 and 50. You have 5 attempts to guess it. After every wrong guess your program shows a hint telling you how close you are. Remaining lives are shown as hearts after each attempt.

# 💡 Hint: Store your secret number in a variable — for example: secret = 27



# If you already know the random module, feel free to use it! This test checks your logic (conditions, loops, input/output).


# What you need to use
# ------------------------------------------------------------------------
# 1.  int(input())       →  to read the player's guess
# 2.  while loop         →  stops after 5 attempts or when player wins
# 3.  if/elif/else       →  hint system —

# 🧊 ice cold, 🥶 cold, 🌡️ warm, or 🔥 hot


# 4.  for loop           →  shows 

# remaining ❤️ hearts

#  after each wrong guess
# 5.  win/loss message   →  reveals the secret number if attempts run out
# ------------------------------------------------------------------------

# What you'll be marked on
# ------------------------------------------------------------------------
# 1.  Program runs without any errors                          →   5 marks
# 2.  int(input()) used to read the player's guess             →   5 marks
# 3.  while loop stops after 5 attempts or on correct guess    →  10 marks
# 4.  Hint system prints ice cold / cold / warm / hot          →  10 marks
# 5.  for loop shows correct hearts after each wrong guess     →   5 marks
# 6.  Win message shown / secret revealed if attempts run out  →   5 marks
# ========================================================================
# Total  →  40 marks
# ========================================================================

# How to submit 🚀
# Push your completed code to a public GitHub repository and paste the
# repo link in the box below. Make sure your repo is public and your
# code runs correctly before submitting.



print("WELCOME ! TO NUMBER GUESSING GAME ")
print("ice cold Region = Differnce more than 10 ")
print("cold =less than or equal to 10 ")
print("warm = less than or equal to 5 ")
print("hot = less than or equal to 2 ")
Secret_No = 34
Guess = int(input("Enter Your First Guess :"))
if Guess == Secret_No :
    print("You Won It on the First Try !!")
elif Guess > 44 or Guess < 24 :
    print("Hint : Your in Ice Cold Region.")
elif Guess <= 44 and Guess > 39:
    print("Hint : Your in Cold Region.")
elif Guess <= 39 :
    print("Hint : Your in Warm Region.")
elif Guess < 36 or Guess > 32 :
    print("Hint : Your in Hot Region.")
Guess = int(input("Enter Your Second Guess :"))
if Guess == Secret_No :
    print("You Won It on the First Try !!")
elif Guess > 44 or Guess < 24 :
    print("Hint : Your in Ice Cold Region.")
elif Guess <= 44 and Guess > 39:
    print("Hint : Your in Cold Region.")
elif Guess <= 39 :
    print("Hint : Your in Warm Region.")
elif Guess < 36 or Guess > 32 :
    print("Hint : Your in Hot Region.")
Guess = int(input("Enter Your Third Guess :"))
if Guess == Secret_No :
    print("You Won !!")
elif Guess > 44 or Guess < 24 :
    print("Hint : Your in Ice Cold Region.")
elif Guess <= 44 and Guess > 39:
    print("Hint : Your in Cold Region.")
elif Guess <= 39 :
    print("Hint : Your in Warm Region.")
elif Guess < 36 or Guess > 32 :
    print("Hint : Your in Hot Region.")
Guess = int(input("Enter Your Fourth Guess :"))
if Guess == Secret_No :
    print("You Won !!")
elif Guess > 44 or Guess < 24 :
    print("Hint : Your in Ice Cold Region.")
elif Guess <= 44 and Guess > 39:
    print("Hint : Your in Cold Region.")
elif Guess <= 39 :
    print("Hint : Your in Warm Region.")
elif Guess < 36 or Guess > 32 :
    print("Hint : Your in Hot Region.")
    Guess = int(input("Enter Your Fifth Guess :"))
if Guess == Secret_No :
    print("You Won !!")
elif Guess > 44 or Guess < 24 :
    print("Hint : Your in Ice Cold Region.")
elif Guess <= 44 and Guess > 39:
    print("Hint : Your in Cold Region.")
elif Guess <= 39 :
    print("Hint : Your in Warm Region.")
elif Guess < 36 or Guess > 32 :
    print("Hint : Your in Hot Region.")
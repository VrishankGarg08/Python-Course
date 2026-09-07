# TOPIC : RANDOM & MATH MODULE
# Random Moudule
# Random Module is a built in python tool kit that generates random number.
# Printing Random Number
# import random
# N = random.randint(1,99)
# print(N)
# Math Module 
# Math Module is a built in python tool kit which is like scientific CALCULATOR.
# HCF AND GCD ARE SAME............
# import math
# print(math.ceil(4.8) )#CEILING = UPSIDE = ROUNDS THE NO. UP
# print(math.floor(6.9))#FLOOR = DOWNSIDE = ROUNDS THE NO. DOWN
# print(math.fabs(-5) )# IT IS LIKE ABSULUTE VALUE -5 WILL GIVE 5 # Floating absulute Value 
# # print(math.copysign()) # X = SIZE AND Y = SIGN OF INTEGAR.
# print(math.copysign(4,-1)) # X = SIZE AND Y = SIGN OF INTEGAR 
# print(math.gcd(10,20,30,40,50))# Work The Same as HCF # IT REQUIRES ATLEAST 2 VALUSE

# Activity 1: Number game

# WHAT YOU WILL BUILD
# You build a number-guessing game where the computer picks a secret digit and you keep guessing until you get
# it right

# HOW IT WORKS
# Step 1: Import the random module.
# Step 2: Set a variable playing to True to control the game loop.
# Step 3: Generate a secret number between 0 and 9 using random.randint(0, 9), converting it to a string.
# Step 4: Print instructions explaining the guessing game to the player.
# Step 5: Start a while playing loop that keeps asking for a guess.
# Step 6: If the guess matches the secret number, print a winning message showing the number, then break out of
# the loop.
# Step 7: Otherwise, print a message asking the player to try again, and the loop continues.
import random
Guess = random.randint(1,200)
Num = int(input("Enter A Number Between 1 and 200: "))
while True:
  if Guess > Num:
    print("Your Guess Is Smaller ")
    Num = int(input("Enter A Number: "))
  elif Guess < Num:
    print("Your Guess Is Larger")
    Num = int(input("Enter A Number: "))
  else:
    print("Your guess Is Perfect")
    break

# Activity 2: Rock paper scissors

# WHAT YOU WILL BUILD
# You build a rock-paper-scissors game where the computer picks its move using a random number, and you play
# round after round until you choose to stop.

# HOW IT WORKS
# Step 1: Import the random module.
# Step 2: Start a while True loop so the game can repeat for multiple rounds.
# Step 3: Ask the player for their choice - rock, paper, or scissors.
# Step 4: Generate a random number from 1 to 3 using random.randint(1, 3).
# Step 5: Use if/elif to turn that number into the computer's move: 1 becomes rock, 2 becomes paper, and
# anything else becomes scissors.
# Step 6: Print both the player's and computer's choices using an f-string.
# Step 7: Compare the two choices with if/elif to decide whether it's a tie, a win, or a loss, printing the result.
# Step 8: Ask if the player wants to play again, and break out of the loop if the answer isn't "y".
import random
Valid = True
Score = 0
while Valid:
  Choice = input("Enter You Choice (ROCK/PAPER/SCISSOR) : ").upper()
  if Choice not in ["ROCK","PAPER","SCISSOR"]:
    print("Please Enter Valid Choice")
  Guessing = random.randint(1,3)
  if Guessing == 1 :
    Guess = "ROCK"
  elif Guessing ==2 :
    Guess = "PAPER"
  elif Guessing == 3 :
    Guess = "SCISSOR"
  print(f"Computer's Choice : {Guess} and Your Choice : {Choice}")
  if Guess == "ROCK" and Choice == "SCISSOR" or Guess == "PAPER" and Choice == "ROCK" or Guess == "SCISSOR" and Choice == "PAPER":
    print("Better Luck Next Time!")
    print("Your Total Score ",Score)
    More = int(input("If You Want To Play 1 More Round Type 1 OTHERWISE Type 2 : "))
    if More == int(1) :
      Valid = True
    elif More == int(2):
      Valid = False
    else :
      Again = False
      while not Again :
          try :
              N = int(input("Enter A Number : "))
              Again = True
          except ValueError :
              print(" Your Number WAS NOT Valid.")
  elif Guess == "ROCK" and Choice == "PAPER" or Guess == "PAPER" and Choice == "SCISSOR" or Guess == "SCISSOR" and Choice == "ROCK" :
    print("You Won This Round!")
    Score += 1
    print("Your Score After This Round", Score)
  elif Guess == Choice :
    print("Guess Are Same..")
    print("No Point Will Be Added.")
  
# Activity 3: Mathematical operations
# WHAT YOU WILL BUILD
# You use five different math module functions to round, find absolute values, copy a sign, and calculate a
# greatest common divisor.
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

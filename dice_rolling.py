import random

while True:
# Ask roll the dice
    answer = input("Roll the dice? (y/n): ").lower()

    if answer == "y":
      die = random.randint(1, 6)
      print(f"Your dice roll is: {die}")
    elif answer == "n":
      print("Thank you for playing!")
      break
    else:
      print("Invalid input. Please try again.")

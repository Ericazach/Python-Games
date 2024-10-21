import random

while True:
# Ask roll the dice
    answer = input("Roll the dice? (y/n): ").lower()

    if answer == "y":
      print(random.randint(1, 6))
    elif answer == "n":
      print("Thank you for playing!")
      break
    else:
      print("Invalid input. Please try again.")

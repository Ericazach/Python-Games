import random 

guessed_number = random.randint(1, 100)

while True:
  try:
    guess = int(input("Guess a number between 1 and 100: "))
    if(guess > guessed_number):
      print("Your guess is too high.")
    elif(guess < guessed_number):
      print("Your guess is too low.")
    else:
      print("Congratulations! You guessed the number.")
      break
  except ValueError:
    print("Invalid input. Please enter a number.")
    
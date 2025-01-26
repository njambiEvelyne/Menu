import random

guess_times = 0
guess_limit = 3
right_guess = random.randint(1, 10)

while guess_times < guess_limit:
  num = int(input("Enter the number: "))
  if num == right_guess:
    print("You win")
    break

  else: 
    print("Oops! Try again.")
    guess_times += 1

if guess_times == guess_limit:
  print(f"Sorry, you've used all the guesses. The number was {right_guess}.")

else:
  print("Thank you for playing.")
  
 

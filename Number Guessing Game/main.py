import random

def main():
  # Set the initial values
  lower_bound = 1
  upper_bound = 100
  target = random.randint(lower_bound, upper_bound)
  num_guesses = 0
  
  print("I'm thinking of a number between {} and {}. Can you guess what it is?".format(lower_bound, upper_bound))
  
  # Start the loop
  while True:
    # Get the player's guess
    guess = input("Your guess: ")
    
    # Check if the input is valid
    if not guess.isdigit():
      print("Please enter a valid number!")
      continue
    guess = int(guess)
    
    # Check if the guess is within bounds
    if guess < lower_bound or guess > upper_bound:
      print("Please enter a number between {} and {}!".format(lower_bound, upper_bound))
      continue
    
    # Increment the number of guesses
    num_guesses += 1
    
    # Check if the guess is correct
    if guess == target:
      print("Congratulations! You guessed the correct number in {} guesses!".format(num_guesses))
      break
    elif guess < target:
      print("Your guess is too low. Try again!")
    else:
      print("Your guess is too high. Try again!")
      
# Start the game
main()

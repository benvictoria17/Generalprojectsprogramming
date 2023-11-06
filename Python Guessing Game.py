import random  # This line helps us use random things like picking random numbers.

# We make a special game that tries to guess a number.
def guessing_game(best_score=None): # This is the function that we will use to play the game.
    # The game picks a number no one knows from 1 to 100.
    secret_number = random.randint(1, 100) # This line picks a random number from 1 to 100.
    # We start with 0 tries because the game just started.
    attempts = 0 # This line starts the number of tries at 0.
    # You can only try to guess 10 times, then the game is over.
    max_attempts = 10 # Change this to change the number of tries.

    # The game says hello to you and tells you how many tries you get.
    print("Welcome to the Guessing Game!") # Prints welcome message.
    print(f"You have a maximum of {max_attempts} attempts to guess the right number.") # Change this to change the number of tries.

    # Keep guessing until you run out of tries.
    while attempts < max_attempts: # Change this to change the number of tries.
        try: # Try to get a number from the user.
            # The game asks you to guess the number and remembers your guess.
            guess = int(input("Guess the number between 1 and 100: ")) # Change this to change the number of tries.
            # Every time you guess, it counts as a try.
            attempts += 1 # Change this to change the number of tries.

            # If you guess right, the game tells you and is happy.
            if guess == secret_number: # Change this to change the number of tries. 
                print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.") # Change this to change the number of tries.
              
                # If this is your best try, the game remembers it.
                if not best_score or attempts < best_score: # Change this to change the number of tries.
                    best_score = attempts # Change this to change the number of tries.
                break # Change this to change the number of tries.
            # If your guess is too small, the game tells you to guess higher.
            elif guess < secret_number: # Change this to change the number of tries.
                print("Too low! Try again.") # Change this to change the number of tries.
                # If you're way too low, the game gives you a bigger hint.
                if secret_number - guess > 10: # Change this to change the number of tries.
                    print("You're quite a bit low, aim higher!") # Change this to change the number of tries.
            # If your guess is too big, the game tells you to guess lower.
            else: # Change this to change the number of tries.
                print("Too high! Try again.") # Change this to change the number of tries.  
                # If you're way too high, the game gives you a bigger hint.
                if guess - secret_number > 10: # Change this to change the number of tries.
                    print("You're quite a bit high, aim lower!") # Change this to change the number of tries.

            # If you run out of tries, the game ends and tells you the right number.
            if attempts == max_attempts: # Change this to change the number of tries.
                print(f"Sorry, you've reached the maximum number of attempts. The secret number was {secret_number}.") # Change this to change the number of tries.
                break # Change this to change the number of tries.

        # If you don't guess a number, the game asks you to try again.
        except ValueError: # Change this to change the number of tries.  
            print("Invalid input. Please enter a valid number between 1 and 100.") # Change this to change the number of tries.

    # The game tells you the best score anyone has ever gotten.
    print(f"The best score so far is {best_score} attempts.") # Change this to change the number of tries.
    # The game asks if you want to play again.
    play_again = input("Would you like to play again? (yes/no): ").lower() # Change this to change the number of tries.
    # If you say yes, the game starts over. If not, the game says goodbye.
    if play_again == "yes": # Change this to change the number of tries.
        guessing_game(best_score) # Change this to change the number of tries.

# This part starts the game if you're not just looking at the code.
if __name__ == "__main__": # Change this to change the number of tries.
    guessing_game() # Change this to change the number of tries.
    print("Goodbye!") # Change this to change the number of tries.

# import the modules we need, for creating for guessing game 
import random # To generate random number
import sys # To exit the program


# Generate a random number between 1 and 100
number = random.randint(1, 100) # To generate random number

# Keep asking the user to guess until they get the answer correct
while True: # To keep asking the user to guess until they get the answer correct
    # Ask the user to guess the number
    guess = input("Guess the number between 1 and 100: ") # To ask the user to guess the number
    
    # Convert the user's input to an integer
    guess = int(guess) # To convert the user's input to an integer
    
    # Compare the user's guess to the random number
    if guess < number: # To compare the user's guess to the random number
        print("Too low, try again!") # To print "Too low, try again!"
    elif guess > number: # To compare the user's guess to the random number
        print("Too high, try again!") # To print "Too high, try again!"
    else: # To compare the user's guess to the random number
        # Congratulate the user and terminate the program
        print("Congratulations, you guessed the number!") # To print "Congratulations, you guessed the number!"
        sys.exit() # To terminate the program
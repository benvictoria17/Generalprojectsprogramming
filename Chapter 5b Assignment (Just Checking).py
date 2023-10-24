# For this assignment, I would like you to take your adding game and add a feature that asks the user if they want another addition question.  This should use a recursive function call in order to ask another question (so that means your addition question asking must be part of a function).

# Take your time as this can be confusing the first time (and we are going to look at a way better way in chapter 7) - don't forget that you can look at the solution if you are totally stuck or ask Mr. Laird for help.

# Program should look something like this:

# Welcome to the Adding Game

# What is 9 + 32: 41
# Yeah! You got it correct

# Would you like another question (y/n)?: y

# What is 10 + 2: 12
# Yeah! You got it correct

# Would you like another question (y/n)?: n

# Okay.... bye!



# Importing the random Module
# We begin by telling the computer to use a special toolbox called "random" that helps us generate random numbers.

# Starting a Loop for the Game:
# We use a loop that keeps going until we decide to stop. 

# Generating Random Numbers:
# In the game, we think of two secret numbers between 1 and 100. We don't tell you what they are; they're our secret.

# Calculating the Correct Answer:
# We add these two secret numbers together to find the correct answer. 

# Asking for Your Answer:
# We ask you, "What is [number] + [number]?" You have to guess the answer and type it in.

# Checking if You're Correct
# We check if your answer is right. If it's correct, we say "Yeah! You got it correct." If not, we tell you the correct answer.

# Asking if You Want to Play Again
#  After each question, we ask if you want to play another round (y for yes, n for no). You decide if you want to continue.

# Exiting the Game
# If you don't want to play anymore (you type 'n' for no), we say "Okay... bye!" and the game ends. If you say 'y' for yes, we start a new question.

# This is how we bring in the random module, which has functions to help generate random numbers.
import random

# Display a welcome message
print("Welcome to the Adding Game")

# This is a loop that keps going until the user says 'n'. At that moment we call 'break' to get out of the loop.
while True:
    # Generate two random numbers for the addition problem. The numbers are integers from 1 to 100.
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    # Prompt the user for the answer
    answer = int(input(f"What is {num1} + {num2}: "))

    # Check if the user's answer is correct. It compares answer to num1 + num2.
    if answer == num1 + num2:
        print("Yeah! You got it correct")
    else:
        print(f"Oops! The correct answer was {num1 + num2}.")

    # Ask if the user wants another question
    another = input("Would you like another question (y/n)?: ").lower()

    # If the user doesn't want another question, exit the loop
    if another != 'y':
        break

# Display a farewell message
print("Okay.... bye!")
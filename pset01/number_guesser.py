# ----------------------------------------------------------------------
# This is the file number_guesser.py

# The intent is to give you practice writing a complete, interactive
# Python program.

# Remove the comments in this file when you have completed your program.
# You can, and should, include your own comments, but please remove the
# comments that are here now.
# ----------------------------------------------------------------------

# Things to do:

import random

def guessing_game():
    print("Guess number between 1 and 100")
    print("type 'bye' or 'exit' to quit the program")

while True: 
    number = random.randint(1,101)

    while True:
        guess = input("enter number:").strip()

        if guess is not a digit():
            print("Please enter a vali number")

        guess_number = int(guess)

        if guess_number < number: 
            print("Too low!")
        
        elif guess_number > number
             print("Too high!")

        if correct guess_number
            print("Congratulations! You guessed the number!")

    

# Ask the user to guess the number. In your prompt, let the user know they
# can type 'bye' or 'exit' to quit the program.
#
# If their guess is not made up entirely of digits, print "Please enter a valid
# number" and ask them to guess again.
#
# If the guess is too high, print "Too high!" and continue asking.
#
# If the guess is too low, print "Too low!" and continue asking.
#
# If the guess is correct, print "Congratulations! You guessed the number!" along
# with the number of attempts it took to guess the number. Start over with a new
# random number. Make sure to zero out the number of attempts.

# Please note: There are likely to be a number of Python guessing games online,
# and most GenAI systems can probably write this for you. Don’t rely on them,
# as they rob you of a chance to practice your Python skills and they might not
# even be correct. Perhaps, worse, they might not follow the instructions
# exactly as given.
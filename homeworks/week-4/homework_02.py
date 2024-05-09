"""
Let's implement the Hangman game in Python, where the player guesses letters to uncover a hidden word.
For each incorrect guess, a part of the hangman will be drawn.

There is a problem with logic of this game. After resolve all TODOs, you can check that, currently, the loop continues
until the number of attempts is less than the maximum number of attempts. However, we need to add a condition to check
if the player has not lost the game, i.e., if the hangman has not been fully drawn. If the hangman is fully drawn,
the game should end regardless of the number of attempts left. Can you fix it?
"""
import random


def draw_hangman(errors):
    """ Each part of the hangman """

    stages = [
        '''
           ____
          |    |
               |
               |
               |
               |
         ______|_
        |        |
        |________|
        ''',
        '''
           ____
          |    |
          O    |
               |
               |
               |
         ______|_
        |        |
        |________|
        ''',
        '''
           ____
          |    |
          O    |
          |    |
               |
               |
         ______|_
        |        |
        |________|
        ''',
        '''
           ____
          |    |
          O    |
         /|    |
               |
               |
         ______|_
        |        |
        |________|
        ''',
        # From below and others, for the left arm and left leg, the first slash "\" is used as an escape character
        '''
           ____
          |    |
          O    |
         /|\\   |
               |
               |
         ______|_
        |        |
        |________|
        ''',
        '''
           ____
          |    |
          O    |
         /|\\   |
         /     |
               |
         ______|_
        |        |
        |________|
        ''',
        '''
           ____
          |    |
          O    |
         /|\\   |
         / \\   |
               |
         ______|_
        |        |
        |________|
        '''
    ]
    errors = min(errors, len(stages) - 1)
    return stages[errors]


def the_hangman_game():
    words = ['apple', 'banana', 'peach', 'coconut', 'water'] # ToDo: Define the list of words for the game. At least 5 single words

    secret_word = random.choice(words)
    # ToDo: Pick a random word from the list. Hint: random.choice()

    # Initialize guessed word to display blanks
    guessed_word = "_" * len(secret_word)

    # Convert the guessed word to a list for easier manipulation
    guessed_word_list = list(guessed_word)

    # Initialize list to keep track of guessed letters
    guessed_letters = []

    # Number of incorrect guesses allowed
    max_attempts = len(draw_hangman(0)) - 1
    attempts = 0

    # Display initial message
    print("Welcome to the Hangman!")
    print("Try to guess the word by guessing one letter at a time.")

    # Change all the 'YOUR_CONDITION_HERE' below for...
    # ToDo: Loop until the player guesses the word or runs out of attempts
    while (''.join(guessed_word_list) != secret_word) and (attempts < max_attempts) :
        print(draw_hangman(attempts))
        print(" ".join(guessed_word_list))  # Display the current state of the guessed word
        print("Guessed letters:", " ".join(guessed_letters))
        guess = input('Write a letter you guess is in: ') # ToDo: Prompt the player to guess a letter

        # ToDo: Validate what the user entered
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        # ToDo: Check if the guessed letter has already been guessed
        if guess in guessed_word_list:
            print("You've already guessed that letter. Try another one.")
            continue

        guessed_letters.append(guess)  # Add guessed letter to list of guessed letters

        # ToDo: Check if the guessed letter is in the secret word
        if guess in secret_word:
            print("Correct guess!")
            # Update the guessed word with the correctly guessed letter
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed_word_list[i] = guess
        else:
            print("Incorrect guess.")
            print(attempts, max_attempts)
            attempts += 1

        # ToDo: Check if the player has guessed the entire word
        if ''.join(guessed_word_list) == secret_word:
            print("Congratulations! You've guessed the word!")
            print("The word was:", secret_word)
            break

    # ToDo: If the player runs out of attempts
    if attempts >= max_attempts:
        print(draw_hangman(attempts))
        print("Sorry, you've run out of attempts!")
        print("The word was:", secret_word)

# ToDo:

the_hangman_game()

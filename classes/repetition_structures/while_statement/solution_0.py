import random

number_to_find = 56
number_guessed = None  # None represents nothing or an empty value
while number_to_find != number_guessed:
    number_guessed = random.randint(0, 101)
    print(f"The number guessed is: {number_guessed}")

print(f"Congrats, that's the correct number: {number_guessed}")


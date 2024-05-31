"""
Let's develop a simple rock, paper, scissors game against the computer.
The output will look like this:

ROCK, PAPER, SCISSORS
0 Wins, 0 Losses, 0 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
p
PAPER versus...
PAPER
It is a tie!
0 Wins, 1 Losses, 1 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
s
SCISSORS versus...
PAPER
You win!
1 Wins, 1 Losses, 1 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
q
"""
import random
import sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

# The main game loop.
while True:
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')

    # The player input loop.
    while True:
        playerMove = input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit: ')
        if playerMove == 'q':
        # ToDo: Quit the program
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
 # ToDo: Break out of the player input loop
        print('Type one of r, p, s, or q.')

    # Display what the player chose:
    if playerMove == 'r':
        # ToDo: Show 'ROCK versus...'
    elif playerMove == 'p':
        # ToDo: Show 'PAPER versus...'
    elif playerMove == 's':
        # ToDO: Show 'SCISSORS versus...'

    # ToDo: Display the computer's choice. Let's use 1 for (r)ock, 2 for (p)aper and 3 for (s)cissors. Tip: Use random.randint
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # ToDo: Calculate, display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')

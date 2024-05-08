"""
In this game, we'll create a number pyramid where each row contains increasing numbers. E.g.: If user types 5, the game
prints:

Number Pyramid:
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
"""


def number_pyramid(rows):
    print("Number Pyramid:")
    for i in range(1, rows + 1):
        # ToDo: Print spaces to center-align the pyramid
        print(" " * (rows - i), end="")
        # ToDo: Print numbers in increasing order
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


# ToDo: Ask user to type a number
number = int(input("Enter the number: "))
number_pyramid(number)

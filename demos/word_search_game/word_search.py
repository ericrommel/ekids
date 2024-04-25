import random


def generate_grid(words, size):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    grid = [[' ' for _ in range(size)] for _ in range(size)]

    # Place words horizontally or vertically
    for word in words:
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            row = random.randint(0, size - 1)
            col = random.randint(0, size - len(word))
            for i, letter in enumerate(word):
                grid[row][col + i] = letter
        else:
            row = random.randint(0, size - len(word))
            col = random.randint(0, size - 1)
            for i, letter in enumerate(word):
                grid[row + i][col] = letter

    # Fill the remaining spaces with random letters
    for row in range(size):
        for col in range(size):
            if grid[row][col] == ' ':
                grid[row][col] = random.choice(letters)

    return grid


def display_grid(grid):
    for row in grid:
        print(" ".join(row))


def find_word(grid, word):
    size = len(grid)
    # Check horizontally
    for row in grid:
        if word in "".join(row):
            return True

    # Check vertically
    for col in range(size):
        if word in "".join(grid[row][col] for row in range(size)):
            return True

    # Check diagonally (top-left to bottom-right)
    for row in range(size):
        for col in range(size):
            if word in "".join(grid[row + i][col + i] for i in range(len(word)) if row + i < size and col + i < size):
                return True

    # Check diagonally (top-right to bottom-left)
    for row in range(size):
        for col in range(size):
            if word in "".join(grid[row + i][col - i] for i in range(len(word)) if row + i < size and col - i >= 0):
                return True

    return False


def word_search(words, size):
    grid = generate_grid(words, size)
    display_grid(grid)

    print("\nWords to find:")
    for word in words:
        print(word)

    found_words = []
    while words:
        guess = input("Enter a word: ").strip().upper()
        if guess in words:
            print("You found:", guess)
            found_words.append(guess)
            words.remove(guess)
        else:
            print("Sorry, that word is not in the list.")

        if not words:
            print("Congratulations! You've found all the words!")
            break


# Example usage
print("Word Search:")
word_search(["PYTHON", "JAVA", "C", "HTML", "CSS"], 10)

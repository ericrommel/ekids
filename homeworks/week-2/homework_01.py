# Make a program that asks for two integers and prints out the sum of those two numbers.
def sum_numbers(n, m):
    # ToDo: write your code here
    print(f'\n\n{'-'*50}\nThe answer is: {n + m}')


if __name__ == '__main__':
    # ToDo: Ask user to provide the values and store them in variables.
    first_number = int(input('Type the first number to sum\t'))
    second_number = int(input('Type the second number\t'))
    sum_numbers(first_number, second_number)

# Make a program that asks for two integers and prints out the sum of those two numbers.
def sum_numbers(n, m):
    # ToDo: write your code here
    j = n + m
    print(j)

if __name__ == '__main__':
    # ToDo: Ask user to provide the values and store them in variables.
    first_number = int(input("Add first number"))
    second_number = int(input("Add second number"))
    sum_numbers(first_number, second_number)
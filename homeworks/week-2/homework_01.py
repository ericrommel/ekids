# Make a program that asks for two integers and prints out the sum of those two numbers.
def sum_numbers(n,m):
    j = n + m
    print(j)
    # ToDo: Ask user to provide the values and store them in variables.


if __name__ == '__main__':
    # ToDo: Ask user to provide the values and store them in variables.

    #Getting my values
    first_number = int(input("Add first number and press enter : "))
    second_number = int(input("Add second number and press enter : "))

    #Calling my functions
    sum_numbers(first_number, second_number)
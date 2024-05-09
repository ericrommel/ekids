def number_pyramid(rows):
    print("Number Pyramid:")
    max_width = len(str(rows))

    for i in range(1, rows + 1):
        spaces = ' ' * ((rows - i) * max_width)# ToDo: Print spaces to center-align the pyramid
        print(spaces, end=' ')
        # ToDo: Print numbers in increasing order
        for j in range(1, i + 1):
            print(f'{j:>{max_width}}', end='  ')

number = int(input('Enter a number please: '))# ToDo: Ask user to type a number
number_pyramid(number)
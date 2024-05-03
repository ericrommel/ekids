# Write a program that reads a value in meters and shows it converted into millimeters
def meters_to_millimeters(n):
    # ToDo: write your code here
    print(f'\n\n{'-'*50}\nYour value in millimeters is: {n*1000}mm')


if __name__ == '__main__':
    # ToDo: Ask user to provide the values and store them in variables.
    value_in_meters = int(input('Type your value in meters\t'))
    meters_to_millimeters(value_in_meters)

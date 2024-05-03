# Write a program that reads a value in meters and shows it converted into millimeters
def meters_to_milimeters(n):
    # ToDo: write your code here

    milimeters = n * 1000

    print(milimeters)


if __name__ == '__main__':
    # ToDo: Ask user to provide the values and store them in variables.

    value_in_meters= int(input("Add first number and press enter : "))

    meters_to_milimeters(value_in_meters)
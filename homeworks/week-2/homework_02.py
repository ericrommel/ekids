# Write a program that reads a value in meters and shows it converted into millimeters
def meters_to_milimeters(n):
    # ToDo: write your code here
    print("value in millimeters is ", n*1000)


if __name__ == '__main__':
    #ToDo: Ask user to provide the values and store them in variables.
    value_in_meters = float(input("Enter a value in meters: "))
    meters_to_milimeters(value_in_meters)

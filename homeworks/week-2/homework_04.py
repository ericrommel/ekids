# Calculate the time of a car trip. Ask about the distance to be covered and the
# average speed expected for the trip.
def duration(distance, speed):
    # ToDo: write your code here
    print("time of a car trip in hours:", distance/speed)


if __name__ == '__main__':
    # ToDo: Ask user to provide the values and store them in variables.
    my_speed = float(input("Enter the speed in km/h: "))
    my_distance = float(input("Enter the distance in kilometers: "))
    duration(my_distance,my_speed)

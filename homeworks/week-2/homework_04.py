# Calculate the time of a car trip. Ask about the distance to be covered and the
# average speed expected for the trip.
def duration(distance, speed):
    # ToDo: write your code here
    a = distance/speed
    print(a)

if __name__ == '__main__':
    # ToDo: Ask user to provide the values and store them in variables.

    my_distance = int(input("Add distance and press enter: "))
    my_speed = int(input("Add speed and press enter: "))

    duration(my_distance, my_speed)


# D/S.
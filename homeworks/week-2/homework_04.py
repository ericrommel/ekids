# Calculate the time of a car trip. Ask about the distance to be covered and the
# average speed expected for the trip.
def duration(distance, speed):
    # ToDo: write your code here
    time = distance/speed
    print(f'\n\n{'-'*50}\nThe estimated travel time will be: {round(time, 1)}hrs')


if __name__ == '__main__':
    # ToDo: Ask user to provide the values and store them in variables.
    my_distance = int(input('Type the distance you want to travel (in km)\t'))
    my_speed = int(input('Type the approximate medium speed you will be travelling at (in km/h)\t'))
    duration(my_distance, my_speed)

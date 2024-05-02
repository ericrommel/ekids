# Write a program that reads the number of days, hours, minutes, and seconds of the user.
# Calculate the total number of seconds.
def time_in_seconds(days, hours, minutes, seconds):
    # ToDo: write your code here

    print("total number of seconds is", days * 24 * 60 * 60 + hours * 60 * 60 +minutes * 60 + seconds)


if __name__ == '__main__':
    # ToDo: Ask user to provide the values and store them in variables.
    days = int(input("Enter number of days: "))
    hours = int(input("Enter number of hours: "))
    minutes = int(input("Enter number of minutes: "))
    seconds = int(input("Enter number of seconds: "))

    time_in_seconds(days, hours, minutes, seconds)

def time_in_seconds(days, hours, minutes, seconds):
    # ToDo: write your code here
    total_seconds = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds
    print(total_seconds)

if __name__ == '__main__':
    # ToDo: Ask user to provide the values and store them in variables.
    try:
        # Get input from the user
        days = int(input("Enter the number of days and press enter: "))
        hours = int(input("Enter the number of hours and press enter: "))
        minutes = int(input("Enter the number of minutes and press enter: "))
        seconds = int(input("Enter the number of seconds and press enter: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for seconds.")
# Calculate total seconds
    time_in_seconds(days, hours, minutes, seconds)
    print(time_in_seconds)



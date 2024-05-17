def time_in_seconds(days, hours, minutes, seconds):
    # ToDo: write your code here
    total_seconds = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds
    return total_seconds
    print(total_seconds)

if __name__ == '__main__':
    # ToDo: Ask user to provide the values and store them in variables.
    try:
        # Get input from the user
        days = int(input("Enter the number of days: "))
        hours = int(input("Enter the number of hours: "))
        minutes = int(input("Enter the number of minutes: "))
        seconds = int(input("Enter the number of seconds: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for seconds.")
# Calculate total seconds
    time_in_seconds(days, hours, minutes, seconds)
    print(time_in_seconds)



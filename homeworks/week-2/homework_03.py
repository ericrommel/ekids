# Write a program that reads the number of days, hours, minutes, and seconds of the user.
# Calculate the total number of seconds.
def time_in_seconds(days, hours, minutes, seconds):
    # ToDo: write your code here
    total_seconds = days*86400 + hours*3600 + minutes*60 + seconds
    print(f'\n\n{'-'*50}\nYour time in seconds only is: {total_seconds}s')

if __name__ == '__main__':
    # ToDo: Ask user to provide the values and store them in variables.
    days = int(input('Type your number of days\t'))
    hours = int(input('Type your number of hours\t'))
    minutes = int(input('Type your number of minutes\t'))
    seconds = int(input('Type your number of seconds\t'))
    time_in_seconds(days, hours, minutes, seconds)

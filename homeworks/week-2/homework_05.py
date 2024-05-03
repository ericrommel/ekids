# Convert a typed temperature in Celsius to Fahrenheit. F = 9*C/5 + 32
def celsius_to_fahrenheit(c):
    # ToDo: write your code here
    temperature_in_fahrenheit = 9*c/5 + 32
    print(f'\n\n{'-'*50}\nYour temperature in fahrenheit is: {round(temperature_in_fahrenheit, 2)}F')


if __name__ == '__main__':
    # ToDo: Ask user to provide the values and store them in variables.
    temperature_in_celsius = int(input('Type your temperature in celsius\t'))
    celsius_to_fahrenheit(temperature_in_celsius)

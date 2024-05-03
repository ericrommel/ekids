# Do it the other way around, from Fahrenheit to Celsius.
def fahrenheit_to_celsius(f):
    # ToDo: write your code here
    temperature_in_celsius = (f-32)*5/9
    print(f'\n\n{'-'*50}\nYour temperature in celsius is: {round(temperature_in_celsius, 2)}C')


if __name__ == '__main__':
    # ToDo: Ask user to provide the values and store them in variables.
    temperature_in_fahrenheit = int(input('Type your temperature in fahrenheit\t'))
    fahrenheit_to_celsius(temperature_in_fahrenheit)

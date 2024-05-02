# Do it the other way around, from Fahrenheit to Celsius.
def farenheit_to_celcius(c):
    # ToDo: write your code here
    print("temperature in Celsius:", 5/9*(temperature_in_fahrenheit - 32))


if __name__ == '__main__':
    # ToDo: Ask user to provide the values and store them in variables.
    temperature_in_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    farenheit_to_celcius(temperature_in_fahrenheit)

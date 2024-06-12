# Do it the other way around, from Fahrenheit to Celsius.
def farenheit_to_celcius(c):
    F = (c - 32) * 5 / 9
    print(F)

if __name__ == '__main__':
    # ToDo: Ask user to provide the values and store them in variables.

    temperature_in_fahrenheit = int(input("Add temperature_in_fahrenheit and press enter : "))

    farenheit_to_celcius(temperature_in_fahrenheit)



#“F = (C * 9/5) + 32″
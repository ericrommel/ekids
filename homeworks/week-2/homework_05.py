# Convert a typed temperature in Celsius to Fahrenheit. F = 9*C/5 + 32
def celsius_to_fahrenheit(c):
    F = (c * 9 / 5) + 32
    print(F)



if __name__ == '__main__':
    # ToDo: Ask user to provide the values and store them in variables.

    temperature_in_celsius = int(input("Add temperature_in_celsius and press enter : "))

    celsius_to_fahrenheit(temperature_in_celsius)

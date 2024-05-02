# Convert a typed temperature in Celsius to Fahrenheit. F = 9*C/5 + 32
def celcius_to_farenheit(c):
    # ToDo: write your code here
    print("temperature in Fahrenheit:", 9*c/5 + 32)


if __name__ == '__main__':
    # ToDo: Ask user to provide the values and store them in variables.
    temperature_in_celsius = float(input("Enter temperature in Celsius: "))
    celcius_to_farenheit(temperature_in_celsius)

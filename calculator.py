def sum(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

selection = ""
while True:
    print("1-sum")
    print("2-sub")
    print("3-mult")
    print("4-division")
    print("5-quit")
    selection = int(input("select an option: "))
    if selection == 5:
        break
    elif selection == 1:
        num1 = int(input("number 1: "))
        num2 = int(input("number 2: "))
        print(f"The sum is {sum(num1, num2)}")
    elif selection == 2:
        num1 = int(input("number 1: "))
        num2 = int(input("number 2: "))
        print(f"The sub is {sub(num1, num2)}")
    elif selection == 3:
        num1 = int(input("number 1: "))
        num2 = int(input("number 2: "))
        print(f"The mult is {mult(num1, num2)}")
    elif selection == 4:
        num1 = int(input("number 1: "))
        num2 = int(input("number 2: "))
        print(f"The division is {division(num1, num2)}")
    else:
        print("else")
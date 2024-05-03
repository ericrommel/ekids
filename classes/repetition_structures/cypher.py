'''
def hello_world(text):
    print(text)

hello_world("Have fun!")
print("Let's see the next...")
hello_world("My name is?")

'''

print("WELCOME TO A SECRET MESSAGE PROGRAMM!")

def encrypt(word):
    new_word = ""
    for i in word:
        print(ord(i))
        new_word = new_word + chr(ord(i) + 3)
    return new_word

message = input("Enter your your message that you want to be converted: ")
print(encrypt(message))
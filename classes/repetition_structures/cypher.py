def hello_world(text):
    for i in text:
        print(i)


def encrypt(word):
    new_word = ''
    for i in word:
        print(ord(i))
        new_word = new_word + chr(ord(i) + 3)
    return new_word


my_message = "This is my secret: I'm a teacher"
print(encrypt(my_message))

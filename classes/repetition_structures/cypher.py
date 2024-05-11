#Function to encrypt the word
def encrypt(word, key):
    secret_word = ""
    '''
    HOMEWORK:
    ToDo: Improve this code to:
    0. Ask the user to provide key value and the message. Make sure to have special character
    on it (because you want to test it, right?)                                                         1/1
    1. Only use letters from A to Z (in a big letters)                                                  1/1
    2. If there is a special character, keep it as it is. E.g. 'EP;AM' -> 'JU;FR'                       1/1
    3. If the character is a SPACE, keep the space as well. E.g. 'I am a legend' -> 'N fr f gjljsi'     1/1
    '''
    word = word.upper()
    for i in word:
        if i.isalpha():  # Check if it's a letter
            ascii_number = ord(i.upper())
            new_number = (ascii_number - 65 + user_key) % 26 + 65  # Shift within A-Z range
            new_character = chr(new_number)
        else:
            new_character = i  # Keep non-alphabetic characters as they are
        secret_word += new_character
    return secret_word

#Function to decrypt the word
def decrypt(message, key):
    message = message.upper()
    original_word = ""
    for i in message:
        if i.isalpha():
            ascii_number_secret = ord(i.upper())
            ascii_number_original = (ascii_number_secret - 65 - key) % 26 + 65
            original_character = chr(ascii_number_original)
        else:
            original_character = i
        original_word += original_character
    return original_word

#How to check if the number is in the range of numbers
def check_if_in_range():
    if 75 in range (65, 128):
        print("It is in the range")
    else:
        print("It's not in the range")
    

#Getting User's data
user_message = input("Eneter your message: ")
user_key = int(input("Enter your key in number only: "))

#Using the functions to proccess
encrypted_message = encrypt(user_message, user_key)
decrypted_message = decrypt(encrypted_message, user_key)

#Printing the data
print(f"Encrypted message: {encrypted_message}")
print(f"Decrypted message: {decrypted_message}")

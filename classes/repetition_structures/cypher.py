#Function to encrypt the word
def encrypt(word):
    secret_word = ""
    '''
    HOMEWORK:
    ToDo: Improve this code to:
    0. Ask the user to provide key value and the message. Make sure to have special character
    on it (because you want to test it, right?)
    1. Only use letters from A to Z (in a big letters)
    2. If there is a special character, keep it as it is. E.g. 'EP;AM' -> 'JU;FR'
    3. If the character is a SPACE, keep the space as well. E.g. 'I am a legend' -> 'N fr f gjljsi' 
    '''
    for i in word:
        ascii_number = ord(i)
        print(f"My ASCII number is {ascii_number}")
        key = user_key
        print(f"My key is {key}")
        new_number = ascii_number + key
        print(f"My new number is {new_number}")
        new_character = chr(new_number)
        secret_word = secret_word + new_character
    return secret_word

#Function to decrypt the word
def decrypt(message):
    original_word = ""
    for i in message:
        ascii_number_secret = ord(i)
        key = user_key
        ascii_number_original = ascii_number_secret - key
        ascii_character = chr(ascii_number_original)
        original_word = original_word + ascii_character
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
encrypted_message = encrypt(user_message)
decrypted_message = decrypt(encrypted_message)

#Printing the data
print(f"Encrypted message: {encrypted_message}")
print(f"Decrypted message: {decrypted_message}")

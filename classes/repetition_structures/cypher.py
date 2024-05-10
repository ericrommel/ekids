#Function to encrypt the word
def encrypt(word):
    new_word = ""
    for i in word:
        ascii_number = ord(i)
        print(f"My ASCII number is {ascii_number}")
        key = user_key
        print(f"My key is {key}")
        new_number = ascii_number + key
        print(f"My new number is {new_number}")
        new_character = chr(new_number)
        new_word = new_word + new_character
    return new_word

#Function to decrypt the word
def decrypt(message):
    original_word = ""
    for i in message:
        ascii_number_s = ord(i)
        key = user_key
        ascii_number_o = ascii_number_s - key
        ascii_character = chr(ascii_number_o)
        original_word = original_word + ascii_character
    return original_word


#Getting User's data
user_message = input("Eneter your message: ")
user_key = int(input("Enter your key in number only: "))

#Using the functions to proccess
encrypted_message = encrypt(user_message)
decrypted_message = decrypt(encrypted_message)

#Printing the data
print(f"Encrypted message: {encrypted_message}")
print(f"Decrypted message: {decrypted_message}")

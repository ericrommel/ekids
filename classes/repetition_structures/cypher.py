def encrypt(word):
    new_word = ""
    ''' Homework
    ToDo: Improve this code to:
        0. Ask the user to provide the key value and the message. Make sure to have special character
           on it (because you want to test it, right?)
        1. Only use letters from A to Z (in big letters)
        2. If there is a special character, keep it as it is. E.g.: 'EP;AM'  -> 'JU;FR'
        3. If the character is a SPACE, keep the space as well. E.g: 'I am a legend' -> 'N fr f qjljsi'        
    '''

    for i in word:
        ascii_number = ord(i)
        print(f"My ASCII number is {ascii_number}")
        key = 5
        print(f"My key is {key}")
        new_number = ascii_number + key
        print(f"My new number is {new_number}")
        new_character = chr(new_number)
        print(f"My new character is {new_character}")
        new_word = new_word + new_character
    return new_word


def decrypt(message):
    original_word = ""
    for i in message:
        ascii_number = ord(i)
        print(f"My ASCII number is {ascii_number}")
        key = 5
        print(f"My key is {key}")
        new_number = ascii_number - key
        print(f"My new number is {new_number}")
        new_character = chr(new_number)
        print(f"My new character is {new_character}")
        original_word = original_word + new_character
    return original_word


def check_if_it_is_in_a_range():
    if 75 in range(65, 128):
        print("Yes, it is in that range")
    else:
        print("No, it's not in the range")


my_message = "I am a legend"
encrypted_message = encrypt(my_message)
decrypted_message = decrypt(encrypted_message)

print(f"Encrypted message: {encrypted_message}")
print(f"Decrypted message: {decrypted_message}")

check_if_it_is_in_a_range()

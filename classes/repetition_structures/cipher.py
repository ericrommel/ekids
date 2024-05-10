key = int(input('Type your key\t'))
my_message = input('Type your message\t')


def encrypt(word):
    new_word = ''
    for i in word:
        ascii_number = ord(i)
        new_number = ascii_number + key
        if new_number in range(65, 91):
            new_number = new_number - 26
        new_character = chr(new_number)
        new_word = new_word + new_character
    return new_word


def decrypt(word):
    original_word = ''
    for i in word:
        ascii_number = ord(i)
        original_number = ascii_number - key
        original_character = chr(original_number)
        original_word = original_word + original_character
    return original_word


encrypted_message = encrypt(my_message)
decrypted_message = decrypt(encrypted_message)

print(f'Encrypted message: {encrypted_message}')
print(f'Decrypted message: {decrypted_message}')

# CREATE A PROGRAM TO COUNT HOW MANY UNIQUE LETTERS AND THEIR QUANTITY FROM A PHRASE!
# E.G; HELLO WORLD!

def count_unique_letters(phrase):
    # Remove spaces and punctuation, convert to lowercase
    cleaned_phrase = "".join(c.lower() for c in phrase if c.isalpha())

    # Initialize an empty dictionary
    my_dict = {}

    # Update letter frequencies
    for char in cleaned_phrase:
        my_dict[char] = my_dict.get(char, 0) + 1

    return my_dict

# Example usage
phrase = "I do not know what I am doing at all. I need help, PLEASE"
result = count_unique_letters(phrase)

# Display the unique letters and their quantities
for letter, count in result.items():
    print(f"{letter}: {count}")



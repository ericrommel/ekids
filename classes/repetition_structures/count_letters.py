import re  # regex - regex101.com

phrase = "Hello.World!"
my_dict = {}
special_ch = ['!', '.', ' ']
for i in phrase:
    if i.isalpha() == True:
        if i in my_dict:  # in my_dict.values() if you want to check if it's there as a value
            my_dict[i] += 1
        else:
            my_dict[i] = 1
for k, v in my_dict.items():
    print(f"{k}: {v} times")

# Dictionary is a data structure that uses key-value pairs
# Keys are unique
# Keys may not use mutual types/data structure
my_dict = {
    "name": "Tofunmi",
    "age": "14",
    "address": "bla bla bla"
}

for k, v in my_dict.items():
    print(f"key: {k} and value: {v}")
    print(f"my_dict['{k}'] = {my_dict[k]}")
    if my_dict[k] == "Tofunmi":
        my_dict[k] = "Anything"

my_dict["grade"] = "2oESO"
print(my_dict)
print(len(my_dict))
print(f"Only keys: {my_dict.keys()}")
print(f"Only values: {my_dict.values()}")

for i in my_dict.keys():
    print(i)

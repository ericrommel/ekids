my_list = [1, 2, 3, 4, 5, 6]

my_list.pop(0)  # Removes an element from the list (1 is in the position 0 in the list, so it will be removed)
my_list.pop(1)  # Here, it will remove the 2 which is in the position 1

my_list.remove(3)  # Removes an element from the list (by its value which is 3 here)
my_list.remove(4)  # It will remove the 4 from the list

my_list.append(7)  # Adds an element to the last space of the list (here, it will put the 7 after the 6)
my_list.append(8)  # Adds an 8 after the 7 which I appended before

my_list.insert(0, 0)  # Adds an element to a set position in the list (here, it will put a 0 before the 1)
my_list.insert(1, 8)  # Adds an 8 at the position 1

my_list.clear()  # Clears the list


my_dict = {
    'apple': 'fruit',
    'cherry': 'berry',
    'orange': 'citrus',
    'almond': 'nut',
    'tomato': 'vegetable'
}

my_dict.pop('apple')  # Removes an element of the dictionary by its key (removes the element with key "apple")
my_dict.pop('cherry')  # Removes the element with key "cherry"

my_dict.get('orange')  # Returns an element by inputting its key (it will return "citrus") (basically the same as my_dict[orange])
my_dict.get('almond')  # It will return "nut"

my_dict.clear()  # Clears your dictionary

my_dict.keys()  # Shows all the keys from a list

my_dict.items()  # Shows all the values from a list

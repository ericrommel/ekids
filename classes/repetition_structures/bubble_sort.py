# Unordered list
my_list = [-5, -3, 11, -10, 1, 2]
#           0   1   2   3   4  5

length_of_the_list = len(my_list)

print(f"My list is: {my_list}")
print(f"How many items do we have in our list? {length_of_the_list}")
print(f"Print the index 5 from the list: {my_list[5]}")

try:
    print(f"Print the index 6 from the list: {my_list[6]}")
except IndexError:
    print(f"The list has length of {length_of_the_list}. So, this index is out of range")

print(f"The last element of the list is : {my_list[length_of_the_list - 1]}")
print(f"Another way to get the last element of the list: {my_list[-1]}")

# Slicing:
print(f"Items from the 2nd till 4th index: {my_list[2:5]}")
print(f"Last 3 items from the list are: {my_list[-3:]}")
print(f"Last 3 items from the list are: {my_list[:-3]}")
print(f"Last 3 items from the list are: {my_list[1:-1:2]}")
print(f"Last 3 items from the list are: {my_list[1::2]}")

# for i in my_list:

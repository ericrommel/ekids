# Unordered list
my_list = [-9, 2, 4, 45, 12, -54, 0, 32]

my_list.append("i_love_myself")
lenght_of_the_list = len(my_list)
print(f"My list is: {my_list}")
print(f"How many items do we have in our list: {lenght_of_the_list}")
print(f"Print the index 5 from the list: {my_list[5]}")
try:
    print(f"Print the index 6 from the list: {my_list[6]}")
except IndexError:
    print(f"The list has length of {lenght_of_the_list}. So, this index eis out of range")

print(f"The last element of the list is: {my_list[lenght_of_the_list - 1]}")
print(f"Another way to get the last element of my list: {my_list[-1]}")

# Slicing
print(f"Items from the 2nd till 4th index: {my_list[2:4]}")
print(f"The last 3 items on my list are: {my_list[-3:]}")
print(f"The last 3 items on my list are: {my_list[:-3]}")
print(f"The last 3 items on my list are: {my_list[1:-1:2]}")

# for i in my_list
# print(i)

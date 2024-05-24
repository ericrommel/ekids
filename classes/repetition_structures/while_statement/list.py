#Unordered list
my_list = [-5, -3, 11, -10, 1, 2]
#           0   1  2    3   4  5
lenth_of_the_list = len(my_list)

print(f"How many items do we have in our list: {lenth_of_the_list}")
print(f"Print the index 5 from the list: {my_list[5]}")
try:
    print(f"Print the index 6 from the list: {my_list[6]}")
except IndexError:
    print(f"This list has length of {lenth_of_the_list}. So, this index is out of range.")

print(f"The last element of the list is: {my_list[-1]}")

#Slicing
START = -1
END = -4
JUMP = 1
print(f"Items from the 2nd till 4th index: {my_list[2:4]}")

print(f"The last 3 items from the list are: {my_list[-3:]}")

print(f"The last 3 items from the list are: {my_list[:-3]}")
print(f"The last 3 items from the list are: {my_list[1::2]}")
#for i in my_list:
#    print(i)
my_list = [1 ,4 ,7 ,-3 ,9 ]
my_list.




1)reverse :	Reverses the order of the list

my_list = [1 ,4 ,7 ,-3 ,9 ]
my_list.reverse()
print(my_list)  # [9, -3, 7, 4, 1]

2)extend : Add the elements of a list (or any iterable), to the end of the current list

my_list = [1 ,4 ,7 ,-3 ,9 ]
my_list.extend([5 ,20 ,-6 ,2 ])
print(my_list)  # [1 ,4 ,7 ,-3 ,9 ,5 ,20 ,-6 ,2 ]

3)insert : Adds an element at the specified position

my_list.insert(1, 5)
print(my_list)  # [1 ,5 ,4 ,7 ,-3 ,9 ]

my_list.insert(3,18)
print(my_list)  # [1 ,5 ,4 ,18 ,7 ,-3 ,9 ]

4)pop :	Removes the element at the specified position

popped_item = my_list.pop()
print(popped_item)  # 7
print(my_list)      # [1 ,4 ,-3 ,9 ]

popped_item = my_list.pop(1)
print(popped_item)  # 4
print(my_list)      # [1 ,-3 ,9 ]

5)append : Adds an element at the end of the list
my_list.append(4)
print(my_list)  # [1 ,4 ,7 ,-3 ,9 ]
my_list.append(7)
print(my_list)  # [1 ,4 ,7 ,-3 ,9 ]

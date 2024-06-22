my_list = [9, 4, -7, 12]
if len(my_list) != 0:
    value = my_list.pop(-1)
    my_list.insert(0, value)
print(my_list)

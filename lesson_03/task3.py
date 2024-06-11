my_list = [12, 3, 8, 14, 15, 19, -3, 81, 37]
# my_list = [12, 3, 8, 14, 15, 19, -3, 81]
# my_list = []
# my_list = [12]

if len(my_list) % 2 == 0:
    first = my_list[:int(len(my_list) // 2)]
    second = my_list[int(len(my_list) // 2):]
else:
    first = my_list[:int(len(my_list) // 2 + 1)]
    second = my_list[int(len(my_list) // 2 + 1):]

print([first, second])

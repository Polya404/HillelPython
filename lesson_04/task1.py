list_of_numbers = [1, 0, 5, 0, 0, -3, 0, 4]
list_of_numbers_2 = [0, 11, 0, 5, 0, 0, -3, 73, -81, 0, 0, 4, 0]

##### first solution #####
zeros = list_of_numbers.count(0)
for num in list_of_numbers:
    list_of_numbers.remove(0)
list_of_numbers.extend([0] * zeros)

##### second solution #####
for i, num in enumerate(list_of_numbers_2):
    if num == 0:
        list_of_numbers_2.insert(len(list_of_numbers_2), num)
        list_of_numbers_2.remove(num)

print(list_of_numbers)
print(list_of_numbers_2)

list_of_numbers = [1, 16, 37, 17, 9, 0, 13, 2]

##### first solution #####
print(sum(list_of_numbers[0::2]))

##### second solution #####
sum_of_num = 0
for num in range(0, len(list_of_numbers), 2):
    sum_of_num += list_of_numbers[num]

print(sum_of_num)

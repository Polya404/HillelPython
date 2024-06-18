list_of_numbers = [0, 1, 7, 2, 4, 8]

##### first solution #####
print(sum(list_of_numbers[0::2]) * list_of_numbers[-1])

##### second solution #####
sum_of_num = 0
for num in range(0, len(list_of_numbers), 2):
    sum_of_num += list_of_numbers[num]
sum_of_num *= list_of_numbers[-1]

print(sum_of_num)

import timeit

##### First Solution #####
def add_one(some_list):
    if some_list[-1] < 9:
        some_list[-1] += 1
        return some_list
    else:
        for i in range(len(some_list) - 1, -1, -1):
            if some_list[i] < 9:
                some_list[i] += 1
                break
            some_list[i] = 0
        else:
            some_list.insert(0, 1)

        return some_list


##### Second solution #####
def add_one_second(some_list):
    string_numbers = ''
    for x in some_list:
        string_numbers += str(x)
    updated_num = int(string_numbers) + 1
    return [int(digit) for digit in str(updated_num)]


##### Tests #####
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
assert add_one([8, 9, 9]) == [9, 0, 0], 'Test5'

assert add_one_second([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one_second([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one_second([0]) == [1], 'Test3'
assert add_one_second([9]) == [1, 0], 'Test4'
assert add_one_second([8, 9, 9]) == [9, 0, 0], 'Test5'


##### Speed check #####
test_list_1 = [1, 2, 3, 4, 9, 9, 2]
test_list_2 = [9, 9, 9, 9, 9, 9, 9]

# Timing add_one
time_add_one_1 = timeit.timeit(lambda: add_one(test_list_1[:]), number=100000)
time_add_one_2 = timeit.timeit(lambda: add_one(test_list_2[:]), number=100000)

# Timing add_one_second
time_add_one_second_1 = timeit.timeit(lambda: add_one_second(test_list_1[:]), number=100000)
time_add_one_second_2 = timeit.timeit(lambda: add_one_second(test_list_2[:]), number=100000)

print(f"add_one with [1, 2, 3, 4, 9, 9, 2]: {time_add_one_1:.5f} seconds")
print(f"add_one with [9, 9, 9, 9, 9, 9, 9]: {time_add_one_2:.5f} seconds")
print(f"add_one_second with [1, 2, 3, 4, 9, 9, 2]: {time_add_one_second_1:.5f} seconds")
print(f"add_one_second with [9, 9, 9, 9, 9, 9, 9]: {time_add_one_second_2:.5f} seconds")
print("ОК")

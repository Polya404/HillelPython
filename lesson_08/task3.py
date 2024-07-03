def get_key_by_value(my_dict, target_value):
    for key, value in my_dict.items():
        if value == target_value:
            return key
    return None


def find_unique_value(some_list):
    my_dict = {}
    for number in some_list:
        if number in my_dict:
            my_dict[number] += 1
        else:
            my_dict[number] = 1
    return get_key_by_value(my_dict, 1)


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")

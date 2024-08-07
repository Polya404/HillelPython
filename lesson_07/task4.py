def common_elements():
    multiples_of_3 = [x for x in range(0, 100, 3)]
    multiples_of_5 = [x for x in range(0, 100, 5)]
    return set(multiples_of_3).intersection(set(multiples_of_5))


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

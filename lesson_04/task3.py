import random

result = []
random_list = [random.randint(-10, 10) for _ in range(random.randint(3, 10))]
print(random_list)

##### first solution #####
a, b, *c = random_list[::2]
result.extend([a, b, random_list[-2]])

##### second solution #####
result.extend([random_list[0], random_list[2], random_list[-2]])


##### third solution #####
result.extend(random_list[:3:2])
random_list.reverse()
result.append(random_list[1])

print(result)

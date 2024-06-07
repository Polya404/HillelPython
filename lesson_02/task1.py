entered_num = int(input("Enter your number "))

first_num = entered_num % 10
second_num = entered_num % 100 // 10
third_num = entered_num % 1000 // 100
fourth_num = entered_num % 10000 // 1000

print(fourth_num)
print(third_num)
print(second_num)
print(first_num)
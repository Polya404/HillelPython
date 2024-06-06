entered_num = int(input("Enter your number "))

first_num = entered_num % 10
second_num = entered_num % 100 // 10
third_num = entered_num % 1000 // 100
fourth_num = entered_num % 10000 // 1000
fifth_num = entered_num % 100000 // 10000

print(first_num, second_num, third_num, fourth_num, fifth_num)
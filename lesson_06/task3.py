##### First Solution #####
number = int(input("Enter number: "))
result = 1
while number > 9:
    for digit in str(number):
        result *= int(digit)
    number = result
    result = 1

print(number)


##### Second solution #####
number = int(input("Enter number: ")) or 1
while number > 9:
    number = eval('*'.join(str(number)))
print(number)

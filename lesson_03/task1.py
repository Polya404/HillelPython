first_num = int(input("Enter first number: "))
action = input("Enter action: ")
second_num = int(input("Enter second number: "))

if action == "+":
    result = first_num + second_num
elif action == "-":
    result = first_num - second_num
elif action == "/" and second_num != 0:
    result = first_num / second_num
elif action == "*":
    result = first_num * second_num
else:
    result = "sorry, this operation is not supported"

print(result)

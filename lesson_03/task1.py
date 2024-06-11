first_num = int(input("Enter first number: "))
action = input("Enter action: ")
second_num = int(input("Enter second number: "))

if action == "+":
    print(first_num + second_num)
elif action == "-":
    print(first_num - second_num)
elif action == "/" and second_num != 0:
    print(first_num / second_num)
elif action == "*":
    print(first_num * second_num)
else:
    print("sorry, this operation is not supported")

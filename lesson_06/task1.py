import string

letter_range = input("Enter letters: ")
start, end = string.ascii_letters.index(letter_range[0]), string.ascii_letters.index(letter_range[2])
print(string.ascii_letters[start:end + 1])

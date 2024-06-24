import keyword
import string
import re

input_string = input("Enter variable name: ")

##### First Solution #####
not_allow_list = set(string.punctuation) - {"_"}
not_allow_list.update(string.ascii_uppercase)
not_allow_list.update(string.whitespace)
not_allow_list.update(keyword.kwlist)


result = (
    input_string[0] not in string.digits and
    input_string.count("_") <= 1 and
    all(char not in not_allow_list for char in input_string)
)


##### Second Solution #####
pattern = re.compile(r'^[a-z_][a-z0-9_]*$')
result = bool(pattern.match(input_string)) and input_string not in keyword.kwlist and input_string.count("_") < 2

print(result)

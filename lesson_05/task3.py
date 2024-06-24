import string

input_string = input("Enter hashtag name: ")

hashtag_str = ("#" + input_string.title().replace(" ", "")
               .translate(str.maketrans('', '', string.punctuation)))
hashtag_str = hashtag_str[:140] if len(hashtag_str) > 140 else hashtag_str
print(hashtag_str)

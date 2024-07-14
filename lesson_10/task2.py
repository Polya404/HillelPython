import re
import string


def replace_punctuation_with_spaces(text):
    punctuation = string.punctuation.replace("'", "")
    translator = str.maketrans(punctuation, ' ' * len(punctuation))
    return text.translate(translator)


def first_word(text):
    """ Пошук першого слова """
    text_list = replace_punctuation_with_spaces(text).split(" ")
    for word in text_list:
        if bool(re.match(r"^[a-zA-Z]", word)):
            return word


def first_word_2(text):
    """ Пошук першого слова """
    text_list = replace_punctuation_with_spaces(text).split()
    for word in text_list:
        if word and word[0].isalpha():
            return word


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
assert first_word("' '' Hello.World") == "Hello", 'Test7'
assert first_word("'' ' Hello.World") == "Hello", 'Test8'

assert first_word_2("Hello world") == "Hello", 'Test1'
assert first_word_2("greetings, friends") == "greetings", 'Test2'
assert first_word_2("don't touch it") == "don't", 'Test3'
assert first_word_2(".., and so on ...") == "and", 'Test4'
assert first_word_2("hi") == "hi", 'Test5'
assert first_word_2("Hello.World") == "Hello", 'Test6'
assert first_word_2("' '' Hello.World") == "Hello", 'Test7'
assert first_word("'' ' Hello.World") == "Hello", 'Test8'
print('OK')

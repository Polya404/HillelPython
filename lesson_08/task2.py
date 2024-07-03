import string


def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator).replace(" ", "").lower()


def is_palindrome(text):
    text = remove_punctuation(text)
    for i in range(len(text) // 2):
        if text[i] != text[-(i + 1)]:
            return False
    return True


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")

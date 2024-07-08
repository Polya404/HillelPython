from collections import Counter


def popular_words(text, words):
    my_dict = dict.fromkeys(words, 0)
    for text in text.lower().split(" "):
        if text in words:
            my_dict[text] += 1
    return my_dict


def popular_words_2(text, words):
    text = text.lower().split()
    word_count = Counter(text)
    return {word: word_count.get(word, 0) for word in words}


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'

assert popular_words_2('''When I was One I had just begun When I was Two I was nearly new ''',
                       ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')

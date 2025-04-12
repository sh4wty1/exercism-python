import string


def is_isogram(sentence):
    word_list = list()
    word_set = set()
    for i in sentence.lower():
        if i in string.ascii_lowercase:
            word_list.append(i)
            word_set.add(i)
    if len(word_set) == len(word_list):
        return True
    return False

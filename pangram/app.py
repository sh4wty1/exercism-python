import string


def is_pangram(sentence):
    letters = set()
    for i in sentence.lower():
        if i in string.ascii_lowercase:
            letters.add(i)
    return len(letters) == 26

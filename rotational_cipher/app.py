def rotate(text, key):
    result = []
    for word in text.split():
        encrypted_word = []
        for c in word:
            if c.isalpha():
                shift = 65 if c.isupper() else 97
                encrypted_c = chr((ord(c) - shift + key) % 26 + shift)
                encrypted_word.append(encrypted_c)
            else:
                encrypted_word.append(c)
        result.append("".join(encrypted_word))
    return " ".join(result)

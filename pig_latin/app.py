def translate(text):
    """
    Translates English to Pig Latin

    Args:
        text (str): English text to be translated

    Returns:
        str: The translated text in Pig Latin
    """
    # Special condition for phrases
    if " " in text:
        return " ".join(translate(word) for word in text.split())

    # Rule 1
    if text.startswith(("a", "e", "i", "o", "u", "xr", "yt")):
        return text + "ay"

    # Rule 2 and 3
    for i, letter in enumerate(text):
        if letter in "aeiou":
            if i > 0 and text[i] == "u" and text[i - 1] == "q":
                return text[i + 1 :] + text[: i + 1] + "ay"
            return text[i:] + text[:i] + "ay"

    # Rule 4
    for i, letter in enumerate(text):
        if letter == "y":
            return text[i:] + text[:i] + "ay"

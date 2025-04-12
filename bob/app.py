def response(hey_bob):
    hey_bob = hey_bob.strip()
    if hey_bob.isupper():
        if hey_bob.endswith("?"):
            return "Calm down, I know what I'm doing!"
    if hey_bob.endswith("?"):
        return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if not hey_bob:
        return "Fine. Be that way!"
    else:
        return "Whatever."

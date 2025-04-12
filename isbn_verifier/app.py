def is_valid(isbn):

    num_isbn = isbn.replace("-", "")

    if len(num_isbn) != 10:
        return False

    total = 0

    for i, c in enumerate(num_isbn):
        if c == "X":
            if i == 9:
                total += 10 * (10 - i)
            else:
                return False
        elif c.isdigit():
            total += int(c) * (10 - i)
        else:
            return False
    if total % 11 == 0:
        return True
    return False

def convert(number):
    if number % 3 == 0 and number % 5 != 0 and number % 7 != 0:
        return "Pling"
    if number % 5 == 0 and number % 3 != 0 and number % 7 != 0:
        return "Plang"
    if number % 7 == 0 and number % 3 != 0 and number % 5 != 0:
        return "Plong"
    if number % 7 != 0 and number % 3 == 0 and number % 5 == 0:
        return "PlingPlang"
    if number % 7 == 0 and number % 3 == 0 and number % 5 != 0:
        return "PlingPlong"
    if number % 7 == 0 and number % 3 != 0 and number % 5 == 0:
        return "PlangPlong"
    if number % 7 == 0 and number % 3 == 0 and number % 5 == 0:
        return "PlingPlangPlong"
    else:
        number = str(number)
        return number

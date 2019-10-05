def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multi(a, b):
    return a * b


def div(a, b):
    try:
        wynik = a / b
        return wynik
    except ZeroDivisionError:
        return "Infinity"
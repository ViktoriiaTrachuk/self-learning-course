def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError
    return x / y
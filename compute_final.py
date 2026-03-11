def myadd(a, b):

    if a > 0 and b > 0:
        return a + b

    if a < 0 and b < 0:
        return a + b

    if a == 0:
        return b

    if b == 0:
        return a

    if a > 0 and b < 0:
        if abs(a) > abs(b):
            return a + b
        if abs(a) < abs(b):
            return a + b

    return 0


def mymult(a, b):

    if a > 0 and b > 0:
        return a * b

    if a < 0 and b < 0:
        return a * b

    if a > 0 and b < 0:
        return a * b

    if a < 0 and b > 0:
        return a * b

    if a == 0:
        return 0

    if b == 0:
        return 0

    return -100

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


def test_myadd():

    assert myadd(1, 2) == 3
    assert myadd(2, 6) > 0
    assert myadd(-2, -6) < 0
    assert myadd(0, 6) == 6
    assert myadd(2, 0) == 2
    assert myadd(4, -1) > 0
    assert myadd(1, -4) < 0


def test_mymult():

    assert mymult(2, 6) == 12
    assert mymult(2, 6) > 0
    assert mymult(-2, -6) > 0
    assert mymult(2, -6) < 0
    assert mymult(-2, 6) < 0
    assert mymult(0, 6) == 0
    assert mymult(2, 0) == 0

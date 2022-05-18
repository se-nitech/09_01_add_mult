import pytest

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


@pytest.mark.parametrize(
    ("a", "b", "c"), [
        (1, 2, 3),
        (0, 6, 6),
        (2, 0, 2),
    ])
def test_myadd_eq(a, b, c):

    assert myadd(a, b) == c


@pytest.mark.parametrize(
    ("a", "b"), [
        (-2, -6),
        (1, -4),
    ])
def test_myadd_lt(a, b):

    assert myadd(a, b) < 0


@pytest.mark.parametrize(
    ("a", "b"), [
        (2, 6),
        (4, -1),
    ])
def test_myadd_gt(a, b):

    assert myadd(a, b) > 0


def test_mymult():

    assert mymult(2, 6) == 12
    assert mymult(2, 6) > 0
    assert mymult(-2, -6) > 0
    assert mymult(2, -6) < 0
    assert mymult(-2, 6) < 0
    assert mymult(0, 6) == 0
    assert mymult(2, 0) == 0

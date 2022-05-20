import pytest
from compute import myadd, mymult


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


@pytest.mark.parametrize(
    ("a", "b", "c"), [
        (2, 6, 12),
        (0, 6, 0),
        (2, 0, 0),
    ])
def test_mymult_eq(a, b, c):

    assert mymult(a, b) == c


@pytest.mark.parametrize(
    ("a", "b"), [
        (2, -6),
        (-2, 6),
    ])
def test_mymult_lt(a, b):

    assert mymult(a, b) < 0


@pytest.mark.parametrize(
    ("a", "b"), [
        (2, 6),
        (-2, -6),
    ])
def test_mymult_gt(a, b):

    assert mymult(a, b) > 0
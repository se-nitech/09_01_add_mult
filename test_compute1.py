from compute import myadd, mymult


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



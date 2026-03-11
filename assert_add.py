from compute import myadd


def main():

    assert 3 == myadd(1, 2), '1+2 is not 3'
    assert -2 == myadd(4, -6), '4+(-6) is not -2'

if __name__ == '__main__':
    main()

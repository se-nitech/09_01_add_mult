import unittest
from compute import myadd


class TestMyCompute(unittest.TestCase):

    def test_myadd1(self):
        val = myadd(1, 2)
        self.assertEqual(3, val)

    def test_myadd2(self):
        val = myadd(4, 2)
        self.assertEqual(6, val)

if __name__ == "__main__":
    unittest.main()

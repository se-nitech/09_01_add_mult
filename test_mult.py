import unittest
from compute_final import mymult


class TestMyMult(unittest.TestCase):

    def test_mult(self):
        val = mymult(2, 6)
        self.assertEqual(12, val)

    def test_mult_pp(self):
        val = mymult(2, 6)
        self.assertTrue(val > 0)

    def test_mult_nn(self):
        val = mymult(-2, -6)
        self.assertTrue(val > 0)

    def test_mult_pn(self):
        val = mymult(2, -6)
        self.assertTrue(val < 0)

    def test_mult_np(self):
        val = mymult(-2, 6)
        self.assertTrue(val < 0)

    def test_add_a0(self):
        val = mymult(0, 6)
        self.assertEqual(0, val)

    def test_add_b0(self):
        val = mymult(2, 0)
        self.assertEqual(0, val)


if __name__ == "__main__":
    unittest.main()

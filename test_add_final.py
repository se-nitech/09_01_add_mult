import unittest
from compute_final import myadd


class TestMyAdd(unittest.TestCase):

    def test_add(self):
        val = myadd(1, 2)
        self.assertEqual(3, val)

    def test_add_pp(self):
        val = myadd(2, 6)
        self.assertTrue(val > 0)

    def test_add_nn(self):
        val = myadd(-2, -6)
        self.assertTrue(val < 0)

    def test_add_a0(self):
        val = myadd(0, 6)
        self.assertEqual(6, val)

    def test_add_b0(self):
        val = myadd(2, 0)
        self.assertTrue(2, val)

    def test_add_pn_a_gt_b(self):
        val = myadd(4, -1)
        self.assertTrue(val > 0)

    def test_add_pn_a_lt_b(self):
        val = myadd(1, -4)
        self.assertTrue(val < 0)


if __name__ == "__main__":
    unittest.main()

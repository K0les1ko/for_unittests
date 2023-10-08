import unittest

from utils.arrs import get, my_slice


class TestArrs(unittest.TestCase):
    def test_get(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(get(array, 2), 3)

    def test_my_slice(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(my_slice(array, start=1, end=4), [2, 3, 4])
import unittest

from Sorting import bubble_sort


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.A = [44,22,11,33,2,1,5,5,5]
        self.B = [0,0,1,2,3,4,4,1,10,2,3]

    def test_A(self) -> None:
        result = bubble_sort(self.A)
        expected = sorted(self.A)
        self.assertEqual(result, expected)

    def test_A(self) -> None:
        result = bubble_sort(self.B)
        expected = sorted(self.B)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

import unittest
from lab import add  # Импортируем нашу функцию из lab.py

class TestSumOfTwo(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(add([2, 7, 11, 15], 9), [0, 1])

    def test_case_2(self):
        self.assertEqual(add([3, 2, 4], 6), [1, 2])

    def test_case_3(self):
        self.assertEqual(add([3, 3], 6), [0, 1])

    def test_no_solution(self):
        self.assertEqual(add([1, 2, 3], 10), [])

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
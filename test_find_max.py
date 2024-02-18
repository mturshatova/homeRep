import unittest
from find_max import find_max 
class FindMaxTestCase(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max([3, 7, 2, 9, 1]), 9)
        self.assertEqual(find_max([5, 8, 2, 4]), 8)
        self.assertEqual(find_max([-1, -5, -3, -9]), -1)
        self.assertEqual(find_max([1]), 1)
        self.assertEqual(find_max([]), None)

if __name__ == '__main__':
    unittest.main()
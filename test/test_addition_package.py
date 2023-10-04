import unittest

from calculator.addition_package import increment_num, add_two_nums

class TestSimple(unittest.TestCase):

    def test_increment_num(self):
        self.assertEqual(increment_num(5), 6)
        
    def test_add_two_nums(self):
        self.assertEqual(add_two_nums(1, 2), 3)
        
if __name__ == '__main__':
    unittest.main()
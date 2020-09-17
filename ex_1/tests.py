import unittest

# WTF
# To run this file use: 
# from r_1_1 import is_multiple

from ex_1.r_1_1 import is_multiple

class Test_r_1_1(unittest.TestCase):

    def test_is_100_multiple_of_2(self):
        self.assertTrue(is_multiple(100, 2))

    def test_is_40_multiple_of_3(self):
        self.assertFalse(is_multiple(49, 3))

    def test_if_both_input_params_are_strings(self):
        with self.assertRaises(TypeError):
            is_multiple('a', 'b')

if __name__ == '__main__':
    unittest.main()
import unittest
from random import randint

# WTF
# To run this file use: 
# from r_1_1 import is_multiple
# VSC issue afaiu

#Reinforcement
from ex_1.r_1_1 import is_multiple
from ex_1.r_1_2 import is_even
from ex_1.r_1_3 import minmax
from ex_1.r_1_4 import get_sum_of_squares
from ex_1.r_1_5 import get_sum_of_squares_with_sum, \
    get_sum_of_squares_with_sum_and_iterator
from ex_1.r_1_6 import get_sum_of_squares_of_odd_ints
from ex_1.r_1_8 import get_str_positive_idx_by_negaive_idx
from ex_1.r_1_9 import get_a_list_from_50_to_80_with_step_10
from ex_1.r_1_10 import get_a_list_from_8_to_m8_with_step_m2
from ex_1.r_1_11 import get_list_from_1_to_256_of_power_of_2
from ex_1.r_1_12 import pseudo_choice

#Creativity
from ex_1.c_1_13 import pseudo_reverse_list
from ex_1.c_1_14 import is_there_a_distinct_pair_of_numbers_whose_product_id_odd
from ex_1.c_1_15 import is_all_numbers_different_in_seq
from ex_1.c_1_16 import scale, multiply_x_2

#Reinforcement
class Test_r_1_1(unittest.TestCase):

    def test_is_100_multiple_of_2(self):
        self.assertTrue(is_multiple(100, 2))

    def test_is_40_multiple_of_3(self):
        self.assertFalse(is_multiple(40, 3))

    def test_if_both_input_params_are_strings(self):
        with self.assertRaises(TypeError):
            is_multiple('a', 'b')

class Test_r_1_2(unittest.TestCase):

    def test_is_100_even(self):
        self.assertTrue(is_even(100))

    def test_is_65_even(self):
        self.assertFalse(is_even(65))

    def test_is_even_if_string_specified(self):
        with self.assertRaises(TypeError):
            is_even('blablabla')

class Test_r_1_3(unittest.TestCase):

    def test_minmax_for_range_between_76_and_835(self):
        self.assertEqual((76, 835), minmax(list(range(76, 836))))

    def test_minmax_for_list_of_random_numbers(self):
        v_list_length = randint(100, 10000)
        v_list = [randint(1, 9999) for elem in range(v_list_length)]
        v_min = min(v_list)
        v_max = max(v_list)
        self.assertEqual((v_min, v_max), minmax(v_list))

    def test_minmax_if_there_is_a_one_string_in_list(self):
        v_list = ["kill me plz"]
        with self.assertRaises(ValueError):
            minmax(v_list)

    def test_minmax_if_some_list_elements_are_strings(self):
        v_list = [111, 222, "aaa", "bbb", 333]
        with self.assertRaises(TypeError):
            minmax(v_list)

class Test_r_1_4(unittest.TestCase):

    def test_sum_of_squares_from_1_to_4(self):
        v_sum = 1*1 + 2*2 + 3*3 + 4*4
        self.assertEqual(v_sum, get_sum_of_squares(5))

    def test_sum_of_squares_from_1_to_9999(self):
        v_sum = sum([num * num for num in range(1,10000)])
        self.assertEqual(v_sum, get_sum_of_squares(10000))

    def test_sum_of_squares_with_input_is_negative_int(self):
        with self.assertRaises(ValueError):
            get_sum_of_squares(-200)

    def test_sum_of_squares_with_input_is_string(self):
        with self.assertRaises(ValueError):
            get_sum_of_squares("blah blah blah, mr Freeman!")

class Test_r_1_5(unittest.TestCase):

    def test_sum_of_squares_with_sum_from_1_to_4(self):
        v_sum = 1*1 + 2*2 + 3*3 + 4*4
        self.assertEqual(v_sum, get_sum_of_squares_with_sum(5))

    def test_sum_of_squares_with_sum_from_1_to_9999(self):
        v_sum = sum([num * num for num in range(1,10000)])
        self.assertEqual(v_sum, get_sum_of_squares_with_sum(10000))

    def test_sum_of_squares_with_sum_with_input_is_negative_int(self):
        with self.assertRaises(ValueError):
            get_sum_of_squares_with_sum(-200)

    def test_sum_of_squares_with_sum_with_input_is_string(self):
        with self.assertRaises(ValueError):
            get_sum_of_squares_with_sum("blah blah blah, mr Freeman!")

    def test_sum_of_squares_with_sum_and_iterator_from_1_to_4(self):
        v_sum = 1*1 + 2*2 + 3*3 + 4*4
        self.assertEqual(v_sum, get_sum_of_squares_with_sum_and_iterator(5))

    def test_sum_of_squares_with_sum_and_iterator_from_1_to_9999(self):
        v_sum = sum([num * num for num in range(1,10000)])
        self.assertEqual(v_sum, get_sum_of_squares_with_sum_and_iterator(10000))

    def test_sum_of_squares_with_sum_and_iterator_with_input_is_negative_int(self):
        with self.assertRaises(ValueError):
            get_sum_of_squares_with_sum_and_iterator(-200)

    def test_sum_of_squares_with_sum_and_iterator_with_input_is_string(self):
        with self.assertRaises(ValueError):
            get_sum_of_squares_with_sum_and_iterator("blah blah blah, mr Freeman!")

class Test_r_1_6(unittest.TestCase):

    def test_sum_of_squares_of_odd_ints_less_than_5(self):
        v_sum = 1*1 + 3*3 
        self.assertEqual(v_sum, get_sum_of_squares_of_odd_ints(5))

    def test_sum_of_squares_of_odd_ints_less_than_1000(self):
        v_sum = 0
        for num in range(1000):
            if num % 2 == 1:
                v_sum += num * num
        self.assertEqual(v_sum, get_sum_of_squares_of_odd_ints(1000))

    def test_sum_of_squares_of_odd_ints_if_input_is_str(self):
        with self.assertRaises(TypeError):
            get_sum_of_squares_of_odd_ints("Salam!")

class Test_r_1_8(unittest.TestCase):

    def test_get_str_positive_idx_of_str_confuse_a_cat(self):
        v_str = "Confuse-a-cat!"
        v_str_len = len(v_str)
        v_neg_idx = randint(-1 * v_str_len, -1)
        v_pos_idx = get_str_positive_idx_by_negaive_idx(v_str_len, v_neg_idx)
        self.assertEqual(v_str[v_neg_idx], v_str[v_pos_idx])

    def test_get_str_positive_idx_if_neg_idx_is_greater_than_zero(self):
        with self.assertRaises(ValueError):
            get_str_positive_idx_by_negaive_idx(str_length=5, neg_idx=5) 

    def test_get_str_positive_idx_if_neg_idx_exceeds_str_length(self):
        with self.assertRaises(ValueError):
            get_str_positive_idx_by_negaive_idx(str_length=5, neg_idx=-10) 

class Test_r_1_9(unittest.TestCase):

    def test_get_a_list_from_50_to_80_with_step_10_result(self):
        v_list = [50, 60, 70, 80]
        self.assertEqual(v_list, get_a_list_from_50_to_80_with_step_10())

class Test_r_1_10(unittest.TestCase):

    def test_get_a_list_from_8_to_m8_with_step_m2_result(self):
        v_list = [8, 6, 4, 2, 0, -2, -4, -6, -8]
        self.assertEqual(v_list, get_a_list_from_8_to_m8_with_step_m2())

class Test_r_1_11(unittest.TestCase):

    def test_get_list_from_1_to_256_of_power_of_2(self):
        v_list = [1, 2, 4, 8, 16, 32, 64, 128, 256]
        self.assertEqual(v_list, get_list_from_1_to_256_of_power_of_2())

class Test_r_1_12(unittest.TestCase):

    def test_pseudo_choice_with_list(self):
        v_list = ["Konichiwa", 1122, "Salam", 500600, "bratishka"]
        v_elem = pseudo_choice(v_list)
        self.assertTrue(v_elem in v_list)

class Test_c_1_13(unittest.TestCase):

    def test_pseudo_reverse_list(self):
        v_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = pseudo_reverse_list(v_list)
        v_list.reverse()
        self.assertEqual(v_list, result)

class Test_c_1_14(unittest.TestCase):

    def test_is_there_a_distinct_pair_of_numbers_whose_product_is_odd(self):
        # True
        list_with_distinct_pair = [1, 2, 2, 3]
        # False
        list_with_only_even_numbers = [2, 4, 8, 16, 32]
        # False
        list_with_only_odd_but_repeatable_numbers = [3, 3, 3, 19, 19, 19, 29, 29]
        # True 
        list_with_many_distinct_pairs = [99, 101, 103, 105]

        self.assertTrue(is_there_a_distinct_pair_of_numbers_whose_product_id_odd(list_with_distinct_pair))
        self.assertFalse(is_there_a_distinct_pair_of_numbers_whose_product_id_odd(list_with_only_even_numbers))
        self.assertFalse(is_there_a_distinct_pair_of_numbers_whose_product_id_odd(list_with_only_odd_but_repeatable_numbers))
        self.assertTrue(is_there_a_distinct_pair_of_numbers_whose_product_id_odd(list_with_many_distinct_pairs))

class Test_c_1_15(unittest.TestCase):

    def test_is_all_numbers_different_in_seq(self):
        # False
        v_list_repeated_numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        # True
        v_list_distinct_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17]

        self.assertFalse(is_all_numbers_different_in_seq(v_list_repeated_numbers))
        self.assertTrue(is_all_numbers_different_in_seq(v_list_distinct_numbers))

class Test_c_1_16(unittest.TestCase):

    def test_multiply_x_2(self):
        a = 10

        id_before = id(a)
        value_before = a

        multiply_x_2(a)

        id_after = id(a)
        value_after = a

        self.assertEqual(id_before, id_after)
        self.assertEqual(value_before, value_after)

    def test_scale(self):
        data = [1, 2]
        factor = 2 
        
        # Copy values, not references
        value_before = [elem for elem in data]
        id_before = id(data)
        ids_before = [id(elem) for elem in data]

        scale(data, factor)

        # Copy values, not references
        value_after = [elem for elem in data]
        id_after = id(data)
        ids_after = [id(elem) for elem in data]

        self.assertNotEqual(value_before, value_after)
        self.assertEqual(id_before, id_after)
        self.assertNotEqual(ids_before, ids_after)

if __name__ == '__main__':
    unittest.main()

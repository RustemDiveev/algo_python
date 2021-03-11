import unittest
import io
import sys
from unittest.mock import patch
from platform import system
from random import randint, choice 
from statistics import mean
from math import sqrt

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
from ex_1.c_1_17 import scale_incorrect, scale_correct
from ex_1.c_1_18 import produce_list
from ex_1.c_1_19 import produce_list_of_alphabet
from ex_1.c_1_20 import randint_version_of_shuffle, get_randint_probability, get_shuffle_probability 
from ex_1.c_1_21 import reverse_output
from ex_1.c_1_22 import dot_product_of_lists
from ex_1.c_1_23 import list_index_out_of_bounds
from ex_1.c_1_24 import count_vowels_in_str
from ex_1.c_1_25 import get_remove_punctuation
from ex_1.c_1_26 import check_correct_arithmetic_formula
from ex_1.c_1_27 import factors_increase_order
from ex_1.c_1_28 import norm 

#Projects
from ex_1.p_1_29 import get_all_possible_strings_using_character_once
from ex_1.p_1_30 import get_log_of_base_2
from ex_1.p_1_31 import get_change
from ex_1.p_1_32 import process_input, calculate_expression, reset_input, clear_input
from ex_1.p_1_33 import get_type_value_by_key, get_char_type_id, is_char, \
    is_char_number, is_operator, is_equation, is_opening_bracket, is_closing_bracket, \
    is_dot, is_valid_char, is_number, trim_whitespace, is_valid_input, \
    to_char_list, to_char_type_list, С_DICT_CHAR_TYPE, to_token_list, \
    check_char_list_brackets, check_char_list_beginning, check_char_list_ending, \
    check_pattern, check_char_list_operator, check_char_list_equation, check_char_list_dot

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

#Creativity
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

class Test_c_1_17(unittest.TestCase):

    def test_scale_incorrect_works_with_list(self):
        v_input_list = [1, 2, 3]
        for elem in v_input_list:
            elem *= 2
        v_data = [1, 2, 3]
        scale_incorrect(v_data, 2)
        self.assertEqual(v_input_list, v_data) 

    def test_scale_incorrect_works_with_tuple(self):
        v_input_list = (2, 4, 6)
        v_data = (1, 2, 3)
        scale_incorrect(v_data, 2)
        self.assertNotEqual(v_input_list, v_data)

    def test_scale_correct_works_with_list(self):
        v_data = [1, 2, 3]
        v_input_list = [2, 4, 6]
        self.assertEqual(v_input_list, scale_correct(v_data, 2))

    def test_scale_correct_works_with_tuple(self):
        v_data = (1, 2, 3)
        v_input_tuple = (2, 4, 6)
        self.assertEqual(v_input_tuple, scale_correct(v_data, 2))

    def test_scale_correct_works_with_set(self):
        v_data = {1, 2, 3}
        v_input_set = {2, 4, 6}
        self.assertEqual(v_input_set, scale_correct(v_data, 2))

    def test_scale_correct_works_with_frozenset(self):
        v_data = {1, 2, 3}
        v_input_frozenset = frozenset({2, 4, 6})
        self.assertEqual(v_input_frozenset, scale_correct(v_data, 2))

    def test_scale_correct_works_with_dict(self):
        v_data = {"a": 1, "b": 2, "c": 3}
        v_input_dict = {"a": 2, "b": 4, "c": 6}
        self.assertEqual(v_input_dict, scale_correct(v_data, 2))

class Test_c_1_18(unittest.TestCase):

    def test_produce_list(self):
        v_list = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
        self.assertEqual(v_list, produce_list())

class Test_c_1_19(unittest.TestCase):

    def test_produce_list_of_alphabet(self):
        v_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.assertEqual(v_list, produce_list_of_alphabet())

class Test_c_1_20(unittest.TestCase):

    def test_randint_version_of_shuffle(self):
        # Len is same 
        v_list = [1, "a", 2, "b"]
        v_result = randint_version_of_shuffle(v_list)
        self.assertEqual(len(v_list), len(v_result))

        # All elements are same 
        for elem in v_list:
            self.assertTrue(elem in v_result)

    def test_randint_and_shuttle_has_same_probability(self):
        
        # Some empiric method for determination of same probability
        v_list = [1, 2, 3]
        v_observation_num = 1000000
        v_randint_defaultdict = get_randint_probability(i_list=v_list, i_observation_num=v_observation_num)
        v_shuffle_defaultdict = get_shuffle_probability(i_list=v_list, i_observation_num=v_observation_num)
        v_randint_defaultdict_avg_value = mean(v_randint_defaultdict.values())
        v_shuffle_defaultdict_avg_value = mean(v_shuffle_defaultdict.values())

        v_deviation_threshold = 0.005
        v_observation_threshold = v_deviation_threshold * v_observation_num 

        self.assertTrue(abs(v_randint_defaultdict_avg_value - v_shuffle_defaultdict_avg_value) < v_observation_threshold)

class Test_c_1_21(unittest.TestCase):

    @patch('ex_1.c_1_21.get_input', return_value="Hello, kitty!\nKonichiwa!")
    # Wtf is input?
    def test_reverse_output(self, input):
        self.assertEqual("!awihcinoK\n!yttik ,olleH", reverse_output(print_flg=0))

class Test_c_1_22(unittest.TestCase):

    def test_dot_product_of_lists_correct_result(self):
        a_list = [1, 2, 3, 4, 5]
        b_list = [5, 4, 3, 2, 1]
        result_list = [5, 8, 9, 8, 5]

        self.assertEqual(result_list, dot_product_of_lists(a_list=a_list,b_list=b_list))

    def test_dot_product_of_lists_one_of_list_do_not_contains_int(self):
        a_list = ["a", 2 , 3]
        b_list = []
        with self.assertRaises(ValueError):
            dot_product_of_lists(a_list=a_list,b_list=b_list)

    def test_dot_product_of_lists_input_lists_have_different_lengths(self):
        a_list = [1, 2]        
        b_list = [1]
        with self.assertRaises(ValueError):
            dot_product_of_lists(a_list=a_list,b_list=b_list)

class Test_c_1_23(unittest.TestCase):

    def test_compare_print_output(self):
        # Here comes something dangerous
        # Copied from stackoverflow: 
        # https://stackoverflow.com/questions/33767627/python-write-unittest-for-console-print
        v_captured_output = io.StringIO()
        sys.stdout = v_captured_output
        list_index_out_of_bounds()
        sys.stdout = sys.__stdout__ 
        self.assertEqual("Don't try buffer overflow attacks in Python!\n", v_captured_output.getvalue())

class Test_c_1_24(unittest.TestCase):

    def test_count_vowels_in_str_english(self):
        v_str = "One apple a day keeps a doctor away!"
        v_result = 15
        self.assertEqual(v_result, count_vowels_in_str(i_str=v_str))

    def test_count_vowels_in_str_russian(self):
        v_str = "Хочу литровый фобо!"
        v_result = 7
        self.assertEqual(v_result, count_vowels_in_str(i_str=v_str))

class Test_c_1_25(unittest.TestCase):

    def test_get_remove_punctuation(self):
        v_str = "Let's try, Mike."
        v_result = "Lets try Mike"
        self.assertEqual(v_result, get_remove_punctuation(i_str=v_str))

class Test_c_1_26(unittest.TestCase):

    def test_check_correct_arithmetic_formula_correct_equation(self):
        v_tuple = (1, 2, 3)
        self.assertEqual(True, check_correct_arithmetic_formula(i_tuple=v_tuple))

    def test_check_correct_arithmetic_formula_incorrect_equation(self):
        v_tuple = (2, 7, 8)
        self.assertEqual(False, check_correct_arithmetic_formula(i_tuple=v_tuple))

class Test_c_1_27(unittest.TestCase):

    def test_factors_of_100(self):
        v_test = [1,2,4,5,10,20,25,50,100]
        self.assertEqual(v_test, [factor for factor in factors_increase_order(100)])

class Test_c_1_28(unittest.TestCase):

    def test_euclidean_norm_3_4(self):
        v_result = sqrt(3 * 3 + 4 * 4)
        self.assertEqual(v_result, norm([3,4]))

    def test_triple_root_3_4_5(self):
        v_result = (3 * 3 * 3 + 4 * 4 * 4 + 5 * 5 * 5) ** (1/3)
        self.assertEqual(v_result, norm([3,4,5], 3))

class Test_p_1_29(unittest.TestCase):

    def test_empty_string(self):
        i_str = ""
        with self.assertRaises(ValueError):
            get_all_possible_strings_using_character_once(i_str=i_str)

    def test_nonunique_chars_in_string(self):
        i_str = "alibaba"
        with self.assertRaises(ValueError):
            get_all_possible_strings_using_character_once(i_str=i_str)

    def test_that_result_is_correct(self):
        """
            1. Length must be equal to len(i_str)! (factorial)
            2. All strings must be unique
        """
        i_str = "catdog"
        v_result = get_all_possible_strings_using_character_once(i_str=i_str)
        v_total_combinations = 1

        for i in range(len(i_str)):
            v_total_combinations *= (i + 1)

        self.assertEqual(v_total_combinations, len(v_result))
        self.assertEqual(v_total_combinations, len(set(v_result)))

class Test_p_1_30(unittest.TestCase):

    def test_string_as_param(self):
        with self.assertRaises(TypeError):
            get_log_of_base_2(i_int="I have a dream...")

    def test_input_is_one(self):
        with self.assertRaises(ValueError):
            get_log_of_base_2(i_int=1)

    def test_input_128(self):
        # 2 ** 7 = 128
        v_result = 7
        self.assertEqual(v_result, get_log_of_base_2(i_int=128))

    def test_input_500(self):
        # 500 250 125 62,5 31,25 15,625 ~7,8 3,9 1,95
        v_result = 8
        self.assertEqual(v_result, get_log_of_base_2(i_int=500))

class Test_p_1_31(unittest.TestCase):

    def test_input_params_are_incorrect_money(self):
        with self.assertRaises(ValueError):
            get_change(i_money_charged=3.14159265, i_money_given=2.71828)

    def test_i_cant_afford_it(self):
        with self.assertRaises(ValueError):
            get_change(i_money_charged=20, i_money_given=0)

    def test_change(self):
        self.assertEqual(dict(), get_change(i_money_charged=100, i_money_given=100))
        self.assertEqual({"1000": 2, "100": 3, "10": 4, "5": 1, "0.5": 1, "0.1": 1, "0.05": 1, "0.01": 3}, get_change(i_money_charged=7654.32, i_money_given=10000))

class Test_p_1_32(unittest.TestCase):

    def test_reset_input(self):
        v_input = [1,2,3,4]
        reset_input(io_input=v_input)
        self.assertEqual([1,2,3], v_input) 

    def test_clear_input(self):
        v_input = [1,2,3,4]
        clear_input(io_input=v_input)
        self.assertEqual([], v_input)  

    def test_calculate_expression_random(self):
        v_first_number = randint(-100, 100)
        v_second_number = 0
        while v_second_number == 0:
            v_second_number = randint(-100, 100)
        v_operator = choice("+-*/")

        if v_operator == "+":
            v_result = v_first_number + v_second_number 
        elif v_operator == "-":
            v_result = v_first_number - v_second_number 
        elif v_operator == "*":
            v_result = v_first_number * v_second_number 
        elif v_operator == "/":
            v_result = v_first_number / v_second_number 

        self.assertEqual(v_result, calculate_expression(
            i_first_number=v_first_number, 
            i_second_number=v_second_number, 
            i_operator=v_operator
        ))

    def test_process_input_first_element_is_word(self):
        v_input = ["TESTINK"]
        process_input(io_input=v_input)
        self.assertEqual([], v_input)

    def test_process_input_first_element_is_number(self):
        v_input = ["123.456"]
        process_input(io_input=v_input)
        self.assertEqual(["123.456"], v_input)

    def test_process_input_second_element_is_operator(self):
        v_input = ["123,456", "*"]
        process_input(io_input=v_input)
        self.assertEqual(["123,456", "*"], v_input)

    def test_process_input_second_element_is_word(self):
        v_input = ["8.555", "Plus"]
        process_input(io_input=v_input)
        self.assertEqual(["8.555"], v_input)

    def test_process_input_fourth_element_is_not_equation(self):
        v_input = ["8.555", "+", "10.23", "*"]
        process_input(io_input=v_input)
        self.assertEqual(["8.555", "+", "10.23"], v_input)

    def test_process_input_is_a_valid_arithmetical_expression(self):
        v_input = ["30", "+", "20", "="]
        process_input(io_input=v_input)
        self.assertEqual([], v_input)

class Test_p_1_33(unittest.TestCase):

    def test_get_type_value_by_key_known(self):
        # ID of NUMBER
        l_result = 1
        self.assertEqual(l_result, get_type_value_by_key(p_str="NUMBER"))

    def test_get_type_value_by_key_unknown(self):
        # ID of UNKNOWN
        l_result = 99
        self.assertEqual(l_result, get_type_value_by_key(p_str="BLABLABLA"))
    
    def test_get_char_type_id_all_known(self):
        l_input_list = ["1", "-", "+", "=", "(", ")", ".", "$"]
        l_result_list = [1, 7, 2, 3, 4, 5, 6, 99]
        for idx in range(len(l_input_list) - 1):
            self.assertEqual(l_result_list[idx], get_char_type_id(p_char=l_input_list[idx]))

    def test_get_char_type_id_unknown(self):
        l_input_str = "l"
        l_result = 99
        self.assertEqual(l_result, get_char_type_id(p_char=l_input_str))

    def test_is_char_input_is_symbol(self):
        self.assertTrue(is_char(p_str="a"))

    def test_is_char_input_str_is_greater_than_1(self):
        self.assertFalse(is_char(p_str="abc"))

    def test_is_char_input_is_symbol_and_check_symbol_valid(self):
        self.assertTrue(is_char(p_str="a", p_check_symbol="a")) 

    def test_is_char_input_is_symbol_and_check_symbol_invalid(self):
        self.assertFalse(is_char(p_str="a", p_check_symbol="b"))  

    def test_is_char_input_str_is_greater_than_1_and_check_symbol_valid(self):
        with self.assertRaises(ValueError):
            is_char(p_str="abc", p_check_symbol="abc")

    def test_is_char_number_valid(self):
        self.assertTrue(is_char_number(p_char="1")) 

    def test_is_char_number_invalid(self):
        self.assertFalse(is_char_number(p_char="a"))  

    def test_is_operator_valid(self):
        self.assertTrue(is_operator(p_char="+"))

    def test_is_operator_invalid(self):
        self.assertFalse(is_operator(p_char="1"))

    def test_is_equation_valid(self):
        self.assertTrue(is_equation(p_char="=")) 

    def test_is_equation_invalid(self):
        self.assertFalse(is_equation(p_char="+")) 

    def test_is_opening_bracket_valid(self):
        self.assertTrue(is_opening_bracket(p_char="(")) 

    def test_is_opening_bracket_invalid(self):
        self.assertFalse(is_opening_bracket(p_char="=")) 

    def test_is_closing_bracket_valid(self):
        self.assertTrue(is_closing_bracket(p_char=")")) 

    def test_is_closing_bracket_invalid(self):
        self.assertFalse(is_closing_bracket(p_char="("))  

    def test_is_dot_valid(self):
        self.assertTrue(is_dot(p_char=".")) 

    def test_is_dot_invalid(self):
        self.assertFalse(is_dot(p_char=")")) 

    def test_is_valid_char_valid(self):
        self.assertTrue(is_valid_char(p_char="9")) 

    def test_is_valid_char_invalid(self):
        self.assertFalse(is_valid_char(p_char="["))  

    def test_is_number_valid(self):
        self.assertTrue(is_number(p_str="23.23")) 

    def test_is_number_invalid(self):
        self.assertFalse(is_number(p_str="azaz.asd")) 

    def test_trim_whitespace(self):
        l_str = "       OH!!!       MYYYY!!!      "
        l_result = "OH!!!MYYYY!!!"
        self.assertEqual(l_result, trim_whitespace(p_str=l_str))

    def test_is_valid_input_empty(self):
        l_result = (False, "INFO: Ничего не введено. Введите выражение для расчета.")
        self.assertEqual(l_result, is_valid_input(p_str="")) 

    def test_is_valid_input_valid(self):
        self.assertTrue(is_valid_input(p_str="20+20-20*(3+7)")[0]) 

    def test_is_valid_input_invalid(self):
        self.assertFalse(is_valid_input(p_str="abc30*(20-10)+")[0]) 

    def test_to_char_list_valid(self):
        l_input_str = "8+3-4"
        l_result = ["8", "+", "3", "-", "4"]
        self.assertEqual(l_result, to_char_list(p_str=l_input_str))

    def test_to_char_type_list_valid(self):
        l_input_list = ["8", "+", "3", "-", "(", "2", ".", "1", "/", "4", ")", "="]
        d = С_DICT_CHAR_TYPE
        l_result = to_char_type_list(p_char_list=l_input_list) 
        l_expected_result = [d["NUMBER"], d["OPERATOR"], d["NUMBER"], d["OPERATOR_MINUS"], d["OPENING_BRACKET"], 
            d["NUMBER"], d["DOT"], d["NUMBER"], d["OPERATOR"], d["NUMBER"], d["CLOSING_BRACKET"], d["EQUATION"]]
        self.assertEqual(l_expected_result, l_result)

    # Для оставшихся тестов исходим из утверждения, что to_char_list, to_char_type_list - корректны 
    # На будущее - верно ли так поступать, или надо всегда тестировать модульно, и писать ручками нужные данные?
    def test_to_token_list_1(self):
        l_str = "234.3213+1322134.3213"
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        l_expected_result = [234.3213, "+", 1322134.3213]
        self.assertEqual(l_expected_result, to_token_list(p_char_list=l_char_list, p_char_type_list=l_char_type_list))

    def test_to_token_list_2(self):
        l_str = "(-123.123)+(-4213.123)"
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        l_expected_result = [-123.123, "+", -4213.123]
        self.assertEqual(l_expected_result, to_token_list(p_char_list=l_char_list, p_char_type_list=l_char_type_list))

    def test_to_token_list_3(self):
        l_str = "((200.2342-(-3213.3214)))"
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        l_expected_result = ["(", "(", 200.2342, "-", -3213.3214, ")", ")"]
        self.assertEqual(l_expected_result, to_token_list(p_char_list=l_char_list, p_char_type_list=l_char_type_list))

    def test_check_char_list_brackets_valid(self):
        l_str = "(((())))()()(())(()())"
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual((True, ""), check_char_list_brackets(p_char_type_list=l_char_type_list))

    def test_check_char_list_brackets_invalid(self):
        l_str = "(((())))()()(())(()()"
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (False, "ERROR: В выражении неправильно расставлены скобки. Отсутствует закрывающая скобка."), 
            check_char_list_brackets(p_char_type_list=l_char_type_list)
        )

    def test_check_char_list_beginning_valid(self):
        l_str = "50123+12313"
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (True, ""),
            check_char_list_beginning(p_char_type_list=l_char_type_list)
        )

    def test_check_char_list_beginning_invalid(self):
        l_str = "+123.32+321-123/321"
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (False, "ERROR: Выражение должно начинаться с открывающейся скобки или числа"),
            check_char_list_beginning(p_char_type_list=l_char_type_list)
        )

    def test_check_char_list_ending_valid(self):
        l_str = "50123+12313"
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (True, ""),
            check_char_list_ending(p_char_type_list=l_char_type_list)
        )

    def test_check_char_list_ending_invalid(self):
        l_str = "123.32+321-123/321+"
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (False, "ERROR: Выражение должно заканчиваться на закрывающуюся скобку, число или знак равенства"),
            check_char_list_ending(p_char_type_list=l_char_type_list)
        )

    def test_check_pattern_valid(self):
        l_str = "1+"
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertTrue(check_pattern(p_char_type_list=l_char_type_list, p_first_key="NUMBER", p_second_key="OPERATOR"))

    def test_check_pattern_invalid(self):
        l_str = "+1"
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertFalse(check_pattern(p_char_type_list=l_char_type_list, p_first_key="NUMBER", p_second_key="OPERATOR"))

    def test_check_char_list_operator_valid(self):
        l_str = "1+2-(3/2)="
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (True, ""),
            check_char_list_operator(p_char_type_list=l_char_type_list)
        )

    def test_check_char_list_operator_invalid_operator_x_closing_bracket(self):
        l_str = "+)" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (False, "ERROR: Неправильное выражение - за оператором следует закрывающая скобка"),
            check_char_list_operator(p_char_type_list=l_char_type_list)
        )

    def test_check_char_list_operator_invalid_opening_bracket_x_operator(self):
        l_str = "(+" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (False, "ERROR: Неправильное выражение - оператор следует сразу после открывающей скобки"),
            check_char_list_operator(p_char_type_list=l_char_type_list)
        )

    def test_check_char_list_operator_invalid_operator_x_dot(self):
        l_str = "+." 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (False, "ERROR: Неправильное выражение - после оператора следует разделитель числа"),
            check_char_list_operator(p_char_type_list=l_char_type_list)
        )

    def test_check_char_list_operator_invalid_dot_x_operator(self):
        l_str = ".+" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (False, "ERROR: Неправильное выражение - разделитель числа следует перед оператором"),
            check_char_list_operator(p_char_type_list=l_char_type_list)
        )

    def test_check_char_list_operator_invalid_equation_x_operator(self):
        l_str = "=+" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (False, "ERROR: Неправильное выражение - знак равенства следует перед оператором"),
            check_char_list_operator(p_char_type_list=l_char_type_list)
        )

    def test_check_char_list_operator_invalid_operator_x_equation(self):
        l_str = "+=" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (False, "ERROR: Неправильное выражение - равенство следует после оператора"),
            check_char_list_operator(p_char_type_list=l_char_type_list)
        )

    def test_check_char_list_operator_invalid_operator_x_operator(self):
        l_str = "++" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (False, "ERROR: Неправильное выражение - два оператора следуют подряд"),
            check_char_list_operator(p_char_type_list=l_char_type_list)
        )

    def test_check_char_list_operator_invalid_operator_minus_x_closing_bracket(self):
        l_str = "-)" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (False, "ERROR: Неправильное выражение - за оператором следует закрывающая скобка"),
            check_char_list_operator(p_char_type_list=l_char_type_list)
        )       

    def test_check_char_list_operator_invalid_operator_minus_x_dot(self):
        l_str = "-." 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (False, "ERROR: Неправильное выражение - после оператора следует разделитель числа"),
            check_char_list_operator(p_char_type_list=l_char_type_list)
        )      

    def test_check_char_list_operator_invalid_dot_x_operator_minus(self):
        l_str = ".-" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (False, "ERROR: Неправильное выражение - разделитель числа следует перед оператором"),
            check_char_list_operator(p_char_type_list=l_char_type_list)
        )      

    def test_check_char_list_operator_invalid_equation_x_operator_minus(self):
        l_str = "=-" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (False, "ERROR: Неправильное выражение - знак равенства следует перед оператором"),
            check_char_list_operator(p_char_type_list=l_char_type_list)
        )      

    def test_check_char_list_operator_invalid_operator_minus_x_equation(self):
        l_str = "-=" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (False, "ERROR: Неправильное выражение - равенство следует после оператора"),
            check_char_list_operator(p_char_type_list=l_char_type_list)
        )      

    def test_check_char_list_operator_invalid_minus_x_minus(self):
        l_str = "--" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (False, "ERROR: Неправильное выражение - два оператора следуют подряд"),
            check_char_list_operator(p_char_type_list=l_char_type_list)
        )      

    def test_check_char_list_operator_invalid_minus_x_operator(self):
        l_str = "-+" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (False, "ERROR: Неправильное выражение - два оператора следуют подряд"),
            check_char_list_operator(p_char_type_list=l_char_type_list)
        )     

    def test_check_char_list_operator_invalid_operator_x_minus(self):
        l_str = "+-" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (False, "ERROR: Неправильное выражение - два оператора следуют подряд"),
            check_char_list_operator(p_char_type_list=l_char_type_list)
        )     

    def check_char_list_equation_valid(self):
        l_str = "1+2=" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (True, ""),
            check_char_list_equation(p_char_type_list=l_char_type_list)
        )     

    def check_char_list_equation_invalid(self):
        l_str = "=11+22" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (False, "ERROR: Знак равенства может быть только один и должен находиться в конце выражения"),
            check_char_list_equation(p_char_type_list=l_char_type_list)
        )     

    def check_char_list_dot_valid(self):
        l_str = "1.123+123.321" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (True, ""),
            check_char_list_dot(p_char_type_list=l_char_type_list)
        )     
    def check_char_list_dot_invalid_no_number_before(self):
        l_str = ".321-23" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (False, "ERROR: Перед разделителем числа не найдено цифры"),
            check_char_list_operator(p_char_type_list=l_char_type_list)
        )     

    def check_char_list_dot_invalid_no_number_after(self):
        l_str = "23-3." 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (False, "ERROR: После разделителя числа не найдено цифры"),
            check_char_list_operator(p_char_type_list=l_char_type_list)
        )     

if __name__ == '__main__':
    unittest.main()

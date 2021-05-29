import unittest
import io
import sys
from unittest.mock import patch
from platform import system
from random import randint, choice 
from statistics import mean
from math import sqrt
from datetime import date 

# WTF
# To run this file use: 
# from r1 import is_multiple
# VSC issue afaiu

#Reinforcement
from e1.r1 import is_multiple
from e1.r2 import is_even
from e1.r3 import minmax
from e1.r4 import get_sum_of_squares
from e1.r5 import get_sum_of_squares_with_sum, \
    get_sum_of_squares_with_sum_and_iterator
from e1.r6 import get_sum_of_squares_of_odd_ints
from e1.r8 import get_str_positive_idx_by_negaive_idx
from e1.r9 import get_a_list_from_50_to_80_with_step_10
from e1.r10 import get_a_list_from_8_to_m8_with_step_m2
from e1.r11 import get_list_from_1_to_256_of_power_of_2
from e1.r12 import pseudo_choice

#Creativity
from e1.c13 import pseudo_reverse_list
from e1.c14 import is_there_a_distinct_pair_of_numbers_whose_product_id_odd
from e1.c15 import is_all_numbers_different_in_seq
from e1.c16 import scale, multiply_x_2
from e1.c17 import scale_incorrect, scale_correct
from e1.c18 import produce_list
from e1.c19 import produce_list_of_alphabet
from e1.c20 import randint_version_of_shuffle, get_randint_probability, get_shuffle_probability 
from e1.c21 import reverse_output
from e1.c22 import dot_product_of_lists
from e1.c23 import list_index_out_of_bounds
from e1.c24 import count_vowels_in_str
from e1.c25 import get_remove_punctuation
from e1.c26 import check_correct_arithmetic_formula
from e1.c27 import factors_increase_order
from e1.c28 import norm 

#Projects
from e1.p29 import get_all_possible_strings_using_character_once
from e1.p30 import get_log_of_base_2
from e1.p31 import get_change
from e1.p32 import process_input, calculate_expression, reset_input, clear_input
from e1.p33 import C_TYPE_ID_CLOSING_BRACKET, C_TYPE_ID_MINUS, C_TYPE_ID_NUMBER, C_TYPE_ID_OPENING_BRACKET, C_TYPE_ID_OPERATOR, get_type_value_by_key, get_char_type_id, is_char, \
    is_char_number, is_operator, is_equation, is_opening_bracket, is_closing_bracket, \
    is_dot, is_valid_char, is_number, trim_whitespace, is_valid_input, \
    to_char_list, to_char_type_list, С_DICT_CHAR_TYPE, to_token_list, \
    check_char_list_brackets, check_char_list_beginning, check_char_list_ending, \
    check_pattern, check_char_list_operator, check_char_list_equation, check_char_list_dot, \
    check_char_list, get_expression_list, is_bracket_expression_exists, \
    to_simple_expression_list, get_result, clear, reset, is_input_a_calculator_option, \
    process_input as p_1_33_process_input, calculate
from e1.p34 import error_generator_add_one_random_symbol_to_random_place, error_generator_change_random_symbol_register, error_generator_copy_random_symbol, \
    error_generator_remove_one_random_symbol, error_generator_replace_random_vowel, error_generator_replace_random_consonant, \
    error_generator_remove_dot_from_end, error_generator_remove_random_space, get_list_of_error_sentences
from e1.p35 import generate_birthday, generate_birthdays, count_birthdays, are_same_birthdays_in_list

#Reinforcement
class Test_r1(unittest.TestCase):

    def test_is_100_multiple_of_2(self):
        self.assertTrue(is_multiple(100, 2))

    def test_is_40_multiple_of_3(self):
        self.assertFalse(is_multiple(40, 3))

    def test_if_both_input_params_are_strings(self):
        with self.assertRaises(TypeError):
            is_multiple('a', 'b')

class Test_r2(unittest.TestCase):

    def test_is_100_even(self):
        self.assertTrue(is_even(100))

    def test_is_65_even(self):
        self.assertFalse(is_even(65))

    def test_is_even_if_string_specified(self):
        with self.assertRaises(TypeError):
            is_even('blablabla')

class Test_r3(unittest.TestCase):

    def test_minmax_for_range_between_76_and_835(self):
        self.assertEqual((76, 835), minmax(list(range(76, 836))))

    def test_minmax_for_list_of_random_numbers(self):
        l_list_length = randint(100, 10000)
        l_list = [randint(1, 9999) for elem in range(l_list_length)]
        l_min = min(l_list)
        l_max = max(l_list)
        self.assertEqual((l_min, l_max), minmax(l_list))

    def test_minmax_if_there_is_a_one_string_in_list(self):
        l_list = ["kill me plz"]
        with self.assertRaises(ValueError):
            minmax(l_list)

    def test_minmax_if_some_list_elements_are_strings(self):
        l_list = [111, 222, "aaa", "bbb", 333]
        with self.assertRaises(TypeError):
            minmax(l_list)

class Test_r4(unittest.TestCase):

    def test_sum_of_squares_from_1_to_4(self):
        l_sum = 1*1 + 2*2 + 3*3 + 4*4
        self.assertEqual(l_sum, get_sum_of_squares(5))

    def test_sum_of_squares_from_1_to_9999(self):
        l_sum = sum([num * num for num in range(1,10000)])
        self.assertEqual(l_sum, get_sum_of_squares(10000))

    def test_sum_of_squares_with_input_is_negative_int(self):
        with self.assertRaises(ValueError):
            get_sum_of_squares(-200)

    def test_sum_of_squares_with_input_is_string(self):
        with self.assertRaises(ValueError):
            get_sum_of_squares("blah blah blah, mr Freeman!")

class Test_r5(unittest.TestCase):

    def test_sum_of_squares_with_sum_from_1_to_4(self):
        l_sum = 1*1 + 2*2 + 3*3 + 4*4
        self.assertEqual(l_sum, get_sum_of_squares_with_sum(5))

    def test_sum_of_squares_with_sum_from_1_to_9999(self):
        l_sum = sum([num * num for num in range(1,10000)])
        self.assertEqual(l_sum, get_sum_of_squares_with_sum(10000))

    def test_sum_of_squares_with_sum_with_input_is_negative_int(self):
        with self.assertRaises(ValueError):
            get_sum_of_squares_with_sum(-200)

    def test_sum_of_squares_with_sum_with_input_is_string(self):
        with self.assertRaises(ValueError):
            get_sum_of_squares_with_sum("blah blah blah, mr Freeman!")

    def test_sum_of_squares_with_sum_and_iterator_from_1_to_4(self):
        l_sum = 1*1 + 2*2 + 3*3 + 4*4
        self.assertEqual(l_sum, get_sum_of_squares_with_sum_and_iterator(5))

    def test_sum_of_squares_with_sum_and_iterator_from_1_to_9999(self):
        l_sum = sum([num * num for num in range(1,10000)])
        self.assertEqual(l_sum, get_sum_of_squares_with_sum_and_iterator(10000))

    def test_sum_of_squares_with_sum_and_iterator_with_input_is_negative_int(self):
        with self.assertRaises(ValueError):
            get_sum_of_squares_with_sum_and_iterator(-200)

    def test_sum_of_squares_with_sum_and_iterator_with_input_is_string(self):
        with self.assertRaises(ValueError):
            get_sum_of_squares_with_sum_and_iterator("blah blah blah, mr Freeman!")

class Test_r6(unittest.TestCase):

    def test_sum_of_squares_of_odd_ints_less_than_5(self):
        l_sum = 1*1 + 3*3 
        self.assertEqual(l_sum, get_sum_of_squares_of_odd_ints(5))

    def test_sum_of_squares_of_odd_ints_less_than_1000(self):
        l_sum = 0
        for num in range(1000):
            if num % 2 == 1:
                l_sum += num * num
        self.assertEqual(l_sum, get_sum_of_squares_of_odd_ints(1000))

    def test_sum_of_squares_of_odd_ints_if_input_is_str(self):
        with self.assertRaises(TypeError):
            get_sum_of_squares_of_odd_ints("Salam!")

class Test_r8(unittest.TestCase):

    def test_get_str_positive_idx_of_str_confuse_a_cat(self):
        l_str = "Confuse-a-cat!"
        l_str_len = len(l_str)
        l_neg_idx = randint(-1 * l_str_len, -1)
        l_pos_idx = get_str_positive_idx_by_negaive_idx(l_str_len, l_neg_idx)
        self.assertEqual(l_str[l_neg_idx], l_str[l_pos_idx])

    def test_get_str_positive_idx_if_neg_idx_is_greater_than_zero(self):
        with self.assertRaises(ValueError):
            get_str_positive_idx_by_negaive_idx(p_length=5, p_negative_index=5) 

    def test_get_str_positive_idx_if_neg_idx_exceeds_str_length(self):
        with self.assertRaises(ValueError):
            get_str_positive_idx_by_negaive_idx(p_length=5, p_negative_index=-10) 

class Test_r9(unittest.TestCase):

    def test_get_a_list_from_50_to_80_with_step_10_result(self):
        l_list = [50, 60, 70, 80]
        self.assertEqual(l_list, get_a_list_from_50_to_80_with_step_10())

class Test_r10(unittest.TestCase):

    def test_get_a_list_from_8_to_m8_with_step_m2_result(self):
        l_list = [8, 6, 4, 2, 0, -2, -4, -6, -8]
        self.assertEqual(l_list, get_a_list_from_8_to_m8_with_step_m2())

class Test_r11(unittest.TestCase):

    def test_get_list_from_1_to_256_of_power_of_2(self):
        l_list = [1, 2, 4, 8, 16, 32, 64, 128, 256]
        self.assertEqual(l_list, get_list_from_1_to_256_of_power_of_2())

class Test_r12(unittest.TestCase):

    def test_pseudo_choice_with_list(self):
        l_list = ["Konichiwa", 1122, "Salam", 500600, "bratishka"]
        l_elem = pseudo_choice(l_list)
        self.assertTrue(l_elem in l_list)

#Creativity
class Test_c13(unittest.TestCase):

    def test_pseudo_reverse_list(self):
        l_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        l_result = pseudo_reverse_list(l_list)
        l_list.reverse()
        self.assertEqual(l_list, l_result)

class Test_c14(unittest.TestCase):

    def test_is_there_a_distinct_pair_of_numbers_whose_product_is_odd(self):
        # True
        l_list_with_distinct_pair = [1, 2, 2, 3]
        # False
        l_list_with_only_even_numbers = [2, 4, 8, 16, 32]
        # False
        l_list_with_only_odd_but_repeatable_numbers = [3, 3, 3, 19, 19, 19, 29, 29]
        # True 
        l_list_with_many_distinct_pairs = [99, 101, 103, 105]

        self.assertTrue(is_there_a_distinct_pair_of_numbers_whose_product_id_odd(l_list_with_distinct_pair))
        self.assertFalse(is_there_a_distinct_pair_of_numbers_whose_product_id_odd(l_list_with_only_even_numbers))
        self.assertFalse(is_there_a_distinct_pair_of_numbers_whose_product_id_odd(l_list_with_only_odd_but_repeatable_numbers))
        self.assertTrue(is_there_a_distinct_pair_of_numbers_whose_product_id_odd(l_list_with_many_distinct_pairs))

class Test_c15(unittest.TestCase):

    def test_is_all_numbers_different_in_seq(self):
        # False
        l_list_repeated_numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        # True
        l_list_distinct_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17]

        self.assertFalse(is_all_numbers_different_in_seq(l_list_repeated_numbers))
        self.assertTrue(is_all_numbers_different_in_seq(l_list_distinct_numbers))

class Test_c16(unittest.TestCase):

    def test_multiply_x_2(self):
        a = 10
        l_id_before = id(a)
        l_value_before = a

        multiply_x_2(a)

        l_id_after = id(a)
        l_value_after = a

        self.assertEqual(l_id_before, l_id_after)
        self.assertEqual(l_value_before, l_value_after)

    def test_scale(self):
        l_data = [1, 2]
        l_factor = 2 
        
        # Copy values, not references
        l_value_before = [elem for elem in l_data]
        l_id_before = id(l_data)
        l_ids_before = [id(elem) for elem in l_data]

        scale(l_data, l_factor)

        # Copy values, not references
        l_value_after = [elem for elem in l_data]
        l_id_after = id(l_data)
        l_ids_after = [id(elem) for elem in l_data]

        self.assertNotEqual(l_value_before, l_value_after)
        self.assertEqual(l_id_before, l_id_after)
        self.assertNotEqual(l_ids_before, l_ids_after)

class Test_c17(unittest.TestCase):

    def test_scale_incorrect_works_with_list(self):
        l_input_list = [1, 2, 3]
        for elem in l_input_list:
            elem *= 2
        l_data = [1, 2, 3]
        scale_incorrect(l_data, 2)
        self.assertEqual(l_input_list, l_data) 

    def test_scale_incorrect_works_with_tuple(self):
        l_input_list = (2, 4, 6)
        l_data = (1, 2, 3)
        scale_incorrect(l_data, 2)
        self.assertNotEqual(l_input_list, l_data)

    def test_scale_correct_works_with_list(self):
        l_data = [1, 2, 3]
        l_input_list = [2, 4, 6]
        self.assertEqual(l_input_list, scale_correct(l_data, 2))

    def test_scale_correct_works_with_tuple(self):
        l_data = (1, 2, 3)
        l_input_tuple = (2, 4, 6)
        self.assertEqual(l_input_tuple, scale_correct(l_data, 2))

    def test_scale_correct_works_with_set(self):
        l_data = {1, 2, 3}
        l_input_set = {2, 4, 6}
        self.assertEqual(l_input_set, scale_correct(l_data, 2))

    def test_scale_correct_works_with_frozenset(self):
        l_data = {1, 2, 3}
        l_input_frozenset = frozenset({2, 4, 6})
        self.assertEqual(l_input_frozenset, scale_correct(l_data, 2))

    def test_scale_correct_works_with_dict(self):
        l_data = {"a": 1, "b": 2, "c": 3}
        l_input_dict = {"a": 2, "b": 4, "c": 6}
        self.assertEqual(l_input_dict, scale_correct(l_data, 2))

class Test_c18(unittest.TestCase):

    def test_produce_list(self):
        l_list = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
        self.assertEqual(l_list, produce_list())

class Test_c19(unittest.TestCase):

    def test_produce_list_of_alphabet(self):
        l_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.assertEqual(l_list, produce_list_of_alphabet())

class Test_c20(unittest.TestCase):

    def test_randint_version_of_shuffle(self):
        # Len is same 
        l_list = [1, "a", 2, "b"]
        l_result = randint_version_of_shuffle(l_list)
        self.assertEqual(len(l_list), len(l_result))

        # All elements are same 
        for elem in l_list:
            self.assertTrue(elem in l_result)

    def test_randint_and_shuttle_has_same_probability(self):
        
        # Some empiric method for determination of same probability
        l_list = [1, 2, 3]
        l_observation_num = 1000000
        l_randint_defaultdict = get_randint_probability(p_list=l_list, p_observation_num=l_observation_num)
        l_shuffle_defaultdict = get_shuffle_probability(p_list=l_list, p_observation_num=l_observation_num)
        l_randint_defaultdict_avg_value = mean(l_randint_defaultdict.values())
        l_shuffle_defaultdict_avg_value = mean(l_shuffle_defaultdict.values())

        l_deviation_threshold = 0.005
        l_observation_threshold = l_deviation_threshold * l_observation_num 

        self.assertTrue(abs(l_randint_defaultdict_avg_value - l_shuffle_defaultdict_avg_value) < l_observation_threshold)

class Test_c21(unittest.TestCase):

    @patch('e1.c21.get_input', return_value="Hello, kitty!\nKonichiwa!")
    # Wtf is input?
    def test_reverse_output(self, input):
        self.assertEqual("!awihcinoK\n!yttik ,olleH", reverse_output(p_print_flg=0))

class Test_c22(unittest.TestCase):

    def test_dot_product_of_lists_correct_result(self):
        l_a_list = [1, 2, 3, 4, 5]
        l_b_list = [5, 4, 3, 2, 1]
        l_result_list = [5, 8, 9, 8, 5]

        self.assertEqual(l_result_list, dot_product_of_lists(p_a_list=l_a_list,p_b_list=l_b_list))

    def test_dot_product_of_lists_one_of_list_do_not_contains_int(self):
        l_a_list = ["a", 2 , 3]
        l_b_list = []
        with self.assertRaises(ValueError):
            dot_product_of_lists(p_a_list=l_a_list,p_b_list=l_b_list)

    def test_dot_product_of_lists_input_lists_have_different_lengths(self):
        l_a_list = [1, 2]        
        l_b_list = [1]
        with self.assertRaises(ValueError):
            dot_product_of_lists(p_a_list=l_a_list,p_b_list=l_b_list)

class Test_c23(unittest.TestCase):

    def test_compare_print_output(self):
        # Here comes something dangerous
        # Copied from stackoverflow: 
        # https://stackoverflow.com/questions/33767627/python-write-unittest-for-console-print
        l_captured_output = io.StringIO()
        sys.stdout = l_captured_output
        list_index_out_of_bounds()
        sys.stdout = sys.__stdout__ 
        self.assertEqual("Don't try buffer overflow attacks in Python!\n", l_captured_output.getvalue())

class Test_c24(unittest.TestCase):

    def test_count_vowels_in_str_english(self):
        l_str = "One apple a day keeps a doctor away!"
        l_result = 15
        self.assertEqual(l_result, count_vowels_in_str(p_str=l_str))

    def test_count_vowels_in_str_russian(self):
        l_str = "Хочу литровый фобо!"
        l_result = 7
        self.assertEqual(l_result, count_vowels_in_str(p_str=l_str))

class Test_c25(unittest.TestCase):

    def test_get_remove_punctuation(self):
        l_str = "Let's try, Mike."
        l_result = "Lets try Mike"
        self.assertEqual(l_result, get_remove_punctuation(p_str=l_str))

class Test_c26(unittest.TestCase):

    def test_check_correct_arithmetic_formula_correct_equation(self):
        l_tuple = (1, 2, 3)
        self.assertEqual(True, check_correct_arithmetic_formula(p_tuple=l_tuple))

    def test_check_correct_arithmetic_formula_incorrect_equation(self):
        l_tuple = (2, 7, 8)
        self.assertEqual(False, check_correct_arithmetic_formula(p_tuple=l_tuple))

class Test_c27(unittest.TestCase):

    def test_factors_of_100(self):
        l_test = [1,2,4,5,10,20,25,50,100]
        self.assertEqual(l_test, [factor for factor in factors_increase_order(100)])

class Test_c28(unittest.TestCase):

    def test_euclidean_norm_3_4(self):
        l_result = sqrt(3 * 3 + 4 * 4)
        self.assertEqual(l_result, norm([3,4]))

    def test_triple_root_3_4_5(self):
        l_result = (3 * 3 * 3 + 4 * 4 * 4 + 5 * 5 * 5) ** (1/3)
        self.assertEqual(l_result, norm([3,4,5], 3))

class Test_p29(unittest.TestCase):

    def test_empty_string(self):
        l_str = ""
        with self.assertRaises(ValueError):
            get_all_possible_strings_using_character_once(p_str=l_str)

    def test_nonunique_chars_in_string(self):
        l_str = "alibaba"
        with self.assertRaises(ValueError):
            get_all_possible_strings_using_character_once(p_str=l_str)

    def test_that_result_is_correct(self):
        """
            1. Length must be equal to len(i_str)! (factorial)
            2. All strings must be unique
        """
        l_str = "catdog"
        l_result = get_all_possible_strings_using_character_once(p_str=l_str)
        l_total_combinations = 1

        for i in range(len(l_str)):
            l_total_combinations *= (i + 1)

        self.assertEqual(l_total_combinations, len(l_result))
        self.assertEqual(l_total_combinations, len(set(l_result)))

class Test_p30(unittest.TestCase):

    def test_string_as_param(self):
        with self.assertRaises(TypeError):
            get_log_of_base_2(p_int="I have a dream...")

    def test_input_is_one(self):
        with self.assertRaises(ValueError):
            get_log_of_base_2(p_int=1)

    def test_input_128(self):
        # 2 ** 7 = 128
        l_result = 7
        self.assertEqual(l_result, get_log_of_base_2(p_int=128))

    def test_input_500(self):
        # 500 250 125 62,5 31,25 15,625 ~7,8 3,9 1,95
        l_result = 8
        self.assertEqual(l_result, get_log_of_base_2(p_int=500))

class Test_p31(unittest.TestCase):

    def test_input_params_are_incorrect_money(self):
        with self.assertRaises(ValueError):
            get_change(p_money_charged=3.14159265, p_money_given=2.71828)

    def test_i_cant_afford_it(self):
        with self.assertRaises(ValueError):
            get_change(p_money_charged=20, p_money_given=0)

    def test_change(self):
        self.assertEqual(dict(), get_change(p_money_charged=100, p_money_given=100))
        self.assertEqual({"1000": 2, "100": 3, "10": 4, "5": 1, "0.5": 1, "0.1": 1, "0.05": 1, "0.01": 3}, get_change(p_money_charged=7654.32, p_money_given=10000))

class Test_p32(unittest.TestCase):

    def test_reset_input(self):
        l_input = [1,2,3,4]
        reset_input(po_input=l_input)
        self.assertEqual([1,2,3], l_input) 

    def test_clear_input(self):
        l_input = [1,2,3,4]
        clear_input(po_input=l_input)
        self.assertEqual([], l_input)  

    def test_calculate_expression_random(self):
        l_first_number = randint(-100, 100)
        l_second_number = 0
        while l_second_number == 0:
            l_second_number = randint(-100, 100)
        l_operator = choice("+-*/")

        if l_operator == "+":
            l_result = l_first_number + l_second_number 
        elif l_operator == "-":
            l_result = l_first_number - l_second_number 
        elif l_operator == "*":
            l_result = l_first_number * l_second_number 
        elif l_operator == "/":
            l_result = l_first_number / l_second_number 

        self.assertEqual(l_result, calculate_expression(
            p_first_number=l_first_number, 
            p_second_number=l_second_number, 
            p_operator=l_operator
        ))

    def test_process_input_first_element_is_word(self):
        l_input = ["TESTINK"]
        process_input(po_input=l_input)
        self.assertEqual([], l_input)

    def test_process_input_first_element_is_number(self):
        l_input = ["123.456"]
        process_input(po_input=l_input)
        self.assertEqual(["123.456"], l_input)

    def test_process_input_second_element_is_operator(self):
        l_input = ["123,456", "*"]
        process_input(po_input=l_input)
        self.assertEqual(["123,456", "*"], l_input)

    def test_process_input_second_element_is_word(self):
        l_input = ["8.555", "Plus"]
        process_input(po_input=l_input)
        self.assertEqual(["8.555"], l_input)

    def test_process_input_fourth_element_is_not_equation(self):
        l_input = ["8.555", "+", "10.23", "*"]
        process_input(po_input=l_input)
        self.assertEqual(["8.555", "+", "10.23"], l_input)

    def test_process_input_is_a_valid_arithmetical_expression(self):
        l_input = ["30", "+", "20", "="]
        process_input(po_input=l_input)
        self.assertEqual([], l_input)

class Test_p33(unittest.TestCase):

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

    def test_check_char_list_equation_valid(self):
        l_str = "1+2=" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (True, ""),
            check_char_list_equation(p_char_type_list=l_char_type_list)
        )     

    def test_check_char_list_equation_invalid(self):
        l_str = "=11+22" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (False, "ERROR: Знак равенства может быть только один и должен находиться в конце выражения"),
            check_char_list_equation(p_char_type_list=l_char_type_list)
        )     

    def test_check_char_list_dot_valid(self):
        l_str = "1.123+123.321" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (True, ""),
            check_char_list_dot(p_char_type_list=l_char_type_list)
        )    

    def test_check_char_list_dot_invalid_no_number_before(self):
        l_str = "321-.23" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (False, "ERROR: Перед разделителем числа не найдено цифры"),
            check_char_list_dot(p_char_type_list=l_char_type_list)
        )     

    def test_check_char_list_dot_invalid_no_number_after(self):
        l_str = "23.-3" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertEqual(
            (False, "ERROR: После разделителя числа не найдено цифры"),
            check_char_list_dot(p_char_type_list=l_char_type_list)
        )     

    def test_check_char_list_valid(self):
        l_str = "(1+3)-2" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertTrue(
            check_char_list(p_char_type_list=l_char_type_list)[0]
        )

    def test_check_char_list_invalid_brackets(self):
        l_str = "(1+3)-2)" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertFalse(
            check_char_list(p_char_type_list=l_char_type_list)[0]
        )

    def test_check_char_list_invalid_beginning(self):
        l_str = "+(1+3)-2" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertFalse(
            check_char_list(p_char_type_list=l_char_type_list)[0]
        )

    def test_check_char_list_invalid_ending(self):
        l_str = "(1+3)-2-" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertFalse(
            check_char_list(p_char_type_list=l_char_type_list)[0]
        )

    def test_check_char_list_invalid_operator(self):
        l_str = "(1+3)-+2" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertFalse(
            check_char_list(p_char_type_list=l_char_type_list)[0]
        )

    def test_check_char_list_invalid_equation(self):
        l_str = "(=1+3)+2" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertFalse(
            check_char_list(p_char_type_list=l_char_type_list)[0]
        )

    def test_check_char_list_invalid_dot(self):
        l_str = "(.1+3)+2" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        self.assertFalse(
            check_char_list(p_char_type_list=l_char_type_list)[0]
        )

    def test_get_expression_list_simple(self):
        l_str = "80/8+30-20*4/3" 
        l_expected_result_expression = [80, "/", 8, "+", 30, "-", 20, "*", 4, "/", 3]
        l_expected_result = []
        l_expected_result.append(l_expected_result_expression)
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        l_token_list = to_token_list(p_char_list=l_char_list, p_char_type_list=l_char_type_list)
        l_result = get_expression_list(p_token_list=l_token_list)
        self.assertEqual(l_expected_result, l_result)

    def test_get_expression_list_complex(self):
        l_str = "((80/8)+30)-(20*4/3)"  
        l_expected_result = [
            [80, "/", 8],
            ["expr_0", "+", 30],
            [20, "*", 4, "/", 3],
            ["expr_1", "-", "expr_2"]
        ]
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        l_token_list = to_token_list(p_char_list=l_char_list, p_char_type_list=l_char_type_list)
        l_result = get_expression_list(p_token_list=l_token_list)
        self.assertEqual(l_expected_result, l_result)

    def test_is_bracket_expression_exists_true(self):
        l_list = ["(", 45, "-", 30, ")"]
        self.assertTrue(is_bracket_expression_exists(p_list=l_list))

    def test_is_bracket_expression_exists_false(self):
        l_list = [45, "+", 30, "-", 20]
        self.assertFalse(is_bracket_expression_exists(p_list=l_list))

    def test_to_simple_expression_list_simple(self):
        l_str = "80/8+30-20*4/3" 
        l_expected_result = [
            [
                [80, "/", 8],
                [20, "*", 4],
                ["ref_1", "/", 3],
                ["ref_0", "+", 30],
                ["ref_3", "-", "ref_2"]
            ]
        ] 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        l_token_list = to_token_list(p_char_list=l_char_list, p_char_type_list=l_char_type_list)
        l_expression_list = get_expression_list(p_token_list=l_token_list)
        l_result = to_simple_expression_list(p_expression_list=l_expression_list)
        self.assertEqual(l_expected_result, l_result)

    def test_to_simple_expression_list_complex(self):
        l_str = "((80/8)+30)-(20*4/3)"  
        l_expected_result = [
            [
                [80, "/", 8]
            ],
            [
                ["expr_0", "+", 30]
            ],
            [
                [20, "*", 4],
                ["ref_0", "/", 3]
            ],
            [
                ["expr_1", "-", "expr_2"]
            ]
        ]
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        l_token_list = to_token_list(p_char_list=l_char_list, p_char_type_list=l_char_type_list)
        l_expression_list = get_expression_list(p_token_list=l_token_list)
        l_result = to_simple_expression_list(p_expression_list=l_expression_list)
        self.assertEqual(l_expected_result, l_result)

    def test_get_result_simple(self):
        l_str = "80/8+30-20*4/3" 
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        l_token_list = to_token_list(p_char_list=l_char_list, p_char_type_list=l_char_type_list)
        l_expression_list = get_expression_list(p_token_list=l_token_list)
        l_simple_expression_list = to_simple_expression_list(p_expression_list=l_expression_list)
        l_result = get_result(p_final_expression_list=l_simple_expression_list)
        self.assertEqual(eval(l_str), l_result)

    def test_get_result_complex(self):
        l_str = "((80/8)+30)-(20*4/3)"  
        l_char_list = to_char_list(p_str=l_str)
        l_char_type_list = to_char_type_list(p_char_list=l_char_list)
        l_token_list = to_token_list(p_char_list=l_char_list, p_char_type_list=l_char_type_list)
        l_expression_list = get_expression_list(p_token_list=l_token_list)
        l_simple_expression_list = to_simple_expression_list(p_expression_list=l_expression_list)
        l_result = get_result(p_final_expression_list=l_simple_expression_list)
        self.assertEqual(eval(l_str), l_result)

    def test_clear_result_list_is_not_empty(self):
        l_result_list = [1, 2, 3] 
        l_result = "INFO: Список результатов вычислений очищен. Введите арифметическое выражение для расчета."
        self.assertEqual(l_result, clear(p_result_list=l_result_list))

    def test_clear_result_list_is_empty(self):
        l_result_list = [] 
        l_result = "INFO: Список результатов вычислений уже пуст. Введите арифметическое выражение для расчета."
        self.assertEqual(l_result, clear(p_result_list=l_result_list))

    def test_reset_result_list_has_more_than_one_element(self):
        l_result_list = [1, 2] 
        l_result = "INFO: Выполнен переход к предыдущему результату вычислений - 1"
        self.assertEqual(l_result, reset(p_result_list=l_result_list))

    def test_reset_result_list_has_one_element(self):
        l_result_list = [1] 
        l_result = "INFO: В истории вычислений было только одно значение. История пуста"
        self.assertEqual(l_result, reset(p_result_list=l_result_list))

    def test_reset_result_list_has_no_elements(self):
        l_result_list = []
        l_result = "INFO: Нечего очищать. История вычислений пуста."
        self.assertEqual(l_result, reset(p_result_list=l_result_list)) 

    def test_is_input_a_calculator_option_clear_reset(self):
        self.assertEqual(True, is_input_a_calculator_option(p_str="c"), is_input_a_calculator_option(p_str="r"))

    def test_is_input_a_calculator_option_invalid(self):
        self.assertEqual(False, is_input_a_calculator_option(p_str="crrc"), is_input_a_calculator_option(p_str="b")) 

    def test_process_input_result_list_empty_and_operator_not_first(self):
        l_str = " 20  +  23" 
        l_result_list = []
        l_result = "20+23"
        self.assertEqual(l_result, p_1_33_process_input(p_str=l_str, p_result_list=l_result_list))

    def test_process_input_result_list_not_empty_and_operator_not_first(self):
        l_str = " 20  +  23" 
        l_result_list = [21]
        l_result = "20+23"
        self.assertEqual(l_result, p_1_33_process_input(p_str=l_str, p_result_list=l_result_list)) 

    def test_process_input_result_list_empty_and_operator_first(self):
        l_str = " +  23  " 
        l_result_list = []
        l_result = "+23"
        self.assertEqual(l_result, p_1_33_process_input(p_str=l_str, p_result_list=l_result_list))

    def test_process_input_result_list_not_empty_and_operator_first(self):
        l_str = " +  23  " 
        l_result_list = [17]
        l_result = "17+23"
        self.assertEqual(l_result, p_1_33_process_input(p_str=l_str, p_result_list=l_result_list)) 

    def test_calculate_simple(self):
        l_str = "80/8+30-20*4/3"
        l_char_list = [
            "8", "0", "/", "8", \
            "+", "3", "0", "-", \
            "2", "0", "*", "4", \
            "/", "3"
        ]
        l_char_type_list = [
            C_TYPE_ID_NUMBER, C_TYPE_ID_NUMBER, C_TYPE_ID_OPERATOR, C_TYPE_ID_NUMBER, \
            C_TYPE_ID_OPERATOR, C_TYPE_ID_NUMBER, C_TYPE_ID_NUMBER, C_TYPE_ID_MINUS, \
            C_TYPE_ID_NUMBER, C_TYPE_ID_NUMBER, C_TYPE_ID_OPERATOR, C_TYPE_ID_NUMBER, \
            C_TYPE_ID_OPERATOR, C_TYPE_ID_NUMBER
        ]
        self.assertEqual(eval(l_str), calculate(p_char_list=l_char_list, p_char_type_list=l_char_type_list)) 

    def test_calculate_complex(self):
        l_str = "((80/8)+30)-(20*4/3)" 
        l_char_list = [
            "(", "(", "8", "0",
            "/", "8", ")", "+",
            "3", "0", ")", "-",
            "(", "2", "0", "*",
            "4", "/", "3", ")"
        ]
        l_char_type_list = [
            C_TYPE_ID_OPENING_BRACKET, C_TYPE_ID_OPENING_BRACKET, C_TYPE_ID_NUMBER, C_TYPE_ID_NUMBER,
            C_TYPE_ID_OPERATOR, C_TYPE_ID_NUMBER, C_TYPE_ID_CLOSING_BRACKET, C_TYPE_ID_OPERATOR,
            C_TYPE_ID_NUMBER, C_TYPE_ID_NUMBER, C_TYPE_ID_CLOSING_BRACKET, C_TYPE_ID_MINUS,
            C_TYPE_ID_OPENING_BRACKET, C_TYPE_ID_NUMBER, C_TYPE_ID_NUMBER, C_TYPE_ID_OPERATOR,
            C_TYPE_ID_NUMBER, C_TYPE_ID_OPERATOR, C_TYPE_ID_NUMBER, C_TYPE_ID_CLOSING_BRACKET
        ]
        self.assertEqual(eval(l_str), calculate(p_char_list=l_char_list, p_char_type_list=l_char_type_list)) 

class Test_p_1_34(unittest.TestCase):

    def test_eg_remove_one_random_symbol(self):
        l_str = "All dogs go to heaven."
        l_result = error_generator_remove_one_random_symbol(p_str=l_str)
        self.assertNotEqual(l_str, l_result)
        self.assertNotEqual(len(l_str), len(l_result))

    def test_eg_add_one_random_symbol_to_random_place(self):
        l_str = "All dogs go to heaven."
        l_result = error_generator_add_one_random_symbol_to_random_place(p_str=l_str)
        self.assertNotEqual(l_str, l_result)
        self.assertNotEqual(len(l_str), len(l_result))

    def test_eg_change_random_symbol_register(self):
        l_str = "All dogs go to heaven."
        l_result = error_generator_change_random_symbol_register(p_str=l_str)
        self.assertNotEqual(l_str, l_result)
        self.assertEqual(len(l_str), len(l_result))

    def test_eg_copy_random_symbol(self):
        l_str = "All dogs go to heaven."
        l_result = error_generator_copy_random_symbol(p_str=l_str)
        self.assertNotEqual(l_str, l_result)
        self.assertNotEqual(len(l_str), len(l_result))

    def test_eg_replace_random_vowel(self):
        l_str = "All dogs go to heaven."
        l_result = error_generator_replace_random_vowel(p_str=l_str)
        self.assertNotEqual(l_str, l_result)
        self.assertEqual(len(l_str), len(l_result))

    def test_eg_replace_random_vowel_only_consonants(self):
        l_str = "Ll dgs g t hvn."
        l_result = error_generator_replace_random_vowel(p_str=l_str)
        self.assertEqual(l_str, l_result)
        self.assertEqual(len(l_str), len(l_result))

    def test_eg_replace_random_consonant(self):
        l_str = "All dogs go to heaven."
        l_result = error_generator_replace_random_consonant(p_str=l_str)
        self.assertNotEqual(l_str, l_result)
        self.assertEqual(len(l_str), len(l_result))

    def test_eg_replace_random_consonant_only_vowels(self):
        l_str = "A o o o eae."
        l_result = error_generator_replace_random_consonant(p_str=l_str)
        self.assertEqual(l_str, l_result)
        self.assertEqual(len(l_str), len(l_result))

    def test_eg_remove_dot_from_end(self):
        l_str = "All dogs go to heaven."
        l_result = error_generator_remove_dot_from_end(p_str=l_str)
        self.assertNotEqual(l_str, l_result)
        self.assertNotEqual(len(l_str), len(l_result)) 

    def test_eg_remove_dot_from_end_no_dot_at_the_end(self):
        l_str = "All dogs go to heaven"
        l_result = error_generator_remove_dot_from_end(p_str=l_str)
        self.assertEqual(l_str, l_result)
        self.assertEqual(len(l_str), len(l_result))

    def test_eg_remove_random_space(self):
        l_str = "All dogs go to heaven."
        l_result = error_generator_remove_random_space(p_str=l_str)
        self.assertNotEqual(l_str, l_result)
        self.assertNotEqual(len(l_str), len(l_result))

    def test_eg_remove_random_space_no_space(self):
        l_str = "Alldogsgotoheaven."
        l_result = error_generator_remove_random_space(p_str=l_str)
        self.assertEqual(l_str, l_result)
        self.assertEqual(len(l_str), len(l_result))

    def test_get_list_of_error_sentences(self):
        l_str = "I will never spam my friends again."
        l_result = get_list_of_error_sentences(
            p_str=l_str,
            p_sentence_count=100
        )
        l_counter = 0
        for i in l_result:
            if i != l_str:
                l_counter += 1
        self.assertEqual(l_counter, 8)
        
class Test_p_1_35(unittest.TestCase):

    def test_generate_birthday(self):
        l_start_date = date(2020, 1, 1)
        l_end_date = date(2020, 12, 31)
        l_result_date = generate_birthday()
        self.assertGreaterEqual(l_result_date, l_start_date)
        self.assertLessEqual(l_result_date, l_end_date)

    def test_generate_birthdays(self):
        l_amount = 100
        l_result = generate_birthdays(p_amount=l_amount)
        self.assertEqual(l_amount, len(l_result)) 
        for i in l_result:
            self.assertEqual(i.year, 2020)

    def test_count_birthdays(self):
        l_d1 = date(2021, 1, 1)
        l_d2 = date(2021, 1, 2)
        l_d3 = date(2021, 1, 3)
        l_list = [l_d1, l_d1, l_d1, l_d2, l_d2, l_d3]
        l_result = count_birthdays(p_list=l_list)
        self.assertEqual(l_result[l_d1], 3)
        self.assertEqual(l_result[l_d2], 2)
        self.assertEqual(l_result[l_d3], 1)
        self.assertEqual(l_result[generate_birthday()], 0)

    def test_are_same_birthdays_in_list(self):
        self.assertFalse(are_same_birthdays_in_list(p_amount=1)) 
        self.assertTrue(are_same_birthdays_in_list(p_amount=366)) 

if __name__ == '__main__':
    unittest.main()

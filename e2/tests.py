import unittest
from random import randint
from time import perf_counter

#Reinforcement 
from e2.r4 import Flower 
from e2.r5 import CreditCard_r5
from e2.r6 import CreditCard_r6
from e2.r7 import CreditCard_r7
from e2.r8 import test_credit_card
from e2.r9 import Vector_r9
from e2.r10 import Vector_r10
from e2.r11 import Vector_r11
from e2.r12 import Vector_r12 
from e2.r13 import Vector_r13
from e2.r14 import Vector_r14
from e2.r15 import Vector_r15
from e2.r16 import get_element_cnt_in_range_loop, get_element_cnt_in_range_formula
from e2.r18 import FibonacciProgression
from e2.r22 import ExampleList
from e2.r23 import ExampleList_r23
#Creative
from e2.c25 import Vector_c25
from e2.c26 import ReversedSequenceIterator
from e2.c27 import Range
from e2.c28 import CreditCard_c28, get_current_year_and_month
from e2.c29 import PredatoryCreditCard_c29
from e2.c30 import CreditCard_c30, PredatoryCreditCard_c30
from e2.c31 import ProgressionAbs
from e2.c32 import ProgressionSqrt
#Project 
from e2.p33 import Polynomial

#Reinforcement 
class Test_r4(unittest.TestCase):

    def test_flower_all_correct(self):
        l_name = "Rose"
        l_petals_cnt = 20
        l_price = 129.0
        l_flower = Flower(
            name=l_name, 
            petals_cnt=l_petals_cnt, 
            price=l_price
        )

        # Getters
        self.assertEqual(l_name, l_flower.name)
        self.assertEqual(l_petals_cnt, l_flower.petals_cnt)
        self.assertEqual(l_price, l_flower.price)

        l_name = "Lotus"
        l_petals_cnt = 7
        l_price = 195.0
        l_flower.name = l_name 
        l_flower.petals_cnt = l_petals_cnt 
        l_flower.price = l_price 

        # Setters 
        self.assertEqual(l_name, l_flower.name)
        self.assertEqual(l_petals_cnt, l_flower.petals_cnt)
        self.assertEqual(l_price, l_flower.price)

        # Check default instance variable value 
        l_flower = Flower(
            name="gladiolus",
            petals_cnt=6
        )
        self.assertEqual(0.0, l_flower.price)

    def test_flower_instance_variable_types_incorrect(self):

        # No input varables
        with self.assertRaises(TypeError):
            l_flower = Flower()

        # All params has wrong type
        with self.assertRaises(TypeError):
            l_flower = Flower(123, "asd", "asd")

        # Only name has correct type
        with self.assertRaises(TypeError):
            l_flower = Flower("123", "asd", "asd")

        # Only price has incorrect type 
        with self.assertRaises(TypeError):
            l_flower = Flower("123", 123, "asd")

        # Check setters if first instantiation was correct
        l_flower = Flower(
            name="gladiolus",
            petals_cnt=6,
            price = 29.99
        )

        with self.assertRaises(TypeError):
            l_flower.name = 100500

        with self.assertRaises(TypeError):
            l_flower.petals_cnt = "Too many"

        with self.assertRaises(TypeError):
            l_flower.price = "Very expensive"

class Test_r5(unittest.TestCase):

    def test_credit_card_type_checking(self):
        l_credit_card = CreditCard_r5(
            customer="Johny Silverhand",
            bank="Arasaki Corp",
            acnt="1234 5678 1234 5678",
            limit=8192
        )
        
        with self.assertRaises(TypeError):
            l_credit_card.charge(price="Many")

        with self.assertRaises(TypeError):
            l_credit_card.make_payment(amount="A few coins")

        self.assertTrue(l_credit_card.charge(price=8000))
        self.assertFalse(l_credit_card.charge(price=10000))

        l_credit_card.make_payment(amount=2000)
        self.assertEqual(6000, l_credit_card._balance)

class Test_r6(unittest.TestCase):
    
    def test_credit_card_make_payment_amount_is_negative(self):
        l_credit_card = CreditCard_r6(
            customer="Ravshan Lenkoransky",
            bank="AzerBank",
            acnt="1234 2311 3214 3214",
            limit=500
        )

        with self.assertRaises(ValueError):
            l_credit_card.make_payment(amount=-2000)

class Test_r7(unittest.TestCase):

    def test_credit_card_with_balance_added_in_init(self):
        # Check that if no balance specified it will be zero 
        l_credit_card = CreditCard_r7(
            customer="Alexandr from Macedonia",
            bank="AfinaCorp",
            acnt="123142 domini",
            limit=1000000
        )
        self.assertEqual(l_credit_card._balance, 0)

        # Check that if balance specified, it will be instantiated 
        l_balance = 1234.567
        l_credit_card = CreditCard_r7(
            customer="Andrew Bolkonsky",
            bank="SchererFinanceGroup",
            acnt="500 700 14",
            limit=2000000,
            balance=l_balance
        )
        self.assertEqual(l_credit_card._balance, l_balance)

        # Check that TypeError will be raised, if you specify balance as string 
        with self.assertRaises(TypeError):
            l_balance = "Very poor guy!"
            l_credit_card = CreditCard_r7(
                customer="Andrew Bolkonsky",
                bank="SchererFinanceGroup",
                acnt="500 700 14",
                limit=2000000,
                balance=l_balance
            )

        # Check that ValueError will be raised, if you specify negative balance
        with self.assertRaises(ValueError):
            l_balance = -1234.567
            l_credit_card = CreditCard_r7(
                customer="Andrew Bolkonsky",
                bank="SchererFinanceGroup",
                acnt="500 700 14",
                limit=2000000,
                balance=l_balance
            )

class Test_r8(unittest.TestCase):

    def test_credit_card(self):
        l_result = test_credit_card(p_int=59)
        self.assertTrue(l_result[0])
        self.assertTrue(l_result[1])
        self.assertFalse(l_result[2])

class Test_r9(unittest.TestCase):

    def test_vector(self):
        # Check len
        l_vector = Vector_r9(4)
        self.assertEqual(len(l_vector), 4)

        # Check getitem 
        # Check setitem 
        l_vector[0] = 0
        l_vector[1] = 1
        l_vector[2] = 2 
        self.assertEqual(l_vector[0], 0)
        self.assertEqual(l_vector[1], 1)
        self.assertEqual(l_vector[2], 2)
        self.assertEqual(l_vector[3], 0)

        # Check add 
        l_vector2 = Vector_r9(4)
        l_vector2[0] = 10
        l_vector2[1] = 11
        l_vector2[2] = 12
        l_vector2[3] = 13
        # With same length 
        l_result = l_vector + l_vector2 
        self.assertEqual(l_result[0], 10)
        self.assertEqual(l_result[1], 12)
        self.assertEqual(l_result[2], 14)
        self.assertEqual(l_result[3], 13)
        # Without same length
        l_vector3 = Vector_r9(10)
        with self.assertRaises(ValueError):
            l_result = l_vector + l_vector3 

        # Check eq 
        l_vector4 = Vector_r9(4)
        l_vector4[0] = 0
        l_vector4[1] = 1
        l_vector4[2] = 2
        self.assertEqual(l_vector, l_vector4)
        self.assertTrue(l_vector == l_vector4)

        l_vector5 = Vector_r9(4)
        l_vector5[0] = 2
        l_vector5[1] = 1
        l_vector5[2] = 0
        self.assertNotEquals(l_vector, l_vector5)
        self.assertFalse(l_vector == l_vector5)

        # Check ne 
        self.assertTrue(l_vector != l_vector5)
        self.assertFalse(l_vector != l_vector4)

        # Check str 
        l_str = "<0, 1, 2, 0>"
        self.assertEqual(l_str, str(l_vector))

    def test_vector_sub(self):
        # Check with same length 
        l_vector = Vector_r9(2)
        l_vector[0] = 900
        l_vector[1] = 100
        l_vector2 = Vector_r9(2)
        l_vector2[0] = 300
        l_vector2[1] = 50 
        l_result = l_vector - l_vector2 
        self.assertEqual(l_result[0], 600)
        self.assertEqual(l_result[1], 50)
        
        # Check without same length 
        l_vector3 = Vector_r9(1)
        l_vector3[0] = 777
        with self.assertRaises(ValueError):
            l_result = l_vector - l_vector3 

class Test_r10(unittest.TestCase):

    def test_check_neg(self):
        l_vector = Vector_r10(2)
        l_vector[0] = 222
        l_vector[1] = -222
        l_result = -l_vector 
        self.assertEqual(l_result[0], -222)
        self.assertEqual(l_result[1], 222)

class Test_r11(unittest.TestCase):

    def test_check_radd(self):
        l_vector = Vector_r11(5)
        l_vector[0] = 0
        l_vector[1] = 1
        l_vector[2] = 2
        l_vector[3] = 3 
        l_vector[4] = 4

        l_result = [5, 3, 10, -2, 1] + l_vector 
        self.assertEqual(l_result[0], 5)
        self.assertEqual(l_result[1], 4)
        self.assertEqual(l_result[2], 12)
        self.assertEqual(l_result[3], 1)
        self.assertEqual(l_result[4], 5)

class Test_r12(unittest.TestCase):

    def test_check_mul(self):
        l_vector = Vector_r12(3)
        l_vector[0] = 1
        l_vector[1] = 2
        l_vector[2] = 3
        l_result = l_vector * 3 
        self.assertEqual(l_result[0], 3)
        self.assertEqual(l_result[1], 6)
        self.assertEqual(l_result[2], 9)

        with self.assertRaises(TypeError):
            l_result = l_vector * "too many!"

class Test_r13(unittest.TestCase):

    def test_check_rmul(self):
        l_vector = Vector_r13(3)
        l_vector[0] = 1
        l_vector[1] = 2
        l_vector[2] = 3
        l_result = 3 * l_vector 
        self.assertEqual(l_result[0], 3)
        self.assertEqual(l_result[1], 6)
        self.assertEqual(l_result[2], 9)

class Test_r14(unittest.TestCase):
    
    def test_check_mul_vector_by_vector(self):
        l_vector1 = Vector_r14(2)
        l_vector2 = Vector_r14(2)
        l_vector3 = Vector_r14(1)
        
        l_vector1[0] = 2
        l_vector1[1] = 3
        l_vector2[0] = 4 
        l_vector2[1] = 5 
        l_vector3[0] = 6 

        l_result = l_vector1 * l_vector2
        self.assertEqual(l_result, 23)

        with self.assertRaises(ValueError):
            l_result = l_vector1 * l_vector3

class Test_r15(unittest.TestCase):

    def test_init(self):
        l_vector = Vector_r15(d=10)
        self.assertEqual(len(l_vector), 10)
        for i in range(len(l_vector)):
            self.assertEqual(l_vector[i], 0)

        l_vector = Vector_r15(d=(1,2,3))
        self.assertEqual(len(l_vector), 3)
        self.assertEqual(l_vector[0], 1)
        self.assertEqual(l_vector[1], 2)
        self.assertEqual(l_vector[2], 3)

        l_vector = Vector_r15(d=[1,2,3])
        self.assertEqual(len(l_vector), 3)
        self.assertEqual(l_vector[0], 1)
        self.assertEqual(l_vector[1], 2)
        self.assertEqual(l_vector[2], 3)

        with self.assertRaises(TypeError):
            l_vector = Vector_r15(d="abcd")

class Test_r16(unittest.TestCase):
    
    def test_elements_in_range_randomly(self):
        for i in range(100):
            l_step = 0 
            while l_step == 0:
                l_step = randint(1, 100)
            l_start = randint(-10000, 10000)
            l_stop = l_start + randint(1, 1000000)
            self.assertEqual(
                get_element_cnt_in_range_loop(p_start=l_start, p_stop=l_stop, p_step=l_step),
                get_element_cnt_in_range_formula(p_start=l_start, p_stop=l_stop, p_step=l_step)
            )        

class Test_r18(unittest.TestCase):

    def test_8th_member(self):
        # 8th member is 
        # 2 2 4 6 10 16 26 42 
        l_fp = FibonacciProgression(first=2, second=2)
        for i in range(8-1):
            l_fp._advance()
        self.assertEqual(l_fp._current, 42)

class Test_r19(unittest.TestCase):

    def test_2_in_63_reach_arithmetic_progression(self):
        # 2**63 = 128 (2**7) * 2**56
        l_result = 2 ** 56
        # Previous range formula for amount of elements 
        l_expected_result = (2 ** 63 - 0 + 128 - 1) // 128
        self.assertEqual(l_result, l_expected_result)

class Test_r22(unittest.TestCase):

    def test_eq_examplelist(self):
        l_el_1 = ExampleList([1,2,3])
        l_el_2 = ExampleList([1,2,3])
        l_el_3 = ExampleList([3,2,1,4])
        self.assertTrue(l_el_1 == l_el_2)
        self.assertFalse(l_el_2 == l_el_3)

        with self.assertRaises(TypeError):
            l_el_4 = ExampleList("a sequence but not a list")

class Test_r23(unittest.TestCase):

    def test_lt_examplelist(self):
        l_el_1 = ExampleList_r23([])
        l_el_2 = ExampleList_r23([1,2,3,4,5])
        l_el_3 = ExampleList_r23([1,2,3,4,5])
        l_el_4 = ExampleList_r23([1,2,3,4,6])
        l_el_5 = ExampleList_r23([1,2,3,4,4])
        l_el_6 = ExampleList_r23([1,2,3,4])

        self.assertFalse(l_el_1 < l_el_1)
        self.assertFalse(l_el_2 < l_el_3)
        self.assertTrue(l_el_2 < l_el_4)
        self.assertFalse(l_el_2 < l_el_5)
        self.assertFalse(l_el_2 < l_el_6)

class Test_c25(unittest.TestCase):

    def test_mul_vector(self):
        l_vector = Vector_c25([1,2,3])
        with self.assertRaises(TypeError):
            l_vector * "123"

        self.assertEqual(Vector_c25([2,4,6]), l_vector * 2)

        with self.assertRaises(ValueError):
            l_another_vector = Vector_c25([1,2,3,4])
            l_vector * l_another_vector 

        l_result = 1 * 1 + 2 * 2 + 3 * 3 
        self.assertEqual(l_result, l_vector * l_vector)

class Test_c26(unittest.TestCase):

    def test_reversed_sequence_iterator(self):
        l_rsi = ReversedSequenceIterator(sequence="abcd") 
        self.assertEqual("d", next(l_rsi))
        self.assertEqual("c", next(l_rsi))
        self.assertEqual("b", next(l_rsi))
        self.assertEqual("a", next(l_rsi))
        with self.assertRaises(StopIteration):
            next(l_rsi)

class Test_c27(unittest.TestCase):

    def test_range_contains(self):
        self.assertTrue(2 in Range(999999))
        self.assertTrue(2 in Range(2, 10, 2))
        self.assertFalse(3 in Range(2, 10, 2))
        self.assertFalse(10 in Range(2, 10, 2))
        
        l_start = perf_counter()
        2 in Range(100000000)
        l_time1 = perf_counter() - l_start 

        l_start = perf_counter()
        99999999 in Range(100000000)
        l_time2 = perf_counter() - l_start 

        # time of execution of 2nd case is less or equal than 10*1st case
        self.assertLessEqual(l_time2, l_time1 * 10)

class Test_c28(unittest.TestCase):
    """
        сделать 11 вызовов charge и проверим что баланс уменьшился
        сделать 9 вызовов charge и проверим что баланс уменьшился
        поменять месяц и год на более ранний, и проверить, что при вызове charge он поменяется
    """
    def test_11_charge_calls(self):

        l_instance = CreditCard_c28(
            customer="Mother Mary",
            bank="Sderbank",
            acnt="1111 2222 3333 4444",
            limit=200000,
            apr=0
        )
        for i in range(11):
            l_instance.charge(price=10000)
        self.assertEqual(10000*11 + 1, l_instance.get_balance())

    def test_9_charge_calls(self):

        l_instance = CreditCard_c28(
            customer="Mother Mary",
            bank="Sderbank",
            acnt="1111 2222 3333 4444",
            limit=200000,
            apr=0
        )
        for i in range(9):
            l_instance.charge(price=10000)
        self.assertEqual(10000*9, l_instance.get_balance())

    def test_currentperiod_update(self):

        l_instance = CreditCard_c28(
            customer="Mother Mary",
            bank="Sderbank",
            acnt="1111 2222 3333 4444",
            limit=200000,
            apr=0
        )
        l_instance._currentperiod = (1, 2020)
        l_instance.charge(price=10000)
        self.assertEqual(l_instance._currentperiod, get_current_year_and_month())
        
class Test_c29(unittest.TestCase):
    """
    Инициализируем карту 
    Эмулируем ситуацию, что ежемесячный платеж не был погашен
    Проверяем факт того, что баланс увеличился на нужный процент
    А также, что баланс обновился и обнулилась сумма платежей 
    """
    def test_predatory_credit_card(self):

        l_card = PredatoryCreditCard_c29(
            customer="Vasya",
            bank="DCP",
            acnt="228 282",
            limit=10000,
            apr=0,
            min_monthly_payment_pct=0.5,
            late_fee=100
        )

        l_card.charge(price=5000)
        l_card.process_month()

        # Баланс: 10000-5000, никаких штрафов 
        self.assertEqual(l_card._balance, 5000)

        # Новый месяц, не погашено 50% от баланса на начало месяца,
        # Проверяем наличие штрафа 
        l_card.process_month()
        self.assertEqual(l_card._balance, 5100)
        self.assertEqual(l_card._month_begin_balance, 5100)
        self.assertEqual(l_card._month_customer_payment, 0)

class Test_c30(unittest.TestCase):
    """
        Инициализируем обе карты 
        Пытаемся обратиться к балансу, 
        показываем что баланс можно поменять через метод, 
        несмотря на то, что метод защищенный 
    """

    def test_balance_access(self):

        l_credit_card = CreditCard_c30(
            customer="Diman",
            bank="GrabBank",
            acnt="666 777",
            limit=20000
        )

        l_predatory_credit_card = PredatoryCreditCard_c30(
            customer="Kolyan",
            bank="PKB",
            acnt="888 999",
            limit=100000,
            apr=2000
        )
        self.assertEqual(l_credit_card.balance, 0)
        self.assertEqual(l_predatory_credit_card.balance, 0)

        # Вот тут надо разобраться почему вообще это выполняется...
        with self.assertRaises(AttributeError):
            l_credit_card.balance = 1000

        l_credit_card.__balance = 1000
        self.assertEqual(l_credit_card.balance, 0)

        l_credit_card._set_balance(4000)
        self.assertEqual(l_credit_card.balance, 4000)

        with self.assertRaises(AttributeError):
            l_predatory_credit_card.balance = 1000

        l_predatory_credit_card.__balance = 1000
        self.assertEqual(l_predatory_credit_card.balance, 0)
        
        l_predatory_credit_card._set_balance(2000)
        self.assertEqual(l_predatory_credit_card.balance, 2000)

class Test_c31(unittest.TestCase):

    def test_progression_abs(self):

        l_progression = ProgressionAbs()
        
        self.assertEqual(next(l_progression), 2)
        self.assertEqual(next(l_progression), 200)
        self.assertEqual(next(l_progression), 198)
        self.assertEqual(next(l_progression), 2)
        self.assertEqual(next(l_progression), 196)

class Test_c32(unittest.TestCase):

    def test_progression_sqrt(self):

        l_progression = ProgressionSqrt(start=256)

        self.assertEqual(next(l_progression), 256)
        self.assertEqual(next(l_progression), 16)
        self.assertEqual(next(l_progression), 4)
        self.assertEqual(next(l_progression), 2)

class Test_p33(unittest.TestCase):

    def test_polynomial_findall(self):

        l_string_list = [
            "x+y",
            "-x-y",
            "0+0",
            "-1-3",
            "3.43+2.43",
            "-3.43-4.23",
            "-10x-8y",
            "-2.32x-124.23y",
            "10x^2+20x^3",
            "-10x^(-2)-40x^(-3)",
            "123.24x^2.34+213.321y^7.32",
            "-78.89x^(-23.4)-14.43y^(-23.4)",
            "x^2+y^3",
            "-x^(-2)-y^(-3)",
            "-x^(-2.24)-y^(-3.44)"
        ]

        # x+y 
        l_cls = Polynomial(p_string=l_string_list[0])
        self.assertEqual(l_cls._findall_result, ["x", "+y"])

        # -x-y 
        l_cls = Polynomial(p_string=l_string_list[1])
        self.assertEqual(l_cls._findall_result, ["-x", "-y"])

        # 0+0
        l_cls = Polynomial(p_string=l_string_list[2])
        self.assertEqual(l_cls._findall_result, ["0", "+0"])

        # -1-3
        l_cls = Polynomial(p_string=l_string_list[3])
        self.assertEqual(l_cls._findall_result, ["-1", "-3"])

        # 3.43+2.43
        l_cls = Polynomial(p_string=l_string_list[4])
        self.assertEqual(l_cls._findall_result, ["3.43", "+2.43"])

        # -3.43-4.23
        l_cls = Polynomial(p_string=l_string_list[5])
        self.assertEqual(l_cls._findall_result, ["-3.43", "-4.23"])

        # -10x-8y
        l_cls = Polynomial(p_string=l_string_list[6])
        self.assertEqual(l_cls._findall_result, ["-10x", "-8y"])

        # -2.32x-124.23y
        l_cls = Polynomial(p_string=l_string_list[7])
        self.assertEqual(l_cls._findall_result, ["-2.32x", "-124.23y"])

        # 10x^2+20x^3
        l_cls = Polynomial(p_string=l_string_list[8])
        self.assertEqual(l_cls._findall_result, ["10x^2", "+20x^3"])

        # -10x^(-2)-40x^(-3)
        l_cls = Polynomial(p_string=l_string_list[9])
        self.assertEqual(l_cls._findall_result, ["-10x^(-2)", "-40x^(-3)"])

        # 123.24x^2.34+213.321y^7.32
        l_cls = Polynomial(p_string=l_string_list[10])
        self.assertEqual(l_cls._findall_result, ["123.24x^2.34", "+213.321y^7.32"])

        # -78.89x^(-23.4)-14.43y^(-23.4)
        l_cls = Polynomial(p_string=l_string_list[11])
        self.assertEqual(l_cls._findall_result, ["-78.89x^(-23.4)", "-14.43y^(-23.4)"])

        # x^2+y^3
        l_cls = Polynomial(p_string=l_string_list[12])
        self.assertEqual(l_cls._findall_result, ["x^2", "+y^3"])

        # -x^(-2)-y^(-3)
        l_cls = Polynomial(p_string=l_string_list[13])
        self.assertEqual(l_cls._findall_result, ["-x^(-2)", "-y^(-3)"])

        # -x^(-2.24)-y^(-3.44)
        l_cls = Polynomial(p_string=l_string_list[14])
        self.assertEqual(l_cls._findall_result, ["-x^(-2.24)", "-y^(-3.44)"])

    def test_polynomial_findall_complex(self):

        l_string_list = [
            "20x^10-100x^8.23+723.324y^(-123.456)+10",
            "-3.4323x^(-23.45)+123-2230+800y^123-9.324x^(-234.35)",
            "2+2x+10y^2-20z^3.2+30z^4.87456-0+10x"
        ]

        # "20x^10-100x^8.23+723.324y^(-123.456)+10"
        l_cls = Polynomial(p_string=l_string_list[0])
        self.assertEqual(l_cls._findall_result, ["20x^10", "-100x^8.23", "+723.324y^(-123.456)", "+10"])

        # "-3.4323x^(-23.45)+123-2230+800y^123-9.324x^(-234.35)"
        l_cls = Polynomial(p_string=l_string_list[1])
        self.assertEqual(l_cls._findall_result, ["-3.4323x^(-23.45)", "+123", "-2230", "+800y^123", "-9.324x^(-234.35)"])

        # "2+2x+10y^2-20z^3.2+30z^4.87456-0+10x"
        l_cls = Polynomial(p_string=l_string_list[2])
        self.assertEqual(l_cls._findall_result, ["2", "+2x", "+10y^2", "-20z^3.2", "+30z^4.87456", "-0", "+10x"])

    def test_polynomial_input_string_empty(self):
        
        with self.assertRaises(ValueError):
            l_cls = Polynomial(p_string="")

        with self.assertRaises(ValueError):
            l_cls = Polynomial(p_string="   ")

    def test_polynomial_input_string_is_invalid(self):
        with self.assertRaises(ValueError):
            l_cls = Polynomial(p_string="Привет, дружок!")

if __name__ == '__main__':
    unittest.main()

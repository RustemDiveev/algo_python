import unittest

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

    def check_vector(self):
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

    def check_vector_sub(self):
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

if __name__ == '__main__':
    unittest.main()

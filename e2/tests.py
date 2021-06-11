import unittest

#Reinforcement 
from e2.r4 import Flower 
from e2.r5 import CreditCard_r5
from e2.r6 import CreditCard_r6
from e2.r7 import CreditCard_r7
from e2.r8 import test_credit_card

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

if __name__ == '__main__':
    unittest.main()

import unittest

#Reinforcement 
from e2.r4 import Flower 

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

if __name__ == '__main__':
    unittest.main()

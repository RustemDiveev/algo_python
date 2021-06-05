# R-2.1 Give three examples of life-critical software applications.
"""
    1. Biomedical equipment
    2. Automated car driving 
    3. Rocket launch software
"""
# R-2.2 Give an example of a software application in which adaptability can mean
# the difference between a prolonged lifetime of sales and bankruptcy.
"""
    Accounting system
"""

class Flower:

    def __init__(self, name: str, petals_cnt: int, price: float = 0):
        """
            Constructor
            name - str - name of flower 
            petals_cnt - int - amount of petals 
            price - float - price of flower
        """
        self.name = name 
        self.petals_cnt = petals_cnt 
        self.price = price 

    # Getters
    @property
    def name(self):
        return self._name 

    @property
    def petals_cnt(self):
        return self._petals_cnt 

    @property 
    def price(self):
        return self._price

    # Setters - perfect type checking
    @name.setter 
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Name of flower must be string - argument has type " + str(type(value)))
        else:
            self._name = value

    @petals_cnt.setter
    def petals_cnt(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Petals count of flower must be int - argument has type " + str(type(value)))
        else:
            self._petals_cnt = value

    @price.setter 
    def price(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Price of flower must be int or float - argument has type" + str(type(value)))
        else:
            self._price = float(value)

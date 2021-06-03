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

    def __init__(self, name: str, petals_cnt: int, price: float=0):
        """
            Constructor
            name - str - name of flower 
            petals_cnt - int - amount of petals 
            price - float - price of flower
        """
        self._name = name
        self._petals_cnt = petals_cnt 
        self._price = price 

    # Getters for instance members 
    def get_name(self) -> str:
        return self._name 

    def get_petals_cnt(self) -> int:
        return self._petals_cnt

    def get_price(self) -> float:
        return self._price 

    # Setters for instance members
    def set_name(self, name: str):
        self._name = name 

    def set_petals_cnt(self, petals_cnt: int):
        self._petals_cnt = petals_cnt 

    def set_price(self, price: float):
        self._price = price

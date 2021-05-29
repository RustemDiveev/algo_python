from decimal import Decimal
from collections import defaultdict

def get_change(p_money_charged: float, p_money_given: float) -> dict:
    """
        Returns dictionary with bills and coins 
        as change for money given for charge
        input:
            p_money_charged - sum of money for purchase
            p_money_given - sum of given money
        output:
            dict
    """
    C_MONEY = [5000, 1000, 500, 100, 50, 10, 5, 2, 1, 0.5, 0.1, 0.05, 0.01]
    C_MONEY = [Decimal(str(i)) for i in C_MONEY]

    l_result = defaultdict(int)
    l_money_charged_dec = Decimal(str(p_money_charged))
    l_money_given_dec = Decimal(str(p_money_given))

    # Input param check 
    if not is_input_a_money(p_decimal=l_money_charged_dec):
        raise ValueError("Money charged must be a number with max scale of 2") 
    if not is_input_a_money(p_decimal=l_money_given_dec):
        raise ValueError("Money given must be a number with max scale of 2")     

    l_change = l_money_given_dec - l_money_charged_dec

    if l_change < 0:
        raise ValueError("Charged money must be less or equal than money given")

    while l_change != 0:
        for i in C_MONEY:
            while i <= l_change:
                l_change -= i
                l_result[str(i)] += 1

    return dict(l_result)

def get_scale(p_decimal: Decimal) -> int:
    """
        Get total of numbers after decimal point of float number
        input:
            p_decimal - input decimal
        output:
            int
    """
    return p_decimal.as_tuple().exponent

def is_input_a_money(p_decimal: Decimal) -> bool:
    """
        Check that input decimal has valid money format 
        It's scale should be less or equal to 2
        input:
            p_decimal - input decimal 
        output:
            bool
    """
    l_scale = get_scale(p_decimal=p_decimal)
    return False if l_scale < -2 or p_decimal < 0 else True

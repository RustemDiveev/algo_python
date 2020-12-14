from decimal import Decimal
from collections import defaultdict

def get_change(i_money_charged: float, i_money_given: float) -> dict:
    """
        Returns dictionary with bills and coins 
        as change for money given for charge
    """

    C_MONEY = [5000, 1000, 500, 100, 50, 10, 5, 2, 1, 0.5, 0.1, 0.05, 0.01]
    C_MONEY = [Decimal(str(i)) for i in C_MONEY]

    v_result = defaultdict(int)

    v_money_charged_dec = Decimal(str(i_money_charged))
    v_money_given_dec = Decimal(str(i_money_given))

    # Input param check 
    if not is_input_a_money(i_decimal=v_money_charged_dec):
        raise ValueError("Money charged must be a number with max scale of 2") 

    if not is_input_a_money(i_decimal=v_money_given_dec):
        raise ValueError("Money given must be a number with max scale of 2")     

    v_change = v_money_given_dec - v_money_charged_dec

    if v_change < 0:
        raise ValueError("Charged money must be less or equal than money given")

    while v_change != 0:
        for i in C_MONEY:
            while i <= v_change:
                v_change = v_change - i
                v_result[str(i)] += 1

    return dict(v_result)

def get_scale(i_decimal: Decimal) -> int:
    """
        Get amount of number after decimal point of float number
    """
    return i_decimal.as_tuple().exponent

def is_input_a_money(i_decimal: Decimal) -> bool:
    """
        Check that input float has valid money format 
        It's scale should be less or equal 2 
    """
    v_scale = get_scale(i_decimal=i_decimal)
    return False if v_scale < -2 or i_decimal < 0 else True

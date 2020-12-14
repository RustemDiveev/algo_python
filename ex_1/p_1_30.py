from math import log

def get_log_of_base_2(i_int: int) -> int:
    """
        Returns how many times you have to divide integer greater than 2 by 2 
        to get value less than 2
    """
    if i_int <= 2:
        raise ValueError("Input number must be greater than 2")

    return int(log(i_int, 2))

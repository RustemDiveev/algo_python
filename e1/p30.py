from math import log

def get_log_of_base_2(p_int: int) -> int:
    """
        Returns how many times you have to divide integer greater than 2 by 2 
        to get value less than 2
        input:
            p_int - input integer
        output:
            int
    """
    if p_int <= 2:
        raise ValueError("Input number must be greater than 2")

    return int(log(p_int, 2))

from ex_1.r_1_2 import is_even

# Считаю, что сделал и r_1_7 

def get_sum_of_squares_of_odd_ints(n: int) -> int:
    """
        Returns sum of squares of odd ints smaller than n
    """
    return sum([num * num if not is_even(num) else 0 for num in range(n)])
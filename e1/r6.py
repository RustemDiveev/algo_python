from e1.r2 import is_even
# Считаю, что сделал и r7

def get_sum_of_squares_of_odd_ints(p_n: int) -> int:
    """
        Returns sum of squares of odd ints smaller than n
        input:
            p_n - input number
        output:
            int
    """
    return sum([num * num if not is_even(num) else 0 for num in range(p_n)])
    
def get_sum_of_squares(p_n: int) -> int:
    """
        Returns sum of squares of all positive integers less than n
        input: 
            p_n - positive integer
        output:
            int
    """
    # Check data type (show me better solution, if there any)
    l_n = int(p_n)
    l_sum = 0

    if l_n <= 0:
        raise ValueError("Input parameter must be positive integer")

    for num in range(1, l_n):
        l_sum += num * num

    return l_sum

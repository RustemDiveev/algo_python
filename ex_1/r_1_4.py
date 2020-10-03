def get_sum_of_squares(n: int) -> int:
    """
        Returns sum of squares of all positive integers less than n
        input: n - positive integer
    """

    # Check data type (show me better solution, if there any)
    n = int(n)
    v_sum = 0

    if n <= 0:
        raise ValueError("Input parameter must be positive integer")

    for num in range(1, n):
        v_sum += num * num

    return v_sum

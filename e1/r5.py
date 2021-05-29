from typing import Iterator

def get_sum_of_squares_with_sum(p_n: int) -> int:
    """
        Returns sum of squares of ints less than p_n 
        with usage of built-in sum function and comprehension syntax
        input:
            p_n - input number for generating list
        output:
            int - sum of squares of all integers less than p_n
    """
    # Check data type (show me better solution, if there any)
    l_n = int(p_n)

    if l_n <= 0:
        raise ValueError("Input parameter must be positive integer")

    return sum([num * num for num in range(l_n)])

def get_sum_of_squares_with_sum_and_iterator(p_n: int) -> int:
    """
        Returns sum of squares of ints less than p_n 
        with usage of built-in sum function and iterator
        input:
            p_n - input number for generating list
        output:
            int - sum of squares of all integers less than p_n
    """
    # Check data type (show me better solution, if there any)
    l_n = int(p_n)

    if l_n <= 0:
        raise ValueError("Input parameter must be positive integer")

    return sum(sum_iterator(p_end=l_n))

def sum_iterator(p_end: int) -> Iterator[int]:
    """
        Returns iterator with sum of squares of ints less than p_n
        input:
            p_end - end point for iterator
        output:
            Iterator[int]
    """
    l_start = 1
    if p_end == 1:
        yield 0
    else: 
        while l_start < p_end:
            yield l_start * l_start 
            l_start += 1

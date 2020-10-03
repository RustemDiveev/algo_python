from typing import Iterator

def get_sum_of_squares_with_sum(n: int) -> int:
    """
        Returns sum of squares of ints less than n 
        with usage of built-in sum function and comprehension syntax
    """

    # Check data type (show me better solution, if there any)
    n = int(n)

    if n <= 0:
        raise ValueError("Input parameter must be positive integer")

    return sum([num * num for num in range(n)])

def get_sum_of_squares_with_sum_and_iterator(n: int) -> int:
    """
        Returns sum of squares of ints less than n 
        with usage of built-in sum function and iterator
    """

    # Check data type (show me better solution, if there any)
    n = int(n)

    if n <= 0:
        raise ValueError("Input parameter must be positive integer")

    return sum(sum_iterator(end=n))

def sum_iterator(end: int) -> Iterator[int]:
    start = 1

    if end == 1:
        yield 0
    else: 
        while start < end:
            yield start * start 
            start += 1

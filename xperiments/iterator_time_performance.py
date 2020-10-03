from time import time 
from typing import Iterator

"""
    Using range is fastest - or perhaps i've made some mistakes in iterator function
    With creating list it took
    0.016003847122192383
    With using range it took
    0.007002115249633789
    With using iterator it took
    0.013003110885620117
"""

def measure_time_of_computing_sum_with_creaing_list(n: int):
    """
        Prints time passed for creating list of subsequent ints and calculating sum 
    """
    start_time = time()

    v_list = []
    elem = 1

    while elem < n:
        v_list.append(elem)
        elem += 1

    v_sum = sum(v_list)

    end_time = time()

    print(end_time - start_time)

def measure_time_of_computing_sum_with_using_range_and_list_comprehension(n: int):
    """
        Prints time psased for calculating sum of subsequent ints with using range
    """
    start_time = time()

    v_sum = sum([elem for elem in range(n)]) 

    end_time = time()

    print(end_time - start_time)

def measure_time_of_computing_sum_with_using_iterator(n: int):
    """
        Prints time psased for calculating sum of subsequent ints with using range
    """
    start_time = time()

    def iterator_sum(n: int) -> Iterator[int]:
        start = 1
        while start < n:
            yield start 
            start += 1

    v_sum = sum(iterator_sum(n))

    end_time = time()

    print(end_time - start_time)

def measure_time(n: int):
    """
        Runs all three functions and prints verbose results
    """

    print("With creating list it took")
    measure_time_of_computing_sum_with_creaing_list(n=n)
    print("With using range it took")
    measure_time_of_computing_sum_with_using_range_and_list_comprehension(n=n)
    print("With using iterator it took")
    measure_time_of_computing_sum_with_using_iterator(n=n)


if __name__ == '__main__':
    measure_time(100000)

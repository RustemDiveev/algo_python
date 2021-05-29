from typing import Sequence

def is_there_a_distinct_pair_of_numbers_whose_product_id_odd(p_seq: Sequence[int]) -> bool:
    """
        Returns True if there is a distinct pair 
        of numbers in integer sequence whose product is odd
        input:
            p_seq - sequence of integers
        output:
            bool
    """
    # A slight improvement is to return True as soon as there are two elements found
    return True if len([x for x in p_seq if x % 2 == 1 and p_seq.count(x) == 1]) >= 2 else False
    
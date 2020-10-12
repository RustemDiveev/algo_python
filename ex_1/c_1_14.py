from typing import Sequence

def is_there_a_distinct_pair_of_numbers_whose_product_id_odd(v_seq: Sequence) -> bool:
    """
        Returns True if there is a distinct pair 
        of numbers in integer sequence whose product is odd 
    """
    return True if len([x for x in v_seq if x % 2 == 1 and v_seq.count(x) == 1]) >= 2 else False
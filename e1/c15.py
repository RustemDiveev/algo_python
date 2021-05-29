from typing import Sequence

def is_all_numbers_different_in_seq(p_seq: Sequence) -> bool:
    """
        Determines if all numbers in a sequence are different from each other
        input:
            p_seq - sequence of numbers 
        output:
            bool
    """
    for num in p_seq:
        if p_seq.count(num) > 1:
            return False
    return True
    
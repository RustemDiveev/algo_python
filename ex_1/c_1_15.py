from typing import Sequence

def is_all_numbers_different_in_seq(v_seq: Sequence) -> bool:
    """
        Determines if all numbers in a sequence are different from each other
    """

    for num in v_seq:
        if v_seq.count(num) > 1:
            return False

    return True
    
from typing import List 

def pseudo_reverse_list(i_list: List[int]) -> List[int]:
    """
        Reverses list of integers
    """
    return [i_list[idx] for idx in range(len(i_list)- 1, 0 - 1, -1)]
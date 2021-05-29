from typing import List 

def pseudo_reverse_list(p_list: List[int]) -> List[int]:
    """
        Reverses list of integers
        input:
            p_list - list of integers
        output:
            List[int]
    """
    return [p_list[idx] for idx in range(len(p_list)- 1, 0 - 1, -1)]
    
from typing import List

def get_a_list_from_8_to_m8_with_step_m2() -> List[int]:
    """
        Produces a list of [8, 6, 4, 2, 0, -2, -4, -6, -8]
    """
    return [num for num in range(8, -8 + (-1), -2)]
    
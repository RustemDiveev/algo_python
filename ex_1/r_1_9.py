from typing import List

def get_a_list_from_50_to_80_with_step_10() -> List[int]:
    """
        Produces a list of [50, 60, 70, 80]
    """
    return [num for num in range(50, 81, 10)]
    
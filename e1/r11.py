from typing import List 

def get_list_from_1_to_256_of_power_of_2() -> List[int]:
    """
        Returns a list of [1, 2, 4, 8, 16, 32, 64, 128, 256]
        output:
            List[int]
    """
    return [pow(2, num) for num in range(9)]
    
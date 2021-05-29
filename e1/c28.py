from typing import List 

def norm(p: List[int], v: int=2) -> float:
    """
        Returns sum((a^p+..+z^p)) ^ (1/p)
        input:
            p - list of integers 
            v - multiplier
        output:
            float 
    """
    return sum([i ** v for i in p]) ** (1 / v)

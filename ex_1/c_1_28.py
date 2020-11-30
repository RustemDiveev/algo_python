from typing import List 

def norm(v: List[int], p: int=2) -> float:
    return sum([i ** p for i in v]) ** (1 / p)

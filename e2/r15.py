from typing import Sequence

from e2.r14 import Vector_r14

class Vector_r15(Vector_r14):
    """
        Modified init, you may pass a sequence of numbers
    """
    def __init__(self, d):
        if isinstance(d, int):
            super().__init__(d)
        elif isinstance(d, (tuple, list)):
            super().__init__(len(d))
            for i in range(len(d)):
                self[i] = d[i]
        else:
            raise TypeError("Impossible to instantiate vector - wrong type of argument")

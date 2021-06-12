from e2.r13 import Vector_r13

class Vector_r14(Vector_r13):
    """
        Reworked mul to support vector multiplying 
    """
    def __mul__(self, other):
        if isinstance(other, Vector_r14):
            if len(self) != len(other):
                raise ValueError("dimensions must match")
            else:
                l_result = 0
                for i in range(len(self)):
                    l_result += self[i] * other[i]
            return l_result
        else:
            return self * other

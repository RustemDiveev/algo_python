from e2.r10 import Vector_r10

class Vector_r11(Vector_r10):
    """
        Added radd method
    """
    def __radd__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must match")
        l_result = Vector_r10(len(self))
        for i in range(len(self)):
            l_result[i] = self[i] + other[i]
        return l_result

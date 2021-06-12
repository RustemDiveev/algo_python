from e2.r11 import Vector_r11

class Vector_r12(Vector_r11):
    """
        Implemented __mul__ method
    """
    def __mul__(self, p_number: float):
        if not isinstance(p_number, (int, float)):
            raise TypeError("Vector can be multiplied by number only")
        l_result = Vector_r12(len(self))
        for i in range(len(self)):
            l_result[i] = self[i] * p_number
        return l_result

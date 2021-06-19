from e2.r15 import Vector_r15

class Vector_c25(Vector_r15):

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            l_result = Vector_c25(len(self))
            for i in range(len(self)):
                l_result[i] = self[i] * other 
            return l_result
        elif isinstance(other, (Vector_r15, Vector_c25)):
            if len(self) != len(other):
                raise ValueError("Dimenstions must match!")
            l_result = 0
            for i in range(len(self)):
                l_result += self[i] * other[i]
            return l_result
        else:
            raise TypeError("Unable to multiply - argument should be a number or Vector instance")

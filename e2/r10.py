from e2.r9 import Vector_r9

class Vector_r10(Vector_r9):
    """
        Added __neg__ method 
    """
    def __neg__(self):
        # Useless, because it works for self
        # l_vector = super().__init__(len(self))
        l_vector = Vector_r9(len(self))
        for i in range(len(self)):
            l_vector[i] = self[i] * (-1)
        return l_vector 

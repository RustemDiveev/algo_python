from e2.r12 import Vector_r12 

class Vector_r13(Vector_r12):
    """
        Implemented __rmul__
    """
    def __rmul__(self, other):
        return super().__mul__(p_number=other) 

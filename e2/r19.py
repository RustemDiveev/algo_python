from e2.r18 import Progression

class ArithmeticProgression(Progression):   
    """
        Iterator producing an arithmetic progression
    """

    def __init__(self, increment=1, start=0):
        """
            Create a new arithmetic progression.

            increment   the fixed constant to add to each term (default 1)
            start       the first term of the progression (default 0)
        """
        super().__init__(start)     
        self._increment = increment 

    def _advance(self):
        """
            Update current value by adding the fixed increment.
        """
        self._current += self._increment

"""
# Takes too long
l_ap = ArithmeticProgression(increment=128, start=0)
l_cnt = 0 
l_current_value = 0
while l_current_value < 2**30:
    l_current_value = next(l_ap)
    l_cnt += 1
print(l_cnt)
"""

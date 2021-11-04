from typing import Union
from math import sqrt

from e2.Progression import Progression

class ProgressionSqrt(Progression):
    """
        Every value is squared root of previous value in that progression
    """

    def __init__(self, start: Union[int, float]=65536):
        """
            Initialize current to the first value of the progression.
        """
        super().__init__(start)
        if not isinstance(self._current, (int,float)):
            raise ValueError("start value must be an integer or float")

        self._counter = -1

    def _advance(self):
        """
            Update self._current to a new value - is a sqrt of start_value
        """
        self._current = sqrt(self._current)

    def __next__(self):
        """
            Returns next element
        """
        self._counter += 1
        if self._counter != 0:
            self._advance()
        return self._current

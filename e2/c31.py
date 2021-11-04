from e2.Progression import Progression

class ProgressionAbs(Progression):
    """
        Progression in which every member is an abs of difference 
        between previous two values
    """

    def __init__(self, p_start_value: int=2, p_end_value: int=200):
        """
            Constructor 
            input: 
                p_start_value - starting value 
                p_end_value - ending_value 
        """
        if isinstance(p_start_value, (int)):
            self._start_value = p_start_value 
        else:
            raise ValueError("p_start_value should be an integer.")

        if isinstance(p_end_value, (int)):
            self._end_value = p_end_value 
        else:
            raise ValueError("p_end_value should be an integer.") 

        self._iteration_counter = -1
        
    def _advance(self):
        """
            We assume that end value is current value 
            We calculate current value as abs between previous two values 
            and we assign end_value to a start_value to remember it in further 
            calculations.
        """
        self._start_value, self._end_value = self._end_value, abs(self._end_value - self._start_value)

    def __next__(self):
        """
            Returns the next element
        """
        self._iteration_counter += 1

        if self._iteration_counter == 0:
            return self._start_value
        elif self._iteration_counter == 1:
            return self._end_value
        else:
            self._advance()
            return self._end_value

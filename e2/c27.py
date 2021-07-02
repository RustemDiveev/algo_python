# from time import perf_counter

class Range:
    """
        A class that mimic's the built-in range class.
    """

    def __init__(self, start, stop=None, step=1):
        """
            Initialize a Range instance
            Semantics is similar to built-in range class 
        """
        if step == 0:
            raise ValueError('step cannot be 0')

        if stop is None:                # special case of range(n)
            start, stop = 0, start      # should be treated as if range(0,n)

        # calculate the effective length once 
        self._length = max(0, (stop - start + step - 1) // step)

        # need knowledge of start and step (but not stop) to support __getitem__
        self._start = start 
        self._step = step 

    def __len__(self):
        """
            Return number of entries in the range.
        """
        return self._length 

    def __getitem__(self, k):
        """
            Return entry at index k (using standard interpretation if negative)
        """
        if k < 0:
            k += len(self)

        if not 0 <= k < self._length:
            raise IndexError('index out of range')
        
        return self._start + k * self._step 

    def __contains__(self, p_element: int) -> bool:
        """
            Return True if element exists in a Range, False otherwise 
            input:
                p_element - value, which needs to be searched
            output:
                bool
        """
        l_result = (p_element - self._start) / self._step
        return True if l_result % 1 == 0 and l_result < len(self) else False

# l_start = perf_counter()
# 2 in Range(100000000)
# l_end = perf_counter()
# l_time1 = l_end - l_start
# print(l_time1)

# l_start = perf_counter()
# 99999999 in Range(100000000)
# l_end = perf_counter()
# l_time2 = l_end - l_start
# print(l_time2)

# print(l_time2 / l_time1)

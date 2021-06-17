from abc import ABCMeta, abstractmethod

"""
    Copied from r22.py, because needed to implement method in abstract class 
"""

class Sequence(metaclass=ABCMeta):
    """
        Our own version of collections.Sequence abstract base class. 
    """

    @abstractmethod
    def __len__(self):
        """
            Return the length of the sequence.
        """
    
    @abstractmethod
    def __getitem__(self, j):
        """
            Return the element at index j of the sequence 
        """

    def __contains__(self, val):
        """
            Return True if val found in the sequence; False otherwise 
        """
        for j in range(len(self)):
            if self[j] == val:
                return True 
        return False 

    def index(self, val):
        """
            Return leftmost index at which val is found (or raise ValueError)
        """
        for j in range(len(self)):
            if self[j] == val:      # leftmost match 
                return j 
        raise ValueError('value not in sequence')

    def count(self, val):
        """
            Return the number of elements equal to given value.
        """
        k = 0 
        for j in range(len(self)):
            if self[j] == val:
                k += 1 
        return k

    def __eq__(self, other):
        """
            Returns True if both collection has the same length and elements, returns False otherwise
        """
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False 
        return True

    def __lt__(self, other):
        """
            We take the smallest length from two sequences and within that range begin to compare each element
            if first element of first sequence is less than first element of second sequence - return true - otherwise - False
        """
        l_len = min(len(self), len(other))
        if l_len == 0 and len(self) <= len(other):
            return False 
        else:
            for i in range(l_len):
                if self[i] < other[i]:
                    return True
                elif self[i] == other[i]:
                    pass 
                else:
                    return False
        return False
        
class ExampleList_r23(Sequence):

    def __init__(self, list_data: list):
        """
            Very rude but we need to pass sequence as data for class instance
        """
        if not isinstance(list_data, list):
            raise TypeError("You should pass list to ExampleList")
        self._data = list_data

    def __len__(self):
        return len(self._data)

    def __getitem__(self, idx):
        try:
            return self._data[idx]
        except IndexError:
            raise IndexError("Element with such index doesn't exist in ExampleList")

#l_1 = ExampleList_r23([1,2,3,4])
#l_2 = ExampleList_r23([1,2,3,4])
#print(l_1 < l_2)
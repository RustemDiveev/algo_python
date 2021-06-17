from abc import ABCMeta, abstractmethod

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

class ExampleList(Sequence):

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

#l_a = ExampleList([1,2])        
#l_b = ExampleList([1,2])
#print(l_a == l_b)
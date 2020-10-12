from random import randrange
from typing import Sequence, Any

def pseudo_choice(i_seq: Sequence) -> Any:
    """
        Returns random element from Sequence 
        with usage of randrange function 
    """
    return i_seq[randrange(len(i_seq)-1)]

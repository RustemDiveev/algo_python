from random import randrange
from typing import Sequence, Any

def pseudo_choice(p_seq: Sequence) -> Any:
    """
        Returns random element from Sequence 
        with usage of randrange function 
        input:
            p_seq - any sequence of any elements
    """
    return p_seq[randrange(len(p_seq)-1)]

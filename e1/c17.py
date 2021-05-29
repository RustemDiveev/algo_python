from typing import Sequence

# Function won't work if input params are immutable collectons, ex: frozenset, tuple
# Check tests for proofs
# Function can be changed by adding return final value 
def scale_incorrect(p_data: Sequence, p_factor: int):
    """
        Incorrect function of scale for exercise purpose
        input:
            p_data - sequence of numbers 
            p_factor - multiplier
    """
    for val in p_data:
        val *= p_factor

def scale_correct(p_data: Sequence, p_factor: int) -> Sequence:
    """
        Correct function of scale which works with most sequence types 
        input:
            p_data - sequence of numbers 
            p_factor - multiplier
        output:
            Sequence based on type of p_data
    """
    l_datatype = str(type(p_data))

    if l_datatype == "<class 'list'>":
        l_result = [elem * p_factor for elem in p_data]
    elif l_datatype == "<class 'tuple'>":
        l_result = tuple([elem * p_factor for elem in p_data])
    elif l_datatype == "<class 'set'>":
        l_result = {elem * p_factor for elem in p_data}
    elif l_datatype == "<class 'dict'>":
        # Ugly but simple (probably not the best) - maybe zip is more beautiful
        l_result = p_data
        for elem in l_result:
            l_result[elem] *= p_factor
    elif l_datatype == "<class 'frozenset'>":
        l_result = frozenset({elem * p_factor for elem in p_data})

    return l_result

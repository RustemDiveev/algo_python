from ex_1.c_1_16 import scale
from typing import Sequence

# Function won't work if input params are immutable collectons, ex: frozenset, tuple
# Check tests for proofs
# Function can be changed by adding return final value 

def scale_correct(data: Sequence, factor: int) -> Sequence:

    # TODO:
    # Experiment 1: check what is fastest: str(type) vs isinstance 
    # Experiment 2: zip vs assignment + for loop

    # Assume that possible datatypes of data are tuple, list, dict, set, frozenset
    # Very ugly determination of datatype, isinstance may be better
    datatype = str(type(data))

    if datatype == "<class 'list'>":
        result = [elem * factor for elem in data]
    elif datatype == "<class 'tuple'>":
        result = tuple([elem * factor for elem in data])
    elif datatype == "<class 'set'>":
        result = {elem * factor for elem in data}
    elif datatype == "<class 'dict'>":
        # Ugly but simple (probably not the best) - maybe zip is more beautiful
        result = data
        for elem in result:
            result[elem] *= factor
    elif datatype == "<class 'frozenset'>":
        result = frozenset({elem * factor for elem in data})

    return result
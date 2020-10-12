def get_str_positive_idx_by_negaive_idx(str_length: int, neg_idx: int) -> int:
    """
        Returns positive idx of string element with specified negative idx 
        input:
            str_length - int, a length of input string 
            neg_idx    - int, a negative index of selected element 
    """

    # Check if neg_idx is negative 
    if int(neg_idx) >= 0:
        raise ValueError("neg_idx must be less than a zero")

    # Check if neg_idx doesn't exceed string length 
    if abs(neg_idx) > str_length:
        raise ValueError("neg_idx out of range")

    return str_length + neg_idx
    
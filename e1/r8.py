def get_str_positive_idx_by_negaive_idx(p_length: int, p_negative_index: int) -> int:
    """
        Returns positive idx of string element with specified negative idx 
        input:
            p_length - int, a length of input string 
            p_negative_index - int, a negative index of selected element 
        output:
            int - positive index of negative index string element
    """
    # Check if p_negative_index is negative 
    if int(p_negative_index) >= 0:
        raise ValueError("p_negative_index must be less than a zero")
    # Check if p_negative_index doesn't exceed string length 
    if abs(p_negative_index) > p_length:
        raise ValueError("p_negative_index out of range")

    return p_length + p_negative_index
    
def is_even(p_k: int) -> bool:
    """
        Returns True if k is even, or False otherwise
        input:
            p_k - input number
        output:
            bool
    """
    return not bool(p_k & 1) 
    
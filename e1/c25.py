def get_remove_punctuation(p_str: str) -> str:
    """
        Removes punctuation marks from input string
        input:
            p_str - input string
    """
    l_punctuation_str = ".,?!'"
    l_str = p_str
    for mark in l_punctuation_str:
        l_str = l_str.replace(mark, "")
    return l_str

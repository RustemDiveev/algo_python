def get_remove_punctuation(i_str: str) -> str:
    """
        Removes punctuation marks from input string
    """
    v_punctuation_list = [".", ",",  "?", "!", "'"]
    for mark in v_punctuation_list:
        i_str = i_str.replace(mark, "")

    return i_str

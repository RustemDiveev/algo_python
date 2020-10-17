def produce_list_of_alphabet() -> list:
    """
        Produces a list of small letters of english alphabet
    """
    v_first_letter_idx = ord("a")
    v_last_letter_idx = ord("z")
    
    return [chr(idx) for idx in range(v_first_letter_idx, v_last_letter_idx + 1)]

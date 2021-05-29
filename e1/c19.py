def produce_list_of_alphabet() -> list:
    """
        Produces a list of small letters of english alphabet
        output:
            list
    """
    l_first_letter_idx = ord("a")
    l_last_letter_idx = ord("z")   
    return [chr(idx) for idx in range(l_first_letter_idx, l_last_letter_idx + 1)]

from random import randint

def error_generator_remove_one_random_symbol(p_str: str) -> str:
    """
        Removes random symbol from string and returns the new string
        input:
            p_str - input string
    """

    if len(p_str) == 0:
        return p_str

    l_random_idx = randint(0, len(p_str)- 1)
    return p_str[:l_random_idx] + p_str[l_random_idx+1:]

from random import randint

def error_generator_remove_one_random_symbol(p_str: str) -> str:
    """
        Removes random symbol from string and returns the new string
        input:
            p_str - input string
        output:
            new string
    """
    if len(p_str) == 0:
        return p_str

    l_random_idx = randint(0, len(p_str) - 1)
    return p_str[:l_random_idx] + p_str[l_random_idx+1:]

def error_generator_add_one_random_symbol_to_random_place(p_str: str) -> str:
    """
        Adds random english letter to random place to string an returns new string 
        input:
            p_str - input string 
        output:
            new string
    """
    l_random_idx = randint(0, len(p_str) - 1) 

    """
        ord("a") = 97
        ord("z") = 122 
        ord("A") = 65 
        ord("Z") = 90
    """

    l_random_char_idx = randint(0, 51)
    if l_random_char_idx <= 25:
        l_random_char_idx += 65 
    else:
        l_random_char_idx += 71

    l_random_char = chr(l_random_char_idx)

    return p_str[:l_random_idx] + l_random_char + p_str[l_random_idx:]

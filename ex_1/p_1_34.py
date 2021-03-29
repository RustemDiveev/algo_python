from random import randint, choice

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

def error_generator_change_random_symbol_register(p_str: str) -> str:
    """
        Changes register of one of the random letter in a string and returns new string 
        input:
            p_str - input string
        output: 
            new string
    """
    """
    swapcase() - changes register vice versa
    isalpha() - checks that string consists only of letters
    """
    if len(p_str) == 0:
        return p_str

    l_char_idx_list = []
    for i in range(0, len(p_str) - 1):
        if p_str[i].isalpha():
            l_char_idx_list.append(i)

    if len(l_char_idx_list) == 0:
        return p_str 
    else:
        l_random_idx = choice(l_char_idx_list)
        l_converted_char = p_str[l_random_idx].swapcase()
        return p_str[:l_random_idx] + l_converted_char + p_str[l_random_idx+1:]

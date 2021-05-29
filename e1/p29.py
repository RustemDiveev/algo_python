from typing import List

def get_all_possible_strings_using_character_once(p_str: str) -> List[str]:
    """
        Returns all possible combinations of strings consists of letters of one string 
        which used only once
        input:  
            p_str - input string 
        output:
            List[str] - list of all possible combinations of letters in a string
    """
    l_final_list = []
    if not check_unique_symbols_in_string(p_str=p_str):
        raise ValueError("Input string must contain unique characters!")
    if len(p_str) == 0:
        raise ValueError("Input string must contain at least one character")
    elif len(p_str) == 1:
        l_final_list.append(p_str)
    elif len(p_str) == 2:
        l_first_symbol = p_str[0]
        l_second_symbol = p_str[1]
        l_final_list.append(l_first_symbol + l_second_symbol)
        l_final_list.append(l_second_symbol + l_first_symbol)
    else:
        for i in p_str:
            l_less_str = p_str.replace(i, "")
            l_less_list = get_all_possible_strings_using_character_once(p_str=l_less_str)
            l_final_list += [i + string for string in l_less_list]
    return l_final_list

def check_unique_symbols_in_string(p_str: str) -> bool:
    """
        Checks that input string contains unique characters
        Returns True if it is, False otherwise
        input:
            p_str - input string 
        output:
            bool
    """
    if len(list(p_str)) == len(set(p_str)):
        return True
    else:
        return False

def get_all_strings(p_str: str) -> list:
    """
        Returns list of all possible combinations of symbols in string 
        input:
            p_str - input string 
        output:
            list - all combinations of string symbols
    """
    l_final_list = []
    if len(p_str) == 1:
        return [p_str]
    if len(p_str) == 2:
        l_first_symbol = p_str[0]
        l_second_symbol = p_str[1]
        return [l_first_symbol + l_second_symbol, l_second_symbol + l_first_symbol]        
    else:
        for i in p_str:
            l_str = p_str.replace(i, "")
            l_result = get_all_strings(p_str=l_str)
            l_final_list += [i + string for string in l_result]
        return l_final_list

from random import randint, choice, shuffle

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
    for i in range(len(p_str)):
        if p_str[i].isalpha():
            l_char_idx_list.append(i)

    if len(l_char_idx_list) == 0:
        return p_str 
    else:
        l_random_idx = choice(l_char_idx_list)
        l_converted_char = p_str[l_random_idx].swapcase()
        return p_str[:l_random_idx] + l_converted_char + p_str[l_random_idx+1:]

def error_generator_copy_random_symbol(p_str: str) -> str:
    """
        Chooses random symbol from string and adds it next to the chosen symbol and returns new string 
        input:
            p_str - input string 
        output:
            new string
    """
    if len(p_str) == 0:
        return p_str 

    l_random_idx = randint(0, len(p_str) - 1)
    return p_str[:l_random_idx] + p_str[l_random_idx] + p_str[l_random_idx:]

def error_generator_replace_random_vowel(p_str: str) -> str:
    """
        Replaces random vowel with another random vowel in a string and returns new string
        input:
            p_str - input string 
        output:
            new string
    """
    if len(p_str) == 0:
        return p_str 

    l_vowels_str = "aeiouyAEIOUY"
    l_vowels_str_lower = "aeiouy"
    l_vowels_str_upper = "AEIOUY"
    l_vowels_idx_list = []
    for i in range(len(p_str)):
        if p_str[i] in l_vowels_str:
            l_vowels_idx_list.append(i)
    
    if len(l_vowels_idx_list) == 0:
        return p_str 
    else:
        l_random_vowel_idx = choice(l_vowels_idx_list)
        l_random_vowel = p_str[l_random_vowel_idx]
        if l_random_vowel.isupper():
            l_random_vowel = choice(l_vowels_str_upper.replace(l_random_vowel, ""))
        else:
            l_random_vowel = choice(l_vowels_str_lower.replace(l_random_vowel, ""))

    return p_str[:l_random_vowel_idx] + l_random_vowel + p_str[l_random_vowel_idx + 1:]

def error_generator_replace_random_consonant(p_str: str) -> str:
    """
        Replaces random consonant with another random consonant in a string and returns new string
        input:
            p_str - input string 
        output:
            new string
    """
    if len(p_str) == 0:
        return p_str

    l_consonant_str = "bcdfghjklmnpqrstvwxz"
    l_consonant_idx_list = []
    for i in range(len(p_str)):
        if p_str[i] in l_consonant_str or p_str[i] in l_consonant_str.upper():
            l_consonant_idx_list.append(i)

    if len(l_consonant_idx_list) == 0:
        return p_str 
    else:
        l_random_consonant_idx = choice(l_consonant_idx_list)
        l_random_consonant = p_str[l_random_consonant_idx]
        if l_random_consonant.is_upper():
            l_random_consonant = choice(l_consonant_str.upper().replace(l_random_consonant, ""))
        else:
            l_random_consonant = choice(l_consonant_str.replace(l_random_consonant, ""))

    return p_str[:l_random_consonant_idx] + l_random_consonant + p_str[l_random_consonant_idx+1:]
    
def error_generator_remove_dot_from_end(p_str: str) -> str:
    """
        Removes dot from the end of string and returns new string 
        input:
            p_str - input string 
        output:
            new string 
    """
    if len(p_str) == 0:
        return p_str
    else:
        if p_str[-1] == ".":
            del p_str[-1]
        return p_str

def error_generator_remove_random_space(p_str: str) -> str:
    """
        Removes random space from the string and returns new string 
        input: 
            p_str - input string 
        output:
            new string 
    """
    if len(p_str) == 0:
        return p_str 

    l_space_idx_list = []
    for i in range(len(p_str)):
        if p_str[i] == " ":
            l_space_idx_list.append(i)

    if len(l_space_idx_list) == 0:
        return p_str

    l_random_space_idx = choice(l_space_idx_list)
    return p_str[:l_random_space_idx] + p_str[l_random_space_idx+1:]

def get_list_of_error_sentences(p_str: str, p_sentence_count: int) -> list:
    """
        Returns list of sentences with applied errors 
        input:
            p_str - input sentence
            p_sentence_count - amount of sentences, should be greater or equal to 8
        output:
            list of sentences
    """

    if len(p_str) == 0:
        raise ValueError("get_list_of_error_sentences - p_str must not be an empty string!")

    if p_sentence_count < 8:
        raise ValueError("generate_error_type_set - p_sentence_count must be greater or equal than 8!")

    l_output_list = []
    l_output_list.append(error_generator_remove_one_random_symbol(p_str=p_str))
    l_output_list.append(error_generator_add_one_random_symbol_to_random_place(p_str=p_str))
    l_output_list.append(error_generator_change_random_symbol_register(p_str=p_str))
    l_output_list.append(error_generator_copy_random_symbol(p_str=p_str))
    l_output_list.append(error_generator_replace_random_vowel(p_str=p_str))
    l_output_list.append(error_generator_replace_random_consonant(p_str=p_str))
    l_output_list.append(error_generator_remove_dot_from_end(p_str=p_str))
    l_output_list.append(error_generator_remove_random_space(p_str=p_str))

    while len(l_output_list) < p_sentence_count:
        l_output_list.append(p_str)

    return shuffle(l_output_list)

def print_sentences(p_sentence_list: list):
    """
        Prints sentences from sentence list and labels each with order number
        input: 
            p_sentence_list - input sentence list
    """
    for i in range(len(p_sentence_list)):
        print(str(i+1) + ":" + p_sentence_list[i])

def main(p_str: str, p_sentence_count: int):
    """
        Main block of program - prints sentences with random error
        input:
            p_str - input sentence 
            p_sentence_count - count of sentences
    """
    l_sentence_list = get_list_of_error_sentences(p_str=p_str, p_sentence_count=p_sentence_count)
    print_sentences(p_sentence_list=l_sentence_list)
    
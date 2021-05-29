def count_vowels_in_str(p_str: str) -> int:
    """
        Return amount of vowels in a string
        input:
            p_str - input string 
        output:
            int 
    """
    # Perhaps there is more beautiful solution
    l_vowels_str = "aeiouyаеёиоуыэюя"
    l_str = p_str.lower()
    l_result = 0 
    for vowel in l_vowels_str:
        l_result += l_str.count(vowel)

    return l_result

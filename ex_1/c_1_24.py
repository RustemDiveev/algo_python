def count_vowels_in_str(i_str: str) -> int:
    """
        Return amount of vowels in a string 
    """
    # Perhaps there is more beautiful solution
    v_vowels_str = "aeiouyаеёиоуыэюя"
    v_str = i_str.lower()
    v_result = 0 

    for vowel in v_vowels_str:
        v_result += v_str.count(vowel)

    return v_result

def minmax(p_data: list) -> tuple:
    """
        Returns tuple of length two of min and max value in number sequence
        input:
            p_data - a list of numbers
        output
            tuple
    """
    l_min = l_max = int(p_data[0])

    for number in p_data:
        l_min = number if number < l_min else l_min
        l_max = number if number > l_max else l_max

    return (l_min, l_max) 
        
def minmax(data: list) -> tuple:
    """
        Returns tuple of length two of min and max value in number sequence
        input:
            data - a list of numbers
    """
    v_min = v_max = int(data[0])

    for number in data:
        v_min = number if number < v_min else v_min
        v_max = number if number > v_max else v_max

    return (v_min, v_max) 
        
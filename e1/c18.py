def produce_list() -> list:
    """
        Produces a list with a list comprehension syntax of 
        [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
        output:
            list
    """
    return [x * (x+1) for x in range(10)]

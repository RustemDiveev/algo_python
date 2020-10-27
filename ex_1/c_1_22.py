def dot_product_of_lists(a_list: list, b_list: list) -> list:
    """
        Returns a list with each element is a multiply of elements with same idx in two lists
    """

    def check_list_consists_only_of_ints(i_list: list) -> bool:
        """
            Returns True if list consists only of ints
        """
        for i in i_list:
            if isinstance(i, int):
                continue
            else:
                return False

        return True
    
    if check_list_consists_only_of_ints(a_list) is False:
        raise ValueError("a_list should contain only ints")

    if check_list_consists_only_of_ints(a_list) is False:
        raise ValueError("b_list should contain only ints")

    if len(a_list) != len(b_list):
        raise ValueError("Lengths of list should be equal")

    return [a_list[i] * b_list[i] for i in range(len(a_list))]
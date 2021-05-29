def dot_product_of_lists(p_a_list: list, p_b_list: list) -> list:
    """
        Returns a list with each element is a multiply of elements with same idx in two lists
        input:
            p_a_list - first input list 
            p_b_list - second input list 
        output:
            list - result of p_a_list * p_b_list by elements
    """

    def check_list_consists_only_of_ints(p_list: list) -> bool:
        """
            helper - Returns True if list consists only of ints
            input:
                p_list - input list 
            output:
                bool
        """
        for i in p_list:
            if isinstance(i, int):
                continue
            else:
                return False
        return True
    
    if check_list_consists_only_of_ints(p_list=p_a_list) is False:
        raise ValueError("a_list should contain only ints")

    if check_list_consists_only_of_ints(p_list=p_a_list) is False:
        raise ValueError("b_list should contain only ints")

    if len(p_a_list) != len(p_b_list):
        raise ValueError("Lengths of list should be equal")

    return [p_a_list[i] * p_b_list[i] for i in range(len(p_a_list))]
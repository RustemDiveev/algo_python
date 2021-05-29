# Some useless task
def list_index_out_of_bounds():
    """
        Catches IndexError and prints message 
    """
    l_list = []
    try:
        l_list[0] = "blablabla"
    except IndexError:
        print("Don't try buffer overflow attacks in Python!")
        
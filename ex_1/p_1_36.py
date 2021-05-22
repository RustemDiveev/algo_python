from collections import Counter

def print_counter(p_counter: Counter):
    """
        Helper for debugging 
        Prints counter to text file 
        input:
            p_counter - counter to print
    """
    l_file = open("ex_1/p_1_36_result.txt", "w+")
    for i in p_counter.keys():
        l_file.write(i + ": " + str(p_counter[i]) + "\n")

def read_simple_file() -> Counter:
    """
        Reads file with space delimited words and returns counter of words
    """
    l_list = []
    l_file = open("ex_1/p_1_36_txt_space_delimited_words.txt", "r")
    l_lines = l_file.readlines()
    for line in l_lines:
        l_list += line.split()
    l_result = Counter(l_list)
    return l_result

print_counter(p_counter=read_simple_file())
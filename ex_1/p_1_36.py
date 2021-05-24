from collections import Counter

C_IGNORE_TOKENS_SET = {"-", "–"}

def print_counter(p_counter: Counter):
    """
        Helper for debugging 
        Prints counter to text file 
        input:
            p_counter - counter to print
    """
    l_file = open("ex_1/p_1_36_result.txt", "w+", encoding="utf8")
    for i in p_counter.most_common():
        l_file.write(i[0] + ": " + str(i[1]) + "\n")

def format_line(p_str: str) -> str:
    """
        Removes punctuation and other useless symbols from a string
        input:
            p_str - input string 
        output:
            str
    """
    l_restricted_token_str = ".,;?!\"[]()0123456789"
    l_str = p_str
    for token in l_restricted_token_str:
        l_str = l_str.replace(token, "")
    l_str = l_str.lower()
    return l_str

def read_simple_file() -> Counter:
    """
        Reads file with space delimited words and returns counter of words
    """
    l_list = []
    l_file = open("ex_1/p_1_36/p_1_36_txt_space_delimited_words.txt", "r")
    l_lines = l_file.readlines()
    for line in l_lines:
        l_list += line.split()
    l_result = Counter(l_list)
    return l_result

def count_words_in_file(p_file_path: str) -> Counter:
    """
        Reads text file and returns counter of words
        input:
            p_file_path - path to text file 
        output:
            word counter
    """
    l_list = []
    try:
        l_file = open(p_file_path, "r", encoding="utf8")
        l_lines = l_file.readlines()
        for line in l_lines:
            l_list += format_line(p_str=line).split()
        l_result = Counter(elem for elem in l_list if elem not in C_IGNORE_TOKENS_SET)
        return l_result
    except FileNotFoundError:
        print("Файл по пути " + p_file_path + " не обнаружен.")

#print_counter(p_counter=read_simple_file()) 
#print_counter(p_counter=count_words_in_file(p_file_path="ex_1/p_1_36/_kryzhovnik.txt"))
print_counter(p_counter=count_words_in_file(p_file_path="ex_1/p_1_36/_voyna_i_mir.txt"))
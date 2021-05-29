from collections import Counter

C_IGNORE_TOKENS_SET = {"-", "–", "—", "и", "в", "не", "на", "он", "c", "как", "я", "а", \
    "что", "но", "всё", "к", "это", "его", "то", "от", "было", "у", "был", "уже", "из", "тогда", \
    "только", "когда", "теперь", "по", "него", "о", "во", "ни", "за", "с", "только", "говорил", \
    "бы", "они", "мы", "себе", "меня", "ему", "мне", "же", "да", "мой", "для", "бы", "были", "который", \
    "себя", "без", "которые", "потом", "вы", "через", "тут", "где", "или", "тоже", "свое", "эти", "есть", "нет", \
    "если", "нужно", "пока", "была", "свои", "нас", "так", "там", "про", "ли", "под", "уж", "тех", "чтобы", \
    "даже", "себя", "она", "все", "ее", "еще", "того", "ты", "этого", "их", "быть", "ей", "до", "опять", "этот", "тем", \
    "сказал", "сказала", "вот", "всех", "ничего", "чем", "потому", "очень", "после", "своей", "ну", "при", "вдруг", "ним", \
    "будет", "будто", "может", "надо", "что-то", "конечно", "хоть", "можно", "стал", "них", "лишь", "слишком", "почти", "со", "тот", \
    "том", "вам", "этом", "просто", "вас", "кто", "собой", "например", "свою", "всего", "ибо", "ведь", "над", "тебя", \
    "сразу", "тебе", "всем", "ней", "которого", "моей", "нам", "всю", "нее", "м", "именно", "этой", "об", "г", \
    "своих", "им", "т", "те", "ко"}

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
    l_restricted_token_str = ".,;?!\"[]()*%«»№/0123456789"
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
#print_counter(p_counter=count_words_in_file(p_file_path="ex_1/p_1_36/_voyna_i_mir.txt"))
#print_counter(p_counter=count_words_in_file(p_file_path="ex_1/p_1_36/albtair.txt"))
#print_counter(p_counter=count_words_in_file(p_file_path="ex_1/p_1_36/anti_zeland.txt"))
#print_counter(p_counter=count_words_in_file(p_file_path="ex_1/p_1_36/avtobiograficheskaja_proza.txt"))
#print_counter(p_counter=count_words_in_file(p_file_path="ex_1/p_1_36/kak_delajut_antisemitom.txt"))
#print_counter(p_counter=count_words_in_file(p_file_path="ex_1/p_1_36/zapiski_yunogo_vracha.txt"))

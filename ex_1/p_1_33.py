"""
Воспроизведение пользовательских ошибок
1. ERROR: Есть недопустимый символ в выражении.
Воспроизведение:
1. blablabla

2. ERROR: В выражении неправильно расставлены скобки. Преждевременно встретилась закрывающая скобка.
Воспроизведение:
1. )

3. ERROR: В выражении неправильно расставлены скобки. Отсутствует закрывающая скобка.
Воспроизведение:
1. (

4. ERROR: Выражение должно начинаться с открывающейся скобки или числа.
Воспроизведение:
1. -32

5. ERROR: Выражение должно заканчиваться на закрывающуюся скобку, число или знак равенства.
Воспроизведение:
1. 3-

6. ERROR: Неправильное выражение - за оператором следует закрывающая скобка.
Воспроизведение:
1. 20 + (3-3*)

7. ERROR: Неправильное выражение - оператор следует сразу после открывающей скобки.
Воспроизведение:
1. 20 + (+3-2)

8. ERROR: Неправильное выражение - после оператора следует разделитель числа.
Воспроизведение: 
1. 8+.4

9. ERROR: Неправильное выражение - разделитель числа следует перед оператором.
Воспроизведение:
1. 30.+23

10. ERROR: Неправильное выражение - знак равенства следует перед оператором.
Воспроизведение:
1. 1+1=-4

11. ERROR: Неправильное выражение - равенство следует после оператора.
Воспроизведение:
1. 5-=3

12. ERROR: Неправильное выражение - два оператора следуют подряд
Воспроизведение:
1. 8++3

13. ERROR: Знак равенства может быть только один и должен находиться в конце выражения
Воспроизведение
1. 8 = 3

14. ERROR: Перед разделителем числа не найдено цифры
Воспроизведение:
1. (.3+123)

15. ERROR: После разделителя числа не найдено цифры
Воспроизведение:
1. (3+13.)

16. INFO: Список результатов вычислений очищен. Введите арифметическое выражение для расчета.
Воспроизведение:
1. 2 + 3
2. c

17. INFO: Список результатов вычислений уже пуст. Введите арифметическое выражение для расчета.
Воспроизведение:
1. c

18. INFO: Выполнен переход к предыдущему результату вычислений - 
Воспроизведение:
1. 80 + 20
2. -30
3. r

19. INFO: В истории вычислений было только одно значение. История пуста
Воспроизведение:
1. 20 + 30
2. r

20. INFO: Нечего очищать. История вычислений пуста.
Воспроизведение:
1. r

21. ERROR: Отсутствует результат предыдущего расчета для использовании в заданном выражении
Воспроизведение:
1. +23
"""

"""Глобальные переменные"""

"""
    Блок констант, содержащих идентификаторы типов символов в выражениях
"""
C_TYPE_ID_NUMBER = 1
C_TYPE_ID_OPERATOR = 2 
C_TYPE_ID_EQUATION = 3 
C_TYPE_ID_OPENING_BRACKET = 4
C_TYPE_ID_CLOSING_BRACKET = 5 
C_TYPE_ID_DOT = 6
C_TYPE_ID_MINUS = 7
C_TYPE_ID_UNKNOWN = 99

"""
    Словарь с идетификаторами типов символов в выражениях
"""
С_DICT_CHAR_TYPE = {
    "NUMBER": C_TYPE_ID_NUMBER,
    "OPERATOR": C_TYPE_ID_OPERATOR,
    "EQUATION": C_TYPE_ID_EQUATION,
    "OPENING_BRACKET": C_TYPE_ID_OPENING_BRACKET,
    "CLOSING_BRACKET": C_TYPE_ID_CLOSING_BRACKET,
    "DOT": C_TYPE_ID_DOT,
    "OPERATOR_MINUS": C_TYPE_ID_MINUS,
    "UNKNOWN": C_TYPE_ID_UNKNOWN
}

"""Хэлперы - вспомогательные функции"""

def get_type_value_by_key(p_str: str) -> int:
    """
        Возвращает значение типа идентификатора исходя из ключа в С_DICT_CHAR_TYPE
        Если ключ не найден в словаре, то возвращает unknown
        input:
            p_str - строка с названием ключа
        output:
            int - идентификатор типа символа 
    """
    try:
        return С_DICT_CHAR_TYPE[p_str]
    except KeyError:
        return C_TYPE_ID_UNKNOWN

def get_char_type_id(p_char: str) -> int:
    """
        Возвращает значение типа идентификатора у заданного символа
        input:
            p_char - символ (строка)
        output:
            int - идентификатор типа символа
    """
    if is_char_number(p_char):
        return get_type_value_by_key("NUMBER")
    elif is_char(p_char, ("-")):
        return get_type_value_by_key("OPERATOR_MINUS")
    elif is_operator(p_char):
        return get_type_value_by_key("OPERATOR")
    elif is_equation(p_char):
        return get_type_value_by_key("EQUATION")
    elif is_opening_bracket(p_char):
        return get_type_value_by_key("OPENING_BRACKET")
    elif is_closing_bracket(p_char):
        return get_type_value_by_key("CLOSING_BRACKET")
    elif is_dot(p_char):
        return get_type_value_by_key("DOT")
    else: 
        return get_type_value_by_key("UNKNOWN")

"""Пользовательские структуры данных"""

class Stack:
    """
        Реализация стека для проверки скобочной последовательности
    """

    def __init__(self):
        """
            Инициализация экземпляра класса 
        """
        self.items = []

    def push(self, item):
        """
            Добавление нового элемента в стек
        """
        self.items.append(item)

    def pop(self):
        """
            Удаление и возврат последнего элемента стека 
        """
        return self.items.pop()

    def __len__(self):
        """
            Текущая длина стека
        """
        return len(self.items)

"""Пользовательские исключения"""

class Error(Exception):
    """
        Стандартный класс для создания пользовательских исключений
    """
    pass 

class InputParameterError(Error):
    """
        Исключение для ошибки входного параметра при вызове функции
        input:
            function_name   - строка - название функции
            parameter_name  - строка - название параметра
            message         - строка - сообщение об ошибке
    """
    def __init__(self, function_name: str, parameter_name: str, message: str):
        """
            Инициализация экземпляра класса
        """
        # Если так не сделать, то не будет появляться пользовательское сообщение об ошибке
        super().__init__(message)
        self.function_name = function_name 
        self.parameter_name = parameter_name 

class ArgsLengthParameterError(InputParameterError):
    """
        Исключение для ошибки неправильной длины параметра args
        input:
            function_name   - строка - название функции
            parameter_name  - строка - название параметра
    """
    def __init__(self, function_name, parameter_name="*args"):
        super().__init__(
            function_name=function_name, 
            parameter_name=parameter_name, 
            message=self.get_message(function_name, parameter_name)
        )

    def get_message(self, function_name: str, parameter_name: str) -> str:
        """
            Геттер сообщения об ошибке - формирование шаблона для отображения интерпретатором 
            input:
                function_name   - строка - название функции
                parameter_name  - строка - название параметра
        """
        return "Function: {0} -> Parameter: {1} -> Parameter must has a length of one.".format(
            function_name, parameter_name
        )

class ListsHaveNonEqualLengthError(Error):
    """
        Исключение для ошибки несовпадения длин списков 
        Для сравнения списков с символами (токенами) и типами символов (токенов)
        input:
            function_name   - название функции
            list_name_1     - название первого списка 
            list_name_2     - название второго списка 
            length_list_1   - длина первого списка 
            length_list_2   - длина второго списка 
            message         - сообщение об ошибке
    """
    def __init__(self, function_name: str, list_name_1: str, list_name_2: str, 
        length_list_1: int, length_list_2: int, message: str):
        super().__init__(message)
        self.function_name = function_name
        self.list_name_1 = list_name_1
        self.list_name_2 = list_name_2
        self.length_list_1 = length_list_1
        self.length_list_2 = length_list_2

class ClosingBracketNotFoundError(Error):
    """
        Исключение для ошибки не найденой закрывающей скобки, при наличии открывающей
        По идее, никогда не воспроизведется при правильной проверке скобочной последовательности
        input:
            function_name           - название функции
            checked_list            - проверяемый список
            opening_bracket_idx     - индекс открывающей скобки в проверяемом списке
            message                 - сообщение об ошибке
    """
    def __init__(self, function_name: str, checked_list: list, opening_bracket_idx: int, message: str):
        super().__init__(message)
        self.function_name = function_name
        self.checked_list = checked_list 
        self.opening_bracket_idx = opening_bracket_idx


"""Проверки символов"""

def is_char(p_str: str, p_check_symbol: str="") -> bool:
    """
        Является ли входящая строка одним символом. 
        Если есть *args и его длина один, то проверка на совпадение
        input:
            p_str           - входная строка 
            p_check_symbol  - символ, который проверяется на совпадение
        output: 
            bool            - результат проверки (True | False)
    """
    l_result = True if isinstance(p_str, str) and len(p_str) == 1 else False

    if p_check_symbol:
        if len(p_check_symbol) == 1:
            return l_result & (p_str == p_check_symbol)
        else:
            raise ValueError("Длина p_check_symbol превышает единицу")
    else:
        return l_result

def is_char_number(p_char: str) -> bool:
    """
        Является ли символ цифрой.
        input:
            p_char  - входной символ   
        output:
            bool    - результат проверки (True | False)
    """
    if is_char(p_char):
        try:
            int(p_char) 
            return True 
        except ValueError:
            return False 

def is_operator(p_char: str) -> bool:
    """
        Является ли символ оператором 
        input: 
            p_char  - входной символ
        output:
            bool    - результат проверки (True | False)
    """
    return is_char(p_char, "+") or is_char(p_char, "-") \
        or is_char(p_char, "*") or is_char(p_char, "/")

def is_equation(p_char: str) -> bool:
    """
        Является ли символ знаком равенства
        input:
            p_char  - входной символ
        output:
            bool    - результат проверки (True | False)
    """
    return is_char(p_char, "=")

def is_opening_bracket(p_char: str) -> bool:
    """
        Является ли символ открывающейся скобкой
        input:
            p_char  - входной символ
        output:
            bool    - результат проверки (True | False)
    """
    return is_char(p_char, "(") 

def is_closing_bracket(p_char: str) -> bool:
    """
        Является ли символ закрывающейся скобкой
        input:
            p_char  - входной символ
        output:
            bool    - результат проверки (True | False)
    """
    return is_char(p_char, ")") 

def is_dot(p_char: str) -> bool:
    """
        Является ли символ точкой
        input:
            p_char  - входной символ
        output:
            bool    - результат проверки (True | False)
    """
    return is_char(p_char, ".")

def is_valid_char(p_char: str) -> bool: 
    """
        Является ли символ допустимым в введенном выражении
        input:
            p_char  - входной символ
        output:
            bool    - результат проверки (True | False)
    """
    return is_char_number(p_char) or is_operator(p_char) or is_equation(p_char)  \
        or is_equation(p_char) or is_opening_bracket(p_char) or is_closing_bracket(p_char) \
        or is_dot(p_char)

def is_number(p_str: str) -> bool:
    """
        Является ли строка числом (разрешено больше 1 символа)
        input:
            p_str   - входная строка
        output:
            bool    - результат проверки (True | False)
    """
    try:
        float(p_str) 
        return True
    # ValueError, TypeError - могут быть разные ошибки, поэтому обрабатываем все возможные исключения
    except:
        return False
        
"""Парсинг и преобразование строки"""

def trim_whitespace(p_str: str) -> str:
    """
        Функция удаляет все пробелы из строки и возвращает преобразованную строку 
        input: 
            p_str   - входная строка
        output:
            str     - преобразованная строка 
    """
    return p_str.replace(" ", "") 

def is_valid_input(p_str: str) -> tuple:
    """
        Проверка введенного выражения на валидность
        input:
            p_str   - входная строка 
        output:
            tuple
            [0]     - результат проверки: True/False
            [1]     - сообщение об ошибке
    """
    l_position_number = 0

    if len(p_str) == 0:
        return (False, "INFO: Ничего не введено. Введите выражение для расчета.")

    for i_char in p_str:
        l_position_number += 1
        if not is_valid_char(p_char=i_char):
            l_message = "ERROR: Введенное выражение содержит недопустимый символ:\n" + \
                "Выражение: " + p_str + "\n" + \
                "Позиция: " + str(l_position_number) + "\n" + \
                "Символ: " + i_char
            return (False, l_message)
    
    return (True, "")

def to_char_list(p_str: str) -> list:
    """
        Преобразование строки в список из символов
        input:
            p_str   - входная строка 
        output:
            list    - список из символов
    """
    return list(p_str) 

def to_char_type_list(p_char_list: list) -> list:
    """
        Создание списка из типов символов на базе списка символов
        input:
            p_char_list     - список из символов
        output:
            list            - список из типов идентификаторов символов
    """
    l_list = []
    for i_char in p_char_list:
        l_list.append(get_char_type_id(p_char=i_char))
        
    if len(p_char_list) != len(l_list):
        raise ListsHaveNonEqualLengthError(
            function_name="to_char_type_list",
            list_name_1="v_char_list",
            list_name_2="v_list",
            length_list_1=len(p_char_list),
            length_list_2=len(l_list),
            message="Длина списков не совпадает!"
        )

    return l_list 

def to_token_list(p_char_list: list, p_char_type_list: list) -> list:
    """
        Создание списка из токенов на базе списка символов и списка типов символов - склеивание чисел
        input:
            p_char_list         - список из символов
            p_char_type_list    - список типов идентификаторов символов
        output:
            list                - список из токенов (со склеенными числами)
    """
    l_token_list = []

    idx = 0
    while idx <= len(p_char_type_list) - 1:

        # Обработка отрицательного числа
        if p_char_type_list[idx] == C_TYPE_ID_OPENING_BRACKET and \
            p_char_type_list[idx+1] == C_TYPE_ID_MINUS and \
            p_char_type_list[idx+2] == C_TYPE_ID_NUMBER:
            l_str_number_token = ""
            idx += 1
            while idx <= len(p_char_type_list) - 1 or p_char_type_list[idx] != C_TYPE_ID_CLOSING_BRACKET:
                if p_char_type_list[idx] in (C_TYPE_ID_NUMBER, C_TYPE_ID_DOT, C_TYPE_ID_MINUS):
                    l_str_number_token += p_char_list[idx]
                else:
                    break
                idx += 1
            l_token_list.append(float(l_str_number_token))
            # Для игнорирования закрывающей скобки
            idx += 1

        # Склеивание символов в число
        elif p_char_type_list[idx] == C_TYPE_ID_NUMBER:
            l_str_number_token = ""
            while idx <= len(p_char_type_list) - 1:
                if p_char_type_list[idx] in (C_TYPE_ID_NUMBER, C_TYPE_ID_DOT):
                    l_str_number_token += p_char_list[idx]
                else:
                    break
                idx += 1
            l_token_list.append(float(l_str_number_token))

        # В остальных случаях - копируем символы
        else:
            l_token_list.append(p_char_list[idx])
            idx += 1

    return l_token_list


"""Проверка списка символов"""

def check_char_list_brackets(p_char_type_list: list) -> tuple:
    """
        Наконец-то это пригодилось :)
        Проверка скобочной последовательости
        input:
            p_char_type_list    - список из типов идентификаторов символов
        output:
            tuple 
            [0] - bool - результат проверки (True - проверка пройдена, False - проверка не пройдена)
            [1] - str - сообщение об ошибке 
    """
    l_stack = Stack()

    for char in p_char_type_list:
        if char == C_TYPE_ID_OPENING_BRACKET:
            l_stack.push(char)
        elif char == C_TYPE_ID_CLOSING_BRACKET:
            if len(l_stack) > 0:
                l_stack.pop()
            else:
                return (False, "ERROR: В выражении неправильно расставлены скобки. Преждевременно встретилась закрывающая скобка.")
    
    if len(l_stack) > 0:
        return (False, "ERROR: В выражении неправильно расставлены скобки. Отсутствует закрывающая скобка.")
    else:
        return (True, "")

def check_char_list_beginning(p_char_type_list: list) -> tuple:
    """
        Проверка начала выражения 
        Выражение должно начинаться с открывающейся скобки или числа
        input:
            p_char_type_list - список из типов идентификаторов символов
        output:
            tuple
            [0] - (bool) результат проверки (True - проверка пройдена, False - проверка не пройдена)
            [1] - (str) сообщение об ошибке  
    """
    if p_char_type_list[0] in (C_TYPE_ID_NUMBER, C_TYPE_ID_OPENING_BRACKET):
        return (True, "")
    else: 
        return (False, "ERROR: Выражение должно начинаться с открывающейся скобки или числа")

def check_char_list_ending(p_char_type_list: list):
    """
        Проверка окончания выражения
        Выражение должно заканчиваться на закрывающуюся скобку, число или знак равенства
        input:
            p_char_type_list - список из типов идентификаторов символов
        output:
            tuple
            [0] - (bool) результат проверки (True - проверка пройдена, False - проверка не пройдена)
            [1] - (str) сообщение об ошибке  
    """
    if p_char_type_list[-1] in (C_TYPE_ID_NUMBER, C_TYPE_ID_CLOSING_BRACKET, C_TYPE_ID_EQUATION):
        return (True, "")
    else: 
        return (False, "ERROR: Выражение должно заканчиваться на закрывающуюся скобку, число или знак равенства")

def check_pattern(p_char_type_list: list, p_first_key: str, p_second_key: str) -> bool:
    """
        Проверка списка типов идентификаторов символов на наличие определенных, расположенных рядом типов символов
        input:
            p_char_type_list    - список из типов идентификаторов символов
            p_first_key         - ключ первого типа символа из справочника типов символов
            p_second_key        - ключ второго типа символа из справочника типов символов
        output:
            bool                - результат проверки - True - паттерн найден, False - паттерн не найден
    """
    l_first_id = get_type_value_by_key(p_first_key)
    l_second_id = get_type_value_by_key(p_second_key)

    for idx in range(len(p_char_type_list) - 1):
        l_first_elem = p_char_type_list[idx]
        l_second_elem = p_char_type_list[idx+1]
        if (l_first_elem, l_second_elem) == (l_first_id, l_second_id):
            return True 
    return False

def check_char_list_operator(p_char_type_list: list) -> tuple:
    """
        Проверка допустимого расположения оператора в выражении
        input:
            p_char_type_list    - список из типов идентификаторов символов 
        output:
            tuple 
            [0] - (bool) результат проверки: True - не найдено недопустимых паттернов, False - найден недопустимый паттерн
            [1] - (str) сообщение об ошибке
    """
    """
        Список проверок, где:
            + оператор (сложение, умножение, деление)
            - оператор минус
            ( открывающая скобка
            ) закрывающая скобка
            = равенство
            . разделитель

        1. +)
        2. (+
        3. +.
        4. .+
        5. =+
        6. +=
        7. ++
        8. -)
        9. -.
        10. .-
        11. =-
        12. -=
        13. --
        14. -+
        15. +-
    """
    if check_pattern(p_char_type_list, "OPERATOR", "CLOSING_BRACKET"):
        return (False, "ERROR: Неправильное выражение - за оператором следует закрывающая скобка")
    elif check_pattern(p_char_type_list, "OPENING_BRACKET", "OPERATOR"):
        return (False, "ERROR: Неправильное выражение - оператор следует сразу после открывающей скобки")
    elif check_pattern(p_char_type_list, "OPERATOR", "DOT"):
        return (False, "ERROR: Неправильное выражение - после оператора следует разделитель числа")
    elif check_pattern(p_char_type_list, "DOT", "OPERATOR"):
        return (False, "ERROR: Неправильное выражение - разделитель числа следует перед оператором")
    elif check_pattern(p_char_type_list, "EQUATION", "OPERATOR"):
        return (False, "ERROR: Неправильное выражение - знак равенства следует перед оператором")
    elif check_pattern(p_char_type_list, "OPERATOR", "EQUATION"):
        return (False, "ERROR: Неправильное выражение - равенство следует после оператора")
    elif check_pattern(p_char_type_list, "OPERATOR", "OPERATOR"):
        return (False, "ERROR: Неправильное выражение - два оператора следуют подряд")

    elif check_pattern(p_char_type_list, "OPERATOR_MINUS", "CLOSING_BRACKET"):
        return (False, "ERROR: Неправильное выражение - за оператором следует закрывающая скобка")
    elif check_pattern(p_char_type_list, "OPERATOR_MINUS", "DOT"):
        return (False, "ERROR: Неправильное выражение - после оператора следует разделитель числа")
    elif check_pattern(p_char_type_list, "DOT", "OPERATOR_MINUS"):
        return (False, "ERROR: Неправильное выражение - разделитель числа следует перед оператором")
    elif check_pattern(p_char_type_list, "EQUATION", "OPERATOR_MINUS"):
        return (False, "ERROR: Неправильное выражение - знак равенства следует перед оператором")
    elif check_pattern(p_char_type_list, "OPERATOR_MINUS", "EQUATION"):
        return (False, "ERROR: Неправильное выражение - равенство следует после оператора")
    elif check_pattern(p_char_type_list, "OPERATOR_MINUS", "OPERATOR_MINUS"):
        return (False, "ERROR: Неправильное выражение - два оператора следуют подряд")
    elif check_pattern(p_char_type_list, "OPERATOR_MINUS", "OPERATOR"):
        return (False, "ERROR: Неправильное выражение - два оператора следуют подряд")
    elif check_pattern(p_char_type_list, "OPERATOR", "OPERATOR_MINUS"):
        return (False, "ERROR: Неправильное выражение - два оператора следуют подряд")
    else:
        return (True, "")

def check_char_list_equation(p_char_type_list: list) -> tuple:
    """
        Проверка допустимого расположения знака равенства 
        input:
            p_char_type_list - список из типов идентификаторов символов 
        output:
            tuple
            [0] - (bool) результат проверки: True - пройдена, False - не пройдена
            [1] - (str) сообшение об ошибке
    """
    for idx in range(len(p_char_type_list) - 1):
        if p_char_type_list[idx] == C_TYPE_ID_EQUATION and idx != len(p_char_type_list) - 1:
            return (False, "ERROR: Знак равенства может быть только один и должен находиться в конце выражения")

    return (True, "")

def check_char_list_dot(p_char_type_list: list) -> tuple:
    """
        До точки и после точки должны быть цифры 
        пока не будет или скобки или оператора или края строки
    """

    v_dot_id = C_TYPE_ID_DOT
    v_number_id = C_TYPE_ID_NUMBER

    for idx in range(len(p_char_type_list) - 1): 
        if p_char_type_list[idx] == v_dot_id:
            v_number_before_found = v_number_after_found = False
            v_number_before_found = True if p_char_type_list[idx - 1] == v_number_id else False 
            v_number_after_found = True if p_char_type_list[idx + 1] == v_number_id else False 

            if v_number_before_found is False:
                return (False, "ERROR: Перед разделителем числа не найдено цифры")

            if v_number_after_found is False:
                return (False, "ERROR: После разделителя числа не найдено цифры")

    return (True, "")

def check_char_list(v_char_type_list: list) -> tuple: 
    """
        Проверка списка из символов
    """
    v_result_tuple = check_char_list_brackets(v_char_type_list)
    if not v_result_tuple[0]:
        return v_result_tuple 

    v_result_tuple = check_char_list_beginning(v_char_type_list)
    if not v_result_tuple[0]:
        return v_result_tuple 

    v_result_tuple = check_char_list_ending(v_char_type_list)
    if not v_result_tuple[0]:
        return v_result_tuple 

    v_result_tuple = check_char_list_operator(v_char_type_list)
    if not v_result_tuple[0]:
        return v_result_tuple 

    v_result_tuple = check_char_list_equation(v_char_type_list)
    if not v_result_tuple[0]:
        return v_result_tuple 

    v_result_tuple = check_char_list_dot(v_char_type_list)
    if not v_result_tuple[0]:
        return v_result_tuple 

    return (True, "")


"""Создание списка из выражений"""
def get_expression_list(v_token_list: list) -> list:
    v_expression_list = []
    v_token_copy_list = v_token_list.copy()

    ### На каждой итерации этого цикла - меняем содержимое списка, пока не останется скобок
    while is_bracket_expression_exists(v_list=v_token_copy_list):
        v_current_idx = 0

        # На каждой итерации этого цикла для каждой найденной открытой скобки - ищем следующую закрытую и открытую скобки
        while v_current_idx <= len(v_token_copy_list) - 1:
            if is_opening_bracket(v_str=str(v_token_copy_list[v_current_idx])):
                # Если найдена открытая скобка, то ищем следующие открытые и закрытые скобки
                v_next_opening_bracket_idx = v_next_closing_bracket_idx = v_current_idx + 1
                v_opening_bracket_found = v_closing_bracket_found = False

                # Поиск следующей открытой скобки
                while v_next_opening_bracket_idx <= len(v_token_copy_list) - 1:
                    if is_opening_bracket(v_str=str(v_token_copy_list[v_next_opening_bracket_idx])):
                        v_opening_bracket_found = True 
                        break
                    else:
                        v_next_opening_bracket_idx += 1

                # Поиск следующей закрытой скобки
                while v_next_closing_bracket_idx <= len(v_token_copy_list) - 1:
                    if is_closing_bracket(v_str=str(v_token_copy_list[v_next_closing_bracket_idx])):
                        v_closing_bracket_found = True 
                        break
                    else:
                        v_next_closing_bracket_idx += 1

                # Если закрытая скобка не найдена - то нужно зарейзить исключение 
                if not v_closing_bracket_found:
                    raise ClosingBracketNotFoundError(
                        function_name="get_expression_list",
                        checked_list=v_token_copy_list,
                        opening_bracket_idx=v_current_idx,
                        message="Не найдена закрывающая скобка при наличии открывающей"
                    )

                # Если найдены закрытая и открытая скобка, то необходимо проверить, 
                # что индекс открытой скобки не превышает индекс закрытой скобки
                # Если так - то переходим к следующей итерации
                if v_closing_bracket_found and (
                    (v_opening_bracket_found and v_next_closing_bracket_idx < v_next_opening_bracket_idx)
                    or (not v_opening_bracket_found)
                ):
                    v_found_expression = v_token_copy_list[v_current_idx+1:v_next_closing_bracket_idx]

                    # Специальный случай для повторяющихся скобок в выражении
                    if len(v_found_expression) >= 3:
                        v_expression_list.append(v_found_expression)
                        del v_token_copy_list[v_current_idx:v_next_closing_bracket_idx+1]
                        v_token_copy_list.insert(v_current_idx, "expr_" + str(len(v_expression_list) - 1))
                    elif len(v_found_expression) == 1 and str(v_found_expression[0]).startswith("expr"):
                        del v_token_copy_list[v_current_idx]
                        del v_token_copy_list[v_next_closing_bracket_idx-1]
                    else:
                        del v_token_copy_list[v_current_idx:v_next_closing_bracket_idx+1]

                    v_current_idx = 0
                    break
                else:
                    v_current_idx += 1
            else:
                v_current_idx += 1

    if len(v_token_copy_list) > 0:

        if len(v_token_copy_list) == 1 and str(v_token_copy_list[0]).startswith("expr"):
            pass
        else:
            v_expression_list.append(v_token_copy_list)
        
    return v_expression_list

def is_bracket_expression_exists(v_list: list) -> bool:
    try:
        v_opening_bracket_idx = v_list.index("(")
    except ValueError:
        v_opening_bracket_idx = -1

    try:
        v_closing_bracket_idx = v_list.index(")")
    except ValueError:
        v_closing_bracket_idx = -1

    if v_opening_bracket_idx >= 0 \
        and v_closing_bracket_idx >= 0 \
        and v_opening_bracket_idx < v_closing_bracket_idx:
        return True
    else:
        return False

"""Определение порядка выражений"""
def to_simple_expression_list(v_expression_list: list) -> list:
    """
        1. Для каждого списка в списке
        1.1 Ищем оператор - умножения или деления 
        1.2 Как только оператор найден - находим левый операнд и правый операнд - и заносим в новый список
        1.3 Удаляем найденную часть списка 
        1.4 Заменяем на ссылку 
        1.5 Выполняем пункты 1.1 - 1.5 для операторов сложения и вычитания 
    """
    v_result_list = []

    # Отдельная обработка случая, когда пользователь вбил просто число
    if len(v_expression_list) == 1 and len(v_expression_list[0]) == 1 \
        and is_number(v_expression_list[0][0]):
        return v_expression_list


    for elem in v_expression_list: 
        v_list = elem.copy()
        v_idx = 0 
        v_ref_count = 0
        v_simple_expression_list = []

        while v_idx < len(v_list) - 1:
            if is_char(v_list[v_idx], "*") or is_char(v_list[v_idx], "/"):
                v_left_operand = v_list[v_idx - 1]
                v_operator = v_list[v_idx]
                v_second_operand = v_list[v_idx + 1]
                v_simple_expression_list.append([v_left_operand, v_operator, v_second_operand])
                del v_list[v_idx-1:v_idx+2]
                v_list.insert(v_idx-1, "ref_" + str(v_ref_count))
                v_ref_count += 1
                v_idx = 0
            else:
                v_idx += 1
        
        v_idx = 0

        while v_idx < len(v_list) - 1:
            if is_char(v_list[v_idx], "+") or is_char(v_list[v_idx], "-"):
                v_left_operand = v_list[v_idx - 1]
                v_operator = v_list[v_idx]
                v_second_operand = v_list[v_idx + 1]
                v_simple_expression_list.append([v_left_operand, v_operator, v_second_operand])
                del v_list[v_idx-1:v_idx+2]
                v_list.insert(v_idx-1, "ref_" + str(v_ref_count))
                v_ref_count += 1
                v_idx = 0
            else:
                v_idx += 1

        v_result_list.append(v_simple_expression_list.copy())

    return v_result_list

def get_result(v_final_expression_list: list) -> float:
    """
    [
        [
            ["1", + "2"],
            ["2", -, "ref_0"]
        ],
        [
            ["expr_0", "-", 123]
        ]
    ]
    """
    ### Обработка случая, когда пользователь вбил число 
    if len(v_final_expression_list) == 1 and len(v_final_expression_list[0]) == 1 \
        and is_number(v_final_expression_list[0][0]):
        return v_final_expression_list[0][0]

    v_input_list = v_final_expression_list.copy()
    v_idx = 0
    while v_idx < len(v_input_list):
        v_current_expression = v_input_list[v_idx]
        v_v_idx = 0 

        while v_v_idx < len(v_current_expression):
            v_current_simple_expression = v_current_expression[v_v_idx]
            v_first_operand = v_current_simple_expression[0]
            v_operator = v_current_simple_expression[1]
            v_second_operand = v_current_simple_expression[2]

            if isinstance(v_first_operand, str):
                v_type, v_token_idx = v_first_operand.split("_")
                v_token_idx = int(v_token_idx)
                if v_type == "expr":
                    v_first_operand = v_input_list[v_token_idx]
                elif v_type == "ref":
                    v_first_operand = v_input_list[v_idx][v_token_idx]

            if isinstance(v_second_operand, str):
                v_type, v_token_idx = v_second_operand.split("_")
                v_token_idx = int(v_token_idx)
                if v_type == "expr":
                    v_second_operand = v_input_list[v_token_idx]
                elif v_type == "ref":
                    v_second_operand = v_input_list[v_idx][v_token_idx]

            if v_operator == "+":
                v_result = v_first_operand + v_second_operand 
            elif v_operator == "-":
                v_result = v_first_operand - v_second_operand 
            elif v_operator == "*":
                v_result = v_first_operand * v_second_operand
            elif v_operator == "/":
                v_result = v_first_operand / v_second_operand 

            if v_v_idx == len(v_current_expression) - 1:
                v_input_list[v_idx] = v_result
            else:
                v_input_list[v_idx][v_v_idx] = v_result 
            
            v_v_idx += 1

        v_idx += 1

    v_result = v_input_list[-1]
    return v_result

"""Поддержка clear и reset"""
def clear(p_result_list: list) -> str:
    if len(p_result_list) > 0:
        while len(p_result_list) > 0:
            del p_result_list[0]
        return "INFO: Список результатов вычислений очищен. Введите арифметическое выражение для расчета."
    else:
        return "INFO: Список результатов вычислений уже пуст. Введите арифметическое выражение для расчета."

def reset(p_result_list: list) -> str:
    if len(p_result_list) > 1:
        del p_result_list[-1]
        return "INFO: Выполнен переход к предыдущему результату вычислений - " + str(p_result_list[-1])
    elif len(p_result_list) == 1:
        del p_result_list[-1]
        return "INFO: В истории вычислений было только одно значение. История пуста"
    else:
        return "INFO: Нечего очищать. История вычислений пуста."

def is_input_a_calculator_option(p_str: str) -> bool:
    if len(p_str) == 1 and ((p_str == "c") or (p_str == "r")):
        return True 
    else:
        return False 

"""Основные функции"""
def process_input(v_str: str, v_result_list: list) -> str:
    v_str = trim_whitespace(v_str)
    if len(v_str) > 0 and is_operator(v_str[0]):
        if len(v_result_list) > 0:
            if v_result_list[-1] >= 0:
                v_str = str(v_result_list[-1]) + v_str 
            else:
                v_str = "(" + str(v_result_list[-1]) + ")" + v_str
        else:
            print("ERROR: Отсутствует результат предыдущего расчета для использовании в заданном выражении")
        
    return v_str

def calculate(v_char_list: list, v_char_type_list: list) -> float:
    v_token_list = to_token_list(p_char_list=v_char_list, p_char_type_list=v_char_type_list)
    v_expression_list = get_expression_list(v_token_list=v_token_list)
    v_simple_expression_list = to_simple_expression_list(v_expression_list=v_expression_list)
    v_result = get_result(v_final_expression_list=v_simple_expression_list)
    return v_result

def main():
    v_result_list = []
    while True:
        v_str = input() 
        if is_input_a_calculator_option(p_str=v_str):
            if v_str == "c":
                print(clear(p_result_list=v_result_list))
            elif v_str == "r":
                print(reset(p_result_list=v_result_list))
        else:
            v_str = process_input(v_str=v_str, v_result_list=v_result_list)
            
            l_valid_input_tuple = is_valid_input(p_str=v_str)
            if l_valid_input_tuple[0]:
                v_char_list = to_char_list(p_str=v_str)
                v_char_type_list = to_char_type_list(p_char_list=v_char_list)
                v_tuple = check_char_list(v_char_type_list=v_char_type_list)
                if not v_tuple[0]:
                    print(v_tuple[1])
                else:
                    v_result = calculate(v_char_list=v_char_list, v_char_type_list=v_char_type_list)
                    print(v_result)
                    v_result_list.append(v_result)
            else:
                print(l_valid_input_tuple[1])

main()
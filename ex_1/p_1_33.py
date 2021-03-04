"""Глобальные переменные"""

g_dict_char_type = {
    "NUMBER": 1,
    "OPERATOR": 2,
    "EQUATION": 3,
    "OPENING_BRACKET": 4,
    "CLOSING_BRACKET": 5,
    "DOT": 6,
    "OPERATOR_MINUS": 7,
    "UNKNOWN": 99
}

"""Хэлперы"""

def get_type_value_by_key(v_str: str) -> int:
    return g_dict_char_type[v_str]

def get_char_type_id(v_str: str) -> int:
    if is_char_number(v_str):
        return get_type_value_by_key("NUMBER")
    elif is_char(v_str, ("-")):
        return get_type_value_by_key("OPERATOR_MINUS")
    elif is_operator(v_str):
        return get_type_value_by_key("OPERATOR")
    elif is_operator(v_str):
        return get_type_value_by_key("EQUATION")
    elif is_opening_bracket(v_str):
        return get_type_value_by_key("OPENING_BRACKET")
    elif is_closing_bracket(v_str):
        return get_type_value_by_key("CLOSING_BRACKET")
    elif is_dot(v_str):
        return get_type_value_by_key("DOT")
    else: 
        return get_type_value_by_key("UNKNOWN")

"""Пользовательские структуры данных"""

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
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
    """
    def __init__(self, function_name: str, parameter_name: str, message: str):
        # Если так не сделать, то не будет появляться пользовательское сообщение об ошибке
        super().__init__(message)
        self.function_name = function_name 
        self.parameter_name = parameter_name 

class ArgsLengthParameterError(InputParameterError):
    """
        Исключение для ошибки неправильной длины параметра args
    """

    def __init__(self, function_name, parameter_name="*args"):
        super().__init__(
            function_name=function_name, 
            parameter_name=parameter_name, 
            message=self.get_message(function_name, parameter_name)
        )

    def get_message(self, function_name: str, parameter_name: str) -> str:
        """
            Геттер сообщения об ошибке
        """
        return "Function: {0} -> Parameter: {1} -> Parameter must has a length of one.".format(
            function_name, parameter_name
        )

class ListsHaveNonEqualLengthError(Error):
    """
        Исключение для ошибки несовпадения длин списков 
        Для сравнения списков с символами (токенами) и типами символов (токенов)
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
    """
    def __init__(self, function_name: str, checked_list: list, opening_bracket_idx: int, message: str):
        super().__init__(message)
        self.function_name = function_name
        self.checked_list = checked_list 
        self.opening_bracket_idx = opening_bracket_idx


"""Проверки символов"""

def is_char(v_str: str, *args: tuple) -> bool:
    """
        Является ли входящая строка одним символом
        Если есть *args и его длина один, то проверка на совпадение
    """
    v_result = True if isinstance(v_str, str) and len(v_str) == 1 else False

    if args:
        if len(args) == 1:
            return v_result & (v_str == args[0])
        else:
            raise ArgsLengthParameterError("is_char")
    else:
        return v_result

def is_char_number(v_str: str) -> bool:
    """
        Является ли строка цифрой
    """
    if is_char(v_str):
        try:
            int(v_str) 
            return True 
        except ValueError:
            return False 

def is_operator(v_str: str) -> bool:
    """
        Является ли строка оператором
    """
    return is_char(v_str, ("+")) or is_char(v_str, ("-")) \
        or is_char(v_str, ("*")) or is_char(v_str, ("/"))

def is_equation(v_str: str) -> bool:
    """
        Является ли строка знаком равенства
    """
    return is_char(v_str, ("="))

def is_opening_bracket(v_str: str) -> bool:
    """
        Является ли строка открывающейся скобкой
    """
    return is_char(v_str, ("(")) 

def is_closing_bracket(v_str: str) -> bool:
    """
        Является ли строка закрывающейся скобкой
    """
    return is_char(v_str, (")")) 

def is_dot(v_str: str) -> bool:
    """
        Является ли строка точкой
    """
    return is_char(v_str, ("."))

def is_valid_char(v_str: str) -> bool: 
    """
        Является ли символ допустимым в выражении
    """
    return is_char_number(v_str) or is_operator(v_str) or is_equation(v_str)  \
        or is_equation(v_str) or is_opening_bracket(v_str) or is_closing_bracket(v_str) \
        or is_dot(v_str)

def is_number(v_str: str) -> bool:
    """
        Является ли строка числом (разрешено больше 1 символа)
    """
    try:
        float(v_str) 
        return True
    # ValueError, TypeError
    except:
        return False
        
"""Парсинг и преобразование строки"""

def trim_whitespace(v_str: str) -> str:
    """
        Удалить пробелы из строки
    """
    return v_str.replace(" ", "") 

def is_valid_input(v_str: str) -> bool:
    """
        Проверка всех символов на соответствие допустимым 
        Возвращаемый кортеж имеет следующий вид: (bool, str)
        bool - результат проверки, True - валидно
        str - текст ошибки

        Проверка на непустую строку
    """
    position_number = 0

    if len(v_str) == 0:
        print("INFO: Ничего не введено. Введите выражение для расчета.")
        return False

    for char in v_str:
        position_number += 1
        if not is_valid_char(v_str=char):
            v_message = "ERROR: Введенное выражение содержит недопустимый символ:\n" + \
                "Выражение: " + v_str + "\n" + \
                "Позиция: " + str(position_number) + "\n" + \
                "Символ: " + char
            print(v_message)
            return False
    
    return True

def to_char_list(v_str: str) -> list:
    """
        Преобразование строки в список из символов
    """
    v_list = []
    for char in v_str:
        v_list.append(char)

    return v_list 

def to_char_type_list(v_char_list: list) -> list:
    """
        Создание списка из типов символов на базе списка символов
    """
    v_list = []
    for char in v_char_list:
        v_list.append(get_char_type_id(v_str=char))
        
    if len(v_char_list) != len(v_list):
        raise ListsHaveNonEqualLengthError(
            function_name="to_char_type_list",
            list_name_1="v_char_list",
            list_name_2="v_list",
            length_list_1=len(v_char_list),
            length_list_2=len(v_list),
            message="Длина списков не совпадает!"
        )

    return v_list 

def to_token_list(v_char_list: list, v_char_type_list: list) -> list:
    """
        Создание списка из токенов на базе списка символов и списка типов символов 
        Как минимум, надо склеить цифры 
    """
    v_token_list = []
    v_number_id = get_type_value_by_key("NUMBER")
    v_dot_id = get_type_value_by_key("DOT")
    v_opening_bracket_id = get_type_value_by_key("OPENING_BRACKET")
    v_closing_bracket_id = get_type_value_by_key("CLOSING_BRACKET")
    v_operator_minus_id = get_type_value_by_key("OPERATOR_MINUS")

    idx = 0
    while idx <= len(v_char_type_list) - 1:
        if v_char_type_list[idx] == v_opening_bracket_id and \
            v_char_type_list[idx+1] == v_operator_minus_id and \
            v_char_type_list[idx+2] == v_number_id:
            v_str_number_token = ""
            idx += 1
            while idx <= len(v_char_type_list) - 1 or v_char_type_list[idx] != v_closing_bracket_id:
                if v_char_type_list[idx] in (v_number_id, v_dot_id, v_operator_minus_id):
                    v_str_number_token += v_char_list[idx]
                else:
                    break
                idx += 1
            v_token_list.append(float(v_str_number_token))
            # Для игнорирования закрывающей скобки
            idx += 1
        elif v_char_type_list[idx] == v_number_id:
            v_str_number_token = ""
            while idx <= len(v_char_type_list) - 1:
                if v_char_type_list[idx] in (v_number_id, v_dot_id):
                    v_str_number_token += v_char_list[idx]
                else:
                    break
                idx += 1
            v_token_list.append(float(v_str_number_token))
        else:
            v_token_list.append(v_char_list[idx])
            idx += 1

    return v_token_list


"""Проверка списка символов"""

def check_char_list_brackets(v_char_type_list: list) -> tuple:
    """
        Наконец-то это пригодилось :)
        Проверка скобочной последовательости
        Выходной параметр (bool, str)
        bool - результат проверки (True - проверка пройдена, False - проверка не пройдена)
        str - сообщение об ошибке 
    """
    v_stack = Stack()
    v_opening_bracket_id = get_type_value_by_key("OPENING_BRACKET")
    v_closing_bracket_id = get_type_value_by_key("CLOSING_BRACKET")

    for char in v_char_type_list:
        if char == v_opening_bracket_id:
            v_stack.push(char)
        elif char == v_closing_bracket_id:
            if len(v_stack) > 0:
                v_stack.pop()
            else:
                return (False, "ERROR: В выражении неправильно расставлены скобки. Преждевременно встретилась закрывающая скобка.")
    
    if len(v_stack) > 0:
        return (False, "ERROR: В выражении неправильно расставлены скобки. Отсутствует закрывающая скобка.")
    else:
        return (True, "")


def check_char_list_beginning(v_char_type_list: list) -> tuple:
    """
        Выражение должно начинаться с открывающейся скобки или числа
    """
    v_number_id = get_type_value_by_key("NUMBER")
    v_opening_bracket_id = get_type_value_by_key("OPENING_BRACKET")

    if v_char_type_list[0] in (v_number_id, v_opening_bracket_id):
        return (True, "")
    else: 
        return (False, "ERROR: Выражение должно начинаться с открывающейся скобки или числа")

def check_char_list_ending(v_char_type_list: list):
    """
        Выражение должно заканчиваться на закрывающуюся скобку, число или знак равенства
    """
    v_number_id = get_type_value_by_key("NUMBER") 
    v_closing_bracket_id = get_type_value_by_key("CLOSING_BRACKET")
    v_equation_id = get_type_value_by_key("EQUATION")

    if v_char_type_list[-1] in (v_number_id, v_closing_bracket_id, v_equation_id):
        return (True, "")
    else: 
        return (False, "ERROR: Выражение должно заканчиваться на закрывающуюся скобку, число или знак равенства")

def check_pattern(v_char_type_list: list, first_key: str, second_key: str) -> bool:
    first_id = get_type_value_by_key(first_key)
    second_id = get_type_value_by_key(second_key)

    for idx in range(len(v_char_type_list) - 1):
        first_elem = v_char_type_list[idx]
        second_elem = v_char_type_list[idx+1]
        if (first_elem, second_elem) == (first_id, second_id):
            return True 

    return False

def check_char_list_operator(v_char_type_list: list):
    """
        +)
        (+
        +.
        .+
        =+
        +=
        ++
        Такие паттерны говорят о неправильном выражении
    """
    if check_pattern(v_char_type_list, "OPERATOR", "CLOSING_BRACKET"):
        return (False, "ERROR: Неправильное выражение - за оператором следует закрывающая скобка")
    elif check_pattern(v_char_type_list, "OPENING_BRACKET", "OPERATOR"):
        return (False, "ERROR: Неправильное выражение - оператор следует сразу после открывающей скобки")
    elif check_pattern(v_char_type_list, "OPERATOR", "DOT"):
        return (False, "ERROR: Неправильное выражение - после оператора следует разделитель числа")
    elif check_pattern(v_char_type_list, "DOT", "OPERATOR"):
        return (False, "ERROR: Неправильное выражение - разделитель числа следует перед оператором")
    elif check_pattern(v_char_type_list, "EQUATION", "OPERATOR"):
        return (False, "ERROR: Неправильное выражение - знак равенства следует перед оператором")
    elif check_pattern(v_char_type_list, "OPERATOR", "EQUATION"):
        return (False, "ERROR: Неправильное выражение - равенство следует после оператора")
    elif check_pattern(v_char_type_list, "OPERATOR", "OPERATOR"):
        return (False, "ERROR: Неправильное выражение - два оператора следуют подряд")

    elif check_pattern(v_char_type_list, "OPERATOR_MINUS", "CLOSING_BRACKET"):
        return (False, "ERROR: Неправильное выражение - за оператором следует закрывающая скобка")
    elif check_pattern(v_char_type_list, "OPERATOR_MINUS", "DOT"):
        return (False, "ERROR: Неправильное выражение - после оператора следует разделитель числа")
    elif check_pattern(v_char_type_list, "DOT", "OPERATOR_MINUS"):
        return (False, "ERROR: Неправильное выражение - разделитель числа следует перед оператором")
    elif check_pattern(v_char_type_list, "EQUATION", "OPERATOR_MINUS"):
        return (False, "ERROR: Неправильное выражение - знак равенства следует перед оператором")
    elif check_pattern(v_char_type_list, "OPERATOR_MINUS", "EQUATION"):
        return (False, "ERROR: Неправильное выражение - равенство следует после оператора")
    elif check_pattern(v_char_type_list, "OPERATOR_MINUS", "OPERATOR_MINUS"):
        return (False, "ERROR: Неправильное выражение - два оператора следуют подряд")
    elif check_pattern(v_char_type_list, "OPERATOR_MINUS", "OPERATOR"):
        return (False, "ERROR: Неправильное выражение - два оператора следуют подряд")
    elif check_pattern(v_char_type_list, "OPERATOR", "OPERATOR_MINUS"):
        return (False, "ERROR: Неправильное выражение - два оператора следуют подряд")
    else:
        return (True, "")

def check_char_list_equation(v_char_type_list: list):
    """
        Знак равенства должен находиться только в конце 
    """
    equation_id = get_type_value_by_key("EQUATION")

    for idx in range(len(v_char_type_list) - 1):
        if v_char_type_list[idx] == equation_id and idx != len(v_char_type_list) - 1:
            return (False, "ERROR: Знак равенства может быть только один и должен находиться в конце выражения")

    return (True, "")

def check_char_list_dot(v_char_type_list: list):
    """
        До точки и после точки должны быть цифры 
        пока не будет или скобки или оператора или края строки
    """

    v_dot_id = get_type_value_by_key("DOT")
    v_number_id = get_type_value_by_key("NUMBER")
    v_opening_bracket_id = get_type_value_by_key("OPENING_BRACKET")
    v_closing_bracket_id = get_type_value_by_key("CLOSING_BRACKET")
    v_operator_id = get_type_value_by_key("OPERATOR")
    v_equation_id = get_type_value_by_key("EQUATION")
    v_operator_minus_id = get_type_value_by_key("OPERATOR_MINUS")

    for idx in range(len(v_char_type_list) - 1): 
        if v_char_type_list[idx] == v_dot_id:
            if idx in (0, len(v_char_type_list)-1):
                return (False, "ERROR: Точка не должна быть в начале или в конце выражения")
            else:
                v_number_before_found = v_number_after_found = False
                v_number_before_found = True if v_char_type_list[idx - 1] == v_number_id else False 
                v_number_after_found = True if v_char_type_list[idx + 1] == v_number_id else False 

                if v_number_before_found is False:
                    return (False, "ERROR: Перед разделителем числа не найдено цифры")

                if v_number_after_found is False:
                    return (False, "ERROR: После разделителя числа не найдено цифры")

                v_idx = idx - 1
                while v_idx >= 0:
                    if v_char_type_list[v_idx] == v_number_id:
                        v_idx -= 1
                    elif v_char_type_list[v_idx] in (v_operator_id, v_operator_minus_id, v_opening_bracket_id, v_closing_bracket_id):
                        break
                    else:
                        return (False, "ERROR: Перед разделителем числа в его начале обнаружен недопустимый символ")

                v_idx = idx + 1 
                while v_idx <= len(v_char_type_list) - 1:
                    if v_char_type_list[v_idx] == v_number_id:
                        v_idx += 1
                    elif v_char_type_list[v_idx] in (v_operator_id, v_operator_minus_id, v_opening_bracket_id, v_closing_bracket_id, v_equation_id):
                        break
                    else:
                        return (False, "ERROR: После разделителя числа в его конце обнаружен недопустимый символ")

    return ("True", "")

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
            if is_char(v_list[v_idx], ("*")) or is_char(v_list[v_idx], ("/")):
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
            if is_char(v_list[v_idx], ("+")) or is_char(v_list[v_idx], ("-")):
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
def clear(p_result_list: list):
    if len(p_result_list) > 0:
        while len(p_result_list) > 0:
            del p_result_list[0]
        print("INFO: Список результатов вычислений очищен. Введите арифметическое выражение для расчета.")
    else:
        print("INFO: Список результатов вычислений уже пуст. Введите арифметическое выражение для расчета.")

def reset(p_result_list: list):
    if len(p_result_list) > 1:
        del p_result_list[-1]
        print("INFO: Выполнен переход к предыдущему результату вычислений - " + str(p_result_list[-1]))
    elif len(p_result_list) == 1:
        del p_result_list[-1]
        print("INFO: В истории вычислений было только одно значение. История пуста")
    else:
        print("INFO: Нечего очищать. История вычислений пуста.")

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
    v_token_list = to_token_list(v_char_list=v_char_list, v_char_type_list=v_char_type_list)
    print("v_token_list")
    print(v_token_list)
    v_expression_list = get_expression_list(v_token_list=v_token_list)
    print("v_expression_list")
    print(v_expression_list)
    v_simple_expression_list = to_simple_expression_list(v_expression_list=v_expression_list)
    print("v_simple_expression_list")
    print(v_simple_expression_list)
    v_result = get_result(v_final_expression_list=v_simple_expression_list)
    return v_result

def main():
    v_result_list = []
    while True:
        v_str = input() 
        if is_input_a_calculator_option(p_str=v_str):
            if v_str == "c":
                clear(p_result_list=v_result_list)
            elif v_str == "r":
                reset(p_result_list=v_result_list)
        else:
            v_str = process_input(v_str=v_str, v_result_list=v_result_list)

            if is_valid_input(v_str=v_str):
                v_char_list = to_char_list(v_str=v_str)
                v_char_type_list = to_char_type_list(v_char_list=v_char_list)
                v_tuple = check_char_list(v_char_type_list=v_char_type_list)
                if not v_tuple[0]:
                    print(v_tuple[1])
                else:
                    v_result = calculate(v_char_list=v_char_list, v_char_type_list=v_char_type_list)
                    print(v_result)
                    v_result_list.append(v_result)

main()
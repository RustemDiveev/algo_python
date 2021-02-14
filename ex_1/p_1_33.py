"""
1. Можно писать в одну строку длинные выражения - попробовать учесть скобки и порядок выполнения арифметических операций
2. Можно писать по числу или оператору - результат рассчитывется автоматически по enter 
3. При помощи кнопки "с" (clear) - ресетим в ноль 
4. При помощи кнопки "r" (reset) - откатываем последнее вычисление
"""

"""
План решения задачи:

Пока рассмотрим случай, когда выражение вводится пачкой и ожидается получение результата этого выражения.
Пока рассмотрим случай, где не требуется наличие отрицательных чисел.

MVP!!!!
1. Мы должны проверить то, что ввели, на предмет того, можно ли с этим работать.
	1.1 Необходимо убрать пробелы 
	1.2 Необходимо проверить, является ли каждый символ - цифрой или оператором - также допустимы дробные числа. В питоне разделитель - точка.
		1.2.1 Добавить проверку на точку 
	1.3 Необходимо проверить, есть ли неадекватно введенные значения
		1.3.1 Два оператора подряд 
		1.3.2 Несоответствие скобочной последовательности (здесь сойдет самостоятельная реализация стека)
		1.3.3 Две точки подряд
		1.3.4 Точка без числа 
		1.3.5 Возможно есть что-то еще...
	1.4 Должно быть адекватное сообщение об ошибке, из которого понятно, что именно не так 
	
2. Мы должны распарсить введенное на токены и подготовиться к вычислению
	2.1 Сцепить числа - разбить строку на список - где каждый элемент - это значение 
																				или оператор 
																				или скобка 
	2.2 Разбить на выражения - проверить валидно ли отдельное выражение
		2.2.1 Необходимо задать порядок выполнения выражений - признак выражения - оператор
	2.3 Определить порядок выполнения (скобки + операторы)
	2.4 Можно попробовать список, по которому потребуется идти последовательно
	2.5 Планируется иметь два списка:
		2.5.1 Список со словарями - где есть выражение.
		Примерная структура словаря:
		{
			"is_pointer_1": True | False, 
			"value_1": float 
			"is_pointer_2": True | False 
			"value_2": float 
			"operator": +-*/
		}
		2.5.2 Список с результатом промежуточных вычислений
"""

"""Глобальные переменные"""

g_dict_char_type = {
    "NUMBER": 1,
    "OPERATOR": 2,
    "EQUATION": 3,
    "OPENING_BRACKET": 4,
    "CLOSING_BRACKET": 5,
    "DOT": 6,
    "UNKNOWN": 99
}

"""Хэлперы"""

def get_type_value_by_key(v_str: str) -> int:
    return g_dict_char_type[v_str]

def get_char_type_id(v_str: str) -> int:
    if is_char_number(v_str):
        return get_type_value_by_key("NUMBER")
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
    except ValueError:
        return False
        
"""Парсинг и преобразование строки"""

def trim_whitespace(v_str: str) -> str:
    """
        Удалить пробелы из строки
    """
    return v_str.replace(" ", "") 

def is_valid_input(v_str: str) -> tuple:
    """
        Проверка всех символов на соответствие допустимым 
        Возвращаемый кортеж имеет следующий вид: (bool, str)
        bool - результат проверки, True - валидно
        str - текст ошибки
    """
    position_number = 0

    for char in v_str:
        position_number += 1
        if not is_valid_char(v_str=char):
            v_message = "Введенное выражение содержит недопустимый символ:\n" + \
                "Выражение: " + v_str + "\n" + \
                "Позиция: " + str(position_number) + "\n" + \
                "Символ: " + char
            return (False, v_message)
    
    return (True, "")

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

    idx = 0
    while idx <= len(v_char_type_list) - 1:
        if v_char_type_list[idx] == v_number_id:
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
    

def to_token_type_list(v_list: list) -> list:
    """
        Создание списка из типов токенов на базе списка из токенов
    """
    pass 


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
                return (False, "В выражении неправильно расставлены скобки. Преждевременно встретилась закрывающая скобка.")
    
    if len(v_stack) > 0:
        return (False, "В выражении неправильно расставлены скобки. Отсутствует закрывающая скобка.")
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
        return (False, "Выражение должно начинаться с открывающейся скобки или числа")

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
        return (False, "Выражение должно заканчиваться на закрывающуюся скобку, число или знак равенства")

def check_pattern(v_char_type_list: list, first_key: str, second_key: str) -> bool:
    first_id = get_type_value_by_key(first_key)
    second_id = get_type_value_by_key(second_key)

    for idx in range(len(v_char_type_list) - 2):
        first_elem = v_char_type_list[idx]
        second_elem = v_char_type_list[idx+1]
        if (first_elem, second_elem) == (first_id, second_id):
            return True 
        else:
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
        return (False, "Неправильное выражение - за оператором следует закрывающая скобка")
    elif check_pattern(v_char_type_list, "OPENING_BRACKET", "OPERATOR"):
        return (False, "Неправильное выражение - оператор следует сразу после открывающей скобки")
    elif check_pattern(v_char_type_list, "OPERATOR", "DOT"):
        return (False, "Неправильное выражение - после оператора следует разделитель числа")
    elif check_pattern(v_char_type_list, "DOT", "OPERATOR"):
        return (False, "Неправильное выражение - разделитель числа следует перед оператором")
    elif check_pattern(v_char_type_list, "EQUATION", "OPERATOR"):
        return (False, "Неправильное выражение - знак равенства следует перед оператором")
    elif check_pattern(v_char_type_list, "OPERATOR", "EQUATION"):
        return (False, "Неправильное выражение - равенство следует после оператора")
    elif check_pattern(v_char_type_list, "OPERATOR", "OPERATOR"):
        return (False, "Неправильное выражение - два оператора следуют подряд")
    else:
        return (True, "")

def check_char_list_equation(v_char_type_list: list):
    """
        Знак равенства должен находиться только в конце 
    """
    equation_id = get_type_value_by_key("EQUATION")

    for idx in range(len(v_char_type_list) - 1):
        if v_char_type_list[idx] == equation_id and idx != len(v_char_type_list) - 1:
            return (False, "Знак равенства может быть только один и должен находиться в конце выражения")

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

    for idx in range(len(v_char_type_list) - 1): 
        if v_char_type_list[idx] == v_dot_id:
            if idx in (0, len(v_char_type_list)-1):
                return (False, "Точка не должна быть в начале или в конце выражения")
            else:
                v_number_before_found = v_number_after_found = False
                v_number_before_found = True if v_char_type_list[idx - 1] == v_number_id else False 
                v_number_after_found = True if v_char_type_list[idx + 1] == v_number_id else False 

                if v_number_before_found is False:
                    return (False, "Перед разделителем числа не найдено цифры")

                if v_number_after_found is False:
                    return (False, "После разделителя числа не найдено цифры")

                v_idx = idx - 1
                while v_idx >= 0:
                    if v_char_type_list[v_idx] == v_number_id:
                        v_idx -= 1
                    elif v_char_type_list[v_idx] in (v_operator_id, v_opening_bracket_id, v_closing_bracket_id):
                        break
                    else:
                        return (False, "Перед разделителем числа в его начале обнаружен недопустимый символ")

                v_idx = idx + 1 
                while v_idx <= len(v_char_type_list) - 1:
                    if v_char_type_list[v_idx] == v_number_id:
                        v_idx += 1
                    elif v_char_type_list[v_idx] in (v_operator_id, v_opening_bracket_id, v_closing_bracket_id, v_equation_id):
                        break
                    else:
                        return (False, "После разделителя числа в его конце обнаружен недопустимый символ")

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


"""Основные функции"""
def main():
    while True:
        v_str = input()
        v_str = trim_whitespace(v_str=v_str)
        v_tuple = is_valid_input(v_str=v_str)
        if not v_tuple[0]:
            print(v_tuple[1])
        else:
            v_char_list = to_char_list(v_str=v_str)
            v_char_type_list = to_char_type_list(v_char_list=v_char_list)
            v_tuple = check_char_list(v_char_type_list=v_char_type_list)
            if not v_tuple[0]:
                print(v_tuple[1])
            else:
                v_token_list = to_token_list(v_char_list=v_char_list, v_char_type_list=v_char_type_list)
                print(v_token_list)

main()
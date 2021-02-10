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
        Является ли строка числом (больше 1 символа)
    """
    pass 
        
        
"""Парсинг и преобразование строки"""

def trim_whitespace(v_str: str) -> str:
    """
        Удалить пробелы из строки
    """
    pass 

def is_valid_input(v_str: str) -> tuple:
    """
        Проверка всех символов на соответствие допустимым 
    """
    pass 

def to_char_list(v_str: str) -> list:
    """
        Преобразование строки в список из символов
    """
    pass 

def to_char_type_list(v_char_list: list) -> list:
    """
        Создание списка из типов символов на базе списка символов
    """
    pass 

def to_token_list(v_char_list: list, v_char_type_list: list) -> list:
    """
        Создание списка из токенов на базе списка символов и списка типов символов
    """
    pass 

def to_token_type_list(v_list: list) -> list:
    """
        Создание списка из типов токенов на базе списка из токенов
    """
    pass 


"""Проверка списка"""

def check_char_list_brackets(v_char_type_list: list):
    """
        Наконец-то это пригодилось :)
        Проверка скобочной последовательости
    """
    pass

def check_char_list_beginning(v_char_type_list: list):
    """
        Выражение должно начинаться с открывающейся скобки или числа
    """
    pass

def check_char_list_ending(v_char_type_list: list):
    """
        Выражение должно заканчиваться на закрывающуюся скобку, число или знак равенства
    """
    pass 

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
    pass 

def check_char_list_equation(v_char_type_list: list):
    """
        Знак равенства должен находиться только в конце 
    """
    pass 

def check_char_list_dot(v_char_type_list: list):
    """
        До точки и после точки должны быть цифры 
        пока не будет или скобки или оператора или края строки
    """
    pass

def check_char_list(v_char_type_list: list): 
    """
        Проверка списка из символов
    """
    pass 

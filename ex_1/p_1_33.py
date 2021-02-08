"""
1. Можно писать в одну строку длинные выражения - попробовать учесть скобки и порядок выполнения арифметических операций
2. Можно писать по числу или оператору - результат рассчитывется автоматически по enter 
3. При помощи кнопки "с" (clear) - ресетим в ноль 
4. При помощи кнопки "r" (reset) - откатываем последнее вычисление
"""

"""
Алгоритм 
    1. Проверка того, что введенная строка - валидное арифметическое выражение 
    2. Строка - операция 
    3. Строка - цифра 
    4. Посчитать выражение
        4.1 Проверка скобочной последовательности
        4.2 Проверка того, что отдельные части выражения это выражения или операции или цифры 
    5. Парсинг строки с выражением и формирование списка из элементов

    В порядке очереди:
    1. Распарсить входную строку на отдельные элементы + проверить адекватность введенного
    2. Попробовать посчитать правильно арифметическое выражение в соответствии с принятыми арифметическими правилами (можно забить и попробовать через eval())
"""

class Error(Exception):
    pass 

class InputParameterError(Error):

    def __init__(self, function_name, parameter_name, message):
        super().__init__(message)
        self.function_name = function_name 
        self.parameter_name = parameter_name 

class ArgsLengthParameterError(InputParameterError):

    def get_message(self, function_name, parameter_name) -> str:
        return "Function: {0} -> Parameter: {1} -> Parameter must has a length of one.".format(
            function_name, parameter_name
        )

    def __init__(self, function_name, parameter_name="*args"):
        super().__init__(
            function_name=function_name, 
            parameter_name=parameter_name, 
            message=self.get_message(function_name, parameter_name)
        )

def is_char(v_str: str, *args: tuple) -> bool:
    v_result = True if isinstance(v_str, str) and len(v_str) == 1 else False

    if args:
        if len(args) == 1:
            return v_result & (v_str == args[0])
        else:
            raise ArgsLengthParameterError("is_char")
    else:
        return v_result

def is_number(v_str: str) -> bool:
    if is_char(v_str):
        try:
            int(v_str) 
            return True 
        except ValueError:
            return False 

def is_operation(v_str: str) -> bool:
    return is_char(v_str, ("+")) or is_char(v_str, ("-")) \
        or is_char(v_str, ("*")) or is_char(v_str, ("/"))

def is_equation(v_str: str) -> bool:
    return is_char(v_str, ("="))

def is_opening_bracket(v_str: str) -> bool:
    return is_char(v_str, ("(")) 

def is_closing_bracket(v_str: str) -> bool:
    return is_char(v_str, (")")) 

def parse_expression(v_str: str) -> list:
    pass

print(is_closing_bracket(")"))
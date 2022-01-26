from multiprocessing.sharedctypes import Value
from re import VERBOSE, compile, split, fullmatch

"""
    Write a Python program that inputs a polynomial in standard algebraic
    notation and outputs the first derivative of that polynomial.
"""

# TODO: после всех исправлений, необходимо организовать класс Polynomial таким образом, чтобы при инициализации сразу же вычислялась первая производная

class PolynomialToken:

    """
        Класс для описания части полинома - отдельного токена  
    """

    def __init__(self, p_order_number: int, p_coefficient: float, p_variable: str, p_pow: float):
        """
            p_order_number - порядковый номер 
            p_coefficient - числовой коэффициент 
            p_variable - переменная 
            p_pow - показатель степени
        """
        self.order_number = p_order_number
        self.coefficient = p_coefficient
        self.variable = p_variable 
        self.pow = p_pow 

        self.check_type()
        self.check_value()

    def check_type(self):
        """
            Проверки типов у атрибутов класса
        """

        if not isinstance(self.order_number, (int)):
            raise TypeError("Порядковый номер токена должен быть целым числом")

        if not isinstance(self.coefficient, (int, float)):
            raise TypeError("Числовой коэффициент должен быть числом")

        if not isinstance(self.variable, (str)):
            raise TypeError("Переменная должна быть строкой")

        if len(self.variable) > 1:
            raise TypeError("Переменная должна иметь длину 1")

        if not isinstance(self.pow, (int, float)):
            raise TypeError("Показатель степени должен быть числом")

    def check_value(self):
        """
            Проверки значений у атрибутов класса 
        """

        if self.order_number is None:
            raise ValueError("Порядковый номер должен быть заполнен")

        if self.coefficient is None:
            raise ValueError("Числовой коэффициент должен быть заполнен")

        if self.variable is None:
            raise ValueError("Переменная должна быть заполнена")

        if self.pow is None:
            raise ValueError("Показатель степени должен быть заполнен")
        

    def get_derivative(self):
        """
            Возвращает экземпляр класса токена полинома, являющийся первой производной
        """
        l_coefficient = self.coefficient * self.pow 
        l_pow = self.pow - 1

        return PolynomialToken(
            p_order_number = self.order_number,
            p_coefficient=l_coefficient,
            p_variable=self.variable,
            p_pow=l_pow
        )


class Polynomial:

    """
        Класс для описания полинома 
    """

    def __init__(self, p_str: str):
        self.str = p_str.replace(" ", "")

        self.default_variable = "x"
        self.token_list = []

        self.parse()

        # TODO: Добавить проверку

    def parse(self):
        """
            Разбираем полином на составляющие
        """
        l_pattern_split = compile(pattern="(?=[+-])")
        l_split_result = l_pattern_split.split(string=self.str)

        for i_idx, i_token in enumerate(l_split_result):
            if len(i_token) > 0:
                self.token_list.append(self.parse_token(p_str=i_token, p_order_number=i_idx)) 
    
    def parse_token(self, p_str: str, p_order_number: int) -> PolynomialToken:

        l_pattern = compile(
            pattern="""
                (?P<coefficient>[+-]?\d+(?:\.?\d+)?)? # coefficient
                (?P<variable>[a-zA-Z])? # variable
                ^\(?(?P<pow>\d+(?:[/\.]\d+)?)\)? # pow
            """,
            flags=VERBOSE
        ) 

        l_match_object = l_pattern.fullmatch(string=p_str)

        if l_match_object:

            l_coefficient = l_match_object.group("coefficient") if l_match_object.group("coefficient") else 1
            l_variable = l_match_object.group("variable") if l_match_object.group("variable") else self.default_variable
            l_pow = l_match_object.group("pow") if l_match_object.group("pow") else 0

            if l_variable != self.default_variable:
                self.default_variable = l_variable
            
        else:
            raise ValueError("Не удалось распознать токен: " + p_str)

        return PolynomialToken(
            p_order_number=p_order_number,
            p_coefficient=l_coefficient,
            p_variable=l_variable,
            p_pow=l_pow
        )

    def check(self):
        """
            Полином имеет следующий вид:
            ax^n + bx^(n-1) + ... + yx^1 + z

            Перечень проверок:
            1. Степень все время убывает 
            2. Используется только одна переменная 
        """
        # TODO: Реализовать проверки
        pass 

    def get_derivative(self):
        # TODO: Реализовать получение первой производной
        pass 

    def derivative_to_string(self):
        # TODO: Реализовать получение первой производной в виде строки
        pass



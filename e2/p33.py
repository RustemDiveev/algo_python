"""
    Write a Python program that inputs a polynomial in standard algebraic
    notation and outputs the first derivative of that polynomial.

    Для простоты ведем следующие ограничения:
    1. Полином состоит из следующих элементов ax^c, объединенных + или - 
    2. a - коэффициент, x - переменная, с - показатель степени 
    3. a - любое натуральное число, положительное или отрицательное - недопустимо выражение, не может быть заключено в скобки 
    4. x - любая буква [A-Za-z]
    5. c - то же самое, что и a, но, если отрицательное - то заключено в скобки 
    6. Особые случаи: Переменная может быть опущена - равносильно x^0, 
        степень может быть опущена - равносильно x^1, 
        коэффициент может быть опущен - но должна быть хотя бы переменная

    Постановка задачи:
    Блок 1: Парсинг и проверка входной строки
        1. Разбить полином на члены - рассмотреть все возможные случаи (самая масштабная часть) - покрыть тестами
        2. Проверка на то, что полином не пустой 
        3. Проверка на то, что разбиение полинома по частям суммарно совпадает с первоначальной длиной с учетом удаления пробелов 
    Блок 2: Выделение составляющих отдельного члена 
        1. Выделение коэффициента, переменной и степени 
        2. Проверка, что нет недопустимых символов после выделения  
        3. Проверка, что полином записан в алгебраической нотации, т.е:
            а) Недопустимо, чтобы у двух или более членов совпадали показатели степени 
            б) Степень должна убывать от первого члена к последнему 
            в) Переменная повторяется только один раз
    Блок 3: Реализация класса члена, позволяющего брать производную от него 
    Блок 4: Инициализация класса Полином и генерация производной и её печать 
"""

from re import compile, sub, VERBOSE

class Polynomial:
    """
        Класс, реализующий полином и взятие производной от него
    """

    # Константы, связанные с разбором полинома на отдельные части 
    # Части паттернов для упрощения 
    C_VARIABLE = "[a-zA-Z]"
    C_OPERATOR = "[+-]?"
    C_NUMBER = "\d+(?:\.\d+)?"
    C_POW = "\^(?:" + C_NUMBER + "|\(-" + C_NUMBER + "\))"

    # Основной паттерн для разбора полинома 
    C_FINDALL_PATTERN = C_OPERATOR + "(?:" + \
        C_NUMBER + C_VARIABLE + C_POW + "|" + \
        C_VARIABLE + C_POW + "|" + \
        C_NUMBER + C_VARIABLE + "|" + \
        C_NUMBER + "|" + \
        C_VARIABLE + ")" 

    C_FINDALL_PATTERN = compile(pattern=C_FINDALL_PATTERN)

    def __init__(self, p_string: str):
        """
            Конструктор 
            input: 
                p_string - входная строка 
        """
        # Убираем пробелы из строки 
        self.string = p_string.replace(" ", "")

        # Проверка на пустоту 
        if not self.string:
            raise ValueError("Переданная строка с полиномом является пустой")

        # Разбор полинома на слагаемые
        self._findall()

    def _findall(self):
        """
            Разбирает входную строку на слагаемые, записывает результат в переменную класса 

        """
        self._findall_result = self.C_FINDALL_PATTERN.findall(string=self.string)
        self._check_length()
        self.terms = [Term(p_string=i_element) for i_element in self._findall_result]

    def _check_length(self):
        """
            Проверяем совпадает ли длина строки-полинома с убранными пробелами 
            с суммарной длиной всех найденных элементов 
            Если длина отличается, то считаем, что на вход подана неверная строка 
        """
        l_input_length = len(self.string)
        l_findall_length = 0 
        for i_elem in self._findall_result:
            l_findall_length += len(i_elem)

        if l_input_length != l_findall_length:
            raise ValueError("Переданная строка не является полиномом: ", self.string)

    def _check_algebraic_notation(self):
        """
            Проверяет, является ли входной полином записанным в алгебраической нотации 
        """   

        l_pow, l_variable = None, None

        for i_term in self.terms:

            if l_variable and i_term.variable:
                if l_variable != i_term.variable:
                    raise ValueError(
                        "Полином", self.string, "не записан в алгебраической нотации. Обнаружена переменная ", 
                        i_term.variable, "вместе с переменной ", l_variable
                    )

            if l_pow and i_term.pow:
                if l_pow == i_term.pow:
                    raise ValueError(
                        "Полином", self.string, "не записан в алгебраической нотации.", 
                        "Обнаружен повторяющийся показатель степени у одночлена", i_term.string
                    )

                if l_pow < i_term.pow:
                    raise ValueError(
                        "Полином", self.string, "не записан в алгебраической нотации.", 
                        "Степень должна быть убывающей"
                    )

            l_variable = i_term.variable if l_variable is None and i_term.variable else l_variable
            l_pow = i_term.pow if l_pow is None and i_term.pow else l_pow


    def get_derivative(self) -> str:
        """
            Возвращает строку с первой производной
        """
        self._check_algebraic_notation()
        l_result = ""
        for i_term in self.terms:
            i_term._get_derivative()
            l_result += i_term.derivative_string

        # убираем первый символ, если он +
        if l_result[0] == "+":
            l_result = l_result[1:]

        # убираем ненужные нули 
        l_result = sub(
            pattern="[+-]0(?=[+-])",
            repl="",
            string=l_result
        )
        
        if len(l_result) == 0:
            l_result = "0"

        return l_result


class Term:
    """
        Класс, реализующий слагаемое полинома
    """

    C_COEFFICIENT_PATTERN = compile(
        pattern="^([+-]?\d+(?:\.\d+)?)"
    )

    C_VARIABLE_PATTERN = compile(
        pattern="[a-zA-Z]"
    )

    C_POW_PATTERN = compile(
        pattern="""
            (?<=\^)
            (?:\()?
            (-?\d+(?:\.\d+)?)
            (?:\))?
        """,
        flags=VERBOSE
    )
    
    def __init__(self, p_string: str):
        """
            Конструктор
            input: 
                p_string - входная строка со слагаемым полинома 
        """
        self.string = p_string 
        self.coefficient, self.variable, self.pow = None, None, None
        self._parse() 
        
    def _parse_coefficient(self): 
        """
            Поиск коэффициента в одночлене
        """
        l_result = self.C_COEFFICIENT_PATTERN.search(string=self.string)
        if l_result:
            try:
                self.coefficient = int(l_result[0])
            except ValueError:
                self.coefficient = float(l_result[0])

    def _parse_variable(self):
        """
            Поиск переменной в одночлене
        """
        l_result = self.C_VARIABLE_PATTERN.search(string=self.string)
        if l_result:
            self.variable = l_result[0]

    def _parse_pow(self):
        """
            Поиск показателя степени в одночлене 
        """
        l_result = self.C_POW_PATTERN.search(string=self.string)
        if l_result:
            try:
                self.pow = int(l_result[1])
            except ValueError:
                self.pow = float(l_result[1])

    def __str__(self) -> str:
        return self.string

    def _parse(self):
        """
            Парсинг исходной строки, и нахождение коэффициента, переменной и степени 
        """
        self._parse_coefficient()
        self._parse_variable()
        self._parse_pow()

        # Обработка специальных случаев: 5, x, 
        # Если обычное число, то степень - 1
        # Если просто переменная, то коэффициент - 1 

        if self.variable is None:
            self.pow = 0
        
        if self.coefficient is None:
            self.coefficient = 1 

        if self.pow is None:
            self.pow = 1

    def _get_derivative(self):
        """
            Формирует строку с первой производной одночлена 
            записывает результат в переменную класса 
        """
        l_coefficient = self.coefficient * self.pow 
        if float(l_coefficient) - int(l_coefficient) == 0:
            l_coefficient = int(l_coefficient)

        l_pow = self.pow - 1 
        if float(l_pow) - int(l_pow) == 0:
            l_pow = int(l_pow)

        # Классика - через шаблон 
        C_RESULT_TEMPLATE = "#COEFFICIENT##VARIABLE#^#POW#"

        """
            Возможны крайние случаи 
            1. Коэффициент равен 0 и переменная неизвестна - выводим 0 
            2. Степень равна 0, выводим только коэффициент
            3. Степень равна 1, ничего не выводим 
        """

        if l_coefficient == 0:
            l_result = "+0"
        else:
            l_coefficient = "+" + str(l_coefficient) if l_coefficient > 0 else str(l_coefficient)

            if l_coefficient == "+1" and self.variable:
                l_coefficient = "+"

            if l_coefficient == "-1" and self.variable:
                l_coefficient = "-"

            if l_pow == 0:
                l_result = l_coefficient
            elif l_pow == 1:
                l_result = C_RESULT_TEMPLATE.replace("#COEFFICIENT#", l_coefficient)
                l_result = l_result.replace("#VARIABLE#", self.variable)
                l_result = l_result.replace("^#POW#", "")
            elif l_pow > 0:
                l_result = C_RESULT_TEMPLATE.replace("#COEFFICIENT#", l_coefficient)
                l_result = l_result.replace("#VARIABLE#", self.variable)
                l_result = l_result.replace("#POW#", str(l_pow))
            else:
                l_pow = "(" + str(l_pow) + ")"
                l_result = C_RESULT_TEMPLATE.replace("#COEFFICIENT#", l_coefficient)
                l_result = l_result.replace("#VARIABLE#", self.variable)               
                l_result = l_result.replace("#POW#", l_pow)
        
        self.derivative_string = l_result

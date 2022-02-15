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

from re import compile, findall

C_TEST_STRINGS = [
    "x+y",
    "-x-y",
    "0+0",
    "-1-3",
    "3.43+2.43",
    "-3.43-4.23",
    "-10x-8y",
    "-2.32x-124.23y",
    "10x^2+20x^3",
    "-10x^(-2)-40x^(-3)",
    "123.24x^2.34+213.321y^7.32",
    "-78.89x^(-23.4)-14.43y^(-23.4)",
    "x^2+y^3",
    "-x^(-2)-y^(-3)",
    "-x^(-2.24)-y^(-3.44)"
]

# Части паттернов для упрощения 
C_PATTERN_LETTER = "[a-zA-Z]"
C_OPERATOR = "[+-]"
C_INTEGER_COEFFICIENT = "\d+"
C_PRECISION_COEFFICIENT = "\d+\.\d+"
C_POW_SYMBOL = "\^"
C_NEGATIVE_INTEGER_POW="\(-" + C_INTEGER_COEFFICIENT + "\)"
C_NEGATIVE_PRECISION_POW="\(-" + C_PRECISION_COEFFICIENT + "\)"

l_string = C_TEST_STRINGS[0]
l_findall_pattern = compile(pattern=C_OPERATOR+"?"+C_PATTERN_LETTER)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[1]
l_findall_pattern = compile(pattern=C_OPERATOR+"?"+C_PATTERN_LETTER)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[2]
l_findall_pattern = compile(pattern=C_OPERATOR+"?"+C_INTEGER_COEFFICIENT)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[3]
l_findall_pattern = compile(pattern=C_OPERATOR+"?"+C_INTEGER_COEFFICIENT)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[4]
l_findall_pattern = compile(pattern=C_OPERATOR+"?"+C_PRECISION_COEFFICIENT)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[5]
l_findall_pattern = compile(pattern=C_OPERATOR+"?"+C_PRECISION_COEFFICIENT)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[6]
l_findall_pattern = compile(pattern=C_OPERATOR+"?"+C_INTEGER_COEFFICIENT+C_PATTERN_LETTER)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[7]
l_findall_pattern = compile(pattern=C_OPERATOR+"?"+C_PRECISION_COEFFICIENT+C_PATTERN_LETTER)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[8]
l_findall_pattern = compile(pattern=C_OPERATOR+"?"+C_INTEGER_COEFFICIENT+C_PATTERN_LETTER+C_POW_SYMBOL+C_INTEGER_COEFFICIENT)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[9]
l_findall_pattern = compile(pattern=C_OPERATOR+"?"+C_INTEGER_COEFFICIENT+C_PATTERN_LETTER+C_POW_SYMBOL+C_NEGATIVE_INTEGER_POW)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[10]
l_findall_pattern = compile(pattern=C_OPERATOR+"?"+C_PRECISION_COEFFICIENT+C_PATTERN_LETTER+C_POW_SYMBOL+C_PRECISION_COEFFICIENT)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[11]
l_findall_pattern = compile(pattern=C_OPERATOR+"?"+C_PRECISION_COEFFICIENT+C_PATTERN_LETTER+C_POW_SYMBOL+C_NEGATIVE_PRECISION_POW)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[12]
l_findall_pattern = compile(pattern=C_OPERATOR+"?"+C_PATTERN_LETTER+C_POW_SYMBOL+C_INTEGER_COEFFICIENT)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[13]
l_findall_pattern = compile(pattern=C_OPERATOR+"?"+C_PATTERN_LETTER+C_POW_SYMBOL+C_NEGATIVE_INTEGER_POW)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[14]
l_findall_pattern = compile(pattern=C_OPERATOR+"?"+C_PATTERN_LETTER+C_POW_SYMBOL+C_NEGATIVE_PRECISION_POW)
print(l_string, l_findall_pattern.findall(string=l_string))

# Упростим 
С_PREFIX = C_OPERATOR + "?"
C_COEFFICIENT = "\d+(?:\.\d+)?"
C_VARIABLE = "[a-zA-Z]"
C_POW = "\^(?:" + C_COEFFICIENT + "|\(-" + C_COEFFICIENT + "\))"

# Пробуем еще раз
print("New iteration")
l_string = C_TEST_STRINGS[0]
l_findall_pattern = compile(pattern=С_PREFIX+C_VARIABLE)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[1]
l_findall_pattern = compile(pattern=С_PREFIX+C_VARIABLE)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[2]
l_findall_pattern = compile(pattern=С_PREFIX+C_COEFFICIENT)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[3]
l_findall_pattern = compile(pattern=С_PREFIX+C_COEFFICIENT)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[4]
l_findall_pattern = compile(pattern=С_PREFIX+C_COEFFICIENT)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[5]
l_findall_pattern = compile(pattern=С_PREFIX+C_COEFFICIENT)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[6]
l_findall_pattern = compile(pattern=С_PREFIX+C_COEFFICIENT+C_VARIABLE)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[7]
l_findall_pattern = compile(pattern=С_PREFIX+C_COEFFICIENT+C_VARIABLE)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[8]
l_findall_pattern = compile(pattern=С_PREFIX+C_COEFFICIENT+C_VARIABLE+C_POW)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[9]
l_findall_pattern = compile(pattern=С_PREFIX+C_COEFFICIENT+C_VARIABLE+C_POW)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[10]
l_findall_pattern = compile(pattern=С_PREFIX+C_COEFFICIENT+C_VARIABLE+C_POW)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[11]
l_findall_pattern = compile(pattern=С_PREFIX+C_COEFFICIENT+C_VARIABLE+C_POW)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[12]
l_findall_pattern = compile(pattern=С_PREFIX+C_VARIABLE+C_POW)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[13]
l_findall_pattern = compile(pattern=С_PREFIX+C_VARIABLE+C_POW)
print(l_string, l_findall_pattern.findall(string=l_string))

l_string = C_TEST_STRINGS[14]
l_findall_pattern = compile(pattern=С_PREFIX+C_VARIABLE+C_POW)
print(l_string, l_findall_pattern.findall(string=l_string))

"""
С_PREFIX+C_VARIABLE
С_PREFIX+C_COEFFICIENT
С_PREFIX+C_COEFFICIENT+C_VARIABLE
С_PREFIX+C_COEFFICIENT+C_VARIABLE+C_POW
С_PREFIX+C_VARIABLE+C_POW

C_PREFIX = a
C_COEFFICIENT = b
C_VARIABLE = c 
C_POW = d 
то тогда:

ac
ab
abc
abcd
acd

a(?:c|b|bc|bcd|cd)

a(?:bcd|cd|bc|b|c)
Попробуем воспроизвести и проверить, что все тесты отработают
"""

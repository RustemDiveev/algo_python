from sys import stdout


def println(*objects, sep=' ', file=stdout, flush=False):
    """
        Переопределяет функцию print для удобной демонстрации результатов 
        Разделяет выходные данные двумя переносами строк
    """
    print(*objects, sep=sep, end='\n\n', file=file, flush=flush)

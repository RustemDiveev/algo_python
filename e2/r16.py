# max(0, (stop - start + step - 1) // step)
# Необходимо получить количество итераций - это какое то число от начала до конца, 
# деленное нацело на размер шага - чисто эвристически
# 2, 10, 2 - всего 2, 4, 6, 8 - т.е 4 элемента, т.е (10 - 2) // 2
# Попробуем другой пример:
# 170, 600, 100 - всего 170, 270, 370, 470, 570 - всего 5, т.е 600-170=430//100 = 4, 
# но при этом 5 элементов - значит предыдущая формула не подходит, нужно сделать округление в большую сторону
# Очевидно, что если к (stop - start) прибавить (step - 1), то количество элементов в итерации не увеличится, при этом, округление в большую сторону будет работать
# Здесь мы исходим из того, что step - целое число
# Эту формулу можно считать эвристически верной, но планирую покрыть её случайными тестами 
# Мы считаем, что start, end, step - целые числа, при этом, step - только положительный, для отрицательного не работает

def get_element_cnt_in_range_loop(p_start: int, p_stop: int, p_step: int) -> int:
    """
        Returns amount of elements in a range 
        with usage of a standard "for" loop
        input:
            p_start - starting number
            p_end   - ending number 
            p_step  - step number
        output:
            int
    """
    l_cnt = 0
    for i in range(p_start, p_stop, p_step):
        l_cnt += 1
    return l_cnt 

def get_element_cnt_in_range_formula(p_start: int, p_stop: int, p_step: int) -> int:
    """
        Returns amount of elements in a range 
        with usage of a formula
        input:
            p_start - starting number
            p_end   - ending number 
            p_step  - step number
        output:
            int
    """
    return max(0, (p_stop - p_start + p_step - 1) // p_step)

"""
    Наблюдения:
    1. Если метод был определен только в одном из родительских классов без перегрузки в промежуточных классах,
    то по дебаггеру - обращение идет сразу к нужному методу нужного класса 
    2. Если метод был определен в каждом из классов, то по дебаггеру идет обращение снизу вверх, а затем сверху вниз

    Недостатки глубокой и узкой иерархии классов:
    Размазанная функциональность, из-за чего сложно отследить принцип работы того или иного метода 

    Иерархия должна быть в меру широкой и в меру глубокой (я бы сказал 3-5 классов в ширину и глубину)
"""

class A:

    def __init__(self, p_something):
        self._something = p_something 

    def do_something(self):
        l_result = self._something
        return l_result 

class B(A):
    
    def do_something(self):
        l_result = super().do_something()
        return "Restrukt!"

class C(B):
    
    def do_something(self):
        l_result = super().do_something()
        return "Yavol!"

class D(C):
    
    def do_something(self):
        l_result = super().do_something()
        return "Arbeit!"

#l_c = D("hello!")
#a = l_c.do_something()


from typing import Iterator

def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1 
    if k * k == n:
        yield k
        
def factors_increase_order(n: int) -> Iterator[int]:
    """
        Returns generator which yields factors in increasing order
        input:
            n - input number 
        output:
            Iterator[int]
    """
    k = 1
    
    while k * k <= n:
        if n % k == 0:
            yield k
        k += 1
    else:
        k += 1

    while k * k > n and k <= n:
        if n % k == 0:
            yield k
        k += 1

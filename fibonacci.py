""""
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range (1,11):
    print (n, ":", fibonacci(n))
"""

#Memoization
"""
fibonacci_cache = {}

def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


    # cache the value and return it
    fibonacci_cache[n] = value
    return value

for n in range (1,100):
    print (n, ":", fibonacci(n))

"""
from functools import lru_cache

@lru_cache(maxsize = 1000)

def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)

for n in range (1,100):
    print (n, ":", fibonacci(n))
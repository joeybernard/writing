from math import factorial
from numba import jit

@jit
def calc():
        n = 500
        t = 0.0
        pi = 0.0
        deno= 0.0
        k = 0
        for k in range(n):
            t = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
            deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
            pi += t/deno
        pi = pi * 12.0/(640320.0**(1.5))
        pi = 1/pi
        return pi

if __name__ == '__main__':
        import timeit
        print(timeit.timeit("calc()", setup="from __main__ import calc", number=10))

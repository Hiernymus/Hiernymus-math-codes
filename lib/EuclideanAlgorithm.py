from sage.all import *
from numpy import NaN


def EuclideanAlgorithm(a,b):
    m = 0
    n = 0
    if a>b:
        m = a
        n = b
    elif a<b:
        m = b
        n = a
    r = m % n
    if r == 0:
        return n
    else:
            return EuclideanAlgorithm(b,r)

print(EuclideanAlgorithm(66,99))

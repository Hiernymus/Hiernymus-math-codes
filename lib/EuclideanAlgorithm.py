from queue import Full
from sage.all import *
from numpy import NaN


def EuclideanAlgorithm(a,b,_x=[1,0],_y=[0,1],_count=-1):
    m = 0
    n = 0
    x = _x
    y = _y
    c = _count + 1
    if a>b:
        m = a
        n = b
    elif a<b:
        m = b
        n = a
    r = m % n
    q = m // n
    if c == 0:
        x[1] = x[0] - q*x[1]
        y[1] = y[0] - q*y[1]
    else:
        x.append(-1)
        y.append(-1)
        x[c]=x[c-2] - q*x[c-1]
        y[c]=y[c-2] - q*y[c-1]
    if r == 0:
        return (n,x,y)
    else:
        return EuclideanAlgorithm(b,r,x,y,c)

show(EuclideanAlgorithm(120,94))
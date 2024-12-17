
from sage.all import *
from numpy import NaN


def EuclideanAlgorithm(a,b,_x=[1,0],_y=[0,1],_count=1):
    x = _x
    y = _y
    c = _count + 1
    r = a % b
    q = a // b
    x.append(x[c-2] - q*x[c-1])
    y.append(y[c-2] - q*y[c-1])
    if r == 0:
        return (a,x[c-2],y[c-2])
    else:
        return EuclideanAlgorithm(b,r,x,y,c)


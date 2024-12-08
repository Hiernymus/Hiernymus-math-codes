from sage.all import *

def function(x):
    y = 2*sqrt(1 - x**2)
    return y

int = [-1,1]
dx = 0.00000001

_y = 0
_x = int[0]
while (_x < int[1]):
    _y = add([_y,function(_x)])
    _x = add([_x,dx])
    print(_y*dx)
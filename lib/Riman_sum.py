from sage.all import *

def Riman_sum(f,range,x):
    dx = 0.001

    _y = 0
    _x = range[0]
    
    while (_x < range[1]):
        _y = add([_y,f.subs(x=_x)])
        _x = add([_x,dx])
    return _y*dx

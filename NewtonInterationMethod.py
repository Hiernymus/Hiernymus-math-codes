from sage.all import *

def interation(f,x,a,t):
    j = 0
    df = f.diff(x)
    while j < t:
        print("z")
        a = a - f.subs(x=a)/df.subs(x=a)
        j =j + 1
    return a
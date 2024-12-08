from sage.all import *

def interation(f,x,a,t):
    j = 0
    df = f.diff(x)
    while j < t:
        print("z")
        a = n(a) - n(f.subs(x=a)/df.subs(x=a))
        j =j + 1
    return n(a)
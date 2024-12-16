from sage.all import *

v = 0
t = 0

j = var("j")

a = ((-1)**j/(2*j+1))*(binomial(0.5, j))



while t < 173:
    v = v + a.subs(j=t)
    t = t + 1
    print((4*v))
    print("\n")

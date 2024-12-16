from sage.all import *

v = 0
t = 0

j = var("j")

a = ((-1)**j/(2*j+1))*(binomial(2, j))


while t < 100:
    v = v + binomial(1/2, t)
    t = t + 1
    print((4*v))

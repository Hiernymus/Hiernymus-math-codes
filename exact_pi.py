from sage.all import *

v = 0
t = 0

j = var("j")

a = ((-1)**j/(2*j+1))*(binomial(1/2, j))*(1)

a_num = fast_callable(a, vars=[j], domain=RR)

while t < 50000:
    v = v + a_num(t)
    t = t + 1

print(4*v)
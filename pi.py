from sage.all import *

v = 0

j = var("j")
x = var("x")

f = x**3 - 3
a = ((-1)**j/(2*j+1))*(binomial(1/2, j))*(1)
v = sum(a,j,0,300)

print(4*v)
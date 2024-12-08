from sage.all import *
from NewtonInterationMethod import interation

print("a")

t = 0
v = 0

j = var("j")
x = var("x")

f = x**3 - 3
a = ((-1)**j/(2*j+1))*(binomial(1/2, j))*(1-2**(-2*j-1))
v = sum(a,j,0,50)
print("b")

root3 = interation(f,x,2,15)

print("b")
u = v + root3/8
print(n(8*u))
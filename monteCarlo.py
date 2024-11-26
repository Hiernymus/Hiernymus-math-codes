from sage.all import *

def function1(x):
    y = sqrt(1 - x**2)
    return y

def function2(x):
    y = -sqrt(1 - x**2)
    return y

out_ = 0
in_ = 0
count = 0

while (True):
    count = count + 1
    point = (ZZ.random_element(-1000, 1000)/1000,ZZ.random_element(-1000, 1000)/1000)
    if(point[1] <= function1(point[0]) and point[1] >= function2(point[0])):
        in_ = in_ + 1
    else:
        out_ = out_ + 1
    print(count,":",4*(in_/add([in_,out_])))
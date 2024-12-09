from sage.all import *

def NewtonIterationMethod(f, x, a, t):
    # 将符号表达式转换为可以快速求值的函数
    f_num = fast_callable(f, vars=[x], domain=RR)
    df_num = fast_callable(f.diff(x), vars=[x], domain=RR)
    
    for _ in range(t):  # 使用 for 循环代替 while 循环，更简洁
        a = a - f_num(a) / df_num(a)
    
    return a
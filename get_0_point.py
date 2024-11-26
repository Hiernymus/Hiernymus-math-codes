from sage.all import *

print("var?")
var_input = input()
a = var(var_input) 

def function(x):
    print("f("+var_input+")=")
    f = eval(input())
    return f

solution = solve(function(a),a)
show(solution)
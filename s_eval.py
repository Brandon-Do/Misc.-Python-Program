def s_eval(exp):
    if isinstance(exp, int):
        return exp
    op, x, y = exp

    if isinstance(x, tuple):
        x = s_eval(x)
    if isinstance(y, tuple):
        y = s_eval(y)

    if op == '-':
        return x - y
    if op == '+':
        return x + y

print(s_eval( ('-', ('+', 5, 4), ('-', 5, 3)) ))
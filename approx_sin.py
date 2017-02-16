
from math import log

def approx_log(x, n):

    two = 2
    sum = 0.0

    for k in range(n):

        denom = two * (k + 1)
        sum += x / denom

        two *= 2
        x *= x

    return log(2) - sum

print(approx_log(2, 5))

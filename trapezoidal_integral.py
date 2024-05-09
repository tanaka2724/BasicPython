import math
from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------

def f(x):
    return sin(x)

N = 100
a = 0
b = math.pi / 2

h = (b - a) / N

S = 0
for k in range(1,N + 1):
    S += (h / 2) * (f(a + (k - 1) * h) + f(a + k * h))
    
    print(k)

print(S) 
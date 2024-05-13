import math
def f1(x):
    return math.sin(x)

def f2(x):
    return 4 / (1 + x**2)

def f3(x):
    return math.pi**0.5 * math.exp(-x**2)

def integral(f, a = 0, b = 1, n = 100):
    h = (b - a) / n
    S = 0
    for i in range(1, n+1):
        S += (h / 2) * (f(a + (i - 1)*h) + f(a + i*h))
        
    return S

result_1 = integral(f1, 0, math.pi/2, 50)
result_2 = integral(f2, 0, 1, 100)
result_3 = integral(f3, -100, 100, 1000)

print(result_1)
print(result_2)
print(result_3)

        
from math import *

x1 = 2
xn = 5
xd = 0.5
a = 1.5
b = 4.8
y = 0

for i in range(0, xn):
    s1 = b/x1
    s2 = log(a*x1)/b**2
    s3 = s1 - s2
    y = a*s3
    x1 += xd
    print("Результат №", i+1, "=", y)
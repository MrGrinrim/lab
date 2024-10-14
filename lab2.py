from math import *
import sys

x = float(input("Введите значение x -> "))
y = float(input("Введите значение y -> "))

msg = "Выберите вид функции f(x):  -> 1, e**y -> 2, ln(x) -> 3 "
f = float(input(msg + "\n -> "))
fx = None
s = None
match f:
    case 1:
        fx = cos(x)
    case 2:
        fx = exp(y)
    case 3:
        fx = log(x)
    case _:
        print("Неверный выбор")
        sys.exit() 


if (0.5 < x * y < 10) :
    s = exp(fx - fabs(y))
elif (0.1 < x * y < 0.5) :
    pow(fx + y , 1./3.)
else:
    s = 2 * fx
    
print("Результат: ", s)
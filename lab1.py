from math import * 
x = float(input("Ввевдите значения Х ") )
y = float(input("Ввевдите значения У ") )
z = float(input("Ввевдите значения Z ") )

if -1 <= x <= 1:
    a1 = pow(x, 1./3.) + pow(x, y+2)
    a2 = asin(z)
    a3 = sqrt(a2) - fabs(x)
    a4 = pow(10*a1 , 1/2)
    if a4 >= 0:    
        s = a4 * a3
        print("Результат", s)
    else:
        print("Значение выражения не может быть вычислено")
else:
    print("Число Z недоступно")
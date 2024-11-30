# Ввод списка чисел
numbers = list(map(int, input("Введите целые числа через пробел: ").split()))

# Определяем сумму чисел больше 5
sum_greater_than_5 = sum(number for number in numbers if number > 5)

# Вывод результата
print("Сумма чисел, которые больше 5:", sum_greater_than_5)
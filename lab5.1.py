# Ввод списка чисел
numbers = list(map(int, input("Введите целые числа через пробел: ").split()))

# Находим максимальный элемент
max_element = max(numbers)

# Подсчитываем количество элементов меньше и больше максимального
count_less = sum(1 for number in numbers if number < max_element)
count_greater = sum(1 for number in numbers if number > max_element)

# Вывод результатов
print("Максимальный элемент:", max_element)
print("Количество элементов меньше максимального:", count_less)
print("Количество элементов больше максимального:", count_greater)
import matplotlib.pyplot as plt

# Данные для графика
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Создание графика
plt.plot(x, y, marker='o')

# Добавление заголовка и меток
plt.title('Пример графика')
plt.xlabel('x')
plt.ylabel('y')

# Показать график
plt.grid()
plt.show()
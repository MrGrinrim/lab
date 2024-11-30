def analyze_numbers(numbers):
    if not numbers:  # Проверка на пустой список
        return "Список чисел пуст."

    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count
    max_value = max(numbers)
    min_value = min(numbers)

    return {
        "Сумма": total_sum,
        "Среднее": average,
        "Максимальное": max_value,
        "Минимальное": min_value
    }

# Пример использования
numbers = [10, 20, 30, 40, 50]
result = analyze_numbers(numbers)

print(result)
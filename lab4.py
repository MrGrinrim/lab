def replace_p_with_stars(s):
    n = len(s)
    half_n = n // 2
    # Заменяем 'п' на '*' в первых n/2 символах
    transformed_part = s[:half_n].replace('п', '*')
    # Соединяем преобразованную часть с остальной частью строки
    result = transformed_part + s[half_n:]
    return result

# Пример использования
input_string = "программирование"
output_string = replace_p_with_stars(input_string)
print(output_string)
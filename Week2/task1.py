# Получаем строку от пользователя
input_string = input()

# Переменная для подсчёта найденных стрелок
arrow_count = 0

# Длина строки
length = len(input_string)

# Проверяем, что строка достаточно длинная для поиска стрелок
if length >= 5:
    # Проходим по всем возможным начальным позициям стрелки
    for start in range(length - 4):
        # Вырезаем 5 символов из строки
        part = input_string[start:start+5]
        
        # Проверяем два вида стрелок
        if part == ">>-->":
            arrow_count += 1
        elif part == "<--<<":
            arrow_count += 1

# Печатаем результат
print(arrow_count)

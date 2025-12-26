# Получаем уравнение от пользователя
eq = input()
# Выводим уравнение для проверки (можно удалить)
print("Уравнение:", eq)
# Разбираем уравнение по символам
a = eq[0]  # Первый символ
op = eq[1]  # Оператор (плюс или минус)
b = eq[2]  # Третий символ
c = eq[4]  # Пятый символ (после знака равно)
# Находим, где находится x
if a == 'x':
    # Случай: x ? b = c
    num1 = int(b)  # b точно цифра
    num2 = int(c)  # c точно цифра
    
    if op == '+':
        # x + num1 = num2
        answer = num2 - num1
    else:  # op == '-'
        # x - num1 = num2
        answer = num2 + num1

elif b == 'x':
    # Случай: a ? x = c
    num1 = int(a)  # a точно цифра
    num2 = int(c)  # c точно цифра
    
    if op == '+':
        # num1 + x = num2
        answer = num2 - num1
    else:  # op == '-'
        # num1 - x = num2
        answer = num1 - num2

else:  # c == 'x'
    # Случай: a ? b = x
    num1 = int(a)  # a точно цифра
    num2 = int(b)  # b точно цифра
    
    if op == '+':
        # num1 + num2 = x
        answer = num1 + num2
    else:  # op == '-'
        # num1 - num2 = x
        answer = num1 - num2

# Выводим ответ
print(answer)

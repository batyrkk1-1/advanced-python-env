# Ввод данных
a = input()
b = input()

n = len(a)
m = len(b)

# Если строка b длиннее a, ответ 0
if m > n:
    print(0)
else:
    result = 0
    
    # Готовим все циклические сдвиги b
    b_shifts = []
    for i in range(m):
        new_string = b[i:] + b[:i]
        b_shifts.append(new_string)
    
    # Проверяем каждую подстроку
    for i in range(n - m + 1):
        sub = a[i:i + m]
        if sub in b_shifts:
            result += 1
    
    print(result)

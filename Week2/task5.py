# Создаём множество допустимых букв
allowed_letters = set('ABCEHKMOPTXY')

# Читаем количество номеров
n = int(input())

# Обрабатываем каждый номер
for _ in range(n):
    plate = input().strip()
    
    # Проверяем длину номера
    if len(plate) != 6:
        print("No")
        continue
    
    # Проверяем формат: буква, 3 цифры, 2 буквы
    # 1-й символ - буква
    if plate[0] not in allowed_letters:
        print("No")
        continue
    
    # 2-й, 3-й, 4-й символы - цифры
    if not (plate[1].isdigit() and plate[2].isdigit() and plate[3].isdigit()):
        print("No")
        continue
    
    # 5-й и 6-й символы - буквы
    if plate[4] not in allowed_letters or plate[5] not in allowed_letters:
        print("No")
        continue
    
    # Если все проверки пройдены
    print("Yes")

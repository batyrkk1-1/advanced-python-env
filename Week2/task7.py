# Читаем строку с покупками
purchases = input().split()

# Создаём словарь для подсчёта
count_dict = {}
for item in purchases:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

# Выводим частоту покупок
print("Purchase frequency:")
for item in count_dict:
    print(f"{item}: {count_dict[item]}")

# Находим самый популярный товар
max_count = 0
most_popular = ""
for item, count in count_dict.items():
    if count > max_count:
        max_count = count
        most_popular = item

print(f"\nMost popular item: {most_popular}")

# Находим товары, купленные один раз
once_items = []
for item, count in count_dict.items():
    if count == 1:
        once_items.append(item)

print(f"\nPurchased once: {' '.join(once_items)}")

# Сортируем товары по убыванию частоты
# Сначала создаём список кортежей (частота, товар)
sorted_items = []
for item, count in count_dict.items():
    sorted_items.append((count, item))

# Сортируем по убыванию частоты
sorted_items.sort(reverse=True)

# Выводим отсортированный список
print("\nSorted by frequency:")
for count, item in sorted_items:
    print(f"{item}: {count}")

def all_eq(lst):
    # Находим максимальную длину строки
    max_len = 0
    for s in lst:
        if len(s) > max_len:
            max_len = len(s)
    
    # Создаём новый список
    result = []
    for s in lst:
        # Если строка короче максимальной, добавляем '_' справа
        if len(s) < max_len:
            s = s + '_' * (max_len - len(s))
        result.append(s)
    
    return result


# Пример использования функции
if __name__ == "__main__":
    # Пример 1
    my_list = ["abc", "de", "fghij"]
    print(all_eq(my_list))  # ['abc__', 'de___', 'fghij']
    
    # Пример 2
    my_list2 = ["hello", "world", "python"]
    print(all_eq(my_list2))  # ['hello_', 'world_', 'python']
    
    # Пример 3
    my_list3 = ["a", "bb", "ccc"]
    print(all_eq(my_list3))  # ['a__', 'bb_', 'ccc']

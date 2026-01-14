import string

def analyze_text(input_filename, output_filename):
    try:
        # Словарь для хранения частоты слов
        word_frequency = {}
        total_lines = 0
        total_words = 0

        # Таблица для удаления пунктуации
        translator = str.maketrans('', '', string.punctuation)

        # 1. Чтение файла с использованием context manager
        with open(input_filename, 'r', encoding='utf-8') as file:
            for line in file:
                total_lines += 1
                
                # Приводим к нижнему регистру и удаляем пунктуацию
                # line.lower() - убирает чувствительность к регистру
                # .translate(...) - заменяет знаки препинания на пустоту
                clean_line = line.lower().translate(translator)
                
                # Разбиваем строку на список слов
                words = clean_line.split()
                total_words += len(words)
                
                # Считаем частоту каждого слова
                for word in words:
                    if word in word_frequency:
                        word_frequency[word] += 1
                    else:
                        word_frequency[word] = 1

        # 2. Запись результатов в analysis.txt
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(f"Total number of lines: {total_lines}\n")
            outfile.write(f"Total number of words: {total_words}\n")
            outfile.write("-" * 20 + "\n")
            outfile.write("Word Frequencies:\n")
            
            # Сортируем слова по частоте (по убыванию) для удобства, 
            # но можно убрать sorted(), если порядок не важен.
            sorted_words = sorted(word_frequency.items(), key=lambda item: item[1], reverse=True)
            
            for word, count in sorted_words:
                outfile.write(f"{word}: {count}\n")

        print(f"Анализ завершен! Результаты сохранены в файл '{output_filename}'.")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_filename}' не найден. Создайте его перед запуском.")

# Запуск функции
if __name__ == "__main__":
    # Убедитесь, что файл text.txt существует в той же папке
    analyze_text("text.txt", "analysis.txt")

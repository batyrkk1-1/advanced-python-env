import json

data = [
    {
        "name": "Alice",
        "age": 20,
        "grades": [85, 90, 92]
    },
    {
        "name": "Bob",
        "age": 21,
        "grades": [70, 75, 80]
    },
    {
        "name": "Charlie",
        "age": 22,
        "grades": [95, 88, 91]
    }
]

# Создаем исходный файл
with open('students.json', 'w') as file:
    json.dump(data, file, indent=4)
    print("Файл students.json успешно создан.")\
  import json

def process_student_grades(input_file, output_file):
    try:
        # 1. Чтение JSON файла
        with open(input_file, 'r') as file:
            students = json.load(file)
        
        # 2. Обработка данных (подсчет среднего)
        for student in students:
            grades = student.get('grades', [])
            
            # Проверка, чтобы не делить на ноль, если оценок нет
            if len(grades) > 0:
                average = sum(grades) / len(grades)
                # Округляем до 2 знаков для красоты
                student['average_grade'] = round(average, 2)
            else:
                student['average_grade'] = 0

        # 3. Запись в НОВЫЙ JSON файл (исходный файл не трогаем)
        with open(output_file, 'w') as outfile:
            # indent=4 делает файл читаемым для человека (красивые отступы)
            json.dump(students, outfile, indent=4)
            
        print(f"Обработка завершена. Результаты записаны в '{output_file}'")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден.")
    except json.JSONDecodeError:
        print(f"Ошибка: Не удалось прочитать JSON из файла '{input_file}'.")

# Запуск программы
if __name__ == "__main__":
    process_student_grades('students.json', 'students_with_averages.json')

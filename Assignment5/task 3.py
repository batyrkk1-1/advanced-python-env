# 1. Base Class (Базовый класс)
class Person:
    def __init__(self, name, age):
        self.name = name          # Публичный атрибут
        self.__age = age          # Приватный атрибут (Encapsulation)

    # Метод для демонстрации Полиморфизма (будет переопределен)
    def introduce(self):
        return f"Hello, I am {self.name} and I am a Person."

    # Геттер для доступа к приватному атрибуту (Encapsulation)
    def get_age(self):
        return self.__age

    # Сеттер для изменения приватного атрибута с проверкой (Encapsulation)
    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("Age must be positive!")

# 2. Child Class (Дочерний класс)
class Student(Person):  # Inheritance (Наследование)
    def __init__(self, name, age, student_id):
        # Вызов конструктора родителя
        super().__init__(name, age)
        self.student_id = student_id

    # Overriding a method (Переопределение метода)
    def introduce(self):
        return f"Hi, I am {self.name}, a Student with ID: {self.student_id}."

# --- Демонстрация (Driver Code) ---

if __name__ == "__main__":
    print("--- 1. Encapsulation (Инкапсуляция) ---")
    p1 = Person("John", 40)
    # Прямой доступ к p1.__age вызовет ошибку, поэтому используем методы:
    print(f"Name: {p1.name}")
    print(f"Age (via getter): {p1.get_age()}")
    
    p1.set_age(41) # Изменяем через сеттер
    print(f"New Age: {p1.get_age()}")

    print("\n--- 2. Inheritance (Наследование) ---")
    # Student наследует методы от Person (например, get_age)
    s1 = Student("Alice", 20, "S12345")
    print(f"Student Name: {s1.name}")        # Атрибут из Person
    print(f"Student Age: {s1.get_age()}")    # Метод из Person
    print(f"Student ID: {s1.student_id}")    # Свой атрибут

    print("\n--- 3. Polymorphism (Полиморфизм) ---")
    # Создаем список разных объектов (и Person, и Student)
    people_list = [
        Person("Mike", 35),
        Student("Emma", 19, "S98765"),
        Person("Sarah", 50)
    ]

    # Вызываем один и тот же метод introduce(), но поведение разное
    for person in people_list:
        print(person.introduce())

# 1. Base Class Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        # Private attribute (по конвенции Python _salary считается защищенным/приватным)
        self._salary = salary

    def get_salary(self):
        return self._salary

    def get_role(self):
        return "Employee"

# 2. Child Class Manager
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        # Наследуем инициализацию от родителя
        super().__init__(name, salary)
        self.bonus = bonus

    # Overrides get_role() (Переопределение метода)
    def get_role(self):
        return "Manager"

    # Adds a method get_bonus() (Новый метод)
    def get_bonus(self):
        return self.bonus

# 3. Function to process list of employees
def print_employee_details(employees_list):
    print(f"{'Name':<10} | {'Role':<10} | {'Salary':<10}")
    print("-" * 36)
    
    for emp in employees_list:
        # Полиморфизм: Python сам понимает, чей метод get_role() вызвать
        role = emp.get_role()
        salary = emp.get_salary()
        
        print(f"{emp.name:<10} | {role:<10} | ${salary:<10}")

# --- Демонстрация работы ---
if __name__ == "__main__":
    # Создаем обычных сотрудников
    emp1 = Employee("Alice", 50000)
    emp2 = Employee("Bob", 52000)

    # Создаем менеджера (у него есть зарплата + бонус)
    mgr1 = Manager("Charlie", 80000, 15000)

    # Список всех сотрудников
    staff = [emp1, emp2, mgr1]

    # Вызов функции
    print_employee_details(staff)
    
    # Демонстрация уникального метода менеджера
    print(f"\nManager {mgr1.name} bonus: ${mgr1.get_bonus()}")

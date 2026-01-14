class BankAccount:
    def __init__(self, owner, initial_balance=0):
        # Приватные атрибуты (недоступны напрямую извне)
        self.__owner = owner
        self.__balance = initial_balance

    def deposit(self, amount):
        """Метод для внесения денег с проверкой."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposit successful: +${amount}")
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        """Метод для снятия денег с проверкой баланса."""
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print(f"Error: Insufficient funds. Current balance: ${self.__balance}")
        else:
            self.__balance -= amount
            print(f"Withdrawal successful: -${amount}")

    def get_balance(self):
        """Геттер для безопасного получения текущего баланса."""
        return self.__balance

    def get_owner(self):
        """Дополнительный геттер для имени владельца."""
        return self.__owner

# --- Демонстрация работы (Driver Code) ---
if __name__ == "__main__":
    # 1. Создаем счет
    my_account = BankAccount("Alex", 100)
    print(f"Account Owner: {my_account.get_owner()}")
    print(f"Initial Balance: ${my_account.get_balance()}")
    print("-" * 30)

    # 2. Тестируем депозит (Deposit)
    my_account.deposit(50)      # Успешно
    my_account.deposit(-20)     # Ошибка (отрицательное число)

    print("-" * 3

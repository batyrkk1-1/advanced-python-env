a = float(input())
op = input()
b = float(input())

print(
    a + b if op == '+' else
    a - b if op == '-' else
    a * b if op == '*' else
    "Division by zero" if op == '/' and b == 0 else
    a / b
)


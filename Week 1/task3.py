a = input()

integer_part, fractional_part = a.split('.')

new_number = fractional_part + "." + integer_part
print(new_number)


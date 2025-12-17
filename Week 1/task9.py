ticket = input()

first_sum = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
second_sum = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

if first_sum == second_sum:
    print("YES")
else:
    print("NO")


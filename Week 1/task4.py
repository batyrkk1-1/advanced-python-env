N = int(input())

if N >= 1:
    print(N * (N + 1) // 2)
else:
    print(-(abs(N) * (abs(N) + 1) // 2) + 1)


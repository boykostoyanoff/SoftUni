n = int(input())
avg = 0
for _ in range(n):
    avg += int(input())
avg /= n
print(f'{avg:.2f}')
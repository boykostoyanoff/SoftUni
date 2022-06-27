n = int(input())
start = 1
if n % 2 == 0:
    start = 2

for i in range(start, n + 1, 2):
    line = '-' * ((n - i) // 2) + '*' * i + '-' * ((n - i) // 2)
    print(line)

for i in range(n // 2):
    line = '|' + '*' * (n - 2) + '|'
    print(line)
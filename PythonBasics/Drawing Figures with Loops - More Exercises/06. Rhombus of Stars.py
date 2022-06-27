n = int(input())

for i in range(1, n + 1):
    line = ' ' * (n - i)
    line += '*' + (' *' * (i - 1))
    print(line)

for i in range(n - 1, 0, -1):
    line = ' ' * (n - i)
    line += '*' + (' *' * (i - 1))
    print(line)
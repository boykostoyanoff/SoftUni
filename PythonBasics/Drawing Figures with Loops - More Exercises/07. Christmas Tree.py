n = int(input())

for i in range(n + 1):
    line = ' ' * (n - i) + '*' * i + ' '
    line += '|'
    line += ' ' + '*' * i
    print(line)
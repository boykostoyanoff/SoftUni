n = int(input())
if n == 1 or n == 2:
    print(n * '*')
else:
    start = 1
    if n % 2 == 0:
        start = 2
    line = ((n - start) // 2 ) * '-' + start * '*' + ((n - start) // 2 ) * '-'
    print(line)
    for i in range(start, n, 2):
        line = (n -(i + 2)) // 2 * '-'
        line += '*' + '-' * i + '*'
        line += (n -(i + 2)) // 2 * '-'
        print(line)

    for i in range(1, n // 2):
        line = i * '-'
        line += '*' + '-' * (n - 2 * i - 2) + '*'
        line += i * '-'
        print(line)

    line = ((n - start) // 2 ) * '-' + start * '*' + ((n - start) // 2 ) * '-'
    if n % 2 == 1:
        print(line)
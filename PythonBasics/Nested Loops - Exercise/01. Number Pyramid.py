n = int(input())
number = 0
row = 1

while number <= n:
    for i in range(row):
        number += 1
        if number > n:
            break
        print(number, end=' ')
    print()
    row += 1
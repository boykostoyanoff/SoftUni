start = int(input())
end = int(input())

for n1 in range(start, end + 1):
    for n2 in range(start, end + 1):
        for n3 in range(start, end + 1):
            for n4 in range(start, end + 1):
                if n1 > n4:
                    if (n2 + n3) % 2 == 0:
                        if (n1 % 2 == 0 and not n4 % 2 == 0) or (n4 % 2 == 0 and not n1 % 2 == 0):
                            print(''.join([str(x) for x in [n1, n2, n3, n4]]), end=' ')
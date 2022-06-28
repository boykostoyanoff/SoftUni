j1 = int(input())
j2 = int(input())
j3 = int(input())
for i1 in range(1, j1 + 1):
    for i2 in range(1, j2 + 1):
        for i3 in range(2, j3 + 1):
            if i1 % 2 == 0 and i3 % 2 == 0 and i2 in [2, 3, 5, 7]:
                print(i1, i2, i3)

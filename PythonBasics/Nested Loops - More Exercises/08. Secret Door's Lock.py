n1 = int(input())
n2 = int(input())
n3 = int(input())

for i1 in range(2, n1 + 1, 2):
    for i2 in range(2, n2 + 1):
        is_prime = True
        for j in range(2, i2):
            if i2 % j == 0:
                is_prime = False
        if is_prime:
            for i3 in range(2, n3 + 1, 2):
                print(str(i1), str(i2), str(i3))

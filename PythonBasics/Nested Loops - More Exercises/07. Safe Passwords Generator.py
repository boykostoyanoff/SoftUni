a = int(input()) + 1
b = int(input()) + 1
password_limit = int(input())

A = 35
B = 64

for x in range(1, a):
    for y in range(1, b):
        if password_limit == 0:
            break
        print(chr(A) + chr(B) + str(x) + str(y) + chr(B) + chr(A), end='|')
        A += 1
        B += 1
        if A == 56:
            A = 35
        if B == 97:
            B = 64
        password_limit -= 1
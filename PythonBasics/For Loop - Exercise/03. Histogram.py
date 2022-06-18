p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

n = int(input())

for _ in range(n):
    number = int(input())
    if number < 200:
        p1 += 1
    elif number < 400:
        p2 += 1
    elif number < 600:
        p3 += 1
    elif number < 800:
        p4 += 1
    else:
        p5 += 1

result = p1 / n * 100
print(f'{result:.2f}%')
result = p2 / n * 100
print(f'{result:.2f}%')
result = p3 / n * 100
print(f'{result:.2f}%')
result = p4 / n * 100
print(f'{result:.2f}%')
result = p5 / n * 100
print(f'{result:.2f}%')
stadium_capacity = int(input())
fens_count = int(input())
fens_a = 0
fens_b = 0
fens_v = 0
fens_g = 0

for fen in range(fens_count):
    sector = input()
    if sector == 'A':
        fens_a += 1
    elif sector == 'B':
        fens_b += 1
    elif sector == 'V':
        fens_v += 1
    elif sector == 'G':
        fens_g += 1

result = fens_a / fens_count * 100
print(f'{result:.2f}%')
result = fens_b / fens_count * 100
print(f'{result:.2f}%')
result = fens_v / fens_count * 100
print(f'{result:.2f}%')
result = fens_g / fens_count * 100
print(f'{result:.2f}%')
result = fens_count / stadium_capacity * 100
print(f'{result:.2f}%')
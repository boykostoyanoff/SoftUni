start = int(input())
end = int(input())
magic_number = int(input())
counter = 0
result = ''
for n1 in range(start, end + 1):
    if not result == '':
        break
    for n2 in range(start, end + 1):
        counter += 1
        if n1 + n2 == magic_number:
            result = f'Combination N:{counter} ({n1} + {n2} = {magic_number})'
            break
if result == '':
    result = f'{counter} combinations - neither equals {magic_number}'

print(result)
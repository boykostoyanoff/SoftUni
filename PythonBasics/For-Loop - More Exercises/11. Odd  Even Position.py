n = int(input())
odd_sum = 0
odd_min = ''
odd_max = ''
even_sum = 0
even_min = ''
even_max = ''

for i in range(1, n + 1):
    number = float(input())
    if i % 2 == 1:
        odd_sum += number
        if odd_min == '':
            odd_min = number
            odd_max = number
        else:
            if number > odd_max:
                odd_max = number
            if number < odd_min:
                odd_min = number
    else:
        even_sum += number
        if even_min == '':
            even_min = number
            even_max = number
        else:
            if number > even_max:
                even_max = number
            if number < even_min:
                even_min = number

print(f'OddSum={odd_sum:.2f},')
if odd_min:
    print(f'OddMin={odd_min:.2f},')
else:
    print('OddMin=No,')
if odd_max:
    print(f'OddMax={odd_max:.2f},')
else:
    print(f'OddMax=No,')
print(f'EvenSum={even_sum:.2f},')
if even_min:
    print(f'EvenMin={even_min:.2f},')
else:
    print('EvenMin=No,')
if even_max:
    print(f'EvenMax={even_max:.2f}')
else:
    print('EvenMax=No')
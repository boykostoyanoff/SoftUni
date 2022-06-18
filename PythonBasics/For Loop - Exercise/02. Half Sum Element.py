n = int(input())
max_num = int(input())
max_sum = 0

for _ in range(n - 1):
    number = int(input())
    if number > max_num:
        max_sum += max_num
        max_num = number
    else:
        max_sum += number

if max_sum == max_num:
    print('Yes')
    print(f'Sum = {max_sum}')
else:
    print('No')
    print(f'Diff = {abs(max_num - max_sum)}')
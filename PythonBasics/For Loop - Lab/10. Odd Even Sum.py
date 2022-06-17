n = int(input())
odd_sum = 0
even_sum = 0

for index in range(n):
    number = int(input())
    if index % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

if even_sum == odd_sum:
    print(f'Yes')
    print(f'Sum = {odd_sum}')
else:
    print(f'No')
    print(f'Diff = {abs(odd_sum - even_sum)}')